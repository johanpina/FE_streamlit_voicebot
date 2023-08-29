import streamlit as st
import sounddevice as sd
import numpy as np
from audiorecorder import audiorecorder
import whisper

from Police_cat import df, sentences, encode_DB, embed_sentence, best_similarity, most_similar_class
from setting import DURATION, WAVE_OUTPUT_FILE

import os

os.environ['TOKENIZERS_PARALLELISM'] = 'false'


model_audio = whisper.load_model("small")

model, embeddings = encode_DB(sentences)

st.title("💬 VoiceBot de seguridad 🚔☎️")
st.write("Este es un agente que permite clasificar las llamadas de emergencia para dirigirlas correctamente.")
st.image("https://www.peoplecontact.com.co/images/peoplecontact-1.png"
         , width=300)

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Buenos días, describa brevemente su llamada"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])



if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    prompt_embedd = embed_sentence(model, prompt)
    ind = best_similarity(prompt_embedd, embeddings, 5)
    response = most_similar_class(ind, df, sentences)

    msg = {"content": response, "role": "assistant"}
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg["content"])

audio = audiorecorder("Click to record", "Recording...")
if len(audio) > 0:
    # To play audio in frontend:
    st.audio(audio.tobytes())
    
    # To save audio to a file:
    wav_file = open("audio.mp3", "wb")
    wav_file.write(audio.tobytes())

    result = model_audio.transcribe("audio.mp3")
    prompt=result["text"]
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    prompt_embedd = embed_sentence(model, prompt)
    ind = best_similarity(prompt_embedd, embeddings, 5)
    response = most_similar_class(ind, df, sentences)

    msg = {"content": response, "role": "assistant"}
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg["content"])
