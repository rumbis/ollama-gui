import os
import subprocess
from typing import Optional

import streamlit as st
import sys

sys.path.append(".")

from langchain import LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chat_models import ChatOllama
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate

# Update these variables with your own values
LLM_MODEL = "llama2:latest"
LLM_BASE_URL = "http://localhost:11434"

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

chat_model = ChatOllama(callback_manager=callback_manager)

chat_model.model = LLM_MODEL
chat_model.base_url = LLM_BASE_URL

SYSTEM_PROMPT = f"""
You are a helpful chatbot. 
Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be based on your knowledge
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question
"""

HUMAN_PROMPT = "{question}"

system_message_prompt = SystemMessagePromptTemplate.from_template(SYSTEM_PROMPT)
human_message_prompt = HumanMessagePromptTemplate.from_template(HUMAN_PROMPT)
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

llm_chain = LLMChain(llm=chat_model, prompt=chat_prompt)

def run_streamlit():
    question = st.text_input("Ask me something!", placeholder="Type your question here.")
    
    if question:
        response = llm_chain.run({"question": question})
        st.write(f"My answer: {response}")

if __name__ == "__main__":
    run_streamlit()
