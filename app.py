"""
StoryAnalyzer — Landing Page
Renders the cinematic HTML marketing page inside Streamlit.
"""
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="StoryAnalyzer — PocketFM Script Intelligence",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Hide all default Streamlit chrome ────────────────────────────────────────
st.markdown("""
<style>
#MainMenu, header, footer, .stDeployButton { display: none !important; }
section[data-testid="stSidebar"]           { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
iframe { border: none !important; }
</style>
""", unsafe_allow_html=True)

# ── Load index.html and patch navigation links for Streamlit routing ─────────
html = Path("index.html").read_text(encoding="utf-8")

# Patch href links → JS parent navigation so links work inside the iframe
patches = {
    'href="tool.html"':  'href="#" onclick="window.parent.location.href=\'/Tool\'; return false;"',
    'href="help.html"':  'href="#" onclick="window.parent.location.href=\'/Help\'; return false;"',
    'href="index.html"': 'href="#" onclick="window.parent.location.href=\'/\'; return false;"',
}
for old, new in patches.items():
    html = html.replace(old, new)

# ── Render ───────────────────────────────────────────────────────────────────
st.components.v1.html(html, height=9500, scrolling=True)
