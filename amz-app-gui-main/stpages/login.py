import streamlit as st
import tools
import time

def run():
	# Add the Login title
	st.title("Login")
	st.markdown("Login to access your personalized dashboard, where you'll discover a wealth of tools and resources designed to supercharge your financial decision-making.")

	# Add the username and password input fields
	username = st.text_input("Username")
	password = st.text_input("Password", type="password")

	col1, col2 = st.columns((6,2.5))

	col2.button("Doesn't have an account?", on_click=tools.change_page('signup'))

	def reg():
		accounts = tools.Storage('accounts.json')
		# Check if the username and password are valid
		if accounts.get(username) == None:
			st.error("Invalid username or password. Please try again.")
		elif accounts.get(username).get('password') != password:
			st.error("Invalid username or password. Please try again.")
		else:
			tools.change_page('expense_page')()
	# Add the login button
	col1.button("Login", on_click=reg)