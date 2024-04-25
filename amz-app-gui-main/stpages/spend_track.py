import streamlit as st
import finance_db
import pandas as pd
import tools

# Function to retrieve user data from session state
def get_user_data():
    return st.session_state.user_data

def run():
    if st.session_state.user_data is None:
        st.button("Sign Up", on_click=tools.change_page('signup'))
    else:
        conn = finance_db.connect_db()
        
        st.title("Your spends this month")
        sql = "SELECT * FROM spending"
        record = finance_db.read_record(conn, sql)
        
        df = pd.DataFrame(record, columns=["id", "Date", "Outcome", "Category", "Note"])
        df = df.drop(columns=["id"])

        # Display data in DataFrame format
        st.dataframe(df)
        
    


        
        
        
