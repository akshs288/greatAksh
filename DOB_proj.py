import streamlit as st
from datetime import date, datetime

st.title("Calculating users age")
user_date = st.date_input("Enter your date of birth", value=datetime.now(), min_value = date(1980, 1,1), max_value=datetime.now())

current_year = datetime.now().year
age = current_year - user_date.year
st.success(f"Your current age is {age}")