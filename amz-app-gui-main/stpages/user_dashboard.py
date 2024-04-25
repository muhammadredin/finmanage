import streamlit as st

# Function to clear user data from session state
def logout():
    st.session_state.user_data = None
    
def get_user_data():
    return st.session_state.user_data

def run():
    # Example usage
    user_data = get_user_data()
    if user_data:
        st.title(f"Hello, {user_data['fullname']}")
        st.title(f"Account Balance: {user_data['account_balance']}")
        st.write("This is your recent spending")
    # Create a button to logout
    if st.session_state.user_data:
        if st.button("Logout"):
            logout()
            st.success("You have been logged out successfully.")