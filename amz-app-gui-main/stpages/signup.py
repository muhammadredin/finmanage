import streamlit as st
import streamlit_authenticator as stauth
import tools
from datetime import date
import finance_db

def run():
	st.title("Sign Up")
	st.markdown("Sign up to unleash the potential of your money and embark on a journey towards financial empowerment.")
 
	conn = finance_db.connect_db()

	fullname = st.text_input("Full Name")
	username = st.text_input("Username")
	birthday = st.date_input("Birthday", min_value=date(1970, 1, 1))
	password = st.text_input("Password", type="password")
	verify_password = st.text_input("Verify Password", type="password")
	accept_terms = st.checkbox("I accept the terms and conditions")

	col1, col2 = st.columns((6,2.5))
	if col1.button("Sign Up", on_click=tools.change_page('personalization')):
		if password != verify_password:
			st.error("Passwords do not match. Please try again.")
		elif not accept_terms:
			st.warning("Please accept the terms and conditions.")
		else:      
			verify = finance_db.check_value_exists(username)
			if verify:
				st.error("Username already exists. Please try again.")
				
			else:
				sql = "insert into users(fullname, username, birthday, password) VALUES (%s, %s, %s, %s)"
				data = (fullname, username, birthday, password)
				finance_db.create_record(conn, sql, data)
				st.success("Sign up successful!")
				
	col2.button("Login", on_click=tools.change_page('login'))