import streamlit as st
import page1
import page2

# Set the page configuration at the top of your main script
st.set_page_config(
    page_title="Your Page Title",
    page_icon="👋",
    layout="wide",
)

def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", ["Create your Chatbot", "Customise Your Bot"])

    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    if selection == "Create your Chatbot":
        page1.run_app()
    elif selection == "Customise Your Bot":
        if not st.session_state.submitted:
            st.error("You need to submit on Page 1 first!")
        else:
            page2.run_app()

if __name__ == "__main__":
    main()
