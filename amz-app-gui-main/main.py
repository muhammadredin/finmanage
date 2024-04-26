import streamlit as st
from stpages import dashboard, signup, login, personalization, expense_page, chatbot, spend_track, input_spend, user_dashboard
import tools
import remove_footer

if __name__ == "__main__":
    # Initialization
    if 'page' not in st.session_state:
        st.set_page_config(page_title="AI Finance")
        st.session_state.page = 'dashboard'
    page = st.session_state.page

    if 'user_data' not in st.session_state:
        st.session_state.user_data = None

    if page == 'dashboard':
        dashboard.run()
    elif page == 'signup':
        signup.run()
    elif page == 'login':
        login.run()
    elif page == 'personalization':
        personalization.run()
    elif page == 'chatbot':
        expense_page.run()
    elif page == 'chatbot':
        chatbot.run()
    elif page == 'spend_track':
        spend_track.run()
    elif page == 'input_spend':
        input_spend.run()
    elif page == 'user_dashboard':
        user_dashboard.run()

    if page != None:
        st.sidebar.button("Introduction", on_click=tools.change_page('dashboard'))
        st.sidebar.button("User Dashboard", on_click=tools.change_page('user_dashboard'))
        #st.sidebar.markdown("Authentication")
        st.sidebar.button("Login Form", on_click=tools.change_page('login'))
        st.sidebar.button("Sign Up Form", on_click=tools.change_page('signup'))
        st.sidebar.button("Personalization", on_click=tools.change_page('personalization'))
        st.sidebar.button("Expense Allocation", on_click=tools.change_page("chatbot"))
        st.sidebar.button("Spend Track", on_click=tools.change_page("spend_track"))
        st.sidebar.button("Add Income/Outcome", on_click=tools.change_page("input_spend"))
    remove_footer.run()
