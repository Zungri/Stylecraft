from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st 
from openai import OpenAI

import os
import streamlit as st

# Get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# List all files in the directory containing the script
directory_files = os.listdir(script_dir)


def classify_fruit(img):

    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model_path = os.path.join(script_dir, "Modelo", "keras_model.h5")
    model = load_model(model_path, compile=False)

    # Load the labels
    labels_path = os.path.join(script_dir, "Modelo", "labels.txt")
    class_names = open(labels_path, "r").readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = img.convert("RGB")

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    # print("Class:", class_name[2:], end="")
    # print("Confidence Score:", confidence_score)

    return class_name, confidence_score


def generate_recipe(label):


    client = OpenAI(api_key="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")

    

    response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt= f"sos un experto en moda y tenes que recomendar a la persona que publique la imagen de una prenda como combinarla dependiendo de el estilo de la ropa que se clasifica como {label} brindale 3 formas de combinar esa prenda teniendo en cuenta su estilo",
    temperature=0.5,
    max_tokens=300,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    return response.choices[0].text



# Streamlit App

#st.set_page_config(layout='wide')

logo_path = "logo.png"


# Muestra el logo y el título juntos
st.image(logo_path, width=400)
st.subheader("""Cargá una foto de la prenda que quieras utilizar y determinaremos su estilo.👔""")
st.subheader("""Nuestra avanzada tecnologia te asistira a preparar un outfit para tu ocasion especial🎩""")
input_img = st.file_uploader("Elegir imagen", type=['jpg', 'png', 'jpeg'])
st.markdown(
    """
    <style>
    .stApp {
        background-color: #27B1E9;
    }
    .title {
        font-size: 48px;
        font-weight: bold;
        color: #5d3a1a;
    }
    .subtitle {
        font-size: 24px;
        color: #5d3a1a;
    }
    .info-box {
        font-size: 18px;
        color: #5d3a1a;
    }
    </style>
    """,
    unsafe_allow_html=True
)
if input_img is not None:
    if st.button("Determinar estilo de moda"):
        
        col1, col2, col3 = st.columns([1,1,1])

        with col1:
            st.info("Prenda")
            st.image(input_img, use_column_width=True)

        with col2:
            st.info("Estilo")
            image_file = Image.open(input_img)

            with st.spinner('Comprobando las modas de 2024...'):
                label, confidence_score = classify_fruit(image_file)

                # Extraer el nombre de la etiqueta sin el número
                label_description = label.split(maxsplit=1)[1]  # Divide la etiqueta por el primer espacio y toma el segundo elemento
                label2 = label_description  # Guarda la descripción en label2

                st.success(label2)  # Muestra la etiqueta sin el número

            
        with col3:
                st.info("Posibles outfits")
                result = generate_recipe(label2)
                st.success(result)