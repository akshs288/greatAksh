import streamlit as st
import pywhatkit as pwt
from datetime import date as dt


st.header("Your timer")
st.subheader("Enter your number")
st.warning("Your whatsapp web should be connected to you whatsapp !!!")

col1 = st.columns(1)   # Return a list of columns

s1 = ""
with col1[0]:
    a = st.text_input("Type your number")
    if not a:
        print("you have typed nothing")
    else:
        if len(a) == 10 and a.isdigit():
            s1 = "+91"+ a
        else:
            st.error("You have clear mistake in your number please check again.")

st.subheader("Enter receiver's number")
s2 = ""
col2 = st.columns(1)   # Return a list of columns

with col2[0]:
    b = st.text_input("Type receivers number")
    if not b:
       st.warning("You have typed nothing")
    else:
        if len(b) == 10 and b.isdigit():
            s2 = "+91"+ b
        else:
            st.error("You have clear mistake in your number please check again.")

message = st.text_input("Type your message here ...")

col_a,col_b = st.columns(2)
with col_a:
    if st.button("Send Now"):
        if not message:
            st.error("Please write something in the message box !!!")
        else:
            pwt.sendwhatmsg_instantly(s2, message=message)
            st.success("Message sent successfully")

with col_b:
    date = st.date_input("Select date on which you want to send message")
    time = st.time_input("Select time at which you want to send message")
  
    if st.button("Send at time"):
     
        if not message:
            st.error("Please write something in the message box !!!")
        else:
     
            if date != dt.today():
                st.warning("Only today's scheduling is supported")

            else:
                hour = time.hour
                minute = time.minute  
                pwt.sendwhatmsg(s2, message,hour, minute)