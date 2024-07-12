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
st.markdown("""
<style>
    .page-title {
        text-align: center;
        font-size: 48px;
        font-family: 'Helvetica Neue', sans-serif;
        color: #000000;
        margin-bottom: 20px;
    }
</style>
<div class="page-title">StyleCraft</div>
""", unsafe_allow_html=True)

# Lista de consejos para armar un outfit formal
st.markdown("""
<style>
    .header-title {
        text-align: center;
        font-size: 36px;
        font-family: 'Helvetica Neue', sans-serif;
        color: #000000;
        margin-bottom: 20px;
    }
    .tips {
        font-size: 20px;
        font-family: 'Helvetica Neue', sans-serif;
        color: #000000;
        line-height: 1.6;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="header-title">Consejos para armar un outfit formal</div>', unsafe_allow_html=True)

st.markdown("""
<div class="tips">
    <ol>
        <li><b>Elige un traje de buena calidad:</b> Invierte en un traje bien hecho, preferiblemente en colores clásicos como negro, azul marino o gris.</li>
        <li><b>Camisas:</b> Opta por camisas de colores claros como blanco o azul claro para una apariencia limpia y elegante.</li>
        <li><b>Corbata adecuada:</b> La corbata debe complementar el traje y la camisa. Evita patrones demasiado llamativos.</li>
        <li><b>Zapatos formales:</b> Un buen par de zapatos de vestir, preferiblemente en negro o marrón oscuro, es esencial.</li>
        <li><b>Accesorios discretos:</b> Utiliza accesorios como un buen reloj, gemelos y un pañuelo de bolsillo para agregar un toque de sofisticación sin exagerar.</li>
    </ol>
</div>
""", unsafe_allow_html=True)

# Mostrar las imágenes
col1, col2, col3 = st.columns(3)

with col1:
    st.image(image1, width=350)

with col2:
    st.image(image2, width=350)

with col3:
    st.image(image3, width=350)


# Define the path to your image
image_path = "img/fondoblanco.jpg"

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
        .product-card {{
            background-color: white;
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            text-align: center;
            position: relative;
        }}
        .product-card img {{
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 150px;
            height: 150px;
        }}
        .product-card h3 {{
            text-align: center;
            color: #333;
        }}
        .product-card p {{
            text-align: center;
            color: #666;
        }}
        .logo {{
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100px;
        }}
        .nav-button {{
            background: none;
            border: none;
            font-size: 30px;
            cursor: pointer;
            color: #333;
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
        }}
        .prev-button {{
            left: 10px;
        }}
        .next-button {{
            right: 10px;
        }}
        .centered-text {{
            text-align: center;
            font-size: 22px;
            font-family: 'Helvetica Neue', sans-serif;
            color: #000000;
            margin: 20px 0;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

st.markdown('<div class="centered-text">Ofertas imperdibles</div>', unsafe_allow_html=True)

# Lista de productos simulados con imágenes y logos
products = [
    {"name": "Zapatos Con Cordones Derby De Piel -35%", "price": 129.99, "image": "img/compraF1.png", "logo": "img/logoboss.png"},
    {"name": "Camisa Slim Fit En Sarga De Seda", "price": 940.99, "image": "img/compraF4.png", "logo": "img/armani_logo.png"},
    {"name": "Americana Recta Regular Fit De Crepe Japones -40%", "price": 209.00, "image": "img/compraF2.png", "logo": "img/logoboss.png"},
    {"name": "Pantalones de dos pinzas de raso doble de seda", "price": 2050.99, "image": "img/compraF3.png", "logo": "img/armani_logo.png"}
]

if 'product_index' not in st.session_state:
    st.session_state.product_index = 0

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode()
    return base64_image

def show_product(index):
    product = products[index]
    st.markdown(f"""
    <div class="product-card">
        <img src="data:image/png;base64,{get_base64_image(product['logo'])}" alt="Logo" class="logo">
        <img src="data:image/png;base64,{get_base64_image(product['image'])}" alt="{product['name']}">
        <h3>{product['name']}</h3>
        <p>Precio: ${product['price']:.2f}</p>
    </div>
    """, unsafe_allow_html=True)

# Navigation buttons
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("←", key="prev"):
        st.session_state.product_index = (st.session_state.product_index - 1) % len(products)

with col3:
    if st.button("→", key="next"):
        st.session_state.product_index = (st.session_state.product_index + 1) % len(products)

# Display the current product
show_product(st.session_state.product_index)

# Mostrar cantidad y botón de compra fuera de la tarjeta de producto
product = products[st.session_state.product_index]
quantity = st.number_input("Cantidad", min_value=1, max_value=10, step=1, key="quantity")
total_price = product["price"] * quantity

if 'show_form' not in st.session_state:
    st.session_state.show_form = False

if st.button("Comprar"):
    st.session_state.show_form = True

if st.session_state.show_form:
    with st.form(key="purchase_form"):
        st.subheader("Información de Compra")
        nombre = st.text_input("Nombre")
        apellido = st.text_input("Apellido")
        metodo_pago = st.selectbox("Método de Pago", ["Tarjeta de Crédito", "PayPal", "Transferencia Bancaria"])
        direccion = st.text_area("Dirección")
        email = st.text_input("Email")
        telefono = st.text_input("Teléfono")
        
        submit_button = st.form_submit_button(label="Confirmar Compra")
        
        if submit_button:
            st.write(f"Compra confirmada para {nombre} {apellido}.")
            st.write(f"Método de pago: {metodo_pago}")
            st.write(f"Dirección: {direccion}")
            st.write(f"Email: {email}")
            st.write(f"Teléfono: {telefono}")
            st.write(f"Total: ${total_price:.2f}")
            st.session_state.show_form = False
else:
    st.write("Selecciona la cantidad y luego haz clic en 'Comprar'.")
