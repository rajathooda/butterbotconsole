import streamlit as st
import requests

def make_api_request(pdf_file, bot_name):
    files = {
        "files": (pdf_file.name, pdf_file.getvalue())
    }
    data = {
        "pineconeNamespace": bot_name
    }
    API_URL = "https://butterbot-ml2y.onrender.com/api/v1/prediction/88e6f717-db04-40bc-a3d5-753a7582b37d"
    response = requests.post(API_URL, files=files, data=data)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def chatbot_response(user_message, bot_name):
    API_URL = "https://gnoo.onrender.com/api/v1/prediction/1e32e22f-c9e9-46f2-a7cd-435b3580183f"
    payload = {
        "question": user_message,
        "overrideConfig": {
            "pineconeNamespace": bot_name,
        },
    }
    response = requests.post(API_URL, json=payload)
    if response.status_code == 200 and response.json():
        return response.json()
    else:
        return "Error: received invalid response or status code"

def run_app():
    st.title('Create your Chatbot')

    if 'conversation' not in st.session_state:
        st.session_state.conversation = []
        st.session_state.submitted = False

    bot_name = st.text_input('Enter a unique name for your chatbot:')
    st.session_state.bot_name = bot_name
    website_url = st.text_input('Enter a website URL:')
    pdf_file = st.file_uploader('Upload a PDF file:', type=['pdf'])

    with st.form(key='api_form'):
        submit_button = st.form_submit_button('Submit')

        if submit_button:
            if website_url == '' and pdf_file is None:
                st.error('Please input a URL or upload a PDF file.')
            else:
                if website_url != '':
                    API_URL = "https://gnoo.onrender.com/api/v1/prediction/1b5ba2b2-40a4-4413-b75c-012609b5e7fb"
                    payload = {
                        "question": "Hey, how are you?",
                        "overrideConfig": {
                            "url": website_url,
                            "pineconeNamespace": bot_name,
                            "pineconeIndex": "keeko",
                            "pineconeEnv": "northamerica-northeast1-gcp",
                            "webScrap": True,
                        },
                    }
                    response = requests.post(API_URL, json=payload)
                    if response.status_code == 200:
                        st.success('Website URL processed successfully.')
                        st.session_state.submitted = True
                    else:
                        st.error(f'An error occurred while processing the website URL. Status code: {response.status_code}')

                if pdf_file is not None:
                    api_response = make_api_request(pdf_file, bot_name)
                    if api_response is not None:
                        st.success('PDF file uploaded and processed successfully.')
                        st.session_state.submitted = True
                    else:
                        st.error('An error occurred while processing the PDF file.')

    if st.session_state.submitted:
        with st.form(key='chat_form'):
            user_message = st.text_input("Enter your message:")
            submit_chat = st.form_submit_button("Send")
            if submit_chat:
                bot_response = chatbot_response(user_message, bot_name)
                if bot_response != "Error: received invalid response or status code":
                    st.session_state.conversation.extend([
                        {"role": "user", "message": user_message},
                        {"role": "bot", "message": bot_response}
                    ])

        for message in st.session_state.conversation:
            with st.chat_message(message["role"]):
                st.write(message["message"])
