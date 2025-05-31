import streamlit as st

st.set_page_config(page_title="GitHub Profile Generator", page_icon="✨", layout="centered")

st.title("✨ GitHub Profile Readme Generator")

#  Personal Information#
st.header("👤 Personal Info")
with st.expander("Enter your personal info"):
    col1, col2 = st.columns(2)
    name = col1.text_input("Name")
    email = col2.text_input("Email")
    phone = col1.text_input("Phone")
    homepage = col2.text_input("Homepage")
    location = st.text_input("Location")

#  Social Media Account#
st.header("📱 Social Media")
with st.expander("Enter your social media usernames (not links):"):
    col1, col2 = st.columns(2)
    github = col1.text_input("GitHub")
    linkedin = col2.text_input("LinkedIn")
    twitter = col1.text_input("Twitter")
    facebook = col2.text_input("Facebook")
    instagram = col1.text_input("Instagram")
    youtube = col2.text_input("YouTube")
    medium = col1.text_input("Medium")
