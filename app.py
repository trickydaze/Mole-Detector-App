from img_classification import teachable_machine_classification
import streamlit as st
from PIL import Image

st.title("""
Online Mole Detector
	""")

uploaded_file = st.file_uploader("PLEASE UPLOAD A MOLE PICTURE ...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='File uploaded.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = teachable_machine_classification(image, 'second_model.h5')
    if label == 0:
        st.write("This mole looks okay, nothing to worry about")
    else:
        st.write("This mole looks suspicious, please see a doctor")