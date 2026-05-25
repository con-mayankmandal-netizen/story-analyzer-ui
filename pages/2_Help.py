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

# Force all elements visible (GSAP ScrollTrigger doesn't fire in iframe)
gsap_fix = """
<script>
(function() {
  function revealAll() {
    document.querySelectorAll('.reveal, .opacity-0, .fade-up').forEach(function(el) {
      el.style.opacity = '1'; el.style.transform = 'none';
    });
    if (window.gsap) gsap.set('.reveal, .fade-up', { opacity: 1, y: 0, clearProps: 'all' });
  }
  revealAll();
  setTimeout(revealAll, 300);
  setTimeout(revealAll, 800);
  window.addEventListener('load', revealAll);
})();
</script>
"""
html = html.replace('</body>', gsap_fix + '\n</body>')

st.components.v1.html(html, height=5000, scrolling=True)
