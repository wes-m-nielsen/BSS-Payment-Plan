import streamlit as st

st.title("Payment Plan Calculator")
st.write(
    "For a customer intending to make regular repayments, enter the basic payment intention details and the app will calculate the full repayment schedule and clarify details."
)

# User Inputs

st.divider()

st.subheader("Details")

total = st.number_input("Total amount to be repaid:")
pay_freq = st.radio("Frequency of repayments:", ["Weekly", "Fortnightly", "Monthly", "Quarterly"])
pay_amount = st.slider("Repayment amount:", 10, 1000, step = 5)
start_date = st.date_input("Date of first re payment:", value="today")

st.divider()

st.button("Calculate")

# Calculations

