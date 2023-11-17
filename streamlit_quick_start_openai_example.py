#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
from langchain.llms import OpenAI

st.title('🦜🔗 Quickstart App')

st.sidebar.title("Ask me ay question")
st.sidebar.divider()
st.sidebar.markdown("Developed by Smita Prasad", unsafe_allow_html=True)
st.sidebar.markdown("Current Version: 0.0.1")
st.sidebar.markdown("OpenAI and LangChain, built on stramlit")
st.sidebar.divider()

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)

