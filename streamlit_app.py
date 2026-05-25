import streamlit as st, math

st.set_page_config(page_title="StoryAnalyzer — PocketFM", page_icon="🎬",
                   layout="wide", initial_sidebar_state="collapsed")

st.markdown("""<style>
#MainMenu,header,footer,.stDeployButton{display:none!important;}
section[data-testid="stSidebar"]{display:none!important;}
.block-container{padding:0!important;max-width:100%!important;}
.stApp{background:#06040F!important;}
iframe{border:none!important;display:block!important;}
</style>""", unsafe_allow_html=True)

# ── Build score rings ─────────────────────────────────────────────────────────
dims  = [("Hook",82,"#C9973A"),("Pacing",74,"#A855F7"),("Emotion",88,"#60a5fa"),("CTA",71,"#34d399"),("Story",79,"#f472b6")]
circ  = 2 * math.pi * 16
rings = ""
for label, score, color in dims:
    offset = circ * (1 - score/100)
    rings += f"""<div style="display:flex;flex-direction:column;align-items:center;gap:5px;">
      <svg width="50" height="50" viewBox="0 0 44 44">
        <circle cx="22" cy="22" r="16" fill="none" stroke="rgba(29,26,53,0.8)" stroke-width="4"/>
        <circle cx="22" cy="22" r="16" fill="none" stroke="{color}" stroke-width="4"
          stroke-linecap="round" stroke-dasharray="{circ:.1f}" stroke-dashoffset="{offset:.1f}"
          transform="rotate(-90 22 22)"/>
      </svg>
      <span style="font-size:15px;font-weight:800;color:{color};font-family:Outfit,sans-serif;">{score}</span>
      <span style="font-size:9px;color:#5A5478;text-transform:uppercase;letter-spacing:0.07em;">{label}</span>
    </div>"""

# ── Build feature cards ───────────────────────────────────────────────────────
features = [
    ("🎯","Hook Effectiveness","Analyse the first 5 seconds. Know exactly why your hook wins or loses attention before the story begins."),
    ("⏱","Pacing Intelligence","Map script beats to your retention curve. See where attention drops and why."),
    ("💫","Emotional Arc","Trace the emotional journey through every scene. Understand what keeps listeners in."),
    ("📣","CTA Clarity","Score your call-to-action against real CTR data. Find the line that converts."),
    ("📊","Retention Correlation","Connect script moments to V0–25, V25–50, V50–75, V75–95 data. No more guessing."),
    ("⚡","Multi-Script Compare","Compare up to 4 scripts side-by-side. Find patterns. Replicate winners. Kill what fails."),
]
feat_html = "".join([f"""
  <div style="background:rgba(19,16,38,0.7);border:1px solid rgba(29,26,53,0.9);border-radius:14px;padding:24px;
              transition:transform 0.3s,box-shadow 0.3s;" onmouseover="this.style.transform='translateY(-4px)';this.style.boxShadow='0 20px 60px rgba(124,58,237,0.15)'"
       onmouseout="this.style.transform='';this.style.boxShadow=''">
    <div style="font-size:22px;margin-bottom:14px;">{ic}</div>
    <p style="font-size:14px;font-weight:600;color:#EDE9F8;margin:0 0 8px;font-family:Outfit,sans-serif;">{ti}</p>
    <p style="font-size:13px;color:#5A5478;line-height:1.65;margin:0;font-family:Outfit,sans-serif;">{de}</p>
  </div>""" for ic,ti,de in features])

