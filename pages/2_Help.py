"""
StoryAnalyzer — Help & Contact Page (Native Streamlit)
Redesigned to match help.html: floating particles, film strip, elevated contact cards, styled FAQ.
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

/* ── Animations ── */
@keyframes wavePulse   { from { transform:scaleY(0.4); opacity:0.5; } to { transform:scaleY(1); opacity:1; } }
@keyframes shimmer     { 0% { background-position:-200% center; } 100% { background-position:200% center; } }
@keyframes fadeUp      { from { opacity:0; transform:translateY(24px); } to { opacity:1; transform:translateY(0); } }
@keyframes ringPulse   { 0%,100% { box-shadow:0 0 0 0px rgba(201,151,58,0.35),0 0 30px rgba(124,58,237,0.2); }
                         50%      { box-shadow:0 0 0 8px rgba(201,151,58,0.08),0 0 50px rgba(124,58,237,0.35); } }
@keyframes floatParticle {
  0%   { transform: translateY(0px) translateX(0px) scale(1);   opacity:0.4; }
  33%  { transform: translateY(-18px) translateX(8px) scale(1.1); opacity:0.7; }
  66%  { transform: translateY(-8px) translateX(-6px) scale(0.95); opacity:0.5; }
  100% { transform: translateY(0px) translateX(0px) scale(1);   opacity:0.4; }
}

/* ── Reusable classes ── */
.wave-bar { display:inline-block;width:3px;border-radius:2px;background:#C9973A;
            animation:wavePulse var(--dur,1.2s) ease-in-out var(--delay,0s) infinite alternate; }
.name-shimmer { background:linear-gradient(90deg,#C9973A 0%,#E5C068 30%,#fff 50%,#E5C068 70%,#C9973A 100%);
                background-size:200% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;
                background-clip:text;animation:shimmer 4s linear infinite; }
.glass { background:rgba(19,16,38,0.7);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border:1px solid rgba(29,26,53,0.9); }
.fade-1 { animation:fadeUp 0.7s ease 0.1s both; }
.fade-2 { animation:fadeUp 0.7s ease 0.25s both; }
.fade-3 { animation:fadeUp 0.7s ease 0.4s both; }
.fade-4 { animation:fadeUp 0.7s ease 0.55s both; }
.particle-orb { position:absolute;border-radius:50%;animation:floatParticle var(--dur,6s) ease-in-out var(--delay,0s) infinite;pointer-events:none; }

/* ── Film strip ── */
.film-strip { display:flex;gap:4px; }
.film-hole  { width:8px;height:6px;background:rgba(201,151,58,0.15);border-radius:2px;border:1px solid rgba(201,151,58,0.2); }

/* ── Contact cards ── */
.contact-card-wrap { transition:transform 0.3s ease,box-shadow 0.3s ease; border-radius:16px; overflow:hidden; }
.contact-card-wrap:hover { transform:translateY(-4px); }

/* ── FAQ expander override ── */
[data-testid="stExpander"] {
  background: rgba(19,16,38,0.6) !important;
  border: 1px solid rgba(29,26,53,0.9) !important;
  border-radius: 12px !important;
  margin-bottom: 8px !important;
}
[data-testid="stExpander"] summary {
  color: #EDE9F8 !important;
  font-size: 14px !important;
  font-weight: 500 !important;
  padding: 4px 0 !important;
}
[data-testid="stExpander"] summary:hover { background: rgba(13,11,30,0.4) !important; }
[data-testid="stExpander"] [data-testid="stExpanderDetails"] {
  border-top: 1px solid rgba(29,26,53,0.6) !important;
  padding-top: 12px !important;
}
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="position:sticky;top:0;z-index:999;background:rgba(6,4,15,0.92);
            backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);">
  <div style="padding:6px 40px;border-bottom:1px solid rgba(29,26,53,0.3);
              display:flex;align-items:center;justify-content:space-between;">
    <p style="font-size:11px;color:rgba(90,84,120,0.7);margin:0;">
      Open source &bull; AI-powered &bull; Built for
      <span style="color:#C9973A;font-weight:600;">PocketFM</span>'s creative &amp; performance marketing teams
    </p>
    <div style="display:flex;align-items:center;gap:8px;">
      <svg width="11" height="11" viewBox="0 0 24 24" fill="#A855F7" style="flex-shrink:0;">
        <path d="M5.042 15.165a2.528 2.528 0 0 1-2.52 2.523A2.528 2.528 0 0 1 0 15.165a2.527 2.527 0 0 1 2.522-2.52h2.52v2.52zM6.313 15.165a2.527 2.527 0 0 1 2.521-2.52 2.527 2.527 0 0 1 2.521 2.52v6.313A2.528 2.528 0 0 1 8.834 24a2.528 2.528 0 0 1-2.521-2.522v-6.313zM8.834 5.042a2.528 2.528 0 0 1-2.521-2.52A2.528 2.528 0 0 1 8.834 0a2.528 2.528 0 0 1 2.521 2.522v2.52H8.834zM8.834 6.313a2.528 2.528 0 0 1 2.521 2.521 2.528 2.528 0 0 1-2.521 2.521H2.522A2.528 2.528 0 0 1 0 8.834a2.528 2.528 0 0 1 2.522-2.521h6.312zM18.956 8.834a2.528 2.528 0 0 1 2.522-2.521A2.528 2.528 0 0 1 24 8.834a2.528 2.528 0 0 1-2.522 2.521h-2.522V8.834zM17.688 8.834a2.528 2.528 0 0 1-2.523 2.521 2.527 2.527 0 0 1-2.52-2.521V2.522A2.527 2.527 0 0 1 15.165 0a2.528 2.528 0 0 1 2.523 2.522v6.312zM15.165 18.956a2.528 2.528 0 0 1 2.523 2.522A2.528 2.528 0 0 1 15.165 24a2.527 2.527 0 0 1-2.52-2.522v-2.522h2.52zM15.165 17.688a2.527 2.527 0 0 1-2.52-2.523 2.526 2.526 0 0 1 2.52-2.52h6.313A2.527 2.527 0 0 1 24 15.165a2.528 2.528 0 0 1-2.522 2.523h-6.313z"/>
      </svg>
      <span style="font-size:11px;color:rgba(90,84,120,0.6);">by</span>
      <a href="https://pocket-fm.slack.com/team/U08NHRDM9M2" target="_blank"
         style="font-size:11px;color:#E5C068;font-weight:600;text-decoration:none;
                text-shadow:0 0 10px rgba(229,192,104,0.45);">Mayank Mandal</a>
    </div>
  </div>
  <nav style="display:flex;align-items:center;justify-content:space-between;padding:10px 40px;
              border-bottom:1px solid rgba(29,26,53,0.4);">
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
    <div style="display:flex;align-items:center;gap:4px;">
      <a href="/"     style="font-size:12px;color:#5A5478;padding:6px 12px;text-decoration:none;transition:color 0.2s;"
         onmouseover="this.style.color='#EDE9F8'" onmouseout="this.style.color='#5A5478'">Overview</a>
      <a href="/Tool" style="font-size:12px;color:#5A5478;padding:6px 12px;text-decoration:none;transition:color 0.2s;"
         onmouseover="this.style.color='#EDE9F8'" onmouseout="this.style.color='#5A5478'">Tool</a>
      <a href="/Help" style="font-size:12px;color:#C9973A;font-weight:600;padding:6px 12px;text-decoration:none;">Help</a>
      <a href="https://github.com/con-mayankmandal-netizen/story-analyzer-ui" target="_blank"
         style="font-size:12px;font-weight:600;background:#7C3AED;color:#fff;
                padding:7px 18px;border-radius:100px;text-decoration:none;
                transition:background 0.2s,transform 0.2s;"
         onmouseover="this.style.background='#A855F7';this.style.transform='scale(1.05)'"
         onmouseout="this.style.background='#7C3AED';this.style.transform='scale(1)'">GitHub</a>
    </div>
  </nav>
</div>
""", unsafe_allow_html=True)

