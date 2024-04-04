import streamlit as st
import google.generativeai as genai
from PIL import Image
genai.configure(api_key="AIzaSyBfBKeNznMdvwrqbtPB12hL6aSB8BWDeYc")
model=genai.GenerativeModel("gemini-pro")
vision_model=genai.GenerativeModel("gemini-pro-vision")