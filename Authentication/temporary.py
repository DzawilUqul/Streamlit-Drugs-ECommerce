import streamlit as st


def default_page():
    st.title("Welcome to Streamlit App")
    st.write("This is the default landing page.")
    st.write("Please log in to access the application.")

    # Add login and sign up buttons
    login_button = st.button("Logina")
    sign_up_button = st.button("Sign Up")


default_page()
