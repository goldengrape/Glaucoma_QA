import streamlit as st
from gpt_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import sys
import os

st.title("青光眼AI辅助咨询")
st.write("本系统基于ChatGPT，仅供参考，不作为医疗诊断依据。")

api_key=st.text_input("OpenAI API Key", value="", type="password")
os.environ["OPENAI_API_KEY"]=api_key

question=st.text_input("请输入您的问题", value="", type="default")
ask_button=st.button("咨询")
answer=st.markdown("")

if "index" not in st.session_state:
    if api_key is not None:
        st.session_state.index = GPTSimpleVectorIndex.load_from_disk('index.json')


if ask_button and (st.session_state.index is not None):
    prompt="Answer the question in Chinese:\n"+question
    response=st.session_state.index.query(prompt, response_mode="compact")
    answer.markdown(response.response)