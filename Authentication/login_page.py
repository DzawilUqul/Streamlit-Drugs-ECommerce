import streamlit as st
from menus.admin import insert_pelanggan


# Define the functions for login, signup, and logout
def form_callback():
    st.session_state.logged_in = True


def login(cursor):
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login", on_click=form_callback):
        user_data = authenticate_user(cursor, username, password)
        if user_data is None:
            st.error("Invalid username or password")
            return
        else:
            st.session_state.user_data = user_data


def authenticate_user(cursor, username, password):
    # Your authentication logic goes here
    pass


def signup(connection, cursor):
    insert_pelanggan.app(connection, cursor)


def logout_function(connection, cursor):
    st.session_state.clear()
    st.markdown("""
        <style>
            section[data-testid="stSidebar"][aria-expanded="true"]{
                display: none;
            }
        </style>
        """, unsafe_allow_html=True)
    login(cursor)


# Main function to manage the UI
def main(connection, cursor):
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Login", "Sign Up"])

    if page == "Login":
        login(cursor)  # Pass your cursor object here
    elif page == "Sign Up":
        signup(connection, cursor)
