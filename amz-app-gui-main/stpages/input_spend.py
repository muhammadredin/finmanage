import finance_db
import nosql_db
import streamlit as st

from datetime import date

def get_user_data():
    return st.session_state.user_data

def run():
    conn = finance_db.connect_db()
    nosql_conn = nosql_db.connect_db()

    st.title("Add Income")

    user_data = get_user_data()
    
    date_income = st.date_input("Income Date", min_value=date(1970, 1, 1))
        
    income = st.number_input("Money Received", min_value=0, step=100)

    income_options = ['Payday', 'Gift', 'Transaction', 'Etc.']

    income_category = st.selectbox("Income Category", income_options)

    income_note = st.text_input("Note", key="income_note")

    
    if st.button("Submit", key="income"):
        sql = "insert into incomes(username, date_received, money_received, category, note) VALUES (%s, %s, %s, %s, %s)"
        data = (user_data['username'], date_income, income, income_category, income_note)
        finance_db.create_record(conn, sql, data)
        response = nosql_conn.get_item(Key={'username': user_data['username']})

        if 'Item' in response:
            item = response['Item']
            item['account_balance'] += income
            table.put_item(Item=item)
        
        st.success("Record created successfully.")

    st.title("Add Outcome")
    date_spend = st.date_input("Spending Date", min_value=date(1970, 1, 1))
        
    outcome = st.number_input("Money Spend", min_value=0, step=100)

    outcome_options = ['Foods', 'Bills', 'Transportation', 'Entertainment', 'Etc.']

    outcome_category = st.selectbox("Category", outcome_options)

    spend_note = st.text_input("Note")

    if st.button("Submit"):
        sql = "insert into spending(username, date_spend, money_spend, category, note) VALUES (%s, %s, %s, %s, %s)"
        data = (user_data['username'], date_spend, outcome, outcome_category, spend_note)
        finance_db.create_record(conn, sql, data)

        if 'Item' in response:
            item = response['Item']
            item['account_balance'] -= outcome
            table.put_item(Item=item)
        
        st.success("Record created successfully.")
