import streamlit as st
import rasa.shared.utils.io

from rasa.cli import run
from rasa.model import get_model
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter

# Load Rasa model and agent
model_path = get_model("./models") # path to your Rasa model directory
interpreter = RasaNLUInterpreter(model_path)
agent = Agent.load(model_path, interpreter=interpreter)

# Define streamlit app
def app():
    st.title("Rasa Chatbot")
    user_input = st.text_input("You: ")
    if user_input:
        responses = agent.handle_text(user_input)
        for response in responses:
            st.text(f"Bot: {response['text']}")

# Run streamlit app
if __name__ == "__main__":
    app()
