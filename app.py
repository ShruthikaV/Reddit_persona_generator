import streamlit as st
from reddit_scraper import extract_username, scrape_reddit_user
from persona_generator import generate_persona
import base64

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(120deg, #f0f4f8, #d9e4f5);
        background-attachment: fixed;
    }
    .stApp {
    background-image: url("https://images.unsplash.com/photo-1522202176988-66273c2fd55f");
    background-size: cover;
    background-attachment: fixed;
    }
    .stApp > header {
        background-color: rgba(255, 255, 255, 0.8);
    }

    .block-container {
        padding: 2rem 3rem;
        background-color: rgba(0, 0, 0, 0.85);
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.5);
        max-width: 1000px;
        margin: auto;
        color: white;
    }


    .stTextInput > div > div > input {
        background-color: #f9f9f9;
    }

    .stButton > button {
        border-radius: 8px;
        border: none;
        font-weight: bold;
    }

    .stExpanderHeader {
        font-weight: bold;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#Page_config
st.set_page_config(
    page_title="Reddit Persona Generator",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="auto"
)

#Header
st.markdown("""
<style>
.big-title {
    font-size:48px !important;
    font-weight: bold;
    color: white;
}
.subtitle {
    font-size:20px !important;
    color: #5F6368;
}
.block-container {
    padding-top: 2rem;
}
.stButton > button {
    background-color: #6f42c1;
    color: white;
    font-weight: bold;
    padding: 0.5rem 1rem;
    border-radius: 0.5rem;
}
.stDownloadButton > button {
    background-color: #10b981;
    color: white;
    font-weight: bold;
    border-radius: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">🧠 Reddit Persona Generator</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Generate a detailed user persona from Reddit activity using Google Gemini AI</p>', unsafe_allow_html=True)

st.markdown("---")

# Input
st.markdown("### 🔗 Enter Reddit Profile URL")

url = st.text_input("Example: https://www.reddit.com/user/kojied/")

#Button&Logic
if st.button("🚀 Generate Persona") and url:
    try:
        with st.spinner("⏳ Scraping Reddit and generating persona using Gemini..."):
            username = extract_username(url)
            scrape_reddit_user(username)
            persona = generate_persona(username)

        st.success("✅ Persona generated successfully!")

        #Display
        st.markdown("### 🧾 Download Persona")
        st.download_button(
            "📥 Download TXT",
            data=persona,
            file_name=f"{username}_persona.txt"
        )
        st.download_button(
            "📥 Download PDF",
            data=open(f"output/{username}_persona.pdf", "rb").read(),
            file_name=f"{username}_persona.pdf"
        )

        st.markdown("---")
        st.markdown("### 🧠 Persona Preview")

        def render_pretty_persona(persona):
            sections = persona.split("**")
            for i in range(1, len(sections), 2):
                title = sections[i].strip()
                content = sections[i + 1].strip() if i + 1 < len(sections) else ""
                with st.expander(f"🔹 {title}"):
                    st.markdown(content, unsafe_allow_html=True)

        render_pretty_persona(persona)

    except Exception as e:
        st.error(f"❌ Something went wrong: {str(e)}")

st.markdown("---")
