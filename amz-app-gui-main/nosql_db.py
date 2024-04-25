import boto3
from decimal import Decimal


# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Define table name
table_name = 'finapp_users'

# Get reference to the DynamoDB table
table = dynamodb.Table(table_name)

# Example: Inserting a new item into the table
new_item = {
    'username': 'john_doe',  # This should be the username value
    'fullname': 'John Doe',
    'birthdate': '1990-01-01',
    'password': 'password123',
    'account_balance': Decimal('1000.00')
}

table.put_item(Item=new_item)

print("Item updated successfully.")
