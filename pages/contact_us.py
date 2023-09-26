import streamlit as st

st.header("Связаться со мной")

with st.form(key="email_forms"):
     user_email = st.text_input("Введите свою почту!")
     message = st.text_area("Ваше сообщение")
     button = st.form_submit_button()
     if button:
         print("Письмо отправлено")