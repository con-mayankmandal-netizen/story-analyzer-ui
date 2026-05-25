"""
StoryAnalyzer — Landing Page (Native Streamlit)
Cinematic dark design built directly in Streamlit — no iframe needed.
"""
import streamlit as st

st.set_page_config(
    page_title="StoryAnalyzer — PocketFM Script Intelligence",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Full cinematic CSS ────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@200;300;400;500;600;700;800;900&family=DM+Serif+Display:ital@0;1&display=swap');

html, body, .stApp { background: #06040F !important; font-family: 'Outfit', sans-serif !important; color: #EDE9F8 !important; }
#MainMenu, footer, .stDeployButton, header { display: none !important; }
section[data-testid="stSidebar"] { display: none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
h1,h2,h3,h4 { font-family: 'DM Serif Display', serif !important; color: #EDE9F8 !important; }
a { text-decoration: none !important; }

::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #06040F; }
::-webkit-scrollbar-thumb { background: rgba(201,151,58,0.4); border-radius: 2px; }

/* ── Animations ── */
@keyframes wavePulse  { from { transform:scaleY(0.4); opacity:0.5; } to { transform:scaleY(1); opacity:1; } }
@keyframes floatOrb   { 0%,100% { transform:translateY(0) scale(1); } 50% { transform:translateY(-20px) scale(1.05); } }
@keyframes shimmer    { 0% { background-position:-200% center; } 100% { background-position:200% center; } }
@keyframes fadeUp     { from { opacity:0; transform:translateY(28px); } to { opacity:1; transform:translateY(0); } }
@keyframes marquee    { from { transform:translateX(0); } to { transform:translateX(-50%); } }
@keyframes pulse-ring { 0%,100% { box-shadow:0 0 0 0 rgba(201,151,58,0.3); } 50% { box-shadow:0 0 0 12px rgba(201,151,58,0); } }
@keyframes barWave    { from { transform:scaleY(0.3); opacity:0.4; } to { transform:scaleY(1); opacity:1; } }

.wave-bar { display:inline-block; width:3px; border-radius:2px; background:#C9973A;
            animation:barWave var(--dur,1.2s) ease-in-out var(--delay,0s) infinite alternate; }

.gold-shimmer { background:linear-gradient(90deg,#C9973A 0%,#E5C068 30%,#fff 50%,#E5C068 70%,#C9973A 100%);
                background-size:200% auto; -webkit-background-clip:text; -webkit-text-fill-color:transparent;
                background-clip:text; animation:shimmer 4s linear infinite; }

.fade-up-1 { animation:fadeUp 0.8s ease 0.1s both; }
.fade-up-2 { animation:fadeUp 0.8s ease 0.25s both; }
.fade-up-3 { animation:fadeUp 0.8s ease 0.4s both; }
.fade-up-4 { animation:fadeUp 0.8s ease 0.55s both; }
.fade-up-5 { animation:fadeUp 0.8s ease 0.7s both; }

.glass { background:rgba(19,16,38,0.7); backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px);
         border:1px solid rgba(29,26,53,0.9); }

.card-hover { transition:transform 0.3s ease, box-shadow 0.3s ease; }
.card-hover:hover { transform:translateY(-4px); box-shadow:0 20px 60px rgba(124,58,237,0.15); }

.btn-gold { display:inline-flex; align-items:center; gap:8px; background:linear-gradient(135deg,#C9973A,#E5C068);
            color:#06040F; font-weight:700; font-size:15px; padding:14px 36px; border-radius:100px;
            transition:all 0.3s; box-shadow:0 0 30px rgba(201,151,58,0.3); cursor:pointer; }
.btn-gold:hover { transform:scale(1.05); box-shadow:0 0 50px rgba(201,151,58,0.5); }

.btn-ghost { display:inline-flex; align-items:center; gap:8px; background:rgba(19,16,38,0.7);
             border:1px solid rgba(29,26,53,0.9); color:#EDE9F8; font-weight:500; font-size:15px;
             padding:14px 36px; border-radius:100px; transition:all 0.3s; }
.btn-ghost:hover { border-color:rgba(124,58,237,0.4); background:rgba(124,58,237,0.08); }

.score-ring { display:flex; flex-direction:column; align-items:center; gap:6px; }
.ring-wrap  { position:relative; width:56px; height:56px; }
.ring-bg    { fill:none; stroke:rgba(29,26,53,0.8); stroke-width:4; }
.ring-fill  { fill:none; stroke-width:4; stroke-linecap:round; transition:stroke-dashoffset 1s ease; transform:rotate(-90deg); transform-origin:center; }

.tag { display:inline-block; font-size:11px; padding:3px 12px; border-radius:100px;
       border:1px solid; font-weight:500; }

.orb { position:absolute; border-radius:50%; pointer-events:none; animation:floatOrb var(--dur,8s) ease-in-out var(--delay,0s) infinite; }

/* Marquee */
.marquee-track { display:flex; width:max-content; animation:marquee 28s linear infinite; }
.marquee-item  { display:flex; align-items:center; gap:8px; white-space:nowrap; padding:0 32px;
                 font-size:13px; color:#5A5478; font-family:'Outfit',sans-serif; }

/* Step card */
.step-card { background:rgba(19,16,38,0.5); border:1px solid rgba(29,26,53,0.8); border-radius:16px;
             padding:24px; transition:all 0.3s; }
.step-card:hover { border-color:rgba(201,151,58,0.2); background:rgba(19,16,38,0.8); }

/* Genre pill */
.genre-pill { display:inline-flex; align-items:center; gap:8px; padding:8px 20px; border-radius:100px;
              border:1px solid rgba(29,26,53,0.8); background:rgba(13,11,30,0.6); font-size:13px;
              color:#5A5478; cursor:pointer; transition:all 0.3s; margin:4px; }
.genre-pill:hover { border-color:rgba(201,151,58,0.3); color:#E5C068; background:rgba(201,151,58,0.06); }
</style>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
#  FIXED HEADER
# ════════════════════════════════════════════════════════════════
st.markdown("""
<div style="position:sticky;top:0;z-index:999;background:rgba(6,4,15,0.95);
            backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);
            border-bottom:1px solid rgba(29,26,53,0.8);">

  <!-- Tagline strip -->
  <div style="padding:6px 40px;border-bottom:1px solid rgba(29,26,53,0.4);
              display:flex;align-items:center;justify-content:space-between;">
    <p style="font-size:11px;color:rgba(90,84,120,0.7);margin:0;">
      Open source &bull; AI-powered &bull; Built for
      <span style="color:#C9973A;font-weight:600;">PocketFM</span>'s creative &amp; performance marketing teams
    </p>
    <div style="display:flex;align-items:center;gap:8px;">
      <svg width="11" height="11" viewBox="0 0 24 24" fill="#A855F7"><path d="M5.042 15.165a2.528 2.528 0 0 1-2.52 2.523A2.528 2.528 0 0 1 0 15.165a2.527 2.527 0 0 1 2.522-2.52h2.52v2.52zM6.313 15.165a2.527 2.527 0 0 1 2.521-2.52 2.527 2.527 0 0 1 2.521 2.52v6.313A2.528 2.528 0 0 1 8.834 24a2.528 2.528 0 0 1-2.521-2.522v-6.313zM8.834 5.042a2.528 2.528 0 0 1-2.521-2.52A2.528 2.528 0 0 1 8.834 0a2.528 2.528 0 0 1 2.521 2.522v2.52H8.834zM8.834 6.313a2.528 2.528 0 0 1 2.521 2.521 2.528 2.528 0 0 1-2.521 2.521H2.522A2.528 2.528 0 0 1 0 8.834a2.528 2.528 0 0 1 2.522-2.521h6.312zM18.956 8.834a2.528 2.528 0 0 1 2.522-2.521A2.528 2.528 0 0 1 24 8.834a2.528 2.528 0 0 1-2.522 2.521h-2.522V8.834zM17.688 8.834a2.528 2.528 0 0 1-2.523 2.521 2.527 2.527 0 0 1-2.52-2.521V2.522A2.527 2.527 0 0 1 15.165 0a2.528 2.528 0 0 1 2.523 2.522v6.312zM15.165 18.956a2.528 2.528 0 0 1 2.523 2.522A2.528 2.528 0 0 1 15.165 24a2.527 2.527 0 0 1-2.52-2.522v-2.522h2.52zM15.165 17.688a2.527 2.527 0 0 1-2.52-2.523 2.526 2.526 0 0 1 2.52-2.52h6.313A2.527 2.527 0 0 1 24 15.165a2.528 2.528 0 0 1-2.522 2.523h-6.313z"/></svg>
      <span style="font-size:11px;color:rgba(90,84,120,0.6);">by</span>
      <a href="https://pocket-fm.slack.com/team/U08NHRDM9M2" target="_blank"
         style="font-size:11px;color:#E5C068;font-weight:600;text-shadow:0 0 10px rgba(229,192,104,0.4);">Mayank Mandal</a>
    </div>
  </div>

  <!-- Nav -->
  <nav style="display:flex;align-items:center;justify-content:space-between;padding:10px 40px;">
    <div style="display:flex;align-items:center;gap:10px;">
      <div style="display:flex;align-items:flex-end;gap:2px;height:20px;">
        <div class="wave-bar" style="height:6px;--dur:1.0s;"></div>
        <div class="wave-bar" style="height:14px;--dur:1.3s;--delay:0.12s;"></div>
        <div class="wave-bar" style="height:10px;--dur:1.1s;--delay:0.28s;"></div>
        <div class="wave-bar" style="height:18px;--dur:1.4s;--delay:0.08s;"></div>
        <div class="wave-bar" style="height:8px;--dur:0.9s;--delay:0.22s;"></div>
      </div>
      <span style="font-family:'Outfit',sans-serif;font-weight:600;font-size:15px;color:#EDE9F8;">StoryAnalyzer</span>
    </div>
    <div style="display:flex;align-items:center;gap:8px;">
      <a href="#features"  style="font-size:13px;color:#5A5478;padding:6px 14px;transition:color 0.2s;"
         onmouseover="this.style.color='#EDE9F8'" onmouseout="this.style.color='#5A5478'">Features</a>
      <a href="#howitworks" style="font-size:13px;color:#5A5478;padding:6px 14px;transition:color 0.2s;"
         onmouseover="this.style.color='#EDE9F8'" onmouseout="this.style.color='#5A5478'">How It Works</a>
      <a href="/Help" style="font-size:13px;color:#5A5478;padding:6px 14px;transition:color 0.2s;"
         onmouseover="this.style.color='#EDE9F8'" onmouseout="this.style.color='#5A5478'">Help</a>
      <a href="/Tool" class="btn-gold" style="font-size:13px;padding:9px 24px;">Analyze a Script &rarr;</a>
    </div>
  </nav>
</div>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
#  HERO
# ════════════════════════════════════════════════════════════════
st.markdown("""
<section style="position:relative;overflow:hidden;padding:80px 40px 60px;
                background:linear-gradient(180deg,rgba(124,58,237,0.06) 0%,transparent 60%);">

  <!-- Background orbs -->
  <div class="orb" style="width:500px;height:500px;top:-100px;right:-80px;--dur:10s;--delay:0s;
       background:radial-gradient(circle,rgba(124,58,237,0.1) 0%,transparent 70%);"></div>
  <div class="orb" style="width:400px;height:400px;bottom:-60px;left:-60px;--dur:8s;--delay:2s;
       background:radial-gradient(circle,rgba(201,151,58,0.07) 0%,transparent 70%);"></div>

  <div style="max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center;">

    <!-- Left: Text -->
    <div>
      <div class="fade-up-1" style="display:inline-flex;align-items:center;gap:8px;margin-bottom:20px;
           background:rgba(124,58,237,0.08);border:1px solid rgba(124,58,237,0.2);
           border-radius:100px;padding:6px 16px;">
        <span style="font-size:12px;color:#A855F7;font-weight:500;">🎬 PocketFM Script Intelligence</span>
      </div>

      <h1 class="fade-up-2" style="font-family:'DM Serif Display',serif;font-size:clamp(2.4rem,4.5vw,4rem);
          line-height:1.1;color:#EDE9F8;margin:0 0 8px;">
        Decode your
      </h1>
      <h1 class="fade-up-2" style="font-family:'DM Serif Display',serif;font-size:clamp(2.4rem,4.5vw,4rem);
          line-height:1.1;margin:0 0 24px;">
        <span style="color:#C9973A;font-style:italic;">Promo Story</span>
      </h1>

      <p class="fade-up-3" style="font-size:16px;color:#5A5478;line-height:1.75;max-width:480px;margin-bottom:36px;">
        Connect your data, load your scripts, choose your AI — get deep narrative
        insight on every audio ad. Stop guessing. Start knowing why stories work.
      </p>

      <div class="fade-up-4" style="display:flex;gap:16px;flex-wrap:wrap;margin-bottom:40px;">
        <a href="/Tool" class="btn-gold">✦ Analyze a Script</a>
        <a href="#howitworks" class="btn-ghost">See How It Works</a>
      </div>

      <!-- Stats -->
      <div class="fade-up-5" style="display:flex;gap:32px;padding-top:28px;
           border-top:1px solid rgba(29,26,53,0.8);">
        <div>
          <p style="font-size:26px;font-weight:800;color:#C9973A;margin:0;font-family:'Outfit',sans-serif;">5</p>
          <p style="font-size:11px;color:#5A5478;margin:2px 0 0;text-transform:uppercase;letter-spacing:0.05em;">Analysis Dimensions</p>
        </div>
        <div>
          <p style="font-size:26px;font-weight:800;color:#A855F7;margin:0;font-family:'Outfit',sans-serif;">3</p>
          <p style="font-size:11px;color:#5A5478;margin:2px 0 0;text-transform:uppercase;letter-spacing:0.05em;">AI Providers</p>
        </div>
        <div>
          <p style="font-size:26px;font-weight:800;color:#EDE9F8;margin:0;font-family:'Outfit',sans-serif;">4</p>
          <p style="font-size:11px;color:#5A5478;margin:2px 0 0;text-transform:uppercase;letter-spacing:0.05em;">Scripts at once</p>
        </div>
      </div>
    </div>

    <!-- Right: Live Dashboard Card -->
    <div class="fade-up-3">
      <div class="glass card-hover" style="border-radius:20px;overflow:hidden;
           box-shadow:0 0 80px rgba(124,58,237,0.15),0 0 160px rgba(201,151,58,0.06);">
        <!-- Card header -->
        <div style="padding:16px 20px;border-bottom:1px solid rgba(29,26,53,0.8);
                    display:flex;align-items:center;justify-content:space-between;">
          <div style="display:flex;align-items:center;gap:8px;">
            <div style="width:8px;height:8px;border-radius:50%;background:#ef4444;"></div>
            <div style="width:8px;height:8px;border-radius:50%;background:#f59e0b;"></div>
            <div style="width:8px;height:8px;border-radius:50%;background:#22c55e;"></div>
          </div>
          <span style="font-size:11px;color:#5A5478;font-family:'Outfit',sans-serif;">GAI647 — Analysis Complete</span>
          <span style="font-size:10px;background:rgba(34,197,94,0.1);color:#22c55e;
                       border:1px solid rgba(34,197,94,0.2);border-radius:4px;padding:2px 8px;">Live</span>
        </div>

        <!-- Score rings -->
        <div style="padding:24px 20px;">
          <div style="display:flex;justify-content:space-around;margin-bottom:20px;">
""", unsafe_allow_html=True)

# Score rings
dims = [
    ("Hook",    82, "#C9973A", 100),
    ("Pacing",  74, "#A855F7", 100),
    ("Emotion", 88, "#60a5fa", 100),
    ("CTA",     71, "#34d399", 100),
    ("Story",   79, "#f472b6", 100),
]
circ = 2 * 3.14159 * 16
for label, score, color, _ in dims:
    offset = circ * (1 - score/100)
    st.markdown(f"""
    <div class="score-ring">
      <svg width="44" height="44" viewBox="0 0 44 44">
        <circle class="ring-bg" cx="22" cy="22" r="16"/>
        <circle class="ring-fill" cx="22" cy="22" r="16" stroke="{color}"
          stroke-dasharray="{circ:.1f}" stroke-dashoffset="{offset:.1f}"/>
      </svg>
      <span style="font-size:15px;font-weight:800;color:{color};font-family:'Outfit',sans-serif;">{score}</span>
      <span style="font-size:10px;color:#5A5478;text-transform:uppercase;letter-spacing:0.05em;">{label}</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
          </div>

          <!-- Verdict -->
          <div style="background:rgba(201,151,58,0.06);border:1px solid rgba(201,151,58,0.15);
                      border-radius:10px;padding:12px 14px;margin-bottom:14px;">
            <p style="font-size:11px;color:#5A5478;margin:0 0 4px;text-transform:uppercase;letter-spacing:0.05em;">Verdict</p>
            <p style="font-size:13px;color:#EDE9F8;margin:0;font-family:'DM Serif Display',serif;font-style:italic;">
              "Strong hook, emotional drop at 60s. CTA clarity needs tightening."
            </p>
          </div>

          <!-- Mini retention bars -->
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
            <div style="background:rgba(13,11,30,0.8);border-radius:8px;padding:10px 12px;">
              <p style="font-size:10px;color:#5A5478;margin:0 0 6px;">ThruPlay %</p>
              <div style="height:4px;background:rgba(29,26,53,0.8);border-radius:2px;">
                <div style="height:4px;width:68%;background:linear-gradient(90deg,#7C3AED,#A855F7);border-radius:2px;"></div>
              </div>
              <p style="font-size:12px;color:#A855F7;font-weight:700;margin:4px 0 0;">68%</p>
            </div>
            <div style="background:rgba(13,11,30,0.8);border-radius:8px;padding:10px 12px;">
              <p style="font-size:10px;color:#5A5478;margin:0 0 6px;">CTR</p>
              <div style="height:4px;background:rgba(29,26,53,0.8);border-radius:2px;">
                <div style="height:4px;width:42%;background:linear-gradient(90deg,#C9973A,#E5C068);border-radius:2px;"></div>
              </div>
              <p style="font-size:12px;color:#C9973A;font-weight:700;margin:4px 0 0;">4.2%</p>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</section>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
#  MARQUEE TICKER
# ════════════════════════════════════════════════════════════════
items = ["Hook Effectiveness","Pacing Analysis","Emotional Arc","CTA Clarity","Narrative Quality",
         "Retention Correlation","Multi-Script Compare","AI-Powered Insights","Google Drive Integration","Meta Ads Data"]
ticker = " ".join([f'<span class="marquee-item"><span style="color:#C9973A;">✦</span> {i}</span>' for i in items*3])
st.markdown(f"""
<div style="border-top:1px solid rgba(29,26,53,0.6);border-bottom:1px solid rgba(29,26,53,0.6);
            overflow:hidden;padding:14px 0;background:rgba(13,11,30,0.4);">
  <div class="marquee-track">{ticker}</div>
</div>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
#  FEATURES BENTO GRID
# ════════════════════════════════════════════════════════════════
st.markdown('<div id="features" style="padding:80px 40px 40px;max-width:1200px;margin:0 auto;">', unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center;margin-bottom:48px;">
  <p style="font-size:11px;color:#5A5478;text-transform:uppercase;letter-spacing:0.12em;margin-bottom:8px;">What It Does</p>
  <h2 style="font-family:'DM Serif Display',serif;font-size:clamp(1.8rem,3vw,2.8rem);color:#EDE9F8;margin:0;">
    Everything your script needs,<br><span style="color:#C9973A;font-style:italic;">decoded.</span>
  </h2>
</div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;">
""", unsafe_allow_html=True)

features = [
    ("🎯", "Hook Effectiveness", "Analyse the first 5 seconds. Know exactly why your hook wins or loses attention before the story begins.", "#C9973A"),
    ("⏱", "Pacing Intelligence", "Map script beats to your retention curve. See where attention drops and what caused it.", "#A855F7"),
    ("💫", "Emotional Arc", "Trace the emotional journey through every scene. Understand what keeps listeners coming back.", "#60a5fa"),
    ("📣", "CTA Clarity", "Score your call-to-action against real CTR data. Find the line that converts.", "#34d399"),
    ("📊", "Retention Correlation", "Connect script moments to V0–25, V25–50, V50–75, V75–95 data. No more guessing.", "#f472b6"),
    ("⚡", "Multi-Script Compare", "Compare up to 4 scripts side-by-side. Find patterns. Replicate winners. Kill what fails.", "#fbbf24"),
]
for icon, title, desc, color in features:
    st.markdown(f"""
    <div class="glass card-hover" style="border-radius:14px;padding:24px;
         border-color:rgba(29,26,53,0.9);">
      <div style="width:40px;height:40px;border-radius:10px;display:flex;align-items:center;
                  justify-content:center;font-size:18px;margin-bottom:14px;
                  background:rgba(19,16,38,0.8);border:1px solid rgba(29,26,53,0.8);">{icon}</div>
      <h3 style="font-family:'Outfit',sans-serif;font-size:14px;font-weight:600;
                 color:#EDE9F8;margin:0 0 8px;">{title}</h3>
      <p style="font-size:13px;color:#5A5478;line-height:1.65;margin:0;">{desc}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
#  HOW IT WORKS
# ════════════════════════════════════════════════════════════════
st.markdown('<div id="howitworks" style="padding:80px 40px;background:rgba(13,11,30,0.4);">', unsafe_allow_html=True)
st.markdown("""
<div style="max-width:1200px;margin:0 auto;">
  <div style="text-align:center;margin-bottom:56px;">
    <p style="font-size:11px;color:#5A5478;text-transform:uppercase;letter-spacing:0.12em;margin-bottom:8px;">Process</p>
    <h2 style="font-family:'DM Serif Display',serif;font-size:clamp(1.8rem,3vw,2.8rem);color:#EDE9F8;margin:0;">
      Four inputs. <span style="color:#C9973A;font-style:italic;">One truth.</span>
    </h2>
  </div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px;">
""", unsafe_allow_html=True)

steps = [
    ("01", "🔐", "Service Account JSON", "Upload your Google Cloud service account key for Drive access.", "#C9973A"),
    ("02", "📊", "Performance Data", "Drop your master tracker Excel with Meta Ads retention & CTR data.", "#A855F7"),
    ("03", "📁", "Drive Folder ID", "Paste your Google Drive folder ID containing the .docx script files.", "#60a5fa"),
    ("04", "🤖", "AI Analysis", "Select scripts, pick your AI provider, and get deep narrative intelligence.", "#34d399"),
]
for num, icon, title, desc, color in steps:
    st.markdown(f"""
    <div class="step-card">
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
        <span style="font-size:11px;color:{color};font-weight:700;letter-spacing:0.1em;">{num}</span>
        <span style="font-size:22px;">{icon}</span>
      </div>
      <h3 style="font-family:'Outfit',sans-serif;font-size:14px;font-weight:600;
                 color:#EDE9F8;margin:0 0 8px;">{title}</h3>
      <p style="font-size:13px;color:#5A5478;line-height:1.65;margin:0;">{desc}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div></div></div>', unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
#  AI PROVIDERS
# ════════════════════════════════════════════════════════════════
st.markdown("""
<div style="padding:80px 40px;">
  <div style="max-width:800px;margin:0 auto;text-align:center;">
    <p style="font-size:11px;color:#5A5478;text-transform:uppercase;letter-spacing:0.12em;margin-bottom:8px;">AI Providers</p>
    <h2 style="font-family:'DM Serif Display',serif;font-size:clamp(1.8rem,3vw,2.6rem);color:#EDE9F8;margin-bottom:40px;">
      Your choice of intelligence.
    </h2>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;">
      <div class="glass card-hover" style="border-radius:14px;padding:24px;text-align:center;">
        <div style="font-size:28px;margin-bottom:12px;">🟡</div>
        <p style="font-weight:700;color:#EDE9F8;margin:0 0 6px;font-size:15px;">Gemini Flash</p>
        <p style="font-size:11px;color:#34d399;margin:0 0 10px;">FREE — 1500 req/day</p>
        <p style="font-size:12px;color:#5A5478;line-height:1.6;margin:0;">Great for general narrative analysis. No card needed.</p>
      </div>
      <div class="glass card-hover" style="border-radius:14px;padding:24px;text-align:center;
           border-color:rgba(168,85,247,0.2);">
        <div style="font-size:28px;margin-bottom:12px;">⚡</div>
        <p style="font-weight:700;color:#EDE9F8;margin:0 0 6px;font-size:15px;">Groq Llama</p>
        <p style="font-size:11px;color:#34d399;margin:0 0 10px;">FREE — Ultra fast</p>
        <p style="font-size:12px;color:#5A5478;line-height:1.6;margin:0;">Best for bulk script comparison at speed.</p>
      </div>
      <div class="glass card-hover" style="border-radius:14px;padding:24px;text-align:center;">
        <div style="font-size:28px;margin-bottom:12px;">🤖</div>
        <p style="font-weight:700;color:#EDE9F8;margin:0 0 6px;font-size:15px;">Claude Haiku</p>
        <p style="font-size:11px;color:#fbbf24;margin:0 0 10px;">~$0.001/run</p>
        <p style="font-size:12px;color:#5A5478;line-height:1.6;margin:0;">Deepest insight for nuanced storytelling analysis.</p>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
#  CTA SECTION
# ════════════════════════════════════════════════════════════════
st.markdown("""
<div style="padding:80px 40px;text-align:center;position:relative;overflow:hidden;
            background:linear-gradient(180deg,transparent,rgba(124,58,237,0.08),transparent);">
  <div class="orb" style="width:600px;height:600px;top:50%;left:50%;transform:translate(-50%,-50%);
       --dur:12s;background:radial-gradient(circle,rgba(124,58,237,0.08) 0%,transparent 70%);"></div>
  <div style="position:relative;max-width:680px;margin:0 auto;">
    <div style="font-size:48px;margin-bottom:16px;">🎬</div>
    <h2 style="font-family:'DM Serif Display',serif;font-size:clamp(2rem,4vw,3.2rem);
               color:#EDE9F8;margin:0 0 16px;">
      Ready to decode<br>
      <span style="color:#C9973A;font-style:italic;">your Promo ads?</span>
    </h2>
    <p style="font-size:15px;color:#5A5478;max-width:520px;margin:0 auto 36px;line-height:1.7;">
      Open source, AI-powered, and built specifically for PocketFM's creative
      and performance marketing teams.
    </p>
    <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;">
      <a href="/Tool" class="btn-gold" style="font-size:16px;padding:16px 44px;">✦ Analyze a Script</a>
      <a href="https://github.com/con-mayankmandal-netizen/story-analyzer-ui" target="_blank"
         class="btn-ghost" style="font-size:15px;padding:16px 36px;">View on GitHub</a>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
#  FOOTER
# ════════════════════════════════════════════════════════════════
st.markdown("""
<footer style="border-top:1px solid rgba(29,26,53,0.8);background:rgba(6,4,15,0.95);padding:48px 40px 32px;">
  <div style="max-width:1200px;margin:0 auto;display:flex;flex-direction:column;align-items:center;gap:20px;text-align:center;">

    <div style="display:flex;align-items:center;gap:10px;">
      <div style="display:flex;align-items:flex-end;gap:2px;height:18px;">
        <div class="wave-bar" style="height:5px;--dur:1.0s;"></div>
        <div class="wave-bar" style="height:12px;--dur:1.3s;--delay:0.1s;"></div>
        <div class="wave-bar" style="height:8px;--dur:1.0s;--delay:0.2s;"></div>
        <div class="wave-bar" style="height:16px;--dur:1.4s;--delay:0.08s;"></div>
        <div class="wave-bar" style="height:6px;--dur:0.9s;--delay:0.22s;"></div>
      </div>
      <span style="font-family:'Outfit',sans-serif;font-weight:600;font-size:15px;color:#EDE9F8;">StoryAnalyzer</span>
    </div>

    <div style="width:60px;height:1px;background:linear-gradient(90deg,transparent,#C9973A,transparent);"></div>

    <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;justify-content:center;">
      <span style="font-size:13px;color:rgba(90,84,120,0.7);">Designed &amp; Developed by</span>
      <a href="https://pocket-fm.slack.com/team/U08NHRDM9M2" target="_blank"
         style="display:inline-flex;align-items:center;gap:6px;
                background:rgba(201,151,58,0.08);border:1px solid rgba(201,151,58,0.25);
                border-radius:100px;padding:6px 16px 6px 12px;transition:all 0.3s;"
         onmouseover="this.style.background='rgba(201,151,58,0.15)';this.style.boxShadow='0 0 20px rgba(229,192,104,0.2)'"
         onmouseout="this.style.background='rgba(201,151,58,0.08)';this.style.boxShadow='none'">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="#A855F7"><path d="M5.042 15.165a2.528 2.528 0 0 1-2.52 2.523A2.528 2.528 0 0 1 0 15.165a2.527 2.527 0 0 1 2.522-2.52h2.52v2.52zM6.313 15.165a2.527 2.527 0 0 1 2.521-2.52 2.527 2.527 0 0 1 2.521 2.52v6.313A2.528 2.528 0 0 1 8.834 24a2.528 2.528 0 0 1-2.521-2.522v-6.313zM8.834 5.042a2.528 2.528 0 0 1-2.521-2.52A2.528 2.528 0 0 1 8.834 0a2.528 2.528 0 0 1 2.521 2.522v2.52H8.834zM8.834 6.313a2.528 2.528 0 0 1 2.521 2.521 2.528 2.528 0 0 1-2.521 2.521H2.522A2.528 2.528 0 0 1 0 8.834a2.528 2.528 0 0 1 2.522-2.521h6.312zM18.956 8.834a2.528 2.528 0 0 1 2.522-2.521A2.528 2.528 0 0 1 24 8.834a2.528 2.528 0 0 1-2.522 2.521h-2.522V8.834zM17.688 8.834a2.528 2.528 0 0 1-2.523 2.521 2.527 2.527 0 0 1-2.52-2.521V2.522A2.527 2.527 0 0 1 15.165 0a2.528 2.528 0 0 1 2.523 2.522v6.312zM15.165 18.956a2.528 2.528 0 0 1 2.523 2.522A2.528 2.528 0 0 1 15.165 24a2.527 2.527 0 0 1-2.52-2.522v-2.522h2.52zM15.165 17.688a2.527 2.527 0 0 1-2.52-2.523 2.526 2.526 0 0 1 2.52-2.52h6.313A2.527 2.527 0 0 1 24 15.165a2.528 2.528 0 0 1-2.522 2.523h-6.313z"/></svg>
        <span style="font-size:13px;font-weight:700;color:#E5C068;text-shadow:0 0 12px rgba(229,192,104,0.4);">Mayank Mandal</span>
      </a>
    </div>
    <p style="font-size:11px;color:rgba(90,84,120,0.4);margin:0;">PocketFM Script Intelligence &bull; Open Source &bull; 2025</p>
  </div>
</footer>
""", unsafe_allow_html=True)
