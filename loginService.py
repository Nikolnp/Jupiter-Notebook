import streamlit as st
import requests

API_URL = 'https://'

def login():
  resp = request.post(f'{API_URL}/login', json = {
    'username':
    st.session_state.username,'password'})
    if resp.status_code == 200:
      st.session_state.token  =resp.json()['token']

if 'token' not in st.session_state:
  st.text_input('Password',
                type='password',key = 'password')
st.button('Login', on_click=login)

if 'token' in st.session_state:
  st.sucess('Logged in')
