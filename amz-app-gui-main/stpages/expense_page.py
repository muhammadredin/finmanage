import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import time
import tools

def format_currency(value):
    # Add a '.' as a thousands separator and prepend with 'Rp '
    return f"Rp {value:,.0f}"

def run():
    st.title("Expense Allocation")
    st.write("Here are your expense allocation for this month (July 2023).")

    # Provided data
    categories = ['Food', 'House Bill', 'Water & Electricity', 'Entertainment',
                  'Savings', 'Insurance', 'Transport', 'Education', 'Emergency', 'Investment', 'Internet']
    data = [734000, 275000, 157000, 210000, 1389000, 184000, 275000, 144000, 511000, 1049000, 131000]

    # Calculate the total income
    total_income = 5243000

    # Calculate the percentage for each category relative to the Income
    percentages = [round((value / total_income) * 100, 2) for value in data]

    # Create a pie chart using Plotly
    fig = go.Figure(data=[go.Pie(labels=categories, values=percentages)])

    # Display the plot using Streamlit
    time.sleep(5)
    st.plotly_chart(fig)

    data_table = pd.DataFrame({
        'Category': categories,
        'Allocation': data
    })

    data_table['Allocation'] = data_table['Allocation'].apply(format_currency)
    # Display the table using Streamlit
    #data_table = data_table.reset_index(drop=True)
    st.dataframe(data_table, hide_index=True)
    
    st.write("Any question? Ask our chatbot!")
    st.button("Lets Go!",on_click=tools.change_page('chatbot'))
