import base64
import os
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Asistente de Moda Deportiva",
    page_icon="👟",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Cargar las imágenes
image1 = Image.open("img/sport1.png")
image2 = Image.open("img/sport2.png")
image3 = Image.open("img/sport3.png")

# Ocultar el menú de Streamlit y el pie de página
hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Título de la página
st.title("Outfits Deportivos")

# Lista de consejos para armar un outfit deportivo
st.header("Consejos para armar un outfit deportivo")
st.write("""
1. *Ropa adecuada para el deporte*: Elige ropa específica para el deporte que practicas, ya sea correr, gimnasio, yoga, etc.
2. *Material transpirable*: Opta por prendas hechas de materiales transpirables que absorban el sudor.
3. *Calzado apropiado*: Usa zapatos que brinden el soporte necesario según la actividad deportiva.
4. *Ropa cómoda*: Asegúrate de que la ropa te quede bien y te permita moverte con libertad.
5. *Capas según el clima*: Viste en capas para poder ajustarte a las condiciones climáticas, especialmente si haces deporte al aire libre.
""")
# Enlaces a tiendas de ropa deportiva
st.header("Ofertas imperdibles")
st.write("""
- [Nike](https://www.nike.com/)
- [Adidas](https://www.adidas.com/)
- [Under Armour](https://www.underarmour.com/)
- [Reebok](https://www.reebok.com/)
- [Puma](https://www.puma.com/)
- [Lululemon](https://www.lululemon.com/)
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
