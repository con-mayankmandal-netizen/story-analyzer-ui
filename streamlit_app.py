"""
StoryAnalyzer — Landing Page (Native Streamlit, fully self-contained HTML blocks)
"""
import streamlit as st
import math

st.set_page_config(
    page_title="StoryAnalyzer — PocketFM Script Intelligence",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@200;300;400;500;600;700;800;900&family=DM+Serif+Display:ital@0;1&display=swap');
html,body,.stApp{background:#06040F!important;font-family:'Outfit',sans-serif!important;color:#EDE9F8!important;}
#MainMenu,footer,.stDeployButton,header{display:none!important;}
section[data-testid="stSidebar"]{display:none!important;}
.block-container{padding:0!important;max-width:100%!important;}
h1,h2,h3{font-family:'DM Serif Display',serif!important;color:#EDE9F8!important;}
a{text-decoration:none!important;}
::-webkit-scrollbar{width:4px;}
::-webkit-scrollbar-thumb{background:rgba(201,151,58,0.4);border-radius:2px;}
@keyframes wavePulse{from{transform:scaleY(0.4);opacity:0.5;}to{transform:scaleY(1);opacity:1;}}
@keyframes floatOrb{0%,100%{transform:translateY(0);}50%{transform:translateY(-20px);}}
@keyframes shimmer{0%{background-position:-200% center;}100%{background-position:200% center;}}
@keyframes fadeUp{from{opacity:0;transform:translateY(24px);}to{opacity:1;transform:translateY(0);}}
@keyframes marquee{from{transform:translateX(0);}to{transform:translateX(-50%);}}
.wave-bar{display:inline-block;width:3px;border-radius:2px;background:#C9973A;
          animation:wavePulse var(--dur,1.2s) ease-in-out var(--delay,0s) infinite alternate;}
.fade-1{animation:fadeUp 0.8s ease 0.1s both;}
.fade-2{animation:fadeUp 0.8s ease 0.25s both;}
.fade-3{animation:fadeUp 0.8s ease 0.4s both;}
.fade-4{animation:fadeUp 0.8s ease 0.55s both;}
.fade-5{animation:fadeUp 0.8s ease 0.7s both;}
.glass{background:rgba(19,16,38,0.7);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border:1px solid rgba(29,26,53,0.9);}
.card-h{transition:transform 0.3s,box-shadow 0.3s;}
.card-h:hover{transform:translateY(-4px);box-shadow:0 20px 60px rgba(124,58,237,0.15);}
.orb{position:absolute;border-radius:50%;pointer-events:none;animation:floatOrb var(--dur,8s) ease-in-out var(--delay,0s) infinite;}
.marquee-track{display:flex;width:max-content;animation:marquee 30s linear infinite;}
.marquee-item{display:flex;align-items:center;gap:8px;white-space:nowrap;padding:0 28px;font-size:13px;color:#5A5478;}
.name-shimmer{background:linear-gradient(90deg,#C9973A 0%,#E5C068 30%,#fff 50%,#E5C068 70%,#C9973A 100%);
              background-size:200% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;
              background-clip:text;animation:shimmer 4s linear infinite;}
</style>
""", unsafe_allow_html=True)

SLACK = "https://pocket-fm.slack.com/team/U08NHRDM9M2"
GH    = "https://github.com/con-mayankmandal-netizen/story-analyzer-ui"

SLACK_ICON = """<svg width="11" height="11" viewBox="0 0 24 24" fill="#A855F7"><path d="M5.042 15.165a2.528 2.528 0 0 1-2.52 2.523A2.528 2.528 0 0 1 0 15.165a2.527 2.527 0 0 1 2.522-2.52h2.52v2.52zM6.313 15.165a2.527 2.527 0 0 1 2.521-2.52 2.527 2.527 0 0 1 2.521 2.52v6.313A2.528 2.528 0 0 1 8.834 24a2.528 2.528 0 0 1-2.521-2.522v-6.313zM8.834 5.042a2.528 2.528 0 0 1-2.521-2.52A2.528 2.528 0 0 1 8.834 0a2.528 2.528 0 0 1 2.521 2.522v2.52H8.834zM8.834 6.313a2.528 2.528 0 0 1 2.521 2.521 2.528 2.528 0 0 1-2.521 2.521H2.522A2.528 2.528 0 0 1 0 8.834a2.528 2.528 0 0 1 2.522-2.521h6.312zM18.956 8.834a2.528 2.528 0 0 1 2.522-2.521A2.528 2.528 0 0 1 24 8.834a2.528 2.528 0 0 1-2.522 2.521h-2.522V8.834zM17.688 8.834a2.528 2.528 0 0 1-2.523 2.521 2.527 2.527 0 0 1-2.52-2.521V2.522A2.527 2.527 0 0 1 15.165 0a2.528 2.528 0 0 1 2.523 2.522v6.312zM15.165 18.956a2.528 2.528 0 0 1 2.523 2.522A2.528 2.528 0 0 1 15.165 24a2.527 2.527 0 0 1-2.52-2.522v-2.522h2.52zM15.165 17.688a2.527 2.527 0 0 1-2.52-2.523 2.526 2.526 0 0 1 2.52-2.52h6.313A2.527 2.527 0 0 1 24 15.165a2.528 2.528 0 0 1-2.522 2.523h-6.313z"/></svg>"""

WAVE_BARS = """
<div style="display:flex;align-items:flex-end;gap:2px;height:20px;">
  <div class="wave-bar" style="height:6px;--dur:1.0s;"></div>
  <div class="wave-bar" style="height:14px;--dur:1.3s;--delay:0.12s;"></div>
  <div class="wave-bar" style="height:10px;--dur:1.1s;--delay:0.28s;"></div>
  <div class="wave-bar" style="height:18px;--dur:1.4s;--delay:0.08s;"></div>
  <div class="wave-bar" style="height:8px;--dur:0.9s;--delay:0.22s;"></div>
</div>"""

# ════════════════════════════════════════════════════════════════
#  HEADER
# ════════════════════════════════════════════════════════════════
st.markdown(f"""
<div style="position:sticky;top:0;z-index:999;background:rgba(6,4,15,0.96);
            backdrop-filter:blur(20px);border-bottom:1px solid rgba(29,26,53,0.8);">
  <div style="padding:5px 40px;border-bottom:1px solid rgba(29,26,53,0.4);
              display:flex;align-items:center;justify-content:space-between;">
    <p style="font-size:11px;color:rgba(90,84,120,0.7);margin:0;">
      Open source &bull; AI-powered &bull; Built for
      <span style="color:#C9973A;font-weight:600;">PocketFM</span>
    </p>
    <div style="display:flex;align-items:center;gap:6px;">
      {SLACK_ICON}
      <span style="font-size:11px;color:rgba(90,84,120,0.6);">by</span>
      <a href="{SLACK}" target="_blank"
         style="font-size:11px;color:#E5C068;font-weight:600;text-shadow:0 0 10px rgba(229,192,104,0.4);">Mayank Mandal</a>
    </div>
  </div>
  <nav style="display:flex;align-items:center;justify-content:space-between;padding:10px 40px;">
    <div style="display:flex;align-items:center;gap:10px;">
      {WAVE_BARS}
      <span style="font-weight:600;font-size:15px;color:#EDE9F8;">StoryAnalyzer</span>
    </div>
    <div style="display:flex;align-items:center;gap:4px;">
      <a href="/" style="font-size:13px;color:#5A5478;padding:6px 14px;">Home</a>
      <a href="/Help" style="font-size:13px;color:#5A5478;padding:6px 14px;">Help</a>
      <a href="/Tool" style="display:inline-flex;align-items:center;gap:6px;font-size:13px;font-weight:700;
         background:linear-gradient(135deg,#C9973A,#E5C068);color:#06040F;padding:9px 24px;
         border-radius:100px;box-shadow:0 0 24px rgba(201,151,58,0.3);">
        Analyze a Script &rarr;
      </a>
    </div>
  </nav>
</div>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
#  HERO  — build score rings inline so no split tags
# ════════════════════════════════════════════════════════════════
dims   = [("Hook",82,"#C9973A"),("Pacing",74,"#A855F7"),("Emotion",88,"#60a5fa"),("CTA",71,"#34d399"),("Story",79,"#f472b6")]
circ   = 2 * math.pi * 16
rings  = ""
for label, score, color in dims:
    offset = circ * (1 - score / 100)
    rings += f"""
    <div style="display:flex;flex-direction:column;align-items:center;gap:6px;">
      <svg width="52" height="52" viewBox="0 0 44 44">
        <circle cx="22" cy="22" r="16" fill="none" stroke="rgba(29,26,53,0.8)" stroke-width="4"/>
        <circle cx="22" cy="22" r="16" fill="none" stroke="{color}" stroke-width="4"
          stroke-linecap="round" stroke-dasharray="{circ:.1f}" stroke-dashoffset="{offset:.1f}"
          transform="rotate(-90 22 22)"/>
      </svg>
      <span style="font-size:16px;font-weight:800;color:{color};">{score}</span>
      <span style="font-size:10px;color:#5A5478;text-transform:uppercase;letter-spacing:0.06em;">{label}</span>
    </div>"""

st.markdown(f"""
<section style="position:relative;overflow:hidden;padding:80px 40px 60px;
                background:linear-gradient(160deg,rgba(124,58,237,0.07) 0%,transparent 60%);">
  <div style="position:absolute;width:500px;height:500px;top:-100px;right:-80px;border-radius:50%;
              background:radial-gradient(circle,rgba(124,58,237,0.1) 0%,transparent 70%);
              animation:floatOrb 10s ease-in-out infinite;pointer-events:none;"></div>
  <div style="position:absolute;width:400px;height:400px;bottom:-60px;left:-60px;border-radius:50%;
              background:radial-gradient(circle,rgba(201,151,58,0.07) 0%,transparent 70%);
              animation:floatOrb 8s ease-in-out 2s infinite;pointer-events:none;"></div>

  <div style="max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center;position:relative;">

    <!-- LEFT -->
    <div>
      <div class="fade-1" style="display:inline-flex;align-items:center;gap:8px;margin-bottom:20px;
           background:rgba(124,58,237,0.08);border:1px solid rgba(124,58,237,0.2);
           border-radius:100px;padding:6px 16px;">
        <span style="font-size:12px;color:#A855F7;font-weight:500;">🎬 PocketFM Script Intelligence</span>
      </div>
      <h1 class="fade-2" style="font-family:'DM Serif Display',serif;
          font-size:clamp(2.4rem,4.5vw,4rem);line-height:1.1;color:#EDE9F8;margin:0 0 6px;">
        Decode your
      </h1>
      <h1 class="fade-2" style="font-family:'DM Serif Display',serif;
          font-size:clamp(2.4rem,4.5vw,4rem);line-height:1.1;margin:0 0 24px;
          color:#C9973A;font-style:italic;">
        Promo Story
      </h1>
      <p class="fade-3" style="font-size:16px;color:#5A5478;line-height:1.75;max-width:480px;margin-bottom:36px;">
        Connect your data, load your scripts, choose your AI — get deep narrative
        insight on every audio ad. Stop guessing. Start knowing why stories work.
      </p>
      <div class="fade-4" style="display:flex;gap:14px;flex-wrap:wrap;margin-bottom:40px;">
        <a href="/Tool" style="display:inline-flex;align-items:center;gap:8px;font-weight:700;
           font-size:15px;padding:14px 36px;border-radius:100px;color:#06040F;
           background:linear-gradient(135deg,#C9973A,#E5C068);
           box-shadow:0 0 30px rgba(201,151,58,0.3);">✦ Analyze a Script</a>
        <a href="#howitworks" style="display:inline-flex;align-items:center;gap:8px;font-size:15px;
           padding:14px 36px;border-radius:100px;color:#EDE9F8;font-weight:500;
           background:rgba(19,16,38,0.7);border:1px solid rgba(29,26,53,0.9);">See How It Works</a>
      </div>
      <div class="fade-5" style="display:flex;gap:32px;padding-top:28px;border-top:1px solid rgba(29,26,53,0.8);">
        <div><p style="font-size:26px;font-weight:800;color:#C9973A;margin:0;">5</p>
             <p style="font-size:11px;color:#5A5478;margin:2px 0 0;text-transform:uppercase;letter-spacing:0.05em;">Dimensions</p></div>
        <div><p style="font-size:26px;font-weight:800;color:#A855F7;margin:0;">3</p>
             <p style="font-size:11px;color:#5A5478;margin:2px 0 0;text-transform:uppercase;letter-spacing:0.05em;">AI Providers</p></div>
        <div><p style="font-size:26px;font-weight:800;color:#EDE9F8;margin:0;">4</p>
             <p style="font-size:11px;color:#5A5478;margin:2px 0 0;text-transform:uppercase;letter-spacing:0.05em;">Scripts at once</p></div>
      </div>
    </div>

    <!-- RIGHT: Dashboard card -->
    <div class="fade-3">
      <div class="glass card-h" style="border-radius:20px;overflow:hidden;
           box-shadow:0 0 80px rgba(124,58,237,0.15),0 0 160px rgba(201,151,58,0.06);">
        <div style="padding:14px 20px;border-bottom:1px solid rgba(29,26,53,0.8);
                    display:flex;align-items:center;justify-content:space-between;">
          <div style="display:flex;gap:6px;">
            <div style="width:8px;height:8px;border-radius:50%;background:#ef4444;"></div>
            <div style="width:8px;height:8px;border-radius:50%;background:#f59e0b;"></div>
            <div style="width:8px;height:8px;border-radius:50%;background:#22c55e;"></div>
          </div>
          <span style="font-size:11px;color:#5A5478;">GAI647 — Analysis Complete</span>
          <span style="font-size:10px;background:rgba(34,197,94,0.1);color:#22c55e;
                       border:1px solid rgba(34,197,94,0.2);border-radius:4px;padding:2px 8px;">Live</span>
        </div>
        <div style="padding:24px 20px;">
          <div style="display:flex;justify-content:space-around;margin-bottom:20px;">
            {rings}
          </div>
          <div style="background:rgba(201,151,58,0.06);border:1px solid rgba(201,151,58,0.15);
                      border-radius:10px;padding:12px 14px;margin-bottom:14px;">
            <p style="font-size:10px;color:#5A5478;margin:0 0 4px;text-transform:uppercase;letter-spacing:0.05em;">Verdict</p>
            <p style="font-size:13px;color:#EDE9F8;margin:0;font-family:'DM Serif Display',serif;font-style:italic;">
              "Strong hook, emotional drop at 60s. CTA clarity needs tightening."
            </p>
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
            <div style="background:rgba(13,11,30,0.8);border-radius:8px;padding:10px 12px;">
              <p style="font-size:10px;color:#5A5478;margin:0 0 6px;">ThruPlay %</p>
              <div style="height:4px;background:rgba(29,26,53,0.8);border-radius:2px;margin-bottom:4px;">
                <div style="height:4px;width:68%;background:linear-gradient(90deg,#7C3AED,#A855F7);border-radius:2px;"></div>
              </div>
              <p style="font-size:12px;color:#A855F7;font-weight:700;margin:0;">68%</p>
            </div>
            <div style="background:rgba(13,11,30,0.8);border-radius:8px;padding:10px 12px;">
              <p style="font-size:10px;color:#5A5478;margin:0 0 6px;">CTR</p>
              <div style="height:4px;background:rgba(29,26,53,0.8);border-radius:2px;margin-bottom:4px;">
                <div style="height:4px;width:42%;background:linear-gradient(90deg,#C9973A,#E5C068);border-radius:2px;"></div>
              </div>
              <p style="font-size:12px;color:#C9973A;font-weight:700;margin:0;">4.2%</p>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</section>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
#  MARQUEE — fully self-contained
# ════════════════════════════════════════════════════════════════
items = ["Hook Effectiveness","Pacing Analysis","Emotional Arc","CTA Clarity","Narrative Quality",
         "Retention Correlation","Multi-Script Compare","AI-Powered Insights","Drive Integration","Meta Ads Data"]
ticker = "".join([f'<span class="marquee-item"><span style="color:#C9973A;">✦</span> {i}</span>' for i in items*3])
st.markdown(f"""
<div style="border-top:1px solid rgba(29,26,53,0.6);border-bottom:1px solid rgba(29,26,53,0.6);
            overflow:hidden;padding:14px 0;background:rgba(13,11,30,0.4);">
  <div class="marquee-track">{ticker}</div>
</div>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
#  FEATURES — fully self-contained
# ════════════════════════════════════════════════════════════════
features = [
    ("🎯","Hook Effectiveness","Analyse the first 5 seconds. Know exactly why your hook wins or loses attention.","#C9973A"),
    ("⏱","Pacing Intelligence","Map script beats to your retention curve. See where attention drops and why.","#A855F7"),
    ("💫","Emotional Arc","Trace the emotional journey through every scene. Understand what keeps listeners in.","#60a5fa"),
    ("📣","CTA Clarity","Score your call-to-action against real CTR data. Find the line that converts.","#34d399"),
    ("📊","Retention Correlation","Connect script moments to V0–25, V25–50, V50–75, V75–95 data. No more guessing.","#f472b6"),
    ("⚡","Multi-Script Compare","Compare up to 4 scripts side-by-side. Find patterns. Replicate winners.","#fbbf24"),
]
feat_cards = "".join([f"""
  <div class="glass card-h" style="border-radius:14px;padding:24px;">
    <div style="font-size:22px;margin-bottom:14px;">{ic}</div>
    <p style="font-size:14px;font-weight:600;color:#EDE9F8;margin:0 0 8px;">{ti}</p>
    <p style="font-size:13px;color:#5A5478;line-height:1.65;margin:0;">{de}</p>
  </div>""" for ic,ti,de,_ in features])

st.markdown(f"""
<div id="features" style="padding:80px 40px 40px;">
  <div style="max-width:1200px;margin:0 auto;">
    <div style="text-align:center;margin-bottom:48px;">
      <p style="font-size:11px;color:#5A5478;text-transform:uppercase;letter-spacing:0.12em;margin-bottom:8px;">What It Does</p>
      <h2 style="font-family:'DM Serif Display',serif;font-size:clamp(1.8rem,3vw,2.8rem);color:#EDE9F8;margin:0;">
        Everything your script needs, <span style="color:#C9973A;font-style:italic;">decoded.</span>
      </h2>
    </div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;">
      {feat_cards}
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
#  HOW IT WORKS — fully self-contained
# ════════════════════════════════════════════════════════════════
steps = [
    ("01","🔐","Service Account JSON","Upload your Google Cloud service account key for Drive access.","#C9973A"),
    ("02","📊","Performance Data","Drop your master tracker Excel with Meta Ads retention & CTR data.","#A855F7"),
    ("03","📁","Drive Folder ID","Paste your Google Drive folder ID containing the .docx script files.","#60a5fa"),
    ("04","🤖","AI Analysis","Select scripts, pick your AI provider, and get deep narrative intelligence.","#34d399"),
]
step_cards = "".join([f"""
  <div style="background:rgba(19,16,38,0.5);border:1px solid rgba(29,26,53,0.8);border-radius:16px;padding:24px;">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;">
      <span style="font-size:11px;color:{col};font-weight:700;letter-spacing:0.1em;">{num}</span>
      <span style="font-size:22px;">{ic}</span>
    </div>
    <p style="font-size:14px;font-weight:600;color:#EDE9F8;margin:0 0 8px;">{ti}</p>
    <p style="font-size:13px;color:#5A5478;line-height:1.65;margin:0;">{de}</p>
  </div>""" for num,ic,ti,de,col in steps])

st.markdown(f"""
<div id="howitworks" style="padding:80px 40px;background:rgba(13,11,30,0.4);">
  <div style="max-width:1200px;margin:0 auto;">
    <div style="text-align:center;margin-bottom:56px;">
      <p style="font-size:11px;color:#5A5478;text-transform:uppercase;letter-spacing:0.12em;margin-bottom:8px;">Process</p>
      <h2 style="font-family:'DM Serif Display',serif;font-size:clamp(1.8rem,3vw,2.8rem);color:#EDE9F8;margin:0;">
        Four inputs. <span style="color:#C9973A;font-style:italic;">One truth.</span>
      </h2>
    </div>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px;">
      {step_cards}
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
#  AI PROVIDERS — fully self-contained
# ════════════════════════════════════════════════════════════════
ai_providers = [
    ("🟡","Gemini Flash","FREE — 1500 req/day","#34d399","Great for general narrative analysis. No card needed."),
    ("⚡","Groq Llama","FREE — Ultra fast","#34d399","Best for bulk script comparison at speed."),
    ("🤖","Claude Haiku","~$0.001/run","#fbbf24","Deepest insight for nuanced storytelling analysis."),
]
ai_cards = "".join([f"""
  <div class="glass card-h" style="border-radius:14px;padding:28px;text-align:center;">
    <div style="font-size:32px;margin-bottom:12px;">{ic}</div>
    <p style="font-weight:700;color:#EDE9F8;margin:0 0 6px;font-size:15px;">{name}</p>
    <p style="font-size:11px;color:{bc};margin:0 0 12px;">{badge}</p>
    <p style="font-size:13px;color:#5A5478;line-height:1.6;margin:0;">{desc}</p>
  </div>""" for ic,name,badge,bc,desc in ai_providers])

st.markdown(f"""
<div style="padding:80px 40px;">
  <div style="max-width:900px;margin:0 auto;text-align:center;">
    <p style="font-size:11px;color:#5A5478;text-transform:uppercase;letter-spacing:0.12em;margin-bottom:8px;">AI Providers</p>
    <h2 style="font-family:'DM Serif Display',serif;font-size:clamp(1.8rem,3vw,2.6rem);color:#EDE9F8;margin-bottom:40px;">
      Your choice of intelligence.
    </h2>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;">
      {ai_cards}
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
#  CTA — fully self-contained
# ════════════════════════════════════════════════════════════════
st.markdown(f"""
<div style="padding:80px 40px;text-align:center;
            background:linear-gradient(180deg,transparent,rgba(124,58,237,0.07),transparent);">
  <div style="max-width:680px;margin:0 auto;">
    <div style="font-size:48px;margin-bottom:16px;">🎬</div>
    <h2 style="font-family:'DM Serif Display',serif;font-size:clamp(2rem,4vw,3rem);
               color:#EDE9F8;margin:0 0 16px;">
      Ready to decode<br>
      <span style="color:#C9973A;font-style:italic;">your Promo ads?</span>
    </h2>
    <p style="font-size:15px;color:#5A5478;max-width:500px;margin:0 auto 36px;line-height:1.7;">
      Open source, AI-powered, and built specifically for PocketFM's creative
      and performance marketing teams.
    </p>
    <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;">
      <a href="/Tool" style="display:inline-flex;align-items:center;gap:8px;font-weight:700;font-size:16px;
         padding:16px 44px;border-radius:100px;color:#06040F;
         background:linear-gradient(135deg,#C9973A,#E5C068);
         box-shadow:0 0 40px rgba(201,151,58,0.35);">✦ Analyze a Script</a>
      <a href="{GH}" target="_blank" style="display:inline-flex;align-items:center;gap:8px;
         font-size:15px;padding:16px 36px;border-radius:100px;color:#EDE9F8;font-weight:500;
         background:rgba(19,16,38,0.7);border:1px solid rgba(29,26,53,0.9);">View on GitHub</a>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════
#  FOOTER — fully self-contained
# ════════════════════════════════════════════════════════════════
st.markdown(f"""
<footer style="border-top:1px solid rgba(29,26,53,0.8);background:rgba(6,4,15,0.97);padding:48px 40px 32px;">
  <div style="max-width:1200px;margin:0 auto;display:flex;flex-direction:column;align-items:center;gap:18px;text-align:center;">
    <div style="display:flex;align-items:center;gap:10px;">
      {WAVE_BARS}
      <span style="font-weight:600;font-size:15px;color:#EDE9F8;">StoryAnalyzer</span>
    </div>
    <div style="width:60px;height:1px;background:linear-gradient(90deg,transparent,#C9973A,transparent);"></div>
    <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;justify-content:center;">
      <span style="font-size:13px;color:rgba(90,84,120,0.7);">Designed &amp; Developed by</span>
      <a href="{SLACK}" target="_blank"
         style="display:inline-flex;align-items:center;gap:6px;
                background:rgba(201,151,58,0.08);border:1px solid rgba(201,151,58,0.25);
                border-radius:100px;padding:6px 16px 6px 12px;">
        {SLACK_ICON}
        <span style="font-size:13px;font-weight:700;color:#E5C068;">Mayank Mandal</span>
      </a>
    </div>
    <p style="font-size:11px;color:rgba(90,84,120,0.4);margin:0;">
      PocketFM Script Intelligence &bull; Open Source &bull; 2025
    </p>
  </div>
</footer>
""", unsafe_allow_html=True)
