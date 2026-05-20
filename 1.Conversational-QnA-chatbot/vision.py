from dotenv import load_dotenv
load_dotenv() # loading all the enironment variables

import streamlit as st
import os 
import google.generativeai as genai
from PIL import Image

genai.configure(api_key = os.getenv("GOOGLE_API_KEY")) 

model = genai.GenerativeModel("gemini-3.1-flash-lite")
def get_gemini_response(input_text, image):
    # Ensure we are passing a list of parts to the model
    if input_text != "":
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title = "Gemini Vision Demo")

st.header("Gemini Vision LLM Application")
input = st.text_input("Input prompt: ",key = "input")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_container_width=True)

submit = st.button("Tell me about the image")

# when submited
if submit:
    response = get_gemini_response(input , image)
    st.subheader("Gemini Vision Response")
    st.write(response)