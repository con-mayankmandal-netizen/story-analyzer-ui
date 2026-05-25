"""
StoryAnalyzer — Help & Contact Page
Renders the cinematic HTML help page inside Streamlit.
"""
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Help & Contact — StoryAnalyzer",
    page_icon="❓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
#MainMenu, header, footer, .stDeployButton { display: none !important; }
section[data-testid="stSidebar"]           { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
iframe { border: none !important; }
</style>
""", unsafe_allow_html=True)

html = Path("help.html").read_text(encoding="utf-8")

patches = {
    'href="tool.html"':  'href="#" onclick="window.parent.location.href=\'/Tool\'; return false;"',
    'href="help.html"':  'href="#" onclick="window.parent.location.href=\'/Help\'; return false;"',
    'href="index.html"': 'href="#" onclick="window.parent.location.href=\'/\'; return false;"',
}
for old, new in patches.items():
    html = html.replace(old, new)

st.components.v1.html(html, height=5000, scrolling=True)
