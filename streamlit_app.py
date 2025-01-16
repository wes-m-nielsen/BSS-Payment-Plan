import streamlit as st
import pandas as pd
from datetime import datetime
from datetime import timedelta
from datetime import date

st.title("Payment Plan Calculator")
st.write("For a customer intending to make regular repayments, enter the basic payment intention details and the app will calculate the full repayment schedule and clarify details.")

## USER INPUTS

st.divider()
st.subheader("Details")

purchase = int(st.number_input("Total amount to be repaid:"))
pay_amount = int(st.slider("Repayment amount:", 10, 1000, step = 5))
freq = st.radio("Frequency of repayments:", ["Weekly", "Fortnightly", "Four-weekly"])
start_date = st.date_input("Date of first repayment:", value="today")

no_pay = purchase/pay_amount

if freq == "Weekly":
    freq_index = 1
elif freq == "Fortnightly":
    freq_index = 2
elif freq == "Four-weekly":
    freq_index = 4

st.write("Starting on ", start_date, " there would be ", no_pay, " payments of ", pay_amount, " on a ", freq, "basis.")
st.write(freq_index)

## CALCULATIONS

# Fee calculation
if no_pay * freq_index >= 12:
    fee_total = purchase * 0.07
else: fee_total = 0

fee_weekly = fee_total / 52
end_date = start_date + timedelta(weeks = no_pay * freq_index + 1)

st.write("A weekly fee of ", fee_weekly, " (or ", fee_total, " in total) will apply. The last payment will be on:", end_date)