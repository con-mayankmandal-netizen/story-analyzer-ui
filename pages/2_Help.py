"""
StoryAnalyzer — Help & Contact Page (Native Streamlit)
"""
import streamlit as st

st.set_page_config(
    page_title="Help & Contact — StoryAnalyzer",
    page_icon="❓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@200;300;400;500;600;700;800;900&family=DM+Serif+Display:ital@0;1&display=swap');
html, body, .stApp { background: #06040F !important; font-family: 'Outfit', sans-serif !important; color: #EDE9F8 !important; }
#MainMenu, footer, .stDeployButton, header { display: none !important; }
section[data-testid="stSidebar"] { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
h1,h2,h3 { font-family: 'DM Serif Display', serif !important; color: #EDE9F8 !important; }
@keyframes wavePulse { from { transform:scaleY(0.4); opacity:0.5; } to { transform:scaleY(1); opacity:1; } }
@keyframes shimmer   { 0% { background-position:-200% center; } 100% { background-position:200% center; } }
@keyframes fadeUp    { from { opacity:0; transform:translateY(24px); } to { opacity:1; transform:translateY(0); } }
@keyframes ringPulse { 0%,100% { box-shadow:0 0 0 0 rgba(201,151,58,0.35); } 50% { box-shadow:0 0 0 10px rgba(201,151,58,0); } }
.wave-bar { display:inline-block;width:3px;border-radius:2px;background:#C9973A;
            animation:wavePulse var(--dur,1.2s) ease-in-out var(--delay,0s) infinite alternate; }
.name-shimmer { background:linear-gradient(90deg,#C9973A 0%,#E5C068 30%,#fff 50%,#E5C068 70%,#C9973A 100%);
                background-size:200% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;
                background-clip:text;animation:shimmer 4s linear infinite; }
.glass { background:rgba(19,16,38,0.7);backdrop-filter:blur(20px);border:1px solid rgba(29,26,53,0.9); }
.fade-1 { animation:fadeUp 0.7s ease 0.1s both; }
.fade-2 { animation:fadeUp 0.7s ease 0.25s both; }
.fade-3 { animation:fadeUp 0.7s ease 0.4s both; }
details summary { list-style:none; cursor:pointer; }
details summary::-webkit-details-marker { display:none; }
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="position:sticky;top:0;z-index:999;background:rgba(6,4,15,0.95);
            backdrop-filter:blur(20px);border-bottom:1px solid rgba(29,26,53,0.8);">
  <div style="padding:6px 40px;border-bottom:1px solid rgba(29,26,53,0.4);
              display:flex;align-items:center;justify-content:space-between;">
    <p style="font-size:11px;color:rgba(90,84,120,0.7);margin:0;">
      Open source &bull; AI-powered &bull; Built for
      <span style="color:#C9973A;font-weight:600;">PocketFM</span>
    </p>
    <a href="https://pocket-fm.slack.com/team/U08NHRDM9M2" target="_blank"
       style="font-size:11px;color:#E5C068;font-weight:600;text-decoration:none;">Mayank Mandal</a>
  </div>
  <nav style="display:flex;align-items:center;justify-content:space-between;padding:10px 40px;">
    <a href="/" style="display:flex;align-items:center;gap:10px;text-decoration:none;">
      <div style="display:flex;align-items:flex-end;gap:2px;height:20px;">
        <div class="wave-bar" style="height:6px;--dur:1.0s;"></div>
        <div class="wave-bar" style="height:14px;--dur:1.3s;--delay:0.12s;"></div>
        <div class="wave-bar" style="height:10px;--dur:1.1s;--delay:0.28s;"></div>
        <div class="wave-bar" style="height:18px;--dur:1.4s;--delay:0.08s;"></div>
        <div class="wave-bar" style="height:8px;--dur:0.9s;--delay:0.22s;"></div>
      </div>
      <span style="font-family:'Outfit',sans-serif;font-weight:600;font-size:15px;color:#EDE9F8;">StoryAnalyzer</span>
    </a>
    <div style="display:flex;align-items:center;gap:8px;">
      <a href="/"     style="font-size:13px;color:#5A5478;padding:6px 14px;text-decoration:none;">Overview</a>
      <a href="/Tool" style="font-size:13px;color:#5A5478;padding:6px 14px;text-decoration:none;">Tool</a>
      <a href="/Help" style="font-size:13px;color:#C9973A;font-weight:600;padding:6px 14px;text-decoration:none;">Help</a>
      <a href="https://github.com/con-mayankmandal-netizen/story-analyzer-ui" target="_blank"
         style="font-size:12px;font-weight:600;background:#7C3AED;color:#fff;
                padding:7px 18px;border-radius:100px;text-decoration:none;">GitHub</a>
    </div>
  </nav>
</div>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<section style="padding:60px 40px 40px;text-align:center;
                background:linear-gradient(180deg,rgba(124,58,237,0.05) 0%,transparent 100%);">
  <div class="fade-1" style="display:inline-flex;align-items:center;gap:8px;margin-bottom:16px;
       background:rgba(124,58,237,0.08);border:1px solid rgba(124,58,237,0.2);
       border-radius:100px;padding:5px 14px;">
    <span style="font-size:12px;color:#A855F7;">🎬 Help &amp; Contact</span>
  </div>
  <h1 class="fade-2" style="font-family:'DM Serif Display',serif;font-size:clamp(2rem,4vw,3.5rem);
      color:#EDE9F8;margin:0 0 12px;">
    Got a question?<br><span style="color:#C9973A;font-style:italic;">I'm here to help.</span>
  </h1>
  <p class="fade-3" style="font-size:15px;color:#5A5478;max-width:500px;margin:0 auto;line-height:1.7;">
    Built and maintained by a single developer at PocketFM. Reach out anytime.
  </p>
</section>
""", unsafe_allow_html=True)

# ── Developer card ────────────────────────────────────────────────────────────
st.markdown("""
<div style="max-width:800px;margin:0 auto;padding:0 40px 60px;">
  <div class="glass" style="border-radius:20px;overflow:hidden;
       box-shadow:0 0 60px rgba(124,58,237,0.12);">
    <div style="height:3px;background:linear-gradient(90deg,#7C3AED,#C9973A,#A855F7);"></div>
    <div style="padding:36px;">
      <div style="display:flex;align-items:center;gap:24px;margin-bottom:28px;flex-wrap:wrap;">

        <!-- Avatar -->
        <div style="width:96px;height:96px;border-radius:16px;flex-shrink:0;
                    display:flex;align-items:center;justify-content:center;
                    background:linear-gradient(135deg,rgba(124,58,237,0.25),rgba(201,151,58,0.15));
                    border:1.5px solid rgba(201,151,58,0.3);
                    animation:ringPulse 3s ease-in-out infinite;position:relative;">
          <span style="font-family:'DM Serif Display',serif;font-size:36px;color:#E5C068;">MM</span>
          <div style="position:absolute;bottom:-4px;right:-4px;width:18px;height:18px;
                      border-radius:50%;background:#22c55e;border:2px solid #06040F;
                      display:flex;align-items:center;justify-content:center;">
            <div style="width:8px;height:8px;border-radius:50%;background:#86efac;"></div>
          </div>
        </div>

        <!-- Name & role -->
        <div>
          <p style="font-size:11px;color:#5A5478;text-transform:uppercase;letter-spacing:0.1em;margin:0 0 4px;">Developer &amp; Maintainer</p>
          <h2 class="name-shimmer" style="font-family:'DM Serif Display',serif;font-size:2rem;margin:0 0 4px;">Mayank Mandal</h2>
          <p style="font-size:13px;color:#5A5478;margin:0 0 14px;">PocketFM · Creative &amp; Performance Marketing Tech</p>
          <div style="display:flex;flex-wrap:wrap;gap:8px;">
            <span style="font-size:11px;padding:3px 10px;border-radius:100px;
                         background:rgba(124,58,237,0.1);border:1px solid rgba(124,58,237,0.2);color:#A855F7;">Python</span>
            <span style="font-size:11px;padding:3px 10px;border-radius:100px;
                         background:rgba(201,151,58,0.08);border:1px solid rgba(201,151,58,0.2);color:#C9973A;">AI / LLMs</span>
            <span style="font-size:11px;padding:3px 10px;border-radius:100px;
                         background:rgba(29,26,53,0.6);border:1px solid rgba(29,26,53,0.9);color:#5A5478;">Streamlit</span>
            <span style="font-size:11px;padding:3px 10px;border-radius:100px;
                         background:rgba(16,185,129,0.06);border:1px solid rgba(16,185,129,0.15);color:#34d399;">Open Source</span>
          </div>
        </div>
      </div>

      <!-- Contact methods -->
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:0;
                  border-top:1px solid rgba(29,26,53,0.8);">

        <!-- Email -->
        <a href="mailto:con-mayank.mandal@pocketfm.com"
           style="text-decoration:none;padding:24px;border-right:1px solid rgba(29,26,53,0.6);
                  transition:background 0.3s;"
           onmouseover="this.style.background='rgba(13,11,30,0.6)'"
           onmouseout="this.style.background='transparent'">
          <div style="width:36px;height:36px;border-radius:10px;margin-bottom:12px;
                      display:flex;align-items:center;justify-content:center;
                      background:rgba(201,151,58,0.08);border:1px solid rgba(201,151,58,0.15);">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#C9973A" stroke-width="2">
              <rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
            </svg>
          </div>
          <p style="font-size:10px;color:#5A5478;text-transform:uppercase;letter-spacing:0.08em;margin:0 0 4px;">Email</p>
          <p style="font-size:13px;font-weight:600;color:#C9973A;margin:0 0 8px;">Send a mail</p>
          <p style="font-size:11px;color:#5A5478;font-family:'Outfit',sans-serif;margin:0;word-break:break-all;">
            con-mayank.mandal<br/>@pocketfm.com
          </p>
        </a>

        <!-- Slack -->
        <a href="https://pocket-fm.slack.com/team/U08NHRDM9M2" target="_blank"
           style="text-decoration:none;padding:24px;border-right:1px solid rgba(29,26,53,0.6);
                  transition:background 0.3s;"
           onmouseover="this.style.background='rgba(13,11,30,0.6)'"
           onmouseout="this.style.background='transparent'">
          <div style="width:36px;height:36px;border-radius:10px;margin-bottom:12px;
                      display:flex;align-items:center;justify-content:center;
                      background:rgba(168,85,247,0.08);border:1px solid rgba(168,85,247,0.15);">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="#A855F7">
              <path d="M5.042 15.165a2.528 2.528 0 0 1-2.52 2.523A2.528 2.528 0 0 1 0 15.165a2.527 2.527 0 0 1 2.522-2.52h2.52v2.52zM6.313 15.165a2.527 2.527 0 0 1 2.521-2.52 2.527 2.527 0 0 1 2.521 2.52v6.313A2.528 2.528 0 0 1 8.834 24a2.528 2.528 0 0 1-2.521-2.522v-6.313zM8.834 5.042a2.528 2.528 0 0 1-2.521-2.52A2.528 2.528 0 0 1 8.834 0a2.528 2.528 0 0 1 2.521 2.522v2.52H8.834zM8.834 6.313a2.528 2.528 0 0 1 2.521 2.521 2.528 2.528 0 0 1-2.521 2.521H2.522A2.528 2.528 0 0 1 0 8.834a2.528 2.528 0 0 1 2.522-2.521h6.312zM18.956 8.834a2.528 2.528 0 0 1 2.522-2.521A2.528 2.528 0 0 1 24 8.834a2.528 2.528 0 0 1-2.522 2.521h-2.522V8.834zM17.688 8.834a2.528 2.528 0 0 1-2.523 2.521 2.527 2.527 0 0 1-2.52-2.521V2.522A2.527 2.527 0 0 1 15.165 0a2.528 2.528 0 0 1 2.523 2.522v6.312zM15.165 18.956a2.528 2.528 0 0 1 2.523 2.522A2.528 2.528 0 0 1 15.165 24a2.527 2.527 0 0 1-2.52-2.522v-2.522h2.52zM15.165 17.688a2.527 2.527 0 0 1-2.52-2.523 2.526 2.526 0 0 1 2.52-2.52h6.313A2.527 2.527 0 0 1 24 15.165a2.528 2.528 0 0 1-2.522 2.523h-6.313z"/>
            </svg>
          </div>
          <p style="font-size:10px;color:#5A5478;text-transform:uppercase;letter-spacing:0.08em;margin:0 0 4px;">Slack</p>
          <p style="font-size:13px;font-weight:600;color:#A855F7;margin:0 0 8px;">Message on Slack</p>
          <div style="display:flex;align-items:center;gap:6px;">
            <div style="width:6px;height:6px;border-radius:50%;background:#22c55e;"></div>
            <p style="font-size:11px;color:#5A5478;margin:0;">Usually responds same day</p>
          </div>
        </a>

        <!-- GitHub -->
        <a href="https://github.com/con-mayankmandal-netizen/story-analyzer-ui" target="_blank"
           style="text-decoration:none;padding:24px;transition:background 0.3s;"
           onmouseover="this.style.background='rgba(13,11,30,0.6)'"
           onmouseout="this.style.background='transparent'">
          <div style="width:36px;height:36px;border-radius:10px;margin-bottom:12px;
                      display:flex;align-items:center;justify-content:center;
                      background:rgba(237,233,248,0.05);border:1px solid rgba(237,233,248,0.1);">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="#EDE9F8">
              <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/>
            </svg>
          </div>
          <p style="font-size:10px;color:#5A5478;text-transform:uppercase;letter-spacing:0.08em;margin:0 0 4px;">GitHub</p>
          <p style="font-size:13px;font-weight:600;color:#EDE9F8;margin:0 0 8px;">Open an Issue</p>
          <p style="font-size:11px;color:#5A5478;margin:0;">Bug reports &amp; feature requests</p>
        </a>

      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── FAQ ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="max-width:800px;margin:0 auto;padding:0 40px 80px;">
  <h2 style="font-family:'DM Serif Display',serif;font-size:1.8rem;text-align:center;margin-bottom:24px;color:#EDE9F8;">
    Common Questions
  </h2>
""", unsafe_allow_html=True)

faqs = [
    ("📄 What format should the JSON key file be in?",
     "It should be the <strong style='color:#C9973A;'>Google Cloud service account JSON key</strong> — downloaded from Google Cloud Console → IAM → Service Accounts → Keys. It contains fields like <code style='color:#E5C068;background:rgba(201,151,58,0.08);padding:1px 6px;border-radius:4px;'>client_email</code> and <code style='color:#E5C068;background:rgba(201,151,58,0.08);padding:1px 6px;border-radius:4px;'>private_key</code>."),
    ("📊 What columns does the retention Excel sheet need?",
     "The master tracker should contain: <strong style='color:#C9973A;'>Adset Code, ThruPlay %, CTR, CPI, Spend</strong> and retention buckets (0–25%, 25–50%, 50–75%, 75–95%). Contact Mayank if you need the template."),
    ("📁 Where do I find my Google Drive Folder ID?",
     "Open the folder in Google Drive and look at the URL:<br><code style='display:block;margin-top:8px;padding:10px 14px;background:rgba(201,151,58,0.06);border-radius:8px;font-size:12px;color:#E5C068;'>drive.google.com/drive/folders/<strong style='color:#fff;'>YOUR_FOLDER_ID_HERE</strong></code>"),
    ("🤖 Which AI model should I pick?",
     "<strong style='color:#C9973A;'>Gemini Flash</strong> — Free, great for general analysis.<br><strong style='color:#A855F7;'>Groq Llama</strong> — Ultra-fast, best for bulk comparisons.<br><strong style='color:#EDE9F8;'>Claude Haiku</strong> — Deepest insight, paid (~$0.001/run)."),
    ("🔒 Is my data safe? Who can see my scripts?",
     "Your JSON key and scripts are processed in your Streamlit session only — nothing is stored externally. Scripts are only sent to the AI provider you choose (Gemini/Groq/Claude) per their API privacy policies."),
]

for q, a in faqs:
    with st.expander(q):
        st.markdown(f'<p style="font-size:14px;color:#EDE9F8;line-height:1.75;margin:0;">{a}</p>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<footer style="border-top:1px solid rgba(29,26,53,0.8);background:rgba(6,4,15,0.95);
               padding:36px 40px;text-align:center;">
  <p style="font-size:11px;color:rgba(90,84,120,0.4);margin:0;">
    PocketFM Script Intelligence &bull; Developed by
    <a href="https://pocket-fm.slack.com/team/U08NHRDM9M2" target="_blank"
       style="color:#E5C068;font-weight:600;text-decoration:none;">Mayank Mandal</a>
    &bull; Open Source &bull; 2025
  </p>
</footer>
""", unsafe_allow_html=True)