# ── Build step cards ──────────────────────────────────────────────────────────
steps = [
    ("01","🔐","Service Account JSON","Upload your Google Cloud service account key for Drive access.","#C9973A"),
    ("02","📊","Performance Data","Drop your master tracker Excel with Meta Ads retention & CTR data.","#A855F7"),
    ("03","📁","Drive Folder ID","Paste your Google Drive folder ID containing the .docx script files.","#60a5fa"),
    ("04","🤖","AI Analysis","Select scripts, pick your AI provider, and get deep narrative intelligence.","#34d399"),
]
step_html = "".join([f"""
  <div style="background:rgba(19,16,38,0.5);border:1px solid rgba(29,26,53,0.8);border-radius:16px;padding:24px;">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;">
      <span style="font-size:11px;color:{col};font-weight:700;letter-spacing:0.1em;">{num}</span>
      <span style="font-size:22px;">{ic}</span>
    </div>
    <p style="font-size:14px;font-weight:600;color:#EDE9F8;margin:0 0 8px;font-family:Outfit,sans-serif;">{ti}</p>
    <p style="font-size:13px;color:#5A5478;line-height:1.65;margin:0;font-family:Outfit,sans-serif;">{de}</p>
  </div>""" for num,ic,ti,de,col in steps])

# ── Build marquee items ───────────────────────────────────────────────────────
items  = ["Hook Effectiveness","Pacing Analysis","Emotional Arc","CTA Clarity","Narrative Quality",
          "Retention Correlation","Multi-Script Compare","AI-Powered Insights","Drive Integration","Meta Ads Data"]
ticker = "".join([f'<span style="display:inline-flex;align-items:center;gap:8px;white-space:nowrap;padding:0 28px;font-size:13px;color:#5A5478;font-family:Outfit,sans-serif;"><span style="color:#C9973A;">✦</span>{i}</span>' for i in items*3])

SLACK = "https://pocket-fm.slack.com/team/U08NHRDM9M2"
GH    = "https://github.com/con-mayankmandal-netizen/story-analyzer-ui"

SLACK_SVG = """<svg width="12" height="12" viewBox="0 0 24 24" fill="#A855F7"><path d="M5.042 15.165a2.528 2.528 0 0 1-2.52 2.523A2.528 2.528 0 0 1 0 15.165a2.527 2.527 0 0 1 2.522-2.52h2.52v2.52zM6.313 15.165a2.527 2.527 0 0 1 2.521-2.52 2.527 2.527 0 0 1 2.521 2.52v6.313A2.528 2.528 0 0 1 8.834 24a2.528 2.528 0 0 1-2.521-2.522v-6.313zM8.834 5.042a2.528 2.528 0 0 1-2.521-2.52A2.528 2.528 0 0 1 8.834 0a2.528 2.528 0 0 1 2.521 2.522v2.52H8.834zM8.834 6.313a2.528 2.528 0 0 1 2.521 2.521 2.528 2.528 0 0 1-2.521 2.521H2.522A2.528 2.528 0 0 1 0 8.834a2.528 2.528 0 0 1 2.522-2.521h6.312zM18.956 8.834a2.528 2.528 0 0 1 2.522-2.521A2.528 2.528 0 0 1 24 8.834a2.528 2.528 0 0 1-2.522 2.521h-2.522V8.834zM17.688 8.834a2.528 2.528 0 0 1-2.523 2.521 2.527 2.527 0 0 1-2.52-2.521V2.522A2.527 2.527 0 0 1 15.165 0a2.528 2.528 0 0 1 2.523 2.522v6.312zM15.165 18.956a2.528 2.528 0 0 1 2.523 2.522A2.528 2.528 0 0 1 15.165 24a2.527 2.527 0 0 1-2.52-2.522v-2.522h2.52zM15.165 17.688a2.527 2.527 0 0 1-2.52-2.523 2.526 2.526 0 0 1 2.52-2.52h6.313A2.527 2.527 0 0 1 24 15.165a2.528 2.528 0 0 1-2.522 2.523h-6.313z"/></svg>"""