# ── Hero with floating particles + film strip ─────────────────────────────────
st.markdown("""
<section style="position:relative;overflow:hidden;padding:60px 40px 48px;text-align:center;
                background:linear-gradient(180deg,rgba(124,58,237,0.05) 0%,transparent 100%);">

  <!-- Floating ambient orbs (pure CSS, self-contained) -->
  <div class="particle-orb" style="width:300px;height:300px;top:5%;left:-4%;
       background:radial-gradient(circle,rgba(124,58,237,0.12) 0%,transparent 70%);
       --dur:8s;--delay:0s;"></div>
  <div class="particle-orb" style="width:250px;height:250px;top:8%;right:3%;
       background:radial-gradient(circle,rgba(201,151,58,0.1) 0%,transparent 70%);
       --dur:10s;--delay:2s;"></div>
  <div class="particle-orb" style="width:180px;height:180px;bottom:10%;left:28%;
       background:radial-gradient(circle,rgba(168,85,247,0.08) 0%,transparent 70%);
       --dur:7s;--delay:1s;"></div>

  <div style="position:relative;max-width:700px;margin:0 auto;">

    <!-- Film strip decoration -->
    <div class="fade-1" style="display:flex;justify-content:center;margin-bottom:24px;">
      <div class="film-strip">
        <div class="film-hole"></div><div class="film-hole"></div><div class="film-hole"></div>
        <div class="film-hole"></div><div class="film-hole"></div><div class="film-hole"></div>
        <div class="film-hole"></div><div class="film-hole"></div>
      </div>
    </div>

    <!-- Badge -->
    <div class="fade-1" style="display:inline-flex;align-items:center;gap:8px;margin-bottom:20px;
         background:rgba(124,58,237,0.08);border:1px solid rgba(124,58,237,0.2);
         border-radius:100px;padding:5px 16px;">
      <span style="font-size:12px;color:#A855F7;">🎬 Help &amp; Contact</span>
    </div>

    <!-- Heading -->
    <h1 class="fade-2" style="font-family:'DM Serif Display',serif;
        font-size:clamp(2.2rem,5vw,4rem);line-height:1.12;color:#EDE9F8;margin:0 0 16px;">
      Got a question?<br>
      <span style="color:#C9973A;font-style:italic;">I'm here to help.</span>
    </h1>

    <p class="fade-3" style="font-size:15px;color:#5A5478;max-width:500px;margin:0 auto;line-height:1.7;">
      StoryAnalyzer is built and maintained by a single developer at PocketFM.
      Reach out anytime — whether it's a bug, a feature idea, or just a question about how it works.
    </p>
  </div>
</section>
""", unsafe_allow_html=True)

