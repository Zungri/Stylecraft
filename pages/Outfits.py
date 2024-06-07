import streamlit as st

outfit1_path = "img/outfit1.jpeg"
outfit2_path = "img/outfit2.jpeg"
outfit3_path = "img/outfit.jpeg"

# Sección de recomendados
st.markdown("<h2 style='color: #ffffff;'>Outfits Recomendados</h2>", unsafe_allow_html=True)
st.markdown("<div class='recommended-container'>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.image(outfit1_path, use_column_width=True,)

with col2:
    st.image(outfit2_path, use_column_width=True,)

with col3:
    st.image(outfit3_path,width=200,)

# Cerrar el contenedor del fondo azul oscuro
st.markdown("</div>", unsafe_allow_html=True)