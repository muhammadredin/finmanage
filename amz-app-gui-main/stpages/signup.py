import streamlit as st
import streamlit_authenticator as stauth
import tools
from datetime import date
import finance_db

def run():
	st.title("Sign Up")
	st.markdown("Sign up to unleash the potential of your money and embark on a journey towards financial empowerment.")

	fullname = st.text_input("Full Name")
	username = st.text_input("Username")
	birthday = st.date_input("Birthday", min_value=date(1970, 1, 1))
	password = st.text_input("Password", type="password")
	verify_password = st.text_input("Verify Password", type="password")
	accept_terms = st.checkbox("I accept the terms and conditions")

	col1, col2 = st.columns((6,2.5))
	col1.button("Submit", on_click=tools.change_page("personalization"))
	col2.button("Already have an account?", on_click=tools.change_page('login'))
	'''if col1.button("Sign Up"):
		if password != verify_password:
			st.error("Passwords do not match. Please try again.")
		elif not accept_terms:
			st.warning("Please accept the terms and conditions.")
		else:
			#accounts = tools.Storage('accounts.json')
			#if accounts.get(username) == None:
				#st.success("Sign up successful!")
				#accounts.set(username, {"username":username, "birthday":str(birthday), "password":password})
			#tools.change_page('personalization')
			#else:
				#st.error("Username already exists. Please try again.")'''
