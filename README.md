 # Langchain Streamlit Chat Application

This README file provides instructions on how to set up and run a chat application using the Langchain and Streamlit libraries. This application allows users to input questions, which are then answered by an AI language model.

## Setting Up the Environment

1. Create a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

2. Activate the virtual environment and install the required packages:
```bash
pip install streamlit langchain chat-models callbacks
```

## Running the Streamlit Chat Application

1. Update `LLM_MODEL` and `LLM_BASE_URL` with the correct values for your environment. For this example, use "llama2:latest" and "localhost:11434".




1. Open a terminal or command prompt.
2. Navigate to the directory containing your Streamlit Python script.
3. Run `streamlit run chat.py This will start the Streamlit server from that script.
