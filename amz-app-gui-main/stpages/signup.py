import streamlit as st
import streamlit_authenticator as stauth
import tools
import boto3
from datetime import date
import finance_db
import nosql_db
import hashlib

def run():
    
	st.title("Sign Up")
	st.markdown("Sign up to unleash the potential of your money and embark on a journey towards financial empowerment.")
 
	table = nosql_db.connect_db()
 
	fullname = st.text_input("Full Name")
	username = st.text_input("Username")
	birthdate = st.date_input("Birthdate", min_value=date(1970, 1, 1))
	password = st.text_input("Password", type="password")
	verify_password = st.text_input("Verify Password", type="password")
	accept_terms = st.checkbox("I accept the terms and conditions")
    

	col1, col2 = st.columns((6,2.5))
	if col1.button("Sign Up"):
		if password != verify_password:
			st.error("Passwords do not match. Please try again.")
		elif not accept_terms:
			st.warning("Please accept the terms and conditions.")
		else:      
			registration = nosql_db.add_users(table, username, fullname, birthdate, password)
			if registration:
				tools.change_page("login")
			else:
				st.error("Registration failed. Please try again.")
				
	col2.button("Login", on_click=tools.change_page('login'))
