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

# ── Load index.html ───────────────────────────────────────────────────────────
html = Path("index.html").read_text(encoding="utf-8")

# ── Patch navigation links for Streamlit routing ──────────────────────────────
patches = {
    'href="tool.html"':  'href="#" onclick="window.parent.location.href=\'/Tool\'; return false;"',
    'href="help.html"':  'href="#" onclick="window.parent.location.href=\'/Help\'; return false;"',
    'href="index.html"': 'href="#" onclick="window.parent.location.href=\'/\'; return false;"',
}
for old, new in patches.items():
    html = html.replace(old, new)

# ── Fix: GSAP ScrollTrigger doesn't fire inside iframe → force all elements visible ──
# Without this, every .reveal element stays at opacity:0 → page appears black
gsap_fix = """
<script>
(function() {
  function revealAll() {
    // Force all GSAP-animated elements visible
    var selectors = ['.reveal', '#hero-ctas', '#hero-stats', '#hero-tag',
                     '#hero-h1', '#hero-sub', '#marquee-wrapper',
                     '.opacity-0', '[style*="opacity: 0"]'];
    selectors.forEach(function(sel) {
      document.querySelectorAll(sel).forEach(function(el) {
        el.style.opacity    = '1';
        el.style.transform  = 'none';
        el.style.visibility = 'visible';
      });
    });

    // Kill GSAP ScrollTrigger if loaded, replace with instant reveals
    if (window.ScrollTrigger) { window.ScrollTrigger.killAll(); }
    if (window.gsap) {
      gsap.set('.reveal', { opacity: 1, y: 0, x: 0, clearProps: 'all' });
      gsap.set('#hero-ctas, #hero-stats, #hero-tag, #hero-h1, #hero-sub', { opacity: 1, y: 0, clearProps: 'all' });
    }
  }

  // Run immediately + after short delays to catch late-initialised elements
  revealAll();
  setTimeout(revealAll, 300);
  setTimeout(revealAll, 800);
  setTimeout(revealAll, 1500);

  // Also run once GSAP has loaded
  window.addEventListener('load', revealAll);
})();
</script>
"""
html = html.replace('</body>', gsap_fix + '\n</body>')

# ── Render ───────────────────────────────────────────────────────────────────
st.components.v1.html(html, height=9500, scrolling=True)
