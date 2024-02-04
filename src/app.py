import streamlit as st 
from langchain_core.message import AIMessage, HumanMessage

def get_response(user_input):
    return


st.set_page_config(page_title = "Chat with websites", page_icon=" ")
st.title("Chat with websites")
if "chat_history" not in st.session_state:
    st.session_state.chat_history=[
        AIMessage(content="Hello, How can I help you ?")
    ]

with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")


user_query = st.chat_input("Type your message here....")
if user_query is not None and user_query !='':
    response = get_response(user_query)
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    st.session_state.chat_history.append(AIMessage(content=response))
    with st.chat_message("HUMAN"):
        st.write(user_query)

    with st.chat_message("AI"):
        st.write(response)



    