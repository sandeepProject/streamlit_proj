import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("Pandas & Matplotlib Example")
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.subheader("📄 Data Preview")
    st.write(data.head())
    fig, ax = plt.subplots()
    ax.bar(data['Country'], data['Gold'], color='blue')
    ax.set_xlabel("Country")
    ax.set_ylabel("Gold Medals")
    ax.set_title("Gold Medals by Country")
    plt.xticks(rotation=90)
    st.pyplot(fig)