# ── Developer card — self-contained, correct opening + closing tags ───────────
st.markdown("""
<div style="max-width:820px;margin:0 auto;padding:0 40px 48px;">
  <div class="glass fade-4" style="border-radius:20px;overflow:hidden;
       box-shadow:0 0 60px rgba(124,58,237,0.12),0 0 120px rgba(201,151,58,0.06);">

    <!-- Top accent bar -->
    <div style="height:3px;background:linear-gradient(90deg,#7C3AED,#C9973A,#A855F7);"></div>

    <div style="padding:36px 40px;">
      <div style="display:flex;align-items:flex-start;gap:28px;margin-bottom:28px;flex-wrap:wrap;">

        <!-- Avatar with ring pulse -->
        <div style="flex-shrink:0;">
          <div style="width:96px;height:96px;border-radius:16px;
                      display:flex;align-items:center;justify-content:center;position:relative;
                      background:linear-gradient(135deg,rgba(124,58,237,0.25),rgba(201,151,58,0.15));
                      border:1.5px solid rgba(201,151,58,0.3);
                      animation:ringPulse 3s ease-in-out infinite;">
            <span style="font-family:'DM Serif Display',serif;font-size:36px;color:#E5C068;line-height:1;">MM</span>
            <!-- Online indicator -->
            <div style="position:absolute;bottom:-4px;right:-4px;width:18px;height:18px;
                        border-radius:50%;background:#22c55e;border:2px solid #06040F;
                        display:flex;align-items:center;justify-content:center;">
              <div style="width:8px;height:8px;border-radius:50%;background:#86efac;"></div>
            </div>
          </div>
        </div>

        <!-- Name + role + tags -->
        <div style="flex:1;min-width:200px;">
          <p style="font-size:10px;color:rgba(90,84,120,0.6);text-transform:uppercase;
                    letter-spacing:0.12em;margin:0 0 4px;">Developer &amp; Maintainer</p>
          <h2 class="name-shimmer" style="font-family:'DM Serif Display',serif;
              font-size:clamp(1.6rem,3vw,2.2rem);margin:0 0 4px;">Mayank Mandal</h2>
          <p style="font-size:13px;color:#5A5478;margin:0 0 16px;">
            PocketFM · Creative &amp; Performance Marketing Tech
          </p>
          <div style="display:flex;flex-wrap:wrap;gap:8px;">
            <span style="font-size:11px;padding:3px 12px;border-radius:100px;
                         background:rgba(124,58,237,0.1);border:1px solid rgba(124,58,237,0.2);color:#A855F7;">Python</span>
            <span style="font-size:11px;padding:3px 12px;border-radius:100px;
                         background:rgba(201,151,58,0.08);border:1px solid rgba(201,151,58,0.2);color:#C9973A;">AI / LLMs</span>
            <span style="font-size:11px;padding:3px 12px;border-radius:100px;
                         background:rgba(29,26,53,0.6);border:1px solid rgba(29,26,53,0.9);color:#5A5478;">Streamlit</span>
            <span style="font-size:11px;padding:3px 12px;border-radius:100px;
                         background:rgba(29,26,53,0.6);border:1px solid rgba(29,26,53,0.9);color:#5A5478;">Google Drive API</span>
            <span style="font-size:11px;padding:3px 12px;border-radius:100px;
                         background:rgba(16,185,129,0.06);border:1px solid rgba(16,185,129,0.15);color:#34d399;">Open Source</span>
          </div>
        </div>
      </div>

      <!-- Horizontal divider -->
      <div style="height:1px;background:linear-gradient(90deg,transparent,rgba(29,26,53,1),transparent);margin-bottom:0;"></div>

      <!-- Three contact cards as a grid — fully self-contained -->
      <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:0;min-height:160px;">

        <!-- Email -->
        <a href="mailto:con-mayank.mandal@pocketfm.com"
           style="text-decoration:none;padding:24px;
                  border-right:1px solid rgba(29,26,53,0.6);
                  display:flex;flex-direction:column;gap:12px;
                  transition:background 0.3s,transform 0.3s;"
           onmouseover="this.style.background='rgba(13,11,30,0.6)'"
           onmouseout="this.style.background='transparent'">
          <div style="display:flex;align-items:center;gap:12px;">
            <div style="width:36px;height:36px;border-radius:10px;flex-shrink:0;
                        display:flex;align-items:center;justify-content:center;
                        background:rgba(201,151,58,0.1);border:1px solid rgba(201,151,58,0.2);">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#C9973A" stroke-width="2">
                <rect x="2" y="4" width="20" height="16" rx="2"/>
                <path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>
              </svg>
            </div>
            <div>
              <p style="font-size:10px;color:rgba(90,84,120,0.5);text-transform:uppercase;
                        letter-spacing:0.08em;margin:0 0 2px;">Email</p>
              <p style="font-size:12px;font-weight:600;color:#C9973A;margin:0;">Send a mail</p>
            </div>
          </div>
          <p style="font-size:12px;color:rgba(90,84,120,0.8);font-family:'Outfit',sans-serif;
                    margin:0;line-height:1.5;word-break:break-all;">
            con-mayank.mandal<br/>@pocketfm.com
          </p>
          <div style="display:flex;align-items:center;gap:4px;margin-top:auto;">
            <span style="font-size:11px;color:rgba(90,84,120,0.4);">Click to open mail app</span>
            <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="rgba(90,84,120,0.4)" stroke-width="2">
              <path d="m9 18 6-6-6-6"/>
            </svg>
          </div>
        </a>

        <!-- Slack -->
        <a href="https://pocket-fm.slack.com/team/U08NHRDM9M2" target="_blank" rel="noopener"
           style="text-decoration:none;padding:24px;
                  border-right:1px solid rgba(29,26,53,0.6);
                  display:flex;flex-direction:column;gap:12px;
                  transition:background 0.3s;"
           onmouseover="this.style.background='rgba(13,11,30,0.6)'"
           onmouseout="this.style.background='transparent'">
          <div style="display:flex;align-items:center;gap:12px;">
            <div style="width:36px;height:36px;border-radius:10px;flex-shrink:0;
                        display:flex;align-items:center;justify-content:center;
                        background:rgba(168,85,247,0.1);border:1px solid rgba(168,85,247,0.2);">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="#A855F7">
                <path d="M5.042 15.165a2.528 2.528 0 0 1-2.52 2.523A2.528 2.528 0 0 1 0 15.165a2.527 2.527 0 0 1 2.522-2.52h2.52v2.52zM6.313 15.165a2.527 2.527 0 0 1 2.521-2.52 2.527 2.527 0 0 1 2.521 2.52v6.313A2.528 2.528 0 0 1 8.834 24a2.528 2.528 0 0 1-2.521-2.522v-6.313zM8.834 5.042a2.528 2.528 0 0 1-2.521-2.52A2.528 2.528 0 0 1 8.834 0a2.528 2.528 0 0 1 2.521 2.522v2.52H8.834zM8.834 6.313a2.528 2.528 0 0 1 2.521 2.521 2.528 2.528 0 0 1-2.521 2.521H2.522A2.528 2.528 0 0 1 0 8.834a2.528 2.528 0 0 1 2.522-2.521h6.312zM18.956 8.834a2.528 2.528 0 0 1 2.522-2.521A2.528 2.528 0 0 1 24 8.834a2.528 2.528 0 0 1-2.522 2.521h-2.522V8.834zM17.688 8.834a2.528 2.528 0 0 1-2.523 2.521 2.527 2.527 0 0 1-2.52-2.521V2.522A2.527 2.527 0 0 1 15.165 0a2.528 2.528 0 0 1 2.523 2.522v6.312zM15.165 18.956a2.528 2.528 0 0 1 2.523 2.522A2.528 2.528 0 0 1 15.165 24a2.527 2.527 0 0 1-2.52-2.522v-2.522h2.52zM15.165 17.688a2.527 2.527 0 0 1-2.52-2.523 2.526 2.526 0 0 1 2.52-2.52h6.313A2.527 2.527 0 0 1 24 15.165a2.528 2.528 0 0 1-2.522 2.523h-6.313z"/>
              </svg>
            </div>
            <div>
              <p style="font-size:10px;color:rgba(90,84,120,0.5);text-transform:uppercase;
                        letter-spacing:0.08em;margin:0 0 2px;">Slack</p>
              <p style="font-size:12px;font-weight:600;color:#A855F7;margin:0;">Message on Slack</p>
            </div>
          </div>
          <p style="font-size:12px;color:rgba(90,84,120,0.8);line-height:1.5;margin:0;">
            Find me on PocketFM's Slack workspace. DMs are always open — fastest way to reach me.
          </p>
          <div style="display:flex;align-items:center;gap:6px;margin-top:auto;">
            <div style="width:6px;height:6px;border-radius:50%;background:#22c55e;"></div>
            <span style="font-size:11px;color:rgba(90,84,120,0.4);">Usually responds within the day</span>
          </div>
        </a>

        <!-- GitHub -->
        <a href="https://github.com/con-mayankmandal-netizen/story-analyzer-ui" target="_blank" rel="noopener"
           style="text-decoration:none;padding:24px;
                  display:flex;flex-direction:column;gap:12px;
                  transition:background 0.3s;"
           onmouseover="this.style.background='rgba(13,11,30,0.6)'"
           onmouseout="this.style.background='transparent'">
          <div style="display:flex;align-items:center;gap:12px;">
            <div style="width:36px;height:36px;border-radius:10px;flex-shrink:0;
                        display:flex;align-items:center;justify-content:center;
                        background:rgba(237,233,248,0.05);border:1px solid rgba(237,233,248,0.1);">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="#EDE9F8">
                <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/>
              </svg>
            </div>
            <div>
              <p style="font-size:10px;color:rgba(90,84,120,0.5);text-transform:uppercase;
                        letter-spacing:0.08em;margin:0 0 2px;">GitHub</p>
              <p style="font-size:12px;font-weight:600;color:rgba(237,233,248,0.8);margin:0;">Open an Issue</p>
            </div>
          </div>
          <p style="font-size:12px;color:rgba(90,84,120,0.8);line-height:1.5;margin:0;">
            Found a bug? Have a feature request? Open a GitHub issue — I review them regularly.
          </p>
          <div style="display:flex;align-items:center;gap:4px;margin-top:auto;">
            <span style="font-size:11px;color:rgba(90,84,120,0.4);">Opens in new tab</span>
            <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="rgba(90,84,120,0.4)" stroke-width="2">
              <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>
              <polyline points="15,3 21,3 21,9"/>
              <line x1="10" y1="14" x2="21" y2="3"/>
            </svg>
          </div>
        </a>

      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── FAQ section ───────────────────────────────────────────────────────────────
st.markdown("""
<div style="max-width:820px;margin:0 auto;padding:0 40px 20px;">
  <div style="text-align:center;margin-bottom:28px;">
    <p style="font-size:10px;color:rgba(90,84,120,0.5);text-transform:uppercase;letter-spacing:0.12em;margin:0 0 8px;">Quick Help</p>
    <h2 style="font-family:'DM Serif Display',serif;font-size:clamp(1.5rem,3vw,2rem);color:#EDE9F8;margin:0;">
      Common Questions
    </h2>
  </div>
</div>
""", unsafe_allow_html=True)

faqs = [
    ("📄 What format should the JSON key file be in?",
     "It should be the <strong style='color:#C9973A;'>Google Cloud service account JSON key</strong> — downloaded from Google Cloud Console → IAM → Service Accounts → Keys. It contains fields like <code style='color:#E5C068;background:rgba(201,151,58,0.08);padding:1px 6px;border-radius:4px;'>client_email</code> and <code style='color:#E5C068;background:rgba(201,151,58,0.08);padding:1px 6px;border-radius:4px;'>private_key</code>."),
    ("📊 What columns does the retention Excel sheet need?",
     "The master tracker should contain: <strong style='color:#C9973A;'>Adset Code, ThruPlay %, CTR, CPI, Spend</strong> and retention buckets (0–25%, 25–50%, 50–75%, 75–95%). Contact Mayank if you need the template."),
    ("📁 Where do I find my Google Drive Folder ID?",
     "Open the folder in Google Drive and look at the URL:<br><code style='display:block;margin-top:8px;padding:10px 14px;background:rgba(201,151,58,0.06);border-radius:8px;font-size:12px;color:#E5C068;'>drive.google.com/drive/folders/<strong style='color:#fff;'>YOUR_FOLDER_ID_HERE</strong></code><br>The bold part after <code style='color:#E5C068;background:rgba(201,151,58,0.08);padding:1px 6px;border-radius:4px;'>/folders/</code> is your Folder ID."),
    ("🤖 Which AI model should I pick?",
     "<ul style='margin:0;padding-left:0;list-style:none;'><li style='margin-bottom:6px;'><strong style='color:#C9973A;'>Gemini Flash</strong> — Free, fast, great for general narrative analysis.</li><li style='margin-bottom:6px;'><strong style='color:#A855F7;'>Groq Llama</strong> — Ultra-fast inference, great for bulk script comparisons.</li><li><strong style='color:#EDE9F8;'>Claude Haiku</strong> — Deepest insight for nuanced, emotional storytelling analysis (paid API key required).</li></ul>"),
    ("🔒 Is my data safe? Who can see my scripts?",
     "Your JSON key and scripts are processed <strong style='color:#C9973A;'>locally in your Streamlit session</strong> — nothing is stored on any external server. Scripts are only sent to the AI provider you choose (Gemini/Groq/Claude) for analysis, as per their API privacy policies."),
]

for q, a in faqs:
    with st.expander(q):
        st.markdown(f'<p style="font-size:14px;color:#EDE9F8;line-height:1.75;margin:0;">{a}</p>', unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<footer style="border-top:1px solid rgba(29,26,53,0.8);background:rgba(6,4,15,0.95);
               padding:36px 40px;text-align:center;">

  <!-- Film strip bottom decoration -->
  <div style="display:flex;justify-content:center;margin-bottom:20px;">
    <div class="film-strip">
      <div class="film-hole"></div><div class="film-hole"></div><div class="film-hole"></div>
      <div class="film-hole"></div><div class="film-hole"></div><div class="film-hole"></div>
    </div>
  </div>

  <div style="display:flex;align-items:center;justify-content:center;gap:8px;margin-bottom:12px;">
    <div style="display:flex;align-items:flex-end;gap:2px;height:18px;">
      <div class="wave-bar" style="height:5px;--dur:1.0s;"></div>
      <div class="wave-bar" style="height:13px;--dur:1.3s;--delay:0.12s;"></div>
      <div class="wave-bar" style="height:9px;--dur:1.1s;--delay:0.28s;"></div>
      <div class="wave-bar" style="height:17px;--dur:1.4s;--delay:0.08s;"></div>
      <div class="wave-bar" style="height:7px;--dur:0.9s;--delay:0.22s;"></div>
    </div>
    <span style="font-family:'Outfit',sans-serif;font-weight:600;font-size:14px;color:#EDE9F8;letter-spacing:0.05em;">StoryAnalyzer</span>
  </div>

  <div style="width:60px;height:1px;background:linear-gradient(90deg,transparent,#C9973A,transparent);margin:0 auto 16px;"></div>

  <div style="display:flex;align-items:center;justify-content:center;gap:10px;flex-wrap:wrap;">
    <span style="font-size:12px;color:rgba(90,84,120,0.7);">Designed &amp; Developed by</span>
    <a href="https://pocket-fm.slack.com/team/U08NHRDM9M2" target="_blank" rel="noopener"
       style="display:inline-flex;align-items:center;gap:6px;text-decoration:none;
              background:rgba(201,151,58,0.08);border:1px solid rgba(201,151,58,0.25);
              border-radius:100px;padding:5px 14px 5px 10px;
              transition:background 0.25s,box-shadow 0.25s;"
       onmouseover="this.style.background='rgba(201,151,58,0.15)';this.style.boxShadow='0 0 20px rgba(229,192,104,0.2)';"
       onmouseout="this.style.background='rgba(201,151,58,0.08)';this.style.boxShadow='none';">
      <svg width="13" height="13" viewBox="0 0 24 24" fill="#A855F7">
        <path d="M5.042 15.165a2.528 2.528 0 0 1-2.52 2.523A2.528 2.528 0 0 1 0 15.165a2.527 2.527 0 0 1 2.522-2.52h2.52v2.52zM6.313 15.165a2.527 2.527 0 0 1 2.521-2.52 2.527 2.527 0 0 1 2.521 2.52v6.313A2.528 2.528 0 0 1 8.834 24a2.528 2.528 0 0 1-2.521-2.522v-6.313zM8.834 5.042a2.528 2.528 0 0 1-2.521-2.52A2.528 2.528 0 0 1 8.834 0a2.528 2.528 0 0 1 2.521 2.522v2.52H8.834zM8.834 6.313a2.528 2.528 0 0 1 2.521 2.521 2.528 2.528 0 0 1-2.521 2.521H2.522A2.528 2.528 0 0 1 0 8.834a2.528 2.528 0 0 1 2.522-2.521h6.312zM18.956 8.834a2.528 2.528 0 0 1 2.522-2.521A2.528 2.528 0 0 1 24 8.834a2.528 2.528 0 0 1-2.522 2.521h-2.522V8.834zM17.688 8.834a2.528 2.528 0 0 1-2.523 2.521 2.527 2.527 0 0 1-2.52-2.521V2.522A2.527 2.527 0 0 1 15.165 0a2.528 2.528 0 0 1 2.523 2.522v6.312zM15.165 18.956a2.528 2.528 0 0 1 2.523 2.522A2.528 2.528 0 0 1 15.165 24a2.527 2.527 0 0 1-2.52-2.522v-2.522h2.52zM15.165 17.688a2.527 2.527 0 0 1-2.52-2.523 2.526 2.526 0 0 1 2.52-2.52h6.313A2.527 2.527 0 0 1 24 15.165a2.528 2.528 0 0 1-2.522 2.523h-6.313z"/>
      </svg>
      <span style="font-family:'Outfit',sans-serif;font-size:13px;font-weight:700;color:#E5C068;">Mayank Mandal</span>
    </a>
  </div>

  <p style="font-size:10px;color:rgba(90,84,120,0.4);margin:12px 0 0;">
    PocketFM Script Intelligence &bull; Open Source &bull; 2025
  </p>
</footer>
""", unsafe_allow_html=True)
