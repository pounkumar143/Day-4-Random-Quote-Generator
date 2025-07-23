import streamlit as st

def run_login():
    st.title("Welcome to AI Quote Generator")
    user_name = st.text_input("Enter your name")
    user_email = st.text_input("Enter your Gmail address (must end with @gmail.com)")

    if st.button("Enter"):
        if not user_name or not user_email or not user_email.endswith("@gmail.com"):
            st.error("Please enter a valid name and a Gmail address ending with @gmail.com")
        else:
            st.session_state.user_name = user_name.strip()
            st.session_state.user_email = user_email.strip()
            st.success(f"Welcome, {st.session_state.user_name}!")
            st.rerun()  # Correct function for latest Streamlit versions

# Check if user is already logged in
if "user_name" not in st.session_state or "user_email" not in st.session_state:
    run_login()
    st.stop()

# Main app content after login
st.set_page_config(page_title="AI Quote Generator", layout="wide")
st.title(f"Hello, {st.session_state.user_name}!")
st.markdown("Use the sidebar to access features like quote generation, story creation, and downloads.")
