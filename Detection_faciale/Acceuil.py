import streamlit as st
import cv2

# Chemin vers le fichier XML de détection de visages
xml_file_path = "haarcascade_frontalface_default.xml"

# Titre et description de l'application avec options de style
st.sidebar.title("Options de Style")

# Options de style pour le titre
text_size = st.sidebar.slider("Taille du texte", 40, 100, 40)
text_color = st.sidebar.color_picker("Couleur du texte", "#FFFFFF")
bg_color = st.sidebar.color_picker("Couleur de fond du texte", "#0B162C")

# Titre de l'application
title_style = f"""
<div style="background-color: {bg_color}; padding: 10px; border-radius: 5px; text-align: center;">
<h1 style="color: {text_color}; font-size: {text_size}px;">Détection des visages à l'aide de l'algorithme de Viola-Jones</h1>
</div>
"""
st.markdown(title_style, unsafe_allow_html=True)

# Description
st.subheader("Description : ")

# Variables pour le style du titre
bg_color = '#f0f0f0'
text_color = '#333333'
text_size = 24



# Utilisation des colonnes de Streamlit pour organiser le texte et l'image côte à côte
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div style="text-align: justify;">
    L'algorithme de Viola-Jones est une technique populaire de détection de visages dans les images.  
    Il est largement utilisé dans de nombreuses applications telles que la photographie, la vidéosurveillance, la réalité augmentée, etc.  
    L'application Streamlit pour la détection faciale à l'aide de cet algorithme vise à fournir une interface utilisateur conviviale  
    pour détecter les visages en temps réel à partir de la webcam de l'utilisateur.  
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image("Detection_faciale/images.jpg", caption="Représentation de l'intelligence artificielle (IA)", use_column_width=True)

# Lien vers l'autre page ou section
st.subheader("Visitez la page Visage")
# Liste de lien
st.write("""

- [Visage](http://localhost:8501/Accueil_%F0%9F%87%A8%F0%9F%87%AE)

""")



