import streamlit as st 
from langchain.llms import Ollama
llm = Ollama(model="llama2-uncensored:latest") # 👈 stef default

colA, colB = st.columns([.90, .10])
with colA:
    prompt = st.text_input("prompt", value="", key="prompt")
response = ""
with colB:
    st.markdown("")
    st.markdown("")
    if st.button("🙋‍♀️", key="button"):
        response = llm.predict(prompt)
st.markdown(response)