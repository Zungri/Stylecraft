from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st 
from openai import OpenAI

import os
import streamlit as st

st.set_page_config(
    page_title="Asistente de Moda",
    page_icon="👔",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
    #print("Confidence Score:", confidence_score)

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

logo_path = "img/logo.png"


# Muestra el logo y el título juntos
st.image(logo_path, width=400)
st.subheader("""Cargá una foto de la prenda que quieras utilizar y determinaremos su estilo.👔""")
st.subheader("""Nuestra avanzada tecnologia te asistira a preparar un outfit para tu ocasion especial🎩""")
input_img = st.file_uploader("Elegir imagen", type=['jpg', 'png', 'jpeg'])
# Botón para navegar a la página de outfits recomendados
# Botón para navegar a la página de outfits recomendados


st.markdown(
    """
    <style>
    .stApp {
        background-color: #0f3999;
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
                

            st.success(f"Estilo: {label2}")  # Muestra la etiqueta sin el número
            if confidence_score < 0.80:
                    st.warning(f"No comprendo esta imagen, carga mas imagenes para poder ayudarte.")  # Muestra el confidence score con 2 decimales de precisión
            

            
        with col3:
                st.info("Posibles outfits")
                #result = generate_recipe(label2)
                #st.success(result)#
                st.markdown(
                    """
                  <div class="btn-box">
                  <a href="/Casual" target="_self">
                     <button style="background-color:#000000;color:white;padding:10px 20px;border:none;border-radius:5px;font-size:20px;">
                       Ver Outfits Recomendados
                        </button>
                        </a>
                       </div>
                        """,
                        unsafe_allow_html=True
                        )

st.markdown("---")
tab1, tab2, tab3 = st.tabs(["Quiénes Somos", "Contacto", "Novedades"])

with tab1:
    st.header("Quiénes Somos")
    st.write("""
    Somos un equipo apasionado por la moda y la tecnología. Nuestra misión es hacer que 
    la elección de outfits sea más fácil y divertida para todos, combinando inteligencia 
    artificial con las últimas tendencias de la moda.

    Nuestro equipo está formado por:
    - Expertos en moda
    - Ingenieros de IA
    - Diseñadores de UX/UI
    
    Juntos, trabajamos para brindarte la mejor experiencia en asesoramiento de moda personalizado.
    """)

with tab2:
    st.header("Contacto")
    st.write("""
    ¿Tienes preguntas o sugerencias? ¡Nos encantaría escucharte!
    
    📧 Email: contacto@asistente-moda.com
    📱 Teléfono: +1 (555) 123-4567
    🌐 Sitio web: www.asistente-moda.com
    
    Síguenos en redes sociales:
    - Instagram: @asistente_moda
    - Twitter: @AsistenteModa
    - Facebook: /AsistenteDeModa
    """)
    
    # Formulario de contacto simple
    with st.form("formulario_contacto"):
        st.write("Formulario de Contacto")
        nombre = st.text_input("Nombre")
        email = st.text_input("Email")
        mensaje = st.text_area("Mensaje")
        submitted = st.form_submit_button("Enviar")
        if submitted:
            st.success("¡Gracias por tu mensaje! Te responderemos pronto.")

with tab3:
    st.header("Novedades")
    st.write("""
    ¡Mantente al día con las últimas actualizaciones de nuestro Asistente de Moda!
    
    🆕 Próximas Funcionalidades:
    - Reconocimiento de colores para mejor combinación
    - Integración con tiendas online para compras directas
    - Función de guardarropa virtual
    
    🎉 Eventos:
    - Webinar: "Tendencias de Moda 2024" - 15 de Julio
    - Lanzamiento de nuestra app móvil - Próximamente
    
    📰 Blog:
    - "5 Tips para Combinar Colores en tu Outfit"
    - "Cómo Vestir para Diferentes Ocasiones"
    - "Moda Sostenible: Tendencias y Consejos"
    """)

# Pie de página
st.markdown("---")
st.write("Desarrollado con ❤ por Tu Equipo")
