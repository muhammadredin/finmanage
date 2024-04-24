import streamlit as st
import tools
def run():
	st.write("# 🚀 AI-Powered Financial Management 📊")

	st.markdown("The project aims to develop an AI-based financial management and risk evaluation application for individuals with minimal financial literacy, especially those belonging to the middle to lower-income groups in Indonesia. This application will assist users in managing their personal finances by providing accurate financial projections and risk analysis based on microeconomic and macroeconomic factors such as interest rates and inflation.")

	st.button("Get Started ↗",on_click=tools.change_page('signup'))

	st.markdown(
	"""
	## Key Features
	- User can input their personal financial data, including income, expenses, and assets.
	- The application collects external data on inflation, interest rates, gold prices, and currency exchange rates from reliable sources.
	- Exploratory data analysis will be conducted to analyze and understand patterns and trends in financial data and other economic factors.
	- Various techniques such as regression, clustering, and large language models will be used in the modeling phase to develop an AI model that can project financial outcomes based on the available financial and economic data.
	- The model will predict future inflation, estimate changes in interest rates, and analyze other risk factors that may affect users' personal finances.
	- The model's performance and accuracy will be evaluated by comparing the financial projections with actual data and assessing the accuracy of the risk evaluations provided by the model.

	## Benefits
	- Accurate financial projections and detailed risk evaluations will help users make informed financial decisions.
	- The application will provide recommendations for asset diversification and financial management based on users' personal financial conditions and the prevailing economic conditions.
	- Users will be able to effectively manage their personal finances, reducing the risk of financial crises and poorly managed debts.

	By providing a practical solution for individuals with limited financial literacy, this project aims to empower users to manage their personal finances more effectively and mitigate the risks associated with financial crises and poorly managed debts.

	To learn more about the project:
	- Visit [project-github-repo](https://github.com/your-project-repo)
	- Read the documentation available at [project-docs](https://project-docs.com)
	- Join the community forums at [project-forums](https://project-forums.com)
	"""
	)