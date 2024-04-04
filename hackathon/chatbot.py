import streamlit as st
from PIL import Image
st.title('ONEGPT')
options=['general q & a chatbot','Aishwi chat bot','pdf summarizer',
         'article summarizer']
feature=st.selectbox('select feature',options)
file=st.file_uploader('upload your file if necessary',['pdf','jpg','jpeg']) 
prompt=st.text_input('enter your query')
button=st.button('submit')
if button:
    if feature is 'general q & a chatbot':
       from qa import get_response
       result=get_response(prompt)
       st.write(result)
    elif feature is 'Aishwi chat bot':
       from company import get_response
       result=get_response(prompt)
       st.write(result)
    elif feature == 'pdf summarizer':
       from pdf import get_response
       result=get_response(file)
       st.write(result)
    elif feature is 'article summarizer' :
       from article import get_response
       result=get_response(prompt)
       st.write(result)
       