import streamlit as st
import main_3
import asyncio
import real_time_ret
# Initialize Streamlit app title
st.title("Question and Answers Bot")

# Add a logo or header
st.sidebar.image("logo_moveworks.jpeg", use_column_width=True)


new_webiste = st.sidebar.text_input("New Website Search", "")

if st.sidebar.button("Use New Website"):
    #call some function
    db_to_use = main_3.change_web(new_webiste)

    if db_to_use != "db3":
        main_3.start_ret_script(new_webiste)

def get_db_name():

    # Open the file in read mode
    with open("db_to_file.txt", "r") as file:
        # Read the entire file into a string
        file_contents = file.read()
        file_contents = file_contents.replace("\n", "")
        return file_contents


# Initialize the chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Function to initialize QA system
def initialize_qa(db_name):
    print("IQ", db_name)
    return main_3.initialise_qa(db_name)

# Get user input from Streamlit
user_input = st.text_input("User Input", "")

# Display chat history
for message in st.session_state.chat_history:
    st.write(f"{message['role']}: {message['content']}")

# Clear chat history button
if st.sidebar.button("Clear History"):
    # st.session_state.chat_history.clear()  # Clear the chat history by using the clear() method
    # def history_delete():
    #     return main_3.clear_history()

    # print(st.session_state.chat_history)
    # main_3.clear_history()

    st.session_state.chat_history = []
    main_3.clear_history()  
    st.empty()

if st.button("Search"):
    # st.session_state.chat_history.clear()  # Clear the chat history by using the clear() method
    # def history_delete():
    #     return main_3.clear_history()
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    # Process user input and get assistant response using main_output
    print("sEARCG", get_db_name())
    qa = initialize_qa(get_db_name())  # Initialize QA system here
    assistant_response = main_3.main_output(user_input, qa)
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    for message in st.session_state.chat_history[-2:]:
        st.write(f"{message['role']}: {message['content']}")


