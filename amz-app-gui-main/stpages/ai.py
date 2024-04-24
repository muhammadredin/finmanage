import streamlit as st
from joblib import load
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from tensorflow.keras.models import load_model

def run():
    # Load the model
    gp = load("backend/GaussianModel.joblib")

    # Streamlit UI
    st.title("Financial Projection Dashboard")

    # User input
    age = st.number_input("Enter your age:")
    income = st.number_input("Enter your monthly income:")
    expenses = st.number_input("Enter your monthly expenses:")
    savings = st.number_input("Enter your current savings:")
    loan = st.number_input("Enter your outstanding loan amount:")
    assets = st.number_input("Enter the value of your assets:")

    # New input for prediction
    # X_new = np.array([[age, income, expenses, savings, loan, assets]])

    # Predictions for the new input
    # y_pred, y_std = gp.predict(X_new, return_std=True)

    # # Display the predicted results
    # st.subheader("Financial Projections:")

    # for i in range(len(X_new)):
    #     st.write("Prediction for input:", X_new[i])
    #     st.write("Foods:", y_pred[i, 0])
    #     st.write("House Bills:", y_pred[i, 1])
    #     st.write("Water & Electricity:", y_pred[i, 2])
    #     st.write("Entertainment:", y_pred[i, 3])
    #     st.write("Savings:", y_pred[i, 4])
    #     st.write("Insurance:", y_pred[i, 5])
    #     st.write("Transportation:", y_pred[i, 6])
    #     st.write("Education:", y_pred[i, 7])
    #     st.write("Emergency Fund:", y_pred[i, 8])
    #     st.write("Invest:", y_pred[i, 9])
    #     st.write("Partner:", y_pred[i, 10])
    #     st.write("---")

    # # Visualization of Predicted vs Original Data (Assuming you have the necessary data)

    # st.subheader("Predicted vs Original Data Visualization:")

    # # Assuming your dataset has multiple features, you can choose one to plot
    # data = pd.read_csv('backend/FINPROJ_rev.csv')

    # # Remove rows with NaN values
    # data = data.dropna()

    # # Select only integer features
    # data = data.select_dtypes(exclude=['object']).copy()

    # # Extract input and output data
    # X = data.iloc[:-1, :].values
    # y = data.iloc[1:, :].values

    # # Scale the data
    # scaler = MinMaxScaler()
    # X_scaled = scaler.fit_transform(X)
    # y_scaled = scaler.transform(y)

    # # Reshape the data to match LSTM input shape [samples, time steps, features]
    # X_reshaped = np.reshape(X_scaled, (X_scaled.shape[0], 1, X_scaled.shape[1]))
    # y_reshaped = np.reshape(y_scaled, (y_scaled.shape[0], y_scaled.shape[1]))

    # # Split the data into training and test sets
    # test_size = int(len(X) * 0.02) # 20% of data as test set
    # X_train, X_test, y_train, y_test = X_reshaped[:-test_size], X_reshaped[-test_size:], y_reshaped[:-test_size], y_reshaped[-test_size:]

    # model = load_model('backend/tmp1.h5')
    # y_pred = model.predict(X_train)
    # y_pred_actual = scaler.inverse_transform(y_pred)
    # y_test_actual = scaler.inverse_transform(y_train)
    # feature_options = data.columns
    # selected_feature = st.selectbox("Select a feature to plot:", feature_options)

    # plt.figure(figsize=(10, 6))
    # plt.plot(y_test_actual[:, selected_feature], label='Original Data')
    # plt.plot(y_pred_actual[:, selected_feature], label='Predicted Data')
    # plt.xlabel('Time Step')
    # plt.ylabel('Value')
    # plt.title(f'Predicted vs Original Data for Feature {selected_feature}')
    # plt.legend()
    # plt.grid(True)
    # st.pyplot(plt)
