import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📊",
    layout="wide",
)
st.logo("./img/round_analytics.png")

if "options" not in st.session_state:
    st.session_state.options = None

analytics_page = st.Page(
    "./app/analytics.py",
    title="Analytics Dashboard", 
)

ai_page = st.Page(
    "./app/ai_implementation.py",
    title="AI/ML Implementation", 
)

chat_page = st.Page(
    "./app/chat.py",
    title="Generative AI", 
)

data_page = st.Page(
    "./app/view_data.py",
    title="Raw Data", 
)

about_page = st.Page(
    "./app/about.py", 
    title="About the Data", 
)

selected_page = st.navigation([analytics_page, data_page, ai_page, chat_page, about_page])
selected_page.run()
