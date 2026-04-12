import streamlit as st
from datetime import date, datetime
from dateutil.relativedelta import relativedelta


st.title("Calculating users age")
user_date = st.date_input("Enter your date of birth", value=datetime.now(), min_value = date(1980, 1,1), max_value=datetime.now())

current_date = datetime.now()
main = relativedelta(current_date, user_date)
st.success(f"Your current age is {main.years} year {main.months} months {main.days} days")

