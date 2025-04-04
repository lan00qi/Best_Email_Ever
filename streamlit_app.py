import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
client = OpenAI(api_key = os.getenv("API_KEY"))

"""
This is the best email maker ever/ I LOVE writing email. Looks like you need help writing an email to someone. No problem!
"""
response = ""
with st.form("my_form"):
    users_name = st.text_input("What is your name?")
    reciever_name = st.text_input("And who are you sending this to?")
    style = st.selectbox("Pick from one of these writing styles",["Casual","Formal","Silly"])
    content = st.text_area("What do you want to talk about?")
    submit = st.form_submit_button("Submit")
    if submit:
        response = client.chat.completions.create(
            model = "gpt-3.5-turbo-0125",
            messages = [
                {"role":"system","content":"you are the worlds best email writer. You write email base on the users name, recievers name, style of writing, and the content."},
                {"role":"user","content":"My name is "+users_name+" the recievers name is "+reciever_name+" write in the style of "+style+" base on the topic : "+content+" ."}
            ]
        )

if response:
    st.write(response.choices[0].message.content)
