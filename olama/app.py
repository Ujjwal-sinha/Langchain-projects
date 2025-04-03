import os 
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

#prompt template

prompt= ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful Ai Researcher . Please respond to the question asked"),
        ("user","Question:{question}")
    ]
    
    
)

## streamlit framework
st.title("Langchain Demo With Gemma Model")
input_text=st.text_input("What question you have in mind?")


llm =Ollama(model="gemma3:1b")

chain = prompt|llm
if input_text:
    st.write(chain.invoke({"question":input_text}))
