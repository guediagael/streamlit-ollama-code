import streamlit as st
from client_model import Message, Chat
from datetime import datetime
from operations import update_chat_history
import  llama_model as llama_models
from langchain.llms.ollama import Ollama

default_chat_name = 'New Chat Created'
is_loading = False # When awaiting for the response

st.title("Code with llama 2")

# Initialize chat history
if "chats" not in st.session_state:
    st.session_state.chats = { datetime.timestamp(datetime.now()): {'title':None,'messages':[]}}

# Add a selectbox to the sidebar:
with st.sidebar :
    selected_model = st.selectbox(
        'Which model do you want to use?',
        options= [llama_models.Llama13B(), llama_models.Llama13BPython(), llama_models.Llama13BInstruct(), llama_models.Llama7B(), llama_models.Llama7BPython(), llama_models.Llama7BInstruct()],
        format_func= lambda llama_model : llama_model.name
    )

    llm = Ollama(model=selected_model.name)

    st.button("New Chat")
    current_chat_id = st.radio('Chat history', 
                                [Chat(id= id, title= chat['title'], messages=[Message(** msg) for msg in chat['messages']]) for id, chat in st.session_state.chats.items()],
                                format_func = lambda x : x.title if x.title else default_chat_name).id

      
# Display chat messages from history on app rerun
for message in st.session_state.chats[current_chat_id]['messages']:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What it BUGGING you today?", disabled= is_loading):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
        is_loading = True
    updated_chat_history = update_chat_history(current_chat_id=current_chat_id,  initial_history=st.session_state.chats, prompt=prompt)
    st.session_state.chats = updated_chat_history

    # Send prompt
    with st.chat_message("assistant"):
        response = st.write_stream(llm.stream(selected_model.prompt_prefix + prompt))
        # Save the chat history
        new_message = Message(id= datetime.timestamp(datetime.now()), role='assistant', content=response)
        st.session_state.chats[current_chat_id]['messages'].append(dict(new_message))
        
        #Re-active the user input field
        is_loading = False


