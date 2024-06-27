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
image1 = Image.open("img/formal.png")
image2 = Image.open("img/formal1.png")
image3 = Image.open("img/formal2.png")



# Ocultar el menú de Streamlit y el pie de página
hide_streamlit_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}

        </style>
        """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Título de la página
st.title("Formal")

# Lista de consejos para armar un outfit 
st.header("Consejos para armar un outfit Formal")
st.write("""
1. *Elige un traje de buena calidad*: Invierte en un traje bien hecho, preferiblemente en colores clásicos como negro, azul marino o gris.
2. *Camisas*: Opta por camisas de colores claros como blanco o azul claro para una apariencia limpia y elegante.
3. *Corbata adecuada*: La corbata debe complementar el traje y la camisa. Evita patrones demasiado llamativos.
4. *Zapatos formales*: Un buen par de zapatos de vestir, preferiblemente en negro o marrón oscuro, es esencial.
5. *Accesorios discretos*: Utiliza accesorios como un buen reloj, gemelos y un pañuelo de bolsillo para agregar un toque de sofisticación sin exagerar.
""")
# Enlaces a tiendas de ropa 
st.header("Ofertas imperdibles")
st.write("""
- [Hugo Boss](https://www.hugoboss.com/)
- [Armani](https://www.armani.com/)
- [Brooks Brothers](https://www.brooksbrothers.com/)
- [Ralph Lauren](https://www.ralphlauren.com/)
- [Tom Ford](https://www.tomford.com/)
- [Burberry](https://www.burberry.com/)
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