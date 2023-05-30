import json
import torch
import streamlit as st
import numpy as np
from streamlit_chat import message
import re
from sentence_transformers import util

@st.cache_data()
def get_pipe():

    from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
    tokenizer = AutoTokenizer.from_pretrained("baaaki/cyberbullying")
    model = AutoModelForCausalLM.from_pretrained("baaaki/cyberbullying")

    from sentence_transformers import SentenceTransformer
    similarity = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')
    return model, tokenizer, similarity

def get_response(model, tokenizer, similarity, q):
    with torch.no_grad():
            a = ""
            while 1:
                input_ids = torch.tensor(tokenizer.encode("<usr>" + q + '<unused1>' + "<sys>" + a)).unsqueeze(dim=0)
                pred = model(input_ids)
                pred = pred.logits
                gen = tokenizer.convert_ids_to_tokens(torch.argmax(pred, dim=-1).squeeze().cpu().numpy().tolist())[-1]
                if gen == '</s>':
                    break
                a += gen.replace("▁", " ")

            #유사도 확인
            sim_param=0.65
            sentences = re.split("(?<=[.?!])\s", a.strip())
            vectors = similarity.encode(sentences)
            similarities = util.cos_sim(vectors, vectors)
            tri_mat = np.tril(similarities, k=-1)

            drop = sorted(list(set(np.where(tri_mat > sim_param)[0])),reverse=True)
            for index in drop:
                del sentences[index]
    return ' '.join(sentences)

st.header("🤖CyberBullying Chatbot (Demo)")

with st.spinner("loading model..."):
    model, tokenizer, similarity = get_pipe()

if 'message_history' not in st.session_state:
    st.session_state.message_history =  []
history = st.session_state.message_history


for i, message_ in enumerate(st.session_state.message_history):
    message(message_,is_user=i % 2 == 0)


text_input_container = st.empty()
nickname = text_input_container.text_input("이름을 입력해주세요: ")

if nickname:
    text_input_container.empty()

    
    with st.form('form', clear_on_submit=True):
        user_input = st.text_area('You: ', '', key='input')
        submitted = st.form_submit_button('Send')

    if user_input and len(user_input) > 0:
        if len(history) <= 1 or history[-2] != user_input:
            with st.spinner("잠시 기다려주세요..."):
                st.session_state.message_history.append(user_input)
                response = get_response(model, tokenizer, similarity, user_input)
                response = response.replace("질문자",nickname).replace(" 님", f" {nickname}님")
                st.session_state.message_history.append(response)
                st.experimental_rerun()
