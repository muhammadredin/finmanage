import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def main():
    st.title("Histogram Example")
    st.write("Generating a histogram with sample data.")

    # Generate random data
    np.random.seed(0)
    data = np.random.randn(1000)

    # Display histogram using Matplotlib
    fig, ax = plt.subplots()
    ax.hist(data, bins=30)

    # Display the plot using Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    main()
