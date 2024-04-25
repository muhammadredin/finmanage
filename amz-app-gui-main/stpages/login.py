import streamlit as st
import tools
import time
import nosql_db

def set_session_state(user_data):
    st.session_state.user_data = user_data

def run():
	# Add the Login title
	st.title("Login")
	st.markdown("Login to access your personalized dashboard, where you'll discover a wealth of tools and resources designed to supercharge your financial decision-making.")

	table = nosql_db.connect_db()
	# Add the username and password input fields
	username = st.text_input("Username")
	password = st.text_input("Password", type="password")

	col1, col2 = st.columns((6,2.5))

	col2.button("Doesn't have an account?", on_click=tools.change_page('signup'))

	def reg():
		data = nosql_db.login_user(table, username, password)
		set_session_state(data)
	# Add the login button
	col1.button("Login", on_click=reg)
