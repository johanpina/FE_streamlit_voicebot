import streamlit as st
from Police_cat import df, sentences, encode_DB, embed_sentence, best_similarity, most_similar_class

model, embeddings = encode_DB(sentences)


with st.sidebar:
    
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("💬 Chatbot") 
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Buenos días, describa brevemente su llamada"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    ## PROMPT es lo que se ingresara en el chat
    prompt_embedd = embed_sentence(model, prompt)
    ind = best_similarity(prompt_embedd, embeddings, 5)

    response = most_similar_class(ind, df, sentences)

    #response = "Respuesta " ##openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = {"content": response, "role": "assistant"} ##response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg["content"])