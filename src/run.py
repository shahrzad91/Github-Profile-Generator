import streamlit as st
from pathlib import Path

st.set_page_config(page_title="GitHub Profile Generator", page_icon="✨", layout="centered")

st.title("✨ GitHub Profile Generator")

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
    
    # 🔧 Extra Information
st.header("🛠️ Extra Profile Info")
with st.expander("Add optional content to enrich your profile"):
    project_name = st.text_input("Featured Project or Organization Name", placeholder="e.g. MyPortfolio, OpenMindAI")
    project_link = st.text_input("Project or Organization URL", placeholder="e.g. https://github.com/myportfolio")
    project_desc = st.text_area("Short Description of Project or Organization", placeholder="Describe what it does or why it matters...")

    book_title = st.text_input("What are you currently reading?", placeholder="e.g. Deep Learning with PyTorch")
    book_link = st.text_input("Book URL", placeholder="e.g. https://example.com/book-link")

    
    
# Select Theme#
st.header("🎨 Select a Theme")
theme_dir = Path("themes")
themes = [theme.name for theme in theme_dir.iterdir() if theme.is_file()]
theme = st.selectbox("Choose a theme file", themes)
st.markdown(f"**Selected Theme:** `{theme}`")


# Generate Readme  #
#st.header("📄 Generate Readme")



theme_path = Path("themes") / theme

if theme_path.exists():
    with open(theme_path, "r", encoding="utf-8") as f:
        template = f.read()

    profile = template.format(
        name=name,
        email=email,
        phone=phone,
        homepage=homepage,
        location=location,
        github=github,
        linkedin=linkedin,
        twitter=twitter,
        facebook=facebook,
        instagram=instagram,
        youtube=youtube,
        medium=medium,
        project_name=project_name,
        project_link=project_link,
        project_desc=project_desc,
        book_title=book_title,
        book_link=book_link
    )

    #st.code(profile, language="markdown")

    
else:
    st.error("❌ Selected theme file not found.")

if profile:
    st.header("📄 Generate Readme")
    #st.markdown("Copy the code below and paste it in your README.md file")

    st.markdown(profile, unsafe_allow_html=True)

    with st.expander("🔍 View as raw Markdown code"):
        st.code(profile, language="markdown")

  

