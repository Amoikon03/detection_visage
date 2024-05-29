import streamlit as st
import cv2
import numpy as np

# Chemin vers le fichier XML de détection de visages
xml_file_path = "haarcascade_frontalface_default.xml"

# Chargement du classificateur de cascade faciale
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + xml_file_path)


# Étape 2: Définir la fonction de détection des visages
def detect_faces(frame):
    # Convertir les images en niveaux de gris
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Détecter les visages à l'aide du classificateur en cascade de visages
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    # Tracer des rectangles autour des visages détectés
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return frame


# Étape 3: Définir l'application Streamlit
def app():
    # Chemin vers le fichier XML de détection de visages
    xml_file_path = "haarcascade_frontalface_default.xml"

    # Titre et description de l'application avec options de style
    st.sidebar.title("Options de Style")

    # Options de style pour le titre
    text_size = st.sidebar.slider("Taille du texte", 40, 100, 40)
    text_color = st.sidebar.color_picker("Couleur du texte", "#FFFFFF")
    bg_color = st.sidebar.color_picker("Couleur de fond du texte", "#0B162C")
    title_style = f"""
    <div style="background-color: {bg_color}; padding: 10px; border-radius: 5px; text-align: center;">
    <h1 style="color: {text_color}; font-size: {text_size}px;">Détection des visages</h1>
    </div>
    """
    st.markdown(title_style, unsafe_allow_html=True)

    st.write(" ")
    st.write(" ")

    st.write("**Appuyez sur le bouton ci-dessous pour commencer à détecter les visages à partir de votre webcam**")

    # Initialiser la webcam
    cap = cv2.VideoCapture(0)
    start_detection = st.button("**Démarrer la détection des visages**")
    stop_detection = st.button("**Arrêter la détection**")

    # Variable pour stocker le dernier cadre
    last_frame = None

    # Démarrer la détection si le bouton est pressé
    if start_detection:
        while True:
            ret, frame = cap.read()
            if not ret:
                st.error("Erreur: Impossible de capturer l'image de la webcam.")
                break

            # Détecter les visages
            frame_with_faces = detect_faces(frame)

            # Afficher le cadre avec les visages détectés
            st.image(frame_with_faces, channels="BGR")

            # Stocker le dernier cadre avec les visages détectés
            last_frame = frame_with_faces

            # Vérifier si le bouton d'arrêt est appuyé
            if stop_detection:
                st.write("Détection des visages arrêtée.")
                break

    # Afficher la dernière image capturée après l'arrêt de la détection
    if stop_detection and last_frame is not None:
        st.image(last_frame, channels="BGR", caption="Dernière image capturée avec les visages détectés")

    # Relâcher la webcam et fermer toutes les fenêtres
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    app()

# Lien vers l'autre page ou section
st.subheader("Accès rapide à la page Acceuil")

# Liste de lien
st.write("""

- [Acceuil](http://localhost:8501/)

""")
