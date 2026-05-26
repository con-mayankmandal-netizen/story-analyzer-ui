"""
StoryAnalyzer — Tool Page
Cinematic dark design + full Python backend (Drive + AI analysis)
"""
import streamlit as st
import json, sys, time
import pandas as pd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from modules.analyzer import init_client, analyze_single, compare_scripts
from modules.data    import load_and_aggregate, get_available_adset_codes, get_metrics_for_code, metrics_summary_text
from modules.drive   import get_drive_service, list_scripts_in_folder, extract_text_from_drive_file

# ── Session state defaults ────────────────────────────────────────────────────
for _k, _v in [("drive_svc", None), ("df_metrics", None), ("drive_scripts", {}), ("creds_dict", None)]:
    if _k not in st.session_state:
        st.session_state[_k] = _v

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Script Analyzer — StoryAnalyzer",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS — cinematic dark theme ─────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@200;300;400;500;600;700;800;900&family=DM+Serif+Display:ital@0;1&display=swap');

/* ── Base ── */
html, body, .stApp { background: #06040F !important; font-family: 'Outfit', sans-serif !important; color: #EDE9F8 !important; }
#MainMenu, footer, .stDeployButton { display: none !important; }
section[data-testid="stSidebar"] { display: none !important; }
header[data-testid="stHeader"]   { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
h1,h2,h3 { font-family: 'DM Serif Display', serif !important; color: #EDE9F8 !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 4px; } ::-webkit-scrollbar-track { background: #06040F; }
::-webkit-scrollbar-thumb { background: rgba(201,151,58,0.3); border-radius: 2px; }

/* ── File uploader ── */
[data-testid="stFileUploaderDropzone"] {
  background: rgba(19,16,38,0.4) !important;
  border: 1.5px dashed rgba(201,151,58,0.25) !important;
  border-radius: 12px !important; padding: 24px 16px !important;
  transition: all 0.3s !important;
}
[data-testid="stFileUploaderDropzone"]:hover {
  border-color: rgba(201,151,58,0.6) !important;
  background: rgba(19,16,38,0.7) !important;
  box-shadow: 0 0 30px rgba(201,151,58,0.1) !important;
}
[data-testid="stFileUploaderDropzoneInstructions"] p { color: #5A5478 !important; font-size: 13px !important; }
[data-testid="stFileUploader"] label { color: #EDE9F8 !important; font-size: 14px !important; font-weight: 500 !important; margin-bottom: 8px !important; }
[data-testid="stFileUploader"] small { color: #5A5478 !important; }

/* ── Text input ── */
[data-testid="stTextInput"] input {
  background: rgba(13,11,30,0.8) !important; border: 1px solid rgba(29,26,53,0.9) !important;
  border-radius: 10px !important; color: #EDE9F8 !important;
  font-family: 'Outfit', sans-serif !important; font-size: 14px !important; padding: 12px 16px !important;
}
[data-testid="stTextInput"] input:focus {
  border-color: rgba(201,151,58,0.5) !important; outline: none !important;
  box-shadow: 0 0 0 3px rgba(201,151,58,0.08) !important;
}
[data-testid="stTextInput"] label  { color: #EDE9F8 !important; font-size: 14px !important; font-weight: 500 !important; }

/* ── Multiselect ── */
[data-testid="stMultiSelect"] [data-baseweb="select"] > div:first-child {
  background: rgba(13,11,30,0.8) !important; border: 1px solid rgba(29,26,53,0.9) !important;
  border-radius: 10px !important; min-height: 48px !important;
}
[data-testid="stMultiSelect"] [data-baseweb="tag"] {
  background: rgba(124,58,237,0.15) !important; border: 1px solid rgba(124,58,237,0.3) !important;
  border-radius: 6px !important; color: #A855F7 !important;
}
[data-testid="stMultiSelect"] label { color: #EDE9F8 !important; font-size: 14px !important; font-weight: 500 !important; }
[data-baseweb="popover"] { background: #0D0B1E !important; border: 1px solid rgba(29,26,53,0.9) !important; }
[data-baseweb="menu"] { background: #0D0B1E !important; }
[data-baseweb="menu"] li:hover { background: rgba(201,151,58,0.08) !important; }

/* ── Radio ── */
[data-testid="stRadio"] label    { color: #EDE9F8 !important; font-size: 14px !important; }
[data-testid="stRadio"] > label  { font-size: 14px !important; font-weight: 500 !important; color: #EDE9F8 !important; }
[data-testid="stRadio"] [data-testid="stMarkdown"] p { color: #5A5478 !important; font-size: 12px !important; margin: 0 !important; }

/* ── Buttons ── */
[data-testid="stButton"] > button {
  background: linear-gradient(135deg, #C9973A, #E5C068) !important;
  color: #06040F !important; font-family: 'Outfit', sans-serif !important;
  font-weight: 700 !important; font-size: 15px !important;
  border: none !important; border-radius: 100px !important;
  padding: 14px 40px !important; width: 100% !important;
  cursor: pointer !important; transition: all 0.3s !important;
  box-shadow: 0 0 30px rgba(201,151,58,0.3) !important;
  letter-spacing: 0.02em !important;
}
[data-testid="stButton"] > button:hover {
  transform: scale(1.02) !important; box-shadow: 0 0 50px rgba(201,151,58,0.5) !important;
}
[data-testid="stButton"] > button:disabled { opacity: 0.4 !important; transform: none !important; }

/* ── Alerts ── */
[data-testid="stSuccess"] { background: rgba(16,185,129,0.08) !important; border: 1px solid rgba(16,185,129,0.2) !important; border-radius: 10px !important; color: #34d399 !important; }
[data-testid="stError"]   { background: rgba(239,68,68,0.08) !important;  border: 1px solid rgba(239,68,68,0.2) !important;  border-radius: 10px !important; color: #f87171 !important; }
[data-testid="stWarning"] { background: rgba(245,158,11,0.08) !important;  border: 1px solid rgba(245,158,11,0.2) !important;  border-radius: 10px !important; color: #fbbf24 !important; }
[data-testid="stInfo"]    { background: rgba(124,58,237,0.08) !important;  border: 1px solid rgba(124,58,237,0.2) !important;  border-radius: 10px !important; color: #A855F7 !important; }

/* ── Spinner ── */
.stSpinner > div { border-top-color: #C9973A !important; }

/* ── Progress bar ── */
[data-testid="stProgressBar"] > div > div { background: linear-gradient(90deg, #7C3AED, #C9973A) !important; }

/* ── Expander ── */
[data-testid="stExpander"] { background: rgba(19,16,38,0.5) !important; border: 1px solid rgba(29,26,53,0.8) !important; border-radius: 12px !important; }
[data-testid="stExpander"] summary { color: #EDE9F8 !important; }

/* ── Tabs ── */
[data-testid="stTabs"] [data-baseweb="tab"] { color: #5A5478 !important; font-family: 'Outfit', sans-serif !important; }
[data-testid="stTabs"] [aria-selected="true"] { color: #C9973A !important; border-bottom: 2px solid #C9973A !important; }

/* ── Wave bar animation ── */
@keyframes wavePulse { from { transform: scaleY(0.4); opacity: 0.5; } to { transform: scaleY(1); opacity: 1; } }
.wave-bar { animation: wavePulse var(--dur, 1.2s) ease-in-out var(--delay, 0s) infinite alternate; display: inline-block; width: 3px; border-radius: 2px; background: #C9973A; }
@keyframes pageFlip {
  0%   { transform: rotateY(0deg);   opacity: 1; }
  50%  { transform: rotateY(-140deg); opacity: 0.6; }
  100% { transform: rotateY(-180deg); opacity: 0; }
}

/* ── Step block spacing ── */
.sa-step-block { margin-bottom: 20px; }
</style>
""", unsafe_allow_html=True)


# ── Custom header (cinematic, matches tool.html) ──────────────────────────────
st.markdown("""
<div style="position:sticky; top:0; z-index:999; background:rgba(6,4,15,0.95);
            backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px);
            border-bottom:1px solid rgba(29,26,53,0.8);">

  <!-- Tagline strip -->
  <div style="padding:6px 32px; border-bottom:1px solid rgba(29,26,53,0.5);
              display:flex; align-items:center; justify-content:space-between;">
    <p style="font-size:11px; color:rgba(90,84,120,0.7); font-family:'Outfit',sans-serif; margin:0;">
      Open source &bull; AI-powered &bull; Built for
      <span style="color:#C9973A; font-weight:600;">PocketFM</span>'s creative &amp; performance marketing teams
    </p>
    <div style="display:flex; align-items:center; gap:8px;">
      <svg width="11" height="11" viewBox="0 0 24 24" fill="#A855F7">
        <path d="M5.042 15.165a2.528 2.528 0 0 1-2.52 2.523A2.528 2.528 0 0 1 0 15.165a2.527 2.527 0 0 1 2.522-2.52h2.52v2.52zM6.313 15.165a2.527 2.527 0 0 1 2.521-2.52 2.527 2.527 0 0 1 2.521 2.52v6.313A2.528 2.528 0 0 1 8.834 24a2.528 2.528 0 0 1-2.521-2.522v-6.313zM8.834 5.042a2.528 2.528 0 0 1-2.521-2.52A2.528 2.528 0 0 1 8.834 0a2.528 2.528 0 0 1 2.521 2.522v2.52H8.834zM8.834 6.313a2.528 2.528 0 0 1 2.521 2.521 2.528 2.528 0 0 1-2.521 2.521H2.522A2.528 2.528 0 0 1 0 8.834a2.528 2.528 0 0 1 2.522-2.521h6.312zM18.956 8.834a2.528 2.528 0 0 1 2.522-2.521A2.528 2.528 0 0 1 24 8.834a2.528 2.528 0 0 1-2.522 2.521h-2.522V8.834zM17.688 8.834a2.528 2.528 0 0 1-2.523 2.521 2.527 2.527 0 0 1-2.52-2.521V2.522A2.527 2.527 0 0 1 15.165 0a2.528 2.528 0 0 1 2.523 2.522v6.312zM15.165 18.956a2.528 2.528 0 0 1 2.523 2.522A2.528 2.528 0 0 1 15.165 24a2.527 2.527 0 0 1-2.52-2.522v-2.522h2.52zM15.165 17.688a2.527 2.527 0 0 1-2.52-2.523 2.526 2.526 0 0 1 2.52-2.52h6.313A2.527 2.527 0 0 1 24 15.165a2.528 2.528 0 0 1-2.522 2.523h-6.313z"/>
      </svg>
      <span style="font-size:11px; color:rgba(90,84,120,0.7);">by</span>
      <a href="https://pocket-fm.slack.com/team/U08NHRDM9M2" target="_blank"
         style="font-size:11px; color:#E5C068; font-weight:600; text-decoration:none;
                text-shadow:0 0 10px rgba(229,192,104,0.45);">Mayank Mandal</a>
    </div>
  </div>

  <!-- Nav -->
  <nav style="display:flex; align-items:center; justify-content:space-between; padding:10px 32px;">
    <a href="/" style="display:flex; align-items:center; gap:10px; text-decoration:none;">
      <div style="display:flex; align-items:flex-end; gap:2px; height:20px;">
        <div class="wave-bar" style="height:6px;  --dur:1.0s;"></div>
        <div class="wave-bar" style="height:14px; --dur:1.3s; --delay:0.12s;"></div>
        <div class="wave-bar" style="height:10px; --dur:1.1s; --delay:0.28s;"></div>
        <div class="wave-bar" style="height:18px; --dur:1.4s; --delay:0.08s;"></div>
        <div class="wave-bar" style="height:8px;  --dur:0.9s; --delay:0.22s;"></div>
      </div>
      <span style="font-family:'Outfit',sans-serif; font-weight:600; font-size:14px; color:#EDE9F8;">StoryAnalyzer</span>
      <span style="font-size:10px; color:#A855F7; background:rgba(168,85,247,0.12);
                   border:1px solid rgba(168,85,247,0.2); border-radius:4px; padding:2px 8px;">for PocketFM</span>
    </a>
    <div style="display:flex; align-items:center; gap:8px;">
      <a href="/" style="font-size:12px; color:#5A5478; text-decoration:none; padding:6px 12px;">Overview</a>
      <a href="/Help" style="font-size:12px; color:#5A5478; text-decoration:none; padding:6px 12px; display:flex; align-items:center; gap:4px;">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/></svg>
        Help
      </a>
      <a href="https://github.com/con-mayankmandal-netizen/story-analyzer" target="_blank"
         style="font-size:12px; font-weight:600; background:#7C3AED; color:#fff; text-decoration:none;
                padding:7px 18px; border-radius:100px;">GitHub</a>
    </div>
  </nav>
</div>

<!-- Quote banner -->
<div style="background:linear-gradient(90deg,rgba(124,58,237,0.08),rgba(6,4,15,0),rgba(201,151,58,0.06));
            border-bottom:1px solid rgba(29,26,53,0.4); padding:10px 32px;
            display:flex; align-items:center; gap:12px;">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#A855F7" stroke-width="2"
       style="flex-shrink:0; filter:drop-shadow(0 0 6px rgba(168,85,247,0.6));">
    <circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="3"/>
    <circle cx="12" cy="4.5" r="1" fill="#A855F7" stroke="none"/>
    <circle cx="12" cy="19.5" r="1" fill="#A855F7" stroke="none"/>
    <circle cx="4.5" cy="12" r="1" fill="#A855F7" stroke="none"/>
    <circle cx="19.5" cy="12" r="1" fill="#A855F7" stroke="none"/>
  </svg>
  <p id="banner-q" style="font-family:'DM Serif Display',serif; font-style:italic; font-size:13.5px;
     color:#E5C068; text-shadow:0 0 18px rgba(229,192,104,0.45),0 0 40px rgba(168,85,247,0.2);
     margin:0; flex:1; transition:opacity 0.5s;">
    "Every second of your audio ad is a creative decision. Stop shipping on instinct."
  </p>
</div>
<script>
  const quotes = [
    "Every second of your audio ad is a creative decision. Stop shipping on instinct.",
    "The difference between a scroll and a subscription is often one scene.",
    "CTR is the headline. ThruPlay is the truth.",
    "Meta ads don't fail on budget. They fail on the first eight words.",
    "The best hook doesn't tease — it promises.",
    "Data tells you what happened. The script tells you why.",
    "Your retention curve is a story. Read it.",
    "Stop guessing why your ad worked. Start knowing.",
    "Every drop in the retention funnel is a moment that failed to earn attention.",
    "Great promo writing is invisible — you feel the story, not the sell.",
  ];
  let qi = 0;
  setInterval(() => {
    const el = document.getElementById('banner-q');
    if (!el) return;
    el.style.opacity = '0';
    setTimeout(() => { qi = (qi+1)%quotes.length; el.textContent = '"' + quotes[qi] + '"'; el.style.opacity = '1'; }, 500);
  }, 5500);
</script>
""", unsafe_allow_html=True)


# ── Hero header ───────────────────────────────────────────────────────────────
st.markdown("""
<div style="padding:48px 32px 24px; background:linear-gradient(180deg,rgba(124,58,237,0.05) 0%,transparent 100%);">
  <div style="max-width:900px; margin:0 auto;">
    <div style="display:inline-flex; align-items:center; gap:8px; background:rgba(124,58,237,0.08);
                border:1px solid rgba(124,58,237,0.2); border-radius:100px; padding:5px 14px; margin-bottom:16px;">
      <span style="font-size:12px; color:#A855F7;">🎬 PocketFM Script Intelligence</span>
    </div>
    <h1 style="font-family:'DM Serif Display',serif; font-size:clamp(2rem,4vw,3.2rem);
               line-height:1.15; color:#EDE9F8; margin:0 0 12px;">
      Decode your <span style="color:#C9973A; font-style:italic;">Promo Story</span>
    </h1>
    <p style="color:#5A5478; font-size:15px; max-width:560px; line-height:1.7; margin:0;">
      Connect your data, load your scripts, choose your AI — get deep narrative insight on every
      audio ad. Analyse behaviour, stop guessing and start knowing why stories work.
    </p>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Divider ───────────────────────────────────────────────────────────────────
st.markdown('<div style="height:1px; background:linear-gradient(90deg,transparent,rgba(29,26,53,1),transparent); margin:0 32px;"></div>', unsafe_allow_html=True)

# ── Main layout: step tracker sidebar + content ───────────────────────────────
col_steps, col_main = st.columns([1, 3], gap="large")

# ─────────────────────────── STEP TRACKER SIDEBAR ────────────────────────────
with col_steps:
    st.markdown("""
    <div style="padding:24px 16px 24px 32px; position:sticky; top:140px;">
      <p style="font-size:10px; color:#5A5478; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:20px;">Workflow</p>

      <div style="display:flex; flex-direction:column; gap:0;">
        <!-- Step 1 -->
        <div style="display:flex; align-items:flex-start; gap:12px; padding-bottom:20px;">
          <div style="display:flex; flex-direction:column; align-items:center;">
            <div style="width:28px;height:28px;border-radius:50%;background:rgba(201,151,58,0.15);
                        border:1px solid rgba(201,151,58,0.4);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
              <span style="font-size:11px;color:#C9973A;font-weight:700;">1</span>
            </div>
            <div style="width:1px;flex:1;background:rgba(29,26,53,0.8);margin-top:4px;min-height:24px;"></div>
          </div>
          <div style="padding-top:4px;">
            <p style="font-size:13px;font-weight:600;color:#EDE9F8;margin:0;">Service Account</p>
            <p style="font-size:11px;color:#5A5478;margin:2px 0 0;">Upload JSON key</p>
          </div>
        </div>
        <!-- Step 2 -->
        <div style="display:flex; align-items:flex-start; gap:12px; padding-bottom:20px;">
          <div style="display:flex; flex-direction:column; align-items:center;">
            <div style="width:28px;height:28px;border-radius:50%;background:rgba(201,151,58,0.1);
                        border:1px solid rgba(29,26,53,0.8);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
              <span style="font-size:11px;color:#5A5478;font-weight:700;">2</span>
            </div>
            <div style="width:1px;flex:1;background:rgba(29,26,53,0.8);margin-top:4px;min-height:24px;"></div>
          </div>
          <div style="padding-top:4px;">
            <p style="font-size:13px;font-weight:600;color:#5A5478;margin:0;">Performance Data</p>
            <p style="font-size:11px;color:#5A5478;margin:2px 0 0;">Upload retention &amp; metrics Excel</p>
          </div>
        </div>
        <!-- Step 3 -->
        <div style="display:flex; align-items:flex-start; gap:12px; padding-bottom:20px;">
          <div style="display:flex; flex-direction:column; align-items:center;">
            <div style="width:28px;height:28px;border-radius:50%;background:rgba(201,151,58,0.1);
                        border:1px solid rgba(29,26,53,0.8);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
              <span style="font-size:11px;color:#5A5478;font-weight:700;">3</span>
            </div>
            <div style="width:1px;flex:1;background:rgba(29,26,53,0.8);margin-top:4px;min-height:24px;"></div>
          </div>
          <div style="padding-top:4px;">
            <p style="font-size:13px;font-weight:600;color:#5A5478;margin:0;">Drive Folder</p>
            <p style="font-size:11px;color:#5A5478;margin:2px 0 0;">Enter folder ID</p>
          </div>
        </div>
        <!-- Step 4 -->
        <div style="display:flex; align-items:flex-start; gap:12px; padding-bottom:20px;">
          <div style="display:flex; flex-direction:column; align-items:center;">
            <div style="width:28px;height:28px;border-radius:50%;background:rgba(201,151,58,0.1);
                        border:1px solid rgba(29,26,53,0.8);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
              <span style="font-size:11px;color:#5A5478;font-weight:700;">4</span>
            </div>
            <div style="width:1px;flex:1;background:rgba(29,26,53,0.8);margin-top:4px;min-height:24px;"></div>
          </div>
          <div style="padding-top:4px;">
            <p style="font-size:13px;font-weight:600;color:#5A5478;margin:0;">Select Scripts</p>
            <p style="font-size:11px;color:#5A5478;margin:2px 0 0;">Pick scripts to compare</p>
          </div>
        </div>
        <!-- Step 5 -->
        <div style="display:flex; align-items:flex-start; gap:12px;">
          <div style="width:28px;height:28px;border-radius:50%;background:rgba(124,58,237,0.1);
                      border:1px solid rgba(124,58,237,0.2);display:flex;align-items:center;justify-content:center;flex-shrink:0;">
            <span style="font-size:11px;color:#A855F7;font-weight:700;">5</span>
          </div>
          <div style="padding-top:4px;">
            <p style="font-size:13px;font-weight:600;color:#5A5478;margin:0;">Analyse</p>
            <p style="font-size:11px;color:#5A5478;margin:2px 0 0;">AI scores &amp; insights</p>
          </div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────── MAIN CONTENT ────────────────────────────────────
with col_main:
    st.markdown('<div style="padding:24px 32px 24px 0;">', unsafe_allow_html=True)

    # ── STEP 1: JSON Key ──────────────────────────────────────────────────────
    # Self-contained step header — complete opening AND closing div in one markdown call
    st.markdown("""
    <div class="sa-step-block">
      <div style="display:flex;align-items:center;gap:12px;padding:20px 24px 16px;
                  background:rgba(19,16,38,0.5);border:1px solid rgba(29,26,53,0.8);
                  border-radius:16px 16px 0 0;margin-bottom:0;">
        <div style="width:32px;height:32px;border-radius:8px;background:rgba(201,151,58,0.1);
                    border:1px solid rgba(201,151,58,0.2);display:flex;align-items:center;justify-content:center;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#C9973A" stroke-width="2">
            <rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>
          </svg>
        </div>
        <div style="flex:1;">
          <p style="font-size:14px;font-weight:600;color:#EDE9F8;margin:0;">Service Account JSON Key</p>
          <p style="font-size:11px;color:#5A5478;margin:0;">Required for Google Drive script fetching</p>
        </div>
        <span style="font-size:10px;color:#5A5478;background:rgba(29,26,53,0.6);
                     border:1px solid rgba(29,26,53,0.8);border-radius:4px;padding:3px 8px;">Step 1</span>
      </div>
      <div style="background:rgba(19,16,38,0.3);border:1px solid rgba(29,26,53,0.8);border-top:none;
                  border-radius:0 0 16px 16px;padding:16px 24px 20px;">
    </div>
    """, unsafe_allow_html=True)
    json_file = st.file_uploader("", type=["json"], key="json_upload",
                                  help="Download from Google Cloud Console → IAM → Service Accounts → Keys")
    st.markdown('</div>', unsafe_allow_html=True)

    # ── STEP 2: Excel Upload ──────────────────────────────────────────────────
    st.markdown("""
    <div class="sa-step-block">
      <div style="display:flex;align-items:center;gap:12px;padding:20px 24px 16px;
                  background:rgba(19,16,38,0.5);border:1px solid rgba(29,26,53,0.8);
                  border-radius:16px 16px 0 0;margin-bottom:0;">
        <div style="width:32px;height:32px;border-radius:8px;background:rgba(16,185,129,0.08);
                    border:1px solid rgba(16,185,129,0.15);display:flex;align-items:center;justify-content:center;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#34d399" stroke-width="2">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
            <polyline points="14 2 14 8 20 8"/>
            <line x1="16" y1="13" x2="8" y2="13"/>
            <line x1="16" y1="17" x2="8" y2="17"/>
            <polyline points="10 9 9 9 8 9"/>
          </svg>
        </div>
        <div style="flex:1;">
          <p style="font-size:14px;font-weight:600;color:#EDE9F8;margin:0;">Retention &amp; Performance Data</p>
          <p style="font-size:11px;color:#5A5478;margin:0;">Master tracker Excel — all campaign metrics</p>
        </div>
        <span style="font-size:10px;color:#5A5478;background:rgba(29,26,53,0.6);
                     border:1px solid rgba(29,26,53,0.8);border-radius:4px;padding:3px 8px;">Step 2</span>
      </div>
      <div style="background:rgba(19,16,38,0.3);border:1px solid rgba(29,26,53,0.8);border-top:none;
                  border-radius:0 0 16px 16px;padding:12px 24px 6px;">
        <div style="display:flex;flex-wrap:wrap;gap:6px;margin-bottom:12px;">
          <span style="font-size:11px;background:rgba(16,185,129,0.06);border:1px solid rgba(16,185,129,0.12);
                       border-radius:100px;padding:3px 10px;color:#34d399;">Adset Code</span>
          <span style="font-size:11px;background:rgba(16,185,129,0.06);border:1px solid rgba(16,185,129,0.12);
                       border-radius:100px;padding:3px 10px;color:#34d399;">ThruPlay %</span>
          <span style="font-size:11px;background:rgba(16,185,129,0.06);border:1px solid rgba(16,185,129,0.12);
                       border-radius:100px;padding:3px 10px;color:#34d399;">CTR</span>
          <span style="font-size:11px;background:rgba(16,185,129,0.06);border:1px solid rgba(16,185,129,0.12);
                       border-radius:100px;padding:3px 10px;color:#34d399;">CPI</span>
          <span style="font-size:11px;background:rgba(16,185,129,0.06);border:1px solid rgba(16,185,129,0.12);
                       border-radius:100px;padding:3px 10px;color:#34d399;">Retention Buckets</span>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    excel_file = st.file_uploader("", type=["xlsx", "xls"], key="excel_upload",
                                   help="The master tracker Excel with all Meta Ads performance data")
    st.markdown('<div style="height:8px;"></div>', unsafe_allow_html=True)

    # ── STEP 3: Drive Folder ID ───────────────────────────────────────────────
    st.markdown("""
    <div class="sa-step-block">
      <div style="display:flex;align-items:center;gap:12px;padding:20px 24px 16px;
                  background:rgba(19,16,38,0.5);border:1px solid rgba(29,26,53,0.8);
                  border-radius:16px 16px 0 0;margin-bottom:0;">
        <div style="width:32px;height:32px;border-radius:8px;background:rgba(59,130,246,0.08);
                    border:1px solid rgba(59,130,246,0.15);display:flex;align-items:center;justify-content:center;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#60a5fa" stroke-width="2">
            <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/>
          </svg>
        </div>
        <div style="flex:1;">
          <p style="font-size:14px;font-weight:600;color:#EDE9F8;margin:0;">Google Drive Folder ID</p>
          <p style="font-size:11px;color:#5A5478;margin:0;">The folder containing your .docx script files</p>
        </div>
        <span style="font-size:10px;color:#5A5478;background:rgba(29,26,53,0.6);
                     border:1px solid rgba(29,26,53,0.8);border-radius:4px;padding:3px 8px;">Step 3</span>
      </div>
      <div style="background:rgba(19,16,38,0.3);border:1px solid rgba(29,26,53,0.8);border-top:none;
                  border-radius:0 0 16px 16px;padding:16px 24px 8px;">
    </div>
    """, unsafe_allow_html=True)
    folder_id = st.text_input("", placeholder="e.g. 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs",
                               key="folder_id", help="From your Drive URL: drive.google.com/drive/folders/[FOLDER_ID]")
    st.markdown("""
    <p style="font-size:11px;color:#5A5478;margin:4px 0 0;padding:0 2px;">
      Open the folder in Drive → copy the ID from the URL after <code style="color:#C9973A;background:rgba(201,151,58,0.08);padding:1px 6px;border-radius:4px;">/folders/</code>
    </p>
    <div style="height:16px;"></div>
    """, unsafe_allow_html=True)

    # ── Load scripts from Drive ───────────────────────────────────────────────
    drive_scripts = st.session_state.drive_scripts
    df_metrics    = st.session_state.df_metrics
    warnings_list = []

    if json_file and excel_file and folder_id:
        # Load Excel
        try:
            st.session_state.df_metrics, warnings_list = load_and_aggregate(excel_file)
            st.markdown(f"""
            <div style="background:rgba(16,185,129,0.06);border:1px solid rgba(16,185,129,0.15);
                        border-radius:10px;padding:10px 14px;margin-bottom:12px;display:flex;align-items:center;gap:8px;">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#34d399" stroke-width="2">
                <polyline points="20 6 9 17 4 12"/>
              </svg>
              <span style="font-size:12px;color:#34d399;">Excel loaded — {len(st.session_state.df_metrics)} adsets found</span>
            </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Excel error: {e}")

        # Connect Drive
        try:
            st.session_state.creds_dict   = json.load(json_file)
            st.session_state.drive_svc    = get_drive_service(st.session_state.creds_dict)
            st.session_state.drive_scripts= list_scripts_in_folder(st.session_state.drive_svc, folder_id.strip())
            st.markdown(f"""
            <div style="background:rgba(16,185,129,0.06);border:1px solid rgba(16,185,129,0.15);
                        border-radius:10px;padding:10px 14px;margin-bottom:12px;display:flex;align-items:center;gap:8px;">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#34d399" stroke-width="2">
                <polyline points="20 6 9 17 4 12"/>
              </svg>
              <span style="font-size:12px;color:#34d399;">Drive connected — {len(st.session_state.drive_scripts)} scripts found</span>
            </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Drive connection error: {e}")

    # ── STEP 4: Select Scripts ────────────────────────────────────────────────
    st.markdown("""
    <div class="sa-step-block">
      <div style="display:flex;align-items:center;gap:12px;padding:20px 24px 16px;
                  background:rgba(19,16,38,0.5);border:1px solid rgba(29,26,53,0.8);
                  border-radius:16px 16px 0 0;margin-bottom:0;">
        <div style="width:32px;height:32px;border-radius:8px;background:rgba(168,85,247,0.08);
                    border:1px solid rgba(168,85,247,0.15);display:flex;align-items:center;justify-content:center;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#A855F7" stroke-width="2">
            <path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/>
          </svg>
        </div>
        <div style="flex:1;">
          <p style="font-size:14px;font-weight:600;color:#EDE9F8;margin:0;">Select Scripts to Compare</p>
          <p style="font-size:11px;color:#5A5478;margin:0;">Pick 1–4 scripts from your Drive folder</p>
        </div>
        <span style="font-size:10px;color:#5A5478;background:rgba(29,26,53,0.6);
                     border:1px solid rgba(29,26,53,0.8);border-radius:4px;padding:3px 8px;">Step 4</span>
      </div>
      <div style="background:rgba(19,16,38,0.3);border:1px solid rgba(29,26,53,0.8);border-top:none;
                  border-radius:0 0 16px 16px;padding:16px 24px 8px;">
    </div>
    """, unsafe_allow_html=True)

    script_options = list(st.session_state.drive_scripts.keys()) if st.session_state.drive_scripts else []
    selected_scripts = st.multiselect(
        "",
        options=script_options,
        max_selections=4,
        placeholder="Connect Drive first (Step 1–3) to see available scripts…",
        key="scripts_select",
        help="Select up to 4 scripts to compare side-by-side"
    )
    st.markdown('<div style="height:8px;"></div>', unsafe_allow_html=True)

    # ── STEP 5: AI + Analyse ─────────────────────────────────────────────────
    st.markdown("""
    <div class="sa-step-block">
      <div style="display:flex;align-items:center;gap:12px;padding:20px 24px 16px;
                  background:rgba(19,16,38,0.5);border:1px solid rgba(124,58,237,0.2);
                  border-radius:16px 16px 0 0;margin-bottom:0;">
        <div style="width:32px;height:32px;border-radius:8px;background:rgba(124,58,237,0.12);
                    border:1px solid rgba(124,58,237,0.25);display:flex;align-items:center;justify-content:center;">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#A855F7" stroke-width="2">
            <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>
          </svg>
        </div>
        <div style="flex:1;">
          <p style="font-size:14px;font-weight:600;color:#EDE9F8;margin:0;">AI Provider &amp; Analysis</p>
          <p style="font-size:11px;color:#5A5478;margin:0;">Choose your AI model and run the analysis</p>
        </div>
        <span style="font-size:10px;color:#A855F7;background:rgba(124,58,237,0.08);
                     border:1px solid rgba(124,58,237,0.2);border-radius:4px;padding:3px 8px;">Step 5</span>
      </div>
      <div style="background:rgba(19,16,38,0.3);border:1px solid rgba(124,58,237,0.15);border-top:none;
                  border-radius:0 0 16px 16px;padding:16px 24px 8px;">
    </div>
    """, unsafe_allow_html=True)

    ai_provider = st.radio(
        "AI Model",
        options=["gemini", "groq", "claude"],
        format_func=lambda x: {
            "gemini": "🟡 Gemini Flash — Free (1500 req/day, no card)",
            "groq":   "⚡ Groq Llama — Free (ultra-fast inference)",
            "claude": "🤖 Claude Haiku — Paid (~$0.001/run, best quality)"
        }[x],
        horizontal=True,
        key="ai_provider"
    )

    api_key = st.text_input(
        "API Key",
        type="password",
        placeholder={
            "gemini": "AIza... (get free key at aistudio.google.com)",
            "groq":   "gsk_... (get free key at console.groq.com)",
            "claude": "sk-ant-... (get key at console.anthropic.com)"
        }.get(ai_provider, ""),
        key="api_key"
    )
    st.markdown('<div style="height:8px;"></div>', unsafe_allow_html=True)

    # ── Analyse button ────────────────────────────────────────────────────────
    can_run = bool(json_file and excel_file and folder_id and selected_scripts and api_key
                   and st.session_state.df_metrics is not None
                   and st.session_state.drive_scripts
                   and st.session_state.drive_svc is not None)

    if not can_run:
        missing = []
        if not json_file:        missing.append("JSON key")
        if not excel_file:       missing.append("Excel file")
        if not folder_id:        missing.append("Drive folder ID")
        if not selected_scripts: missing.append("scripts selection")
        if not api_key:          missing.append("API key")
        if missing:
            st.markdown(f"""
            <div style="background:rgba(201,151,58,0.06);border:1px solid rgba(201,151,58,0.15);
                        border-radius:10px;padding:12px 16px;margin-bottom:16px;">
              <p style="font-size:12px;color:rgba(229,192,104,0.8);margin:0;">
                ⏳ Still needed: <strong>{", ".join(missing)}</strong>
              </p>
            </div>
            """, unsafe_allow_html=True)

    analyse_btn = st.button(
        "✦ Analyse Scripts" if can_run else "Complete all steps above to run analysis",
        disabled=not can_run,
        key="run_analysis"
    )

    # ── Run analysis ──────────────────────────────────────────────────────────
    if analyse_btn and can_run:
        analyses   = {}
        metrics_map= {}

        with st.spinner(""):
            st.markdown("""
            <div style="text-align:center;padding:32px 0;display:flex;flex-direction:column;align-items:center;gap:16px;">
              <div style="position:relative;width:48px;height:36px;perspective:90px;">
                <div style="position:absolute;inset:0;background:linear-gradient(135deg,#C9973A,#E5C068);border-radius:2px 4px 4px 2px;"></div>
                <div style="position:absolute;inset:0;background:rgba(237,233,248,0.9);transform-origin:left center;
                            animation:pageFlip 1.4s ease-in-out infinite;border-radius:0 4px 4px 0;"></div>
              </div>
              <p style="font-family:'DM Serif Display',serif;font-size:15px;color:#E5C068;font-style:italic;margin:0;">
                Decoding your scripts…
              </p>
            </div>
            """, unsafe_allow_html=True)

            progress = st.progress(0)
            init_client(api_key, ai_provider)

            for i, script_name in enumerate(selected_scripts):
                progress.progress(int((i / len(selected_scripts)) * 80))
                file_id     = st.session_state.drive_scripts[script_name]
                script_text = extract_text_from_drive_file(st.session_state.drive_svc, file_id)
                code        = script_name
                metrics_d   = get_metrics_for_code(st.session_state.df_metrics, code) if st.session_state.df_metrics is not None else {}
                metrics_txt = metrics_summary_text(metrics_d) if metrics_d else "No metrics found for this adset."
                metrics_map[code] = metrics_txt

                result = analyze_single(script_text, metrics_txt, code)
                analyses[code] = result

            progress.progress(90)

            # Comparison if multiple scripts
            comparison = None
            if len(selected_scripts) > 1:
                comparison = compare_scripts(analyses, metrics_map)

            progress.progress(100)
            time.sleep(0.3)
            progress.empty()

        # ── Results ───────────────────────────────────────────────────────────
        st.markdown("""
        <div style="margin-top:32px; padding:24px; background:rgba(124,58,237,0.05);
                    border:1px solid rgba(124,58,237,0.15); border-radius:16px; margin-bottom:24px;">
          <p style="font-family:'DM Serif Display',serif; font-size:22px; color:#EDE9F8; margin:0 0 4px;">
            Analysis Complete ✦
          </p>
          <p style="font-size:13px; color:#5A5478; margin:0;">
            AI-powered script intelligence powered by your real Meta Ads data
          </p>
        </div>
        """, unsafe_allow_html=True)

        # Comparison banner
        if comparison:
            winner = comparison.get("winner", "")
            reason = comparison.get("winner_reason", "")
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,rgba(201,151,58,0.12),rgba(124,58,237,0.08));
                        border:1px solid rgba(201,151,58,0.3);border-radius:14px;padding:20px 24px;margin-bottom:20px;">
              <div style="display:flex;align-items:center;gap:10px;margin-bottom:8px;">
                <span style="font-size:20px;">🏆</span>
                <p style="font-size:13px;color:#5A5478;margin:0;text-transform:uppercase;letter-spacing:0.06em;">Winner</p>
              </div>
              <p style="font-family:'DM Serif Display',serif;font-size:20px;color:#E5C068;margin:0 0 6px;">{winner}</p>
              <p style="font-size:13px;color:#EDE9F8;margin:0;line-height:1.6;">{reason}</p>
            </div>
            """, unsafe_allow_html=True)

        # Individual script results
        tabs = st.tabs([f"📄 {s}" for s in selected_scripts])
        for tab, script_name in zip(tabs, selected_scripts):
            with tab:
                r = analyses.get(script_name, {})
                if not r:
                    st.warning("No results for this script.")
                    continue

                overall = r.get("overall_score", 0)
                verdict = r.get("verdict", "")

                # Overall score hero — complete self-contained block
                color = "#34d399" if overall >= 70 else ("#fbbf24" if overall >= 50 else "#f87171")
                st.markdown(f"""
                <div style="padding:20px;background:rgba(19,16,38,0.6);border:1px solid rgba(29,26,53,0.8);
                            border-radius:14px;margin-bottom:20px;">
                  <div style="display:flex;align-items:center;gap:24px;flex-wrap:wrap;">
                    <div style="text-align:center;flex-shrink:0;">
                      <div style="width:80px;height:80px;border-radius:50%;display:flex;align-items:center;justify-content:center;
                                  background:conic-gradient({color} {overall*3.6}deg, rgba(29,26,53,0.8) 0deg);
                                  box-shadow:0 0 30px {color}33;">
                        <div style="width:64px;height:64px;border-radius:50%;background:#0D0B1E;
                                    display:flex;align-items:center;justify-content:center;">
                          <span style="font-size:22px;font-weight:800;color:{color};">{overall}</span>
                        </div>
                      </div>
                      <p style="font-size:10px;color:#5A5478;margin:6px 0 0;text-transform:uppercase;">Overall</p>
                    </div>
                    <div style="flex:1;min-width:180px;">
                      <p style="font-size:18px;font-family:'DM Serif Display',serif;color:#EDE9F8;margin:0 0 12px;">{verdict}</p>
                      <div style="display:flex;flex-wrap:wrap;gap:8px;">
                """, unsafe_allow_html=True)

                # Score pills — each is a complete self-contained block
                dims = [
                    ("hook_score",          "Hook",     "#C9973A"),
                    ("pacing_score",        "Pacing",   "#A855F7"),
                    ("emotional_arc_score", "Emotion",  "#60a5fa"),
                    ("cta_score",           "CTA",      "#34d399"),
                ]
                for key, label, col in dims:
                    val = r.get(key, 0)
                    st.markdown(f"""
                    <div style="background:rgba(19,16,38,0.8);border:1px solid rgba(29,26,53,0.9);
                                border-radius:8px;padding:8px 14px;text-align:center;min-width:70px;">
                      <p style="font-size:18px;font-weight:700;color:{col};margin:0;">{val}</p>
                      <p style="font-size:10px;color:#5A5478;margin:2px 0 0;">{label}</p>
                    </div>
                    """, unsafe_allow_html=True)

                st.markdown('</div></div></div></div>', unsafe_allow_html=True)

                # Dimension findings
                for dim_key, dim_label, dim_color, icon in [
                    ("hook",         "Hook Effectiveness",  "#C9973A", "🎯"),
                    ("pacing",       "Pacing",              "#A855F7", "⏱"),
                    ("emotional_arc","Emotional Arc",       "#60a5fa", "💫"),
                    ("cta",          "CTA Clarity",         "#34d399", "📣"),
                ]:
                    finding = r.get(f"{dim_key}_finding", "")
                    rec     = r.get(f"{dim_key}_recommendation", "")
                    score   = r.get(f"{dim_key}_score", 0)
                    with st.expander(f"{icon} {dim_label} — Score: {score}/100"):
                        st.markdown(f"""
                        <div style="padding:4px 0;">
                          <p style="font-size:12px;color:#5A5478;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:8px;">Finding</p>
                          <p style="font-size:14px;color:#EDE9F8;line-height:1.7;margin-bottom:16px;">{finding}</p>
                          <div style="background:rgba(16,185,129,0.05);border-left:3px solid #34d399;
                                      border-radius:0 8px 8px 0;padding:12px 16px;">
                            <p style="font-size:12px;color:#5A5478;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:4px;">Recommendation</p>
                            <p style="font-size:14px;color:#EDE9F8;line-height:1.6;margin:0;">{rec}</p>
                          </div>
                        </div>
                        """, unsafe_allow_html=True)

                # Top improvements
                improvements = r.get("top_3_improvements", [])
                if improvements:
                    st.markdown("""
                    <p style="font-size:13px;font-weight:600;color:#EDE9F8;margin:20px 0 10px;">
                      Top 3 Improvements
                    </p>
                    """, unsafe_allow_html=True)
                    for j, imp in enumerate(improvements, 1):
                        st.markdown(f"""
                        <div style="display:flex;gap:12px;padding:10px 14px;margin-bottom:8px;
                                    background:rgba(201,151,58,0.05);border:1px solid rgba(201,151,58,0.12);
                                    border-radius:8px;align-items:flex-start;">
                          <span style="font-size:13px;font-weight:700;color:#C9973A;flex-shrink:0;">{j}.</span>
                          <p style="font-size:13px;color:#EDE9F8;margin:0;line-height:1.6;">{imp}</p>
                        </div>
                        """, unsafe_allow_html=True)

                # Writer feedback
                feedback = r.get("writer_feedback", "")
                if feedback:
                    st.markdown(f"""
                    <div style="background:rgba(124,58,237,0.06);border:1px solid rgba(124,58,237,0.15);
                                border-radius:12px;padding:18px 20px;margin-top:16px;">
                      <p style="font-size:12px;color:#A855F7;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:8px;">Writer Feedback</p>
                      <p style="font-size:14px;color:#EDE9F8;line-height:1.7;margin:0;font-style:italic;">"{feedback}"</p>
                    </div>
                    """, unsafe_allow_html=True)

                # Retention correlation
                retention = r.get("retention_correlation", "")
                if retention:
                    with st.expander("📊 Retention Funnel Correlation"):
                        st.markdown(f'<p style="font-size:14px;color:#EDE9F8;line-height:1.7;">{retention}</p>', unsafe_allow_html=True)

        # Comparison deep dive
        if comparison and len(selected_scripts) > 1:
            st.markdown("""
            <div style="margin-top:32px;margin-bottom:16px;">
              <p style="font-family:'DM Serif Display',serif;font-size:20px;color:#EDE9F8;margin:0;">
                Comparative Intelligence
              </p>
            </div>
            """, unsafe_allow_html=True)

            col_a, col_b = st.columns(2)
            with col_a:
                replicate = comparison.get("what_to_replicate", [])
                st.markdown('<p style="font-size:13px;color:#34d399;font-weight:600;margin-bottom:8px;">✅ What to Replicate</p>', unsafe_allow_html=True)
                for item in replicate:
                    st.markdown(f'<div style="background:rgba(16,185,129,0.05);border:1px solid rgba(16,185,129,0.12);border-radius:8px;padding:10px 14px;margin-bottom:8px;font-size:13px;color:#EDE9F8;">{item}</div>', unsafe_allow_html=True)

            with col_b:
                avoid = comparison.get("what_to_avoid", [])
                st.markdown('<p style="font-size:13px;color:#f87171;font-weight:600;margin-bottom:8px;">🚫 What to Avoid</p>', unsafe_allow_html=True)
                for item in avoid:
                    st.markdown(f'<div style="background:rgba(239,68,68,0.05);border:1px solid rgba(239,68,68,0.12);border-radius:8px;padding:10px 14px;margin-bottom:8px;font-size:13px;color:#EDE9F8;">{item}</div>', unsafe_allow_html=True)

            pattern = comparison.get("pattern_insights", "")
            next_test = comparison.get("next_test_recommendation", "")
            if pattern:
                with st.expander("🔍 Pattern Insights"):
                    st.markdown(f'<p style="font-size:14px;color:#EDE9F8;line-height:1.7;">{pattern}</p>', unsafe_allow_html=True)
            if next_test:
                st.markdown(f"""
                <div style="background:linear-gradient(135deg,rgba(124,58,237,0.1),rgba(201,151,58,0.06));
                            border:1px solid rgba(124,58,237,0.2);border-radius:12px;padding:18px 20px;margin-top:8px;">
                  <p style="font-size:12px;color:#A855F7;text-transform:uppercase;letter-spacing:0.06em;margin-bottom:8px;">Next Test Recommendation</p>
                  <p style="font-size:14px;color:#EDE9F8;line-height:1.7;margin:0;">{next_test}</p>
                </div>
                """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="border-top:1px solid rgba(29,26,53,0.8);background:rgba(6,4,15,0.95);
            padding:32px;text-align:center;margin-top:48px;">
  <div style="display:flex;align-items:center;justify-content:center;gap:10px;margin-bottom:12px;">
    <span style="font-size:12px;color:rgba(90,84,120,0.7);">Designed &amp; Developed by</span>
    <a href="https://pocket-fm.slack.com/team/U08NHRDM9M2" target="_blank"
       style="display:inline-flex;align-items:center;gap:6px;text-decoration:none;
              background:rgba(201,151,58,0.08);border:1px solid rgba(201,151,58,0.25);
              border-radius:100px;padding:5px 14px 5px 10px;">
      <svg width="12" height="12" viewBox="0 0 24 24" fill="#A855F7">
        <path d="M5.042 15.165a2.528 2.528 0 0 1-2.52 2.523A2.528 2.528 0 0 1 0 15.165a2.527 2.527 0 0 1 2.522-2.52h2.52v2.52zM6.313 15.165a2.527 2.527 0 0 1 2.521-2.52 2.527 2.527 0 0 1 2.521 2.52v6.313A2.528 2.528 0 0 1 8.834 24a2.528 2.528 0 0 1-2.521-2.522v-6.313zM8.834 5.042a2.528 2.528 0 0 1-2.521-2.52A2.528 2.528 0 0 1 8.834 0a2.528 2.528 0 0 1 2.521 2.522v2.52H8.834zM8.834 6.313a2.528 2.528 0 0 1 2.521 2.521 2.528 2.528 0 0 1-2.521 2.521H2.522A2.528 2.528 0 0 1 0 8.834a2.528 2.528 0 0 1 2.522-2.521h6.312zM18.956 8.834a2.528 2.528 0 0 1 2.522-2.521A2.528 2.528 0 0 1 24 8.834a2.528 2.528 0 0 1-2.522 2.521h-2.522V8.834zM17.688 8.834a2.528 2.528 0 0 1-2.523 2.521 2.527 2.527 0 0 1-2.52-2.521V2.522A2.527 2.527 0 0 1 15.165 0a2.528 2.528 0 0 1 2.523 2.522v6.312zM15.165 18.956a2.528 2.528 0 0 1 2.523 2.522A2.528 2.528 0 0 1 15.165 24a2.527 2.527 0 0 1-2.52-2.522v-2.522h2.52zM15.165 17.688a2.527 2.527 0 0 1-2.52-2.523 2.526 2.526 0 0 1 2.52-2.52h6.313A2.527 2.527 0 0 1 24 15.165a2.528 2.528 0 0 1-2.522 2.523h-6.313z"/>
      </svg>
      <span style="font-size:13px;font-weight:700;color:#E5C068;">Mayank Mandal</span>
    </a>
  </div>
  <p style="font-size:10px;color:rgba(90,84,120,0.4);margin:0;">PocketFM Script Intelligence &bull; Open Source &bull; 2025</p>
</div>
""", unsafe_allow_html=True)
