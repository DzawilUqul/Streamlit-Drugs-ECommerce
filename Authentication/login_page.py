import streamlit as st
from menus.admin import insert_pelanggan


# Define the functions for login, signup, and logout
def form_callback():
    st.session_state.logged_in = True


def login(cursor):
    st.title("Login Untuk Mulai Berbelanja")

    with st.form(key="login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        # Submit
        submitted = st.form_submit_button("Login")
        if submitted:
            user_data = authenticate_user(cursor, username, password)
            if user_data is None:
                st.error("Invalid username or password")
                return
            else:
                # change user data to dictionary
                user_data = {
                    "id": user_data[0],
                    "nama": user_data[1],
                    "no_telp": user_data[2],
                    "alamat": user_data[3],
                    "role": user_data[4],
                    "username": user_data[5],
                    "password": user_data[6],
                }
                st.session_state.logged_in = True
                st.session_state.user_data = user_data
                st.rerun()


def authenticate_user(cursor, username, password):
    # Your authentication logic goes here
    cursor.execute(
        f"""
        SELECT * FROM user WHERE username = '{username}' AND password = '{password}'
        """
    )
    user_data = cursor.fetchone()
    return user_data


def signup(connection, cursor):
    insert_pelanggan.app(connection, cursor)


def logout_function(connection, cursor):
    st.session_state.clear()
    # st.markdown("""
    #     <style>
    #         section[data-testid="stSidebar"][aria-expanded="true"]{
    #             display: none;
    #         }
    #     </style>
    #     """, unsafe_allow_html=True)
    st.rerun()
    # login(cursor)


# Main function to manage the UI
def main(connection, cursor):
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Login", "Sign Up"])

    if page == "Login":
        login(cursor)  # Pass your cursor object here
    elif page == "Sign Up":
        signup(connection, cursor)
