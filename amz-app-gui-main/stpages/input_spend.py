import finance_db
import streamlit as st

from datetime import date

def run():
    conn = finance_db.connect_db()
    
    date_spend = st.date_input("Spending Date", min_value=date(1970, 1, 1))
        
    outcome = st.number_input("Money Spend", min_value=0, step=100)

    outcome_options = ['Foods', 'Bills', 'Transportation', 'Entertainment', 'Etc.']

    outcome_category = st.selectbox("Category", outcome_options)

    spend_note = st.text_input("Note")

    if st.button("Submit"):
        sql = "insert into spending(date_spend, money_spend, category, note) VALUES (%s, %s, %s, %s)"
        data = (date_spend, outcome, outcome_category, spend_note)
        finance_db.create_record(conn, sql, data)
        st.success("Record created successfully.")
