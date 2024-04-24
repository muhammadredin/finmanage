import streamlit as st
import finance_db
import pandas as pd


def run():
    conn = finance_db.connect_db()
    
    st.title("Your spends this month")
    sql = "SELECT * FROM outcomes"
    record = finance_db.read_record(conn, sql)
    
    df = pd.DataFrame(record, columns=["id", "Date", "Outcome", "Category", "Note"])
    df = df.drop(columns=["id"])

    # Display data in DataFrame format
    st.dataframe(df)
        
        
        