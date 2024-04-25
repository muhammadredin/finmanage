import streamlit as st
import tools
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import time
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
import boto3

def get_user_data():
    return st.session_state.user_data

def format_currency(value):
    # Add a '.' as a thousands separator and prepend with 'Rp '
    return f"Rp {value:,.0f}"

def run():
    st.title("Personalization Page")
    st.write("Please fill in your personal details.")

    # Field: Age
    age = st.number_input("Age", min_value=1, step=1)

    # Field: Marriage status
    marriage_status_options = ['Single', 'Married']
    marriage_status = st.selectbox("Marriage Status", marriage_status_options)

    # Field: Child
    child = st.number_input("Child", min_value=0, step=1)

    # Field: Country
    country_options = ['Indonesia']
    country = st.selectbox("Country", country_options)

    # Field: City
    city_options = ['Jakarta', 'Yogyakarta']
    city = st.selectbox("City", city_options)

    # Field: Number of children
    # num_children = st.number_input("Number of Children", min_value=0, max_value=10, step=1)

    # Field: Spending type
    # spending_type_options = ['Frugal', 'Big Spender']
    # spending_type = st.selectbox("Spending Type", spending_type_options)

    # Field: Monthly Income
    monthly_income = st.number_input("Monthly Income (in IDR)", min_value=0, step=100)

    if st.button("Submit"):
        with open('model/model_foods.pkl', 'rb') as f:
            foods_model = pickle.load(f)
        
        with open('model/model_house.pkl', 'rb') as f:
            house_model = pickle.load(f)
            
        with open('model/model_we.pkl', 'rb') as f:
            we_model = pickle.load(f)
        
        with open('model/model_ent.pkl', 'rb') as f:
            ent_model = pickle.load(f)
            
        with open('model/model_sav.pkl', 'rb') as f:
            sav_model = pickle.load(f)
            
        with open('model/model_ins.pkl', 'rb') as f:
            ins_model = pickle.load(f)
            
        with open('model/model_trans.pkl', 'rb') as f:
            trans_model = pickle.load(f)
        
        with open('model/model_edu.pkl', 'rb') as f:
            edu_model = pickle.load(f)
            
        with open('model/model_emg.pkl', 'rb') as f:
            emg_model = pickle.load(f)
            
        with open('model/model_inv.pkl', 'rb') as f:
            inv_model = pickle.load(f)
            
        with open('model/model_part.pkl', 'rb') as f:
            part_model = pickle.load(f)

        if marriage_status == 'Married':
            marriage_status = True
        else:
            marriage_status = False
            
        predict = {
            'Age': [int(age)],
            'Child': [int(child)],
            'Income': [int(monthly_income)],
            'Status_Single': [marriage_status],
            'Country_Indonesia': [True],
            'Region_Yogyakarta': [True]
        }
        
        predict = pd.DataFrame(predict)

        foods = foods_model.predict(predict)
        house = house_model.predict(predict)
        we = we_model.predict(predict)
        ent = ent_model.predict(predict)
        sav = sav_model.predict(predict)
        ins = ins_model.predict(predict)
        trans = trans_model.predict(predict)
        edu = edu_model.predict(predict)
        emg = emg_model.predict(predict)
        inv = inv_model.predict(predict)
        partner = part_model.predict(predict)
        
        st.title("Expense Allocation")
        st.write("Here are your expense allocation for this month.")
        
        leftovers = int(monthly_income) - int(foods[0] + house[0] + we[0] + ent[0] + sav[0] + ins[0] + trans[0] + edu[0] + emg[0] + inv[0] + partner[0])
        # Provided data
        categories = ['Food', 'House Bill', 'Water & Electricity', 'Entertainment',
                    'Savings', 'Insurance', 'Transport', 'Education', 'Emergency', 'Investment', 'Leftovers']
        
        data = [foods[0], house[0], we[0], ent[0], sav[0], ins[0], trans[0], 
                edu[0], emg[0], inv[0], leftovers]

        # Calculate the total income
        total_income = monthly_income

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
        
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

        # Define table name
        table_name = 'finapp_users'
    
        # Get reference to the DynamoDB table
        table = dynamodb.Table(table_name)
        user_data = get_user_data()
        
        # Fetch the item from the database
        response = table.get_item(Key={'username': user_data['username']})
        
        # Check if the item exists and has the 'budgets' attribute
        if 'Item' in response and 'budgets' in response['Item']:
            # Update the 'budgets' dictionary with new attributes
            budgets = response['Item']['budgets']
            budgets['foods'] = float(foods[0])
            budgets['house'] = float(house[0])
            budgets['bills'] = float(we[0])
            budgets['entertainment'] = float(ent[0])
            budgets['savings'] = float(sav[0])
            budgets['insurance'] = float(ins[0])
            budgets['transportation'] = float(trans[0])
            budgets['education'] = float(edu[0])
            budgets['emergency'] = float(emg[0])
            budgets['invest'] = float(inv[0])
            budgets['leftovers'] = float(leftovers)
        
            # Update the item with the modified 'budgets' dictionary
            response['Item']['budgets'] = budgets
            table.put_item(Item=response['Item'])
            print("Budgets updated successfully.")
        else:
            print("Item not found or 'budgets' attribute missing.")


        # Open a file in write mode ('w')
        # with open('output.txt', 'w') as f:
        #     f.write(f"This is the monthly income allocation u can preserve\n")
        #     f.write(f"{predictions[0][0]} for foods\n")
        #     f.write(f"{predictions[0][0]} for house bill\n")
        #     f.write(f"{predictions[0][0]} for water & electricity\n")
        #     f.write(f"{predictions[0][0]} for entertainment")

        st.write("Any question? Ask our chatbot!")
        st.button("Lets Go!",on_click=tools.change_page('chatbot'))
    # st.button("Submit",on_click=tools.change_page('expense_page'))
    st.button("Back",on_click=tools.change_page('dashboard'))

