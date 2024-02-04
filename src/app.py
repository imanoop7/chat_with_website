import streamlit as st 

def get_response(user_input):
    return


st.set_page_config(page_title = "Chat with websites", page_icon=" ")


st.title("Chat with websites")

with st.sidebar:
    st.header("Settings")
    website_url = st.text_input("Website URL")


user_query = st.chat_input("Type your message here....")
if user_query is not None and user_query !='':
    response = get_response(user_query)
    with st.chat_message("HUMAN"):
        st.write(user_query)

    with st.chat_message("AI"):
        st.write(response)



    