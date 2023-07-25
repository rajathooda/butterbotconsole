import streamlit as st

def run_app():
    # Page Title
    st.title('Customise Your Bot')

    # Taking inputs from the user
    st.subheader('Please enter the following details:')

    widget_background_color = st.color_picker('Widget Background Color', '#3B81F6')
    main_widget_icon = st.text_input('Main Widget Icon URL')
    welcome_message = st.text_input('Welcome Message')
    chat_window_default_message = st.text_input('Chat Window Default Message', 'Type your question')
    height_pixels = st.number_input('Height in Pixels', value=700)
    width_pixels = st.number_input('Width in Pixels', value=400)
    font_size = st.number_input('Font Size', value=16)
    bot_avatar = st.text_input('Bot Avatar URL')
    bot_message_background_color = st.color_picker('Bot Message Background Color', '#f7f8ff')
    bot_message_text_color = st.color_picker('Bot Message Text Color', '#303235')
    user_avatar = st.text_input('User Avatar URL')
    user_background_message_color = st.color_picker('User Background Message Color', '#3B81F6')
    user_text_message_color = st.color_picker('User Text Message Color', '#ffffff')
    send_button_color = st.color_picker('Send Button Color', '#3B81F6')

    # Generating the code based on user inputs
    if st.button('Generate Code'):
        bot_name = st.session_state.bot_name # Retrieve bot name from session state
        code = f"""<script type="module">
        import Chatbot from "https://cdn.jsdelivr.net/npm/flowise-embed/dist/web.js"
        Chatbot.init({{
            chatflowid: "80dde17d-aa68-4816-8750-0ac1d90682ba",
            apiHost: "https://butterbot-ml2y.onrender.com",
            chatflowConfig: {{
                pineconeNamespace: "{bot_name}",
            }},
            theme: {{
                button: {{
                    backgroundColor: "{widget_background_color}",
                    customIconSrc: "{main_widget_icon}",
                }},
                chatWindow: {{
                    welcomeMessage: "{welcome_message}",
                    height: {height_pixels},
                    width: {width_pixels},
                    fontSize: {font_size},
                    botMessage: {{
                        backgroundColor: "{bot_message_background_color}",
                        textColor: "{bot_message_text_color}",
                        avatarSrc: "{bot_avatar}",
                    }},
                    userMessage: {{
                        backgroundColor: "{user_background_message_color}",
                        textColor: "{user_text_message_color}",
                        avatarSrc: "{user_avatar}",
                    }},
                    textInput: {{
                        placeholder: "{chat_window_default_message}",
                        sendButtonColor: "{send_button_color}",
                    }}
                }}
            }}
        }})
    </script>"""
        st.code(code, language='html')
