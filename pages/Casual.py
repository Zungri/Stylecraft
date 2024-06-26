import base64
import os
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Asistente de Moda",
    page_icon="👔",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Cargar las imágenes
image1 = Image.open("img/outfit3.png")
image2 = Image.open("img/outfit4.png")
image3 = Image.open("img/outfit2.png")



# Ocultar el menú de Streamlit y el pie de página
hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        </style>
        """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Título de la página
st.title("Casual")

# Lista de consejos para armar un outfit casual
st.header("Consejos para armar un outfit casual")
st.write("""
1. *Comodidad ante todo*: Elige prendas que te resulten cómodas y que te permitan moverte con facilidad.
2. *Colores neutros*: Los colores como el blanco, negro, gris y azul son fáciles de combinar y siempre se ven bien.
3. *Capas*: Añadir capas como chaquetas ligeras o cardigans puede darle un toque extra a tu atuendo y es práctico para cambios de temperatura.
4. *Accesorios*: Utiliza accesorios como relojes, pulseras o sombreros para personalizar tu look y darle un toque distintivo.
5. *Calzado adecuado*: Opta por zapatos cómodos y versátiles, como zapatillas blancas o botines, que complementen tu estilo sin sacrificar la comodidad.
""")
# Enlaces a tiendas de ropa casual
st.header("Ofertas imperdibles")
st.write("""
- [H&M](https://www2.hm.com/)
- [Zara](https://www.zara.com/)
- [Uniqlo](https://www.uniqlo.com/)
- [ASOS](https://www.asos.com/)
- [Mango](https://shop.mango.com/)
- [Levi's](https://www.levi.com/)
""")

# Mostrar las imágenes
col1, col2, col3 = st.columns(3)

with col1:
    st.image(image1, width=350)

with col2:
    st.image(image2, width=350)

with col3:
    st.image(image3, width=350)

# Define the path to your image
image_path = "img/fondo3.jpeg"

# Check if the image exists
if not os.path.exists(image_path):
    st.error(f"La imagen no se encuentra en la ruta: {image_path}")
else:
    # Function to convert an image file to a base64 string
    def get_base64_image(image_path):
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode()
        return base64_image

    # Convert the local image to a base64 string
    base64_image = get_base64_image(image_path)
    
    # CSS to set the background image
    st.markdown(
        f"""
        <style>
        body {{
            background-image: url("data:image/png;base64,{base64_image}");
            background-size: cover;       /* Cover the entire page */
            background-repeat: no-repeat; /* Do not repeat the image */
            background-attachment: fixed; /* Make sure the background image stays fixed when scrolling */
            background-position: center;  /* Center the image */
        }}
        .stApp {{
            background: rgba(125, 125, 125, 0.01); /* Semi-transparent background for content */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )