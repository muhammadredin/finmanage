import boto3
import hashlib
import streamlit as st

from boto3.dynamodb.conditions import Key
from decimal import Decimal


def connect_db():
    # Initialize DynamoDB client
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    # Define table name
    table_name = 'finapp_users'

    # Get reference to the DynamoDB table
    table = dynamodb.Table(table_name)
    
    return table

def add_users(table, username, fullname, birthdate, password, balance=0):
    # Check if username already exists
    response = table.query(
        KeyConditionExpression=Key('username').eq(username)
    )
    if response.get('Items'):
        st.error("Username already exists. Please choose a different username.")
        return False
    else:
        # Hash the password
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        # Store user information in DynamoDB
        table.put_item(Item={
            'username': username,  # This should be the username value
            'fullname': fullname,
            'birthdate': birthdate.isoformat(),
            'password': password_hash,
            'account_balance': balance,
            'budgets': {}
        })
        
        st.success("Registration successful. You can now log in.")
        return True
    
def login_user(table, username, password):
    # Retrieve user information from DynamoDB
    response = table.get_item(Key={'username': username})
    if 'Item' in response:
        # Verify password
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        if response['Item']['password'] == password_hash:
            st.success("Login successful.")
            return response['Item']
    st.error("Invalid username or password.")
    return False
