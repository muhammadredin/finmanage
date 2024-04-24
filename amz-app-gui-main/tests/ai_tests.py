from joblib import load
import numpy as np

gp = load("GaussianModel.joblib")

age = 23
income = 2500000
expenses = 2000000
savings = 500000
loan = 200000
assets = 500000000

    # New input for prediction
X_new = np.array([[age, income, expenses, savings, loan, assets]])

    # Predictions for the new input
y_pred, y_std = gp.predict(X_new, return_std=True)

    # # Display the predicted results
    # st.subheader("Financial Projections:")

for i in range(len(X_new)):
    print("Prediction for input:", X_new[i])
    print("Foods:", y_pred[i, 0])
    print("House Bills:", y_pred[i, 1])
    print("Water & Electricity:", y_pred[i, 2])
    print("Entertainment:", y_pred[i, 3])
    print("Savings:", y_pred[i, 4])
    print("Insurance:", y_pred[i, 5])
    print("Transportation:", y_pred[i, 6])
    print("Education:", y_pred[i, 7])
    print("Emergency Fund:", y_pred[i, 8])
    print("Invest:", y_pred[i, 9])
    print("Partner:", y_pred[i, 10])
    print("---")