# ── Full page HTML ────────────────────────────────────────────────────────────
HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet"/>
<style>
*{{box-sizing:border-box;margin:0;padding:0;}}
html,body{{background:#06040F;color:#EDE9F8;font-family:'Outfit',sans-serif;scroll-behavior:smooth;}}
a{{text-decoration:none;color:inherit;}}
::-webkit-scrollbar{{width:4px;}}::-webkit-scrollbar-thumb{{background:rgba(201,151,58,0.4);border-radius:2px;}}

@keyframes wavePulse{{from{{transform:scaleY(0.3);opacity:0.4;}}to{{transform:scaleY(1);opacity:1;}}}}
@keyframes fadeUp{{from{{opacity:0;transform:translateY(28px);}}to{{opacity:1;transform:translateY(0);}}}}
@keyframes marqueeAnim{{from{{transform:translateX(0);}}to{{transform:translateX(-50%);}}}}
@keyframes floatOrb{{0%,100%{{transform:translateY(0px);}}50%{{transform:translateY(-24px);}}}}
@keyframes shimmer{{0%{{background-position:-200% center;}}100%{{background-position:200% center;}}}}
@keyframes glow{{0%,100%{{box-shadow:0 0 30px rgba(201,151,58,0.25);}}50%{{box-shadow:0 0 60px rgba(201,151,58,0.5);}}}}

.wave-bar{{display:inline-block;width:3px;border-radius:2px;background:#C9973A;
           animation:wavePulse var(--dur,1.2s) ease-in-out var(--delay,0s) infinite alternate;}}
.fade-up{{animation:fadeUp 0.9s ease both;}}
.d1{{animation-delay:0.05s;}}.d2{{animation-delay:0.2s;}}.d3{{animation-delay:0.35s;}}
.d4{{animation-delay:0.5s;}}.d5{{animation-delay:0.65s;}}

.gold-text{{background:linear-gradient(90deg,#C9973A 0%,#E5C068 40%,#fff 55%,#E5C068 70%,#C9973A 100%);
           background-size:200% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;
           background-clip:text;animation:shimmer 4s linear infinite;}}

.glass{{background:rgba(19,16,38,0.75);backdrop-filter:blur(24px);-webkit-backdrop-filter:blur(24px);
        border:1px solid rgba(29,26,53,0.9);}}

.btn-gold{{display:inline-flex;align-items:center;gap:8px;font-weight:700;font-size:15px;
           padding:14px 36px;border-radius:100px;color:#06040F;
           background:linear-gradient(135deg,#C9973A,#E5C068);
           box-shadow:0 0 30px rgba(201,151,58,0.3);
           transition:transform 0.3s,box-shadow 0.3s;cursor:pointer;animation:glow 3s ease-in-out infinite;}}
.btn-gold:hover{{transform:scale(1.05);box-shadow:0 0 50px rgba(201,151,58,0.55);}}
.btn-ghost{{display:inline-flex;align-items:center;gap:8px;font-size:15px;font-weight:500;
            padding:14px 36px;border-radius:100px;color:#EDE9F8;
            background:rgba(19,16,38,0.7);border:1px solid rgba(29,26,53,0.9);
            transition:all 0.3s;}}
.btn-ghost:hover{{border-color:rgba(124,58,237,0.4);background:rgba(124,58,237,0.08);}}

.marquee-wrap{{overflow:hidden;}}
.marquee-track{{display:flex;width:max-content;animation:marqueeAnim 30s linear infinite;}}
.orb{{position:absolute;border-radius:50%;pointer-events:none;}}

.card{{transition:transform 0.3s,box-shadow 0.3s;}}
.card:hover{{transform:translateY(-5px);box-shadow:0 24px 60px rgba(124,58,237,0.18)!important;}}

nav a:hover{{color:#EDE9F8!important;}}
</style>
</head>
<body>

<!-- ══ HEADER ══ -->
<div style="position:sticky;top:0;z-index:999;background:rgba(6,4,15,0.96);
            backdrop-filter:blur(20px);border-bottom:1px solid rgba(29,26,53,0.8);">

  <!-- Tagline strip -->
  <div style="padding:5px 40px;border-bottom:1px solid rgba(29,26,53,0.4);
              display:flex;align-items:center;justify-content:space-between;">
    <p style="font-size:11px;color:rgba(90,84,120,0.7);margin:0;">
      Open source &bull; AI-powered &bull; Built for
      <span style="color:#C9973A;font-weight:600;">PocketFM</span>'s creative &amp; performance marketing teams
    </p>
    <div style="display:flex;align-items:center;gap:6px;">
      {SLACK_SVG}
      <span style="font-size:11px;color:rgba(90,84,120,0.5);">by</span>
      <a href="{SLACK}" target="_blank"
         style="font-size:11px;color:#E5C068;font-weight:600;text-shadow:0 0 10px rgba(229,192,104,0.4);">Mayank Mandal</a>
    </div>
  </div>

  <!-- Nav -->
  <nav style="display:flex;align-items:center;justify-content:space-between;padding:10px 40px;">
    <a href="#" onclick="window.parent.location.href='/'" style="display:flex;align-items:center;gap:10px;">
      <div style="display:flex;align-items:flex-end;gap:2px;height:20px;">
        <div class="wave-bar" style="height:6px;--dur:1.0s;"></div>
        <div class="wave-bar" style="height:14px;--dur:1.3s;--delay:0.12s;"></div>
        <div class="wave-bar" style="height:10px;--dur:1.1s;--delay:0.28s;"></div>
        <div class="wave-bar" style="height:18px;--dur:1.4s;--delay:0.08s;"></div>
        <div class="wave-bar" style="height:8px;--dur:0.9s;--delay:0.22s;"></div>
      </div>
      <span style="font-weight:600;font-size:15px;color:#EDE9F8;">StoryAnalyzer</span>
    </a>
    <div style="display:flex;align-items:center;gap:4px;">
      <a href="#features" style="font-size:13px;color:#5A5478;padding:6px 14px;transition:color 0.2s;">Features</a>
      <a href="#howitworks" style="font-size:13px;color:#5A5478;padding:6px 14px;transition:color 0.2s;">How It Works</a>
      <a href="#" onclick="window.parent.location.href='/Help';return false;" style="font-size:13px;color:#5A5478;padding:6px 14px;transition:color 0.2s;">Help</a>
      <a href="#" onclick="window.parent.location.href='/Tool';return false;" class="btn-gold" style="font-size:13px;padding:9px 24px;">Analyze a Script &rarr;</a>
    </div>
  </nav>
</div>

<!-- ══ HERO ══ -->
<section style="position:relative;overflow:hidden;padding:80px 40px 60px;
                background:linear-gradient(160deg,rgba(124,58,237,0.07) 0%,transparent 60%);">
  <!-- Orbs -->
  <div class="orb" style="width:500px;height:500px;top:-80px;right:-60px;
       background:radial-gradient(circle,rgba(124,58,237,0.1) 0%,transparent 70%);
       animation:floatOrb 10s ease-in-out infinite;"></div>
  <div class="orb" style="width:380px;height:380px;bottom:-60px;left:-40px;
       background:radial-gradient(circle,rgba(201,151,58,0.07) 0%,transparent 70%);
       animation:floatOrb 8s ease-in-out 2s infinite;"></div>

  <div style="max-width:1200px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:60px;align-items:center;position:relative;z-index:1;">

    <!-- Left text -->
    <div>
      <div class="fade-up d1" style="display:inline-flex;align-items:center;gap:8px;margin-bottom:20px;
           background:rgba(124,58,237,0.08);border:1px solid rgba(124,58,237,0.2);
           border-radius:100px;padding:6px 16px;">
        <span style="font-size:12px;color:#A855F7;font-weight:500;">🎬 PocketFM Script Intelligence</span>
      </div>
      <h1 class="fade-up d2" style="font-family:'DM Serif Display',serif;
          font-size:clamp(2.4rem,4.5vw,4rem);line-height:1.1;color:#EDE9F8;margin:0 0 4px;">
        Decode your
      </h1>
      <h1 class="fade-up d2" style="font-family:'DM Serif Display',serif;
          font-size:clamp(2.4rem,4.5vw,4rem);line-height:1.1;margin:0 0 24px;
          color:#C9973A;font-style:italic;">
        Promo Story
      </h1>
      <p class="fade-up d3" style="font-size:16px;color:#5A5478;line-height:1.75;max-width:480px;margin-bottom:36px;">
        Connect your data, load your scripts, choose your AI — get deep narrative
        insight on every audio ad. Stop guessing. Start knowing why stories work.
      </p>
      <div class="fade-up d4" style="display:flex;gap:14px;flex-wrap:wrap;margin-bottom:40px;">
        <a href="#" onclick="window.parent.location.href='/Tool';return false;" class="btn-gold">✦ Analyze a Script</a>
        <a href="#howitworks" class="btn-ghost">See How It Works</a>
      </div>
      <div class="fade-up d5" style="display:flex;gap:32px;padding-top:28px;border-top:1px solid rgba(29,26,53,0.8);">
        <div>
          <p style="font-size:28px;font-weight:800;color:#C9973A;margin:0;">5</p>
          <p style="font-size:11px;color:#5A5478;margin:2px 0 0;text-transform:uppercase;letter-spacing:0.06em;">Dimensions</p>
        </div>
        <div>
          <p style="font-size:28px;font-weight:800;color:#A855F7;margin:0;">3</p>
          <p style="font-size:11px;color:#5A5478;margin:2px 0 0;text-transform:uppercase;letter-spacing:0.06em;">AI Providers</p>
        </div>
        <div>
          <p style="font-size:28px;font-weight:800;color:#EDE9F8;margin:0;">4</p>
          <p style="font-size:11px;color:#5A5478;margin:2px 0 0;text-transform:uppercase;letter-spacing:0.06em;">Scripts at once</p>
        </div>
      </div>
    </div>

    <!-- Right: Dashboard mockup card -->
    <div class="fade-up d3">
      <div class="glass card" style="border-radius:20px;overflow:hidden;
           box-shadow:0 0 80px rgba(124,58,237,0.15),0 0 160px rgba(201,151,58,0.06);">
        <!-- Window bar -->
        <div style="padding:14px 20px;border-bottom:1px solid rgba(29,26,53,0.8);
                    display:flex;align-items:center;justify-content:space-between;">
          <div style="display:flex;gap:6px;">
            <div style="width:10px;height:10px;border-radius:50%;background:#ef4444;"></div>
            <div style="width:10px;height:10px;border-radius:50%;background:#f59e0b;"></div>
            <div style="width:10px;height:10px;border-radius:50%;background:#22c55e;"></div>
          </div>
          <span style="font-size:11px;color:#5A5478;">GAI647 — Analysis Complete</span>
          <span style="font-size:10px;background:rgba(34,197,94,0.1);color:#22c55e;
                       border:1px solid rgba(34,197,94,0.2);border-radius:4px;padding:2px 8px;">Live</span>
        </div>
        <!-- Score rings -->
        <div style="padding:24px 20px;">
          <div style="display:flex;justify-content:space-around;margin-bottom:20px;">
            {rings}
          </div>
          <!-- Verdict -->
          <div style="background:rgba(201,151,58,0.06);border:1px solid rgba(201,151,58,0.15);
                      border-radius:10px;padding:12px 14px;margin-bottom:14px;">
            <p style="font-size:10px;color:#5A5478;margin:0 0 4px;text-transform:uppercase;letter-spacing:0.06em;">Verdict</p>
            <p style="font-size:13px;color:#EDE9F8;margin:0;font-family:'DM Serif Display',serif;font-style:italic;">
              "Strong hook, emotional drop at 60s. CTA clarity needs tightening."
            </p>
          </div>
          <!-- Mini stats -->
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
            <div style="background:rgba(13,11,30,0.8);border-radius:8px;padding:10px 12px;">
              <p style="font-size:10px;color:#5A5478;margin:0 0 6px;">ThruPlay %</p>
              <div style="height:4px;background:rgba(29,26,53,0.8);border-radius:2px;margin-bottom:5px;">
                <div style="height:4px;width:68%;background:linear-gradient(90deg,#7C3AED,#A855F7);border-radius:2px;"></div>
              </div>
              <p style="font-size:13px;color:#A855F7;font-weight:700;margin:0;">68%</p>
            </div>
            <div style="background:rgba(13,11,30,0.8);border-radius:8px;padding:10px 12px;">
              <p style="font-size:10px;color:#5A5478;margin:0 0 6px;">CTR</p>
              <div style="height:4px;background:rgba(29,26,53,0.8);border-radius:2px;margin-bottom:5px;">
                <div style="height:4px;width:42%;background:linear-gradient(90deg,#C9973A,#E5C068);border-radius:2px;"></div>
              </div>
              <p style="font-size:13px;color:#C9973A;font-weight:700;margin:0;">4.2%</p>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</section>

<!-- ══ MARQUEE ══ -->
<div style="border-top:1px solid rgba(29,26,53,0.6);border-bottom:1px solid rgba(29,26,53,0.6);
            padding:14px 0;background:rgba(13,11,30,0.5);overflow:hidden;">
  <div class="marquee-track">{ticker}</div>
</div>

<!-- ══ FEATURES ══ -->
<section id="features" style="padding:80px 40px 50px;">
  <div style="max-width:1200px;margin:0 auto;">
    <div style="text-align:center;margin-bottom:52px;">
      <p style="font-size:11px;color:#5A5478;text-transform:uppercase;letter-spacing:0.12em;margin-bottom:8px;">What It Does</p>
      <h2 style="font-family:'DM Serif Display',serif;font-size:clamp(1.8rem,3vw,2.8rem);color:#EDE9F8;margin:0;">
        Everything your script needs, <span style="color:#C9973A;font-style:italic;">decoded.</span>
      </h2>
    </div>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;">
      {feat_html}
    </div>
  </div>
</section>

<!-- ══ HOW IT WORKS ══ -->
<section id="howitworks" style="padding:80px 40px;background:rgba(13,11,30,0.5);">
  <div style="max-width:1200px;margin:0 auto;">
    <div style="text-align:center;margin-bottom:56px;">
      <p style="font-size:11px;color:#5A5478;text-transform:uppercase;letter-spacing:0.12em;margin-bottom:8px;">Process</p>
      <h2 style="font-family:'DM Serif Display',serif;font-size:clamp(1.8rem,3vw,2.8rem);color:#EDE9F8;margin:0;">
        Four inputs. <span style="color:#C9973A;font-style:italic;">One truth.</span>
      </h2>
    </div>
    <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px;">
      {step_html}
    </div>
  </div>
</section>

<!-- ══ AI PROVIDERS ══ -->
<section style="padding:80px 40px;">
  <div style="max-width:900px;margin:0 auto;text-align:center;">
    <p style="font-size:11px;color:#5A5478;text-transform:uppercase;letter-spacing:0.12em;margin-bottom:8px;">AI Providers</p>
    <h2 style="font-family:'DM Serif Display',serif;font-size:clamp(1.8rem,3vw,2.6rem);color:#EDE9F8;margin-bottom:40px;">
      Your choice of intelligence.
    </h2>
    <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:20px;">
      <div class="glass card" style="border-radius:16px;padding:32px;text-align:center;">
        <div style="font-size:32px;margin-bottom:14px;">🟡</div>
        <p style="font-weight:700;color:#EDE9F8;font-size:16px;margin:0 0 6px;">Gemini Flash</p>
        <p style="font-size:12px;color:#34d399;margin:0 0 14px;font-weight:600;">FREE — 1500 req/day</p>
        <p style="font-size:13px;color:#5A5478;line-height:1.65;margin:0;">Great for general narrative analysis. No card needed.</p>
      </div>
      <div class="glass card" style="border-radius:16px;padding:32px;text-align:center;border-color:rgba(168,85,247,0.2);">
        <div style="font-size:32px;margin-bottom:14px;">⚡</div>
        <p style="font-weight:700;color:#EDE9F8;font-size:16px;margin:0 0 6px;">Groq Llama</p>
        <p style="font-size:12px;color:#34d399;margin:0 0 14px;font-weight:600;">FREE — Ultra fast</p>
        <p style="font-size:13px;color:#5A5478;line-height:1.65;margin:0;">Best for bulk script comparison at speed.</p>
      </div>
      <div class="glass card" style="border-radius:16px;padding:32px;text-align:center;">
        <div style="font-size:32px;margin-bottom:14px;">🤖</div>
        <p style="font-weight:700;color:#EDE9F8;font-size:16px;margin:0 0 6px;">Claude Haiku</p>
        <p style="font-size:12px;color:#fbbf24;margin:0 0 14px;font-weight:600;">~$0.001/run</p>
        <p style="font-size:13px;color:#5A5478;line-height:1.65;margin:0;">Deepest insight for nuanced storytelling analysis.</p>
      </div>
    </div>
  </div>
</section>

<!-- ══ CTA ══ -->
<section style="padding:80px 40px;text-align:center;
                background:linear-gradient(180deg,transparent,rgba(124,58,237,0.08),transparent);">
  <div style="max-width:680px;margin:0 auto;position:relative;z-index:1;">
    <div style="font-size:52px;margin-bottom:18px;">🎬</div>
    <h2 style="font-family:'DM Serif Display',serif;font-size:clamp(2rem,4vw,3rem);color:#EDE9F8;margin:0 0 16px;">
      Ready to decode<br><span style="color:#C9973A;font-style:italic;">your Promo ads?</span>
    </h2>
    <p style="font-size:15px;color:#5A5478;max-width:500px;margin:0 auto 36px;line-height:1.75;">
      Open source, AI-powered, and built specifically for PocketFM's creative and performance marketing teams.
    </p>
    <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;">
      <a href="#" onclick="window.parent.location.href='/Tool';return false;" class="btn-gold" style="font-size:16px;padding:16px 48px;">✦ Analyze a Script</a>
      <a href="{GH}" target="_blank" class="btn-ghost" style="font-size:15px;padding:16px 36px;">View on GitHub</a>
    </div>
  </div>
</section>

<!-- ══ FOOTER ══ -->
<footer style="border-top:1px solid rgba(29,26,53,0.8);background:rgba(6,4,15,0.98);padding:48px 40px 32px;">
  <div style="max-width:1200px;margin:0 auto;display:flex;flex-direction:column;align-items:center;gap:18px;text-align:center;">
    <div style="display:flex;align-items:center;gap:10px;">
      <div style="display:flex;align-items:flex-end;gap:2px;height:20px;">
        <div class="wave-bar" style="height:5px;--dur:1.0s;"></div>
        <div class="wave-bar" style="height:13px;--dur:1.3s;--delay:0.1s;"></div>
        <div class="wave-bar" style="height:9px;--dur:1.0s;--delay:0.2s;"></div>
        <div class="wave-bar" style="height:17px;--dur:1.4s;--delay:0.08s;"></div>
        <div class="wave-bar" style="height:7px;--dur:0.9s;--delay:0.22s;"></div>
      </div>
      <span style="font-weight:600;font-size:15px;color:#EDE9F8;">StoryAnalyzer</span>
    </div>
    <div style="width:60px;height:1px;background:linear-gradient(90deg,transparent,#C9973A,transparent);"></div>
    <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;justify-content:center;">
      <span style="font-size:13px;color:rgba(90,84,120,0.7);">Designed &amp; Developed by</span>
      <a href="{SLACK}" target="_blank"
         style="display:inline-flex;align-items:center;gap:7px;
                background:rgba(201,151,58,0.08);border:1px solid rgba(201,151,58,0.3);
                border-radius:100px;padding:7px 18px 7px 13px;transition:all 0.3s;"
         onmouseover="this.style.background='rgba(201,151,58,0.15)';this.style.boxShadow='0 0 20px rgba(229,192,104,0.2)'"
         onmouseout="this.style.background='rgba(201,151,58,0.08)';this.style.boxShadow='none'">
        {SLACK_SVG}
        <span style="font-size:14px;font-weight:700;color:#E5C068;text-shadow:0 0 12px rgba(229,192,104,0.4);">Mayank Mandal</span>
      </a>
    </div>
    <p style="font-size:11px;color:rgba(90,84,120,0.4);margin:0;">PocketFM Script Intelligence &bull; Open Source &bull; 2025</p>
  </div>
</footer>

</body>
</html>"""

st.components.v1.html(HTML, height=4200, scrolling=True)
