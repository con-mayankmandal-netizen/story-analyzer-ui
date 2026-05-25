import streamlit as st

st.set_page_config(page_title="StoryAnalyzer — PocketFM", page_icon="🎬",
                   layout="wide", initial_sidebar_state="collapsed")

st.markdown("""<style>
#MainMenu,header,footer,.stDeployButton{display:none!important;}
section[data-testid="stSidebar"]{display:none!important;}
.block-container{padding:0!important;max-width:100%!important;}
.stApp{background:#06040F!important;}
iframe{border:none!important;display:block!important;}
</style>""", unsafe_allow_html=True)

SLACK = "https://pocket-fm.slack.com/team/U08NHRDM9M2"
GH    = "https://github.com/con-mayankmandal-netizen/story-analyzer-ui"

# Build HTML as a regular string with __SLACK__ and __GH__ placeholders,
# then .replace() to avoid f-string curly brace escaping issues
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Story Analyzer — PocketFM Script Intelligence</title>

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@200;300;400;500;600;700;800;900&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet" />

  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['Outfit', 'sans-serif'],
            serif: ['DM Serif Display', 'serif'],
          },
          colors: {
            void: '#06040F',
            surface: '#0D0B1E',
            card: '#131026',
            border: '#1D1A35',
            gold: '#C9973A',
            'gold-light': '#E5C068',
            violet: '#7C3AED',
            'violet-light': '#A855F7',
            muted: '#5A5478',
            text: '#EDE9F8',
          },
          animation: {
            'wave': 'wavePulse 1.3s ease-in-out infinite',
            'marquee': 'marqueeScroll 28s linear infinite',
            'float': 'floatUp 6s ease-in-out infinite',
          }
        }
      }
    }
  </script>

  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Outfit', sans-serif;
      background: #06040F;
      color: #EDE9F8;
      overflow-x: hidden;
    }

    /* Subtle film-grain overlay */
    body::after {
      content: '';
      position: fixed;
      inset: 0;
      background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)' opacity='0.03'/%3E%3C/svg%3E");
      pointer-events: none;
      z-index: 9998;
      opacity: 0.35;
    }

    /* Scrollbar */
    ::-webkit-scrollbar { width: 3px; }
    ::-webkit-scrollbar-track { background: #06040F; }
    ::-webkit-scrollbar-thumb { background: #7C3AED; border-radius: 2px; }

    /* Glass morphism utility */
    .glass {
      background: rgba(13, 11, 30, 0.75);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border: 1px solid rgba(124, 58, 237, 0.12);
    }
    .glass-gold {
      background: rgba(13, 11, 30, 0.75);
      backdrop-filter: blur(24px);
      border: 1px solid rgba(201, 151, 58, 0.15);
    }

    /* Glows */
    .glow-violet { box-shadow: 0 0 80px rgba(124, 58, 237, 0.12), 0 0 160px rgba(124, 58, 237, 0.05); }
    .glow-gold   { box-shadow: 0 0 80px rgba(201, 151, 58, 0.10), 0 0 160px rgba(201, 151, 58, 0.04); }

    /* Gradient text */
    .gradient-text {
      background: linear-gradient(135deg, #E5C068 0%, #C9973A 30%, #A855F7 70%, #7C3AED 100%);
      -webkit-background-clip: text;
      background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    /* Animated waveform bars */
    @keyframes wavePulse {
      0%, 100% { transform: scaleY(0.25); opacity: 0.35; }
      50%       { transform: scaleY(1);    opacity: 1; }
    }
    .wave-bar { transform-origin: bottom; animation: wavePulse var(--dur, 1.2s) ease-in-out infinite; animation-delay: var(--delay, 0s); }

    /* Infinite marquee */
    @keyframes marqueeScroll {
      from { transform: translateX(0); }
      to   { transform: translateX(-50%); }
    }
    .marquee-track { display: flex; width: max-content; animation: marqueeScroll 30s linear infinite; }
    .marquee-track:hover { animation-play-state: paused; }

    /* Floating particles */
    @keyframes floatUp {
      0%, 100% { transform: translateY(0px)   scale(1);    opacity: 0.25; }
      40%       { transform: translateY(-28px) scale(1.15); opacity: 0.55; }
      70%       { transform: translateY(-14px) scale(0.9);  opacity: 0.2; }
    }
    .particle { position: absolute; border-radius: 50%; pointer-events: none; animation: floatUp var(--dur, 8s) ease-in-out infinite; animation-delay: var(--delay, 0s); }

    /* Film strip edge */
    .film-edge {
      background: repeating-linear-gradient(90deg, transparent 0px, transparent 14px, #14102A 14px, #14102A 18px);
    }

    /* Score ring */
    .score-ring {
      stroke-dasharray: 100.53;
      stroke-dashoffset: 100.53;
      transition: stroke-dashoffset 2s cubic-bezier(0.16, 1, 0.3, 1);
    }

    /* Card hover lift */
    .card-hover { transition: transform 0.55s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.55s ease; }
    .card-hover:hover { transform: translateY(-10px) scale(1.01); }

    /* Reveal base state */
    .reveal { opacity: 0; transform: translateY(44px); transition: opacity 0.9s ease, transform 0.9s ease; }
    .reveal.revealed { opacity: 1; transform: translateY(0); }

    /* Inline image inside heading */
    .heading-img {
      display: inline-block;
      width: 88px;
      height: 48px;
      border-radius: 100px;
      background-size: cover;
      background-position: center;
      vertical-align: middle;
      margin: 0 10px;
      filter: saturate(0.6) contrast(1.15) brightness(0.8);
      border: 1px solid rgba(255,255,255,0.08);
    }

    /* Scrub word — all visible since no GSAP scroll scrub */
    .scrub-word { opacity: 1; }

    /* Stagger entrance for step cards */
    .step-card { opacity: 0; transform: translateX(50px); transition: opacity 0.85s ease, transform 0.85s ease; }
    .step-card.revealed { opacity: 1; transform: translateX(0); }

    /* Radar polygon animation */
    @keyframes radarPulse {
      0%, 100% { opacity: 0.6; transform: scale(1); }
      50%       { opacity: 1;   transform: scale(1.02); }
    }
    .radar-poly { animation: radarPulse 3s ease-in-out infinite; transform-origin: center; }

    /* Number counter tabular */
    .counter { font-variant-numeric: tabular-nums; }

    /* Progress bar fill animation */
    .bar-fill { width: 0; transition: width 1.8s cubic-bezier(0.16, 1, 0.3, 1); }

    /* Horizontal accordion hover */
    .accordion-item { flex: 1; transition: flex 0.6s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.4s ease; overflow: hidden; cursor: pointer; }
    .accordion-item:hover { flex: 3; }
    .accordion-item .acc-content { opacity: 0; transition: opacity 0.4s ease 0.2s; white-space: nowrap; overflow: hidden; }
    .accordion-item:hover .acc-content { opacity: 1; }

    /* Spotlight cursor glow effect */
    .spotlight {
      position: fixed;
      width: 500px;
      height: 500px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(124,58,237,0.06) 0%, transparent 70%);
      pointer-events: none;
      z-index: 9997;
      transform: translate(-50%, -50%);
      transition: opacity 0.3s ease;
    }

    /* Hero entrance animations */
    @keyframes heroFade {
      from { opacity: 0; transform: translateY(30px); }
      to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes heroSlide {
      from { opacity: 0; transform: translateX(60px); }
      to   { opacity: 1; transform: translateX(0); }
    }

    #hero-eyebrow { animation: heroFade 0.8s ease 0.15s both; }
    #hero-h1      { animation: heroFade 1.0s ease 0.35s both; }
    #hero-sub     { animation: heroFade 0.8s ease 0.65s both; }
    #hero-ctas    { animation: heroFade 0.7s ease 0.85s both; }
    #hero-stats   { animation: heroFade 0.7s ease 1.0s both; }
    #hero-card    { animation: heroSlide 1.0s ease 0.55s both; }

    /* Bento card entrance */
    .card-hover { opacity: 0; transform: scale(0.96); transition: opacity 0.7s ease, transform 0.7s ease, box-shadow 0.55s ease; }
    .card-hover.revealed { opacity: 1; transform: scale(1); }
    .card-hover.revealed:hover { transform: scale(1.01) translateY(-10px); }
  </style>
</head>

<body class="bg-void text-text font-sans overflow-x-hidden">

  <!-- Cursor spotlight -->
  <div class="spotlight" id="spotlight"></div>

  <!-- ============================================================
       DEVELOPER CREDIT STRIP — fixed top, always visible
  ============================================================ -->
  <div class="fixed top-0 left-0 right-0 z-[60] flex items-center justify-center gap-2 py-1.5 px-6"
       style="background: linear-gradient(90deg, rgba(124,58,237,0.18) 0%, rgba(6,4,15,0.95) 50%, rgba(201,151,58,0.12) 100%); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); border-bottom: 1px solid rgba(229,192,104,0.12);">
    <!-- Left sparkle -->
    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" style="color:#A855F7; flex-shrink:0;">
      <path d="M12 2L14.09 8.26L21 9.27L16 14.14L17.18 21L12 17.77L6.82 21L8 14.14L3 9.27L9.91 8.26L12 2Z" fill="currentColor"/>
    </svg>
    <p style="font-size:11px; color: rgba(237,233,248,0.65); letter-spacing: 0.04em; font-family: 'Outfit', sans-serif;">
      Developed by
      <a href="__SLACK__" target="_blank" rel="noopener"
         style="color: #E5C068; font-weight: 600; text-decoration: none; letter-spacing: 0.02em; transition: all 0.2s;
                text-shadow: 0 0 14px rgba(229,192,104,0.5);"
         onmouseover="this.style.textShadow='0 0 22px rgba(229,192,104,0.9)'; this.style.color='#fff';"
         onmouseout="this.style.textShadow='0 0 14px rgba(229,192,104,0.5)'; this.style.color='#E5C068';">
        Mayank Mandal
      </a>
      &nbsp;&bull;&nbsp; PocketFM Script Intelligence
    </p>
    <!-- Right sparkle -->
    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" style="color:#C9973A; flex-shrink:0;">
      <path d="M12 2L14.09 8.26L21 9.27L16 14.14L17.18 21L12 17.77L6.82 21L8 14.14L3 9.27L9.91 8.26L12 2Z" fill="currentColor"/>
    </svg>
  </div>

  <!-- ============================================================
       NAV: Floating glass pill
  ============================================================ -->
  <nav id="navbar" class="fixed top-8 left-1/2 -translate-x-1/2 z-50 glass rounded-full px-6 py-3 flex items-center gap-8 transition-all duration-500 max-w-2xl w-[90vw]">
    <!-- Logo mark -->
    <div class="flex items-center gap-2 flex-shrink-0">
      <div class="flex items-end gap-px h-5">
        <div class="wave-bar w-1 bg-gold rounded-full" style="height:6px; --dur:1.0s; --delay:0s;"></div>
        <div class="wave-bar w-1 bg-gold rounded-full" style="height:14px;--dur:1.3s; --delay:0.12s;"></div>
        <div class="wave-bar w-1 bg-gold rounded-full" style="height:10px;--dur:1.1s; --delay:0.28s;"></div>
        <div class="wave-bar w-1 bg-gold rounded-full" style="height:18px;--dur:1.4s; --delay:0.08s;"></div>
        <div class="wave-bar w-1 bg-gold rounded-full" style="height:8px; --dur:0.9s; --delay:0.22s;"></div>
      </div>
      <span class="font-semibold text-sm tracking-wide">StoryAnalyzer</span>
    </div>

    <!-- Links -->
    <div class="hidden md:flex items-center gap-6 text-sm text-muted flex-1 justify-center">
      <a href="#features"     class="hover:text-text transition-colors duration-200">Features</a>
      <a href="#how-it-works" class="hover:text-text transition-colors duration-200">How It Works</a>
      <a href="#why"          class="hover:text-text transition-colors duration-200">Why It Matters</a>
    </div>

    <!-- CTA -->
    <div class="flex items-center gap-3 flex-shrink-0">
      <a href="/Help" target="_blank"
         class="text-xs text-muted hover:text-gold transition-colors duration-200 flex items-center gap-1.5">
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/>
        </svg>
        Help
      </a>
      <a href="/Tool" target="_blank"
         class="text-xs font-semibold bg-violet hover:bg-violet-light text-white px-5 py-2 rounded-full transition-all duration-300 hover:scale-105">
        Analyze
      </a>
    </div>
  </nav>


  <!-- ============================================================
       HERO: Artistic Asymmetry — text left, animated dashboard right
  ============================================================ -->
  <section class="relative min-h-screen flex items-center pt-28 pb-24 overflow-hidden">

    <!-- Ambient blobs -->
    <div class="absolute inset-0 pointer-events-none">
      <div class="absolute top-[-10%] left-[10%]  w-[700px] h-[700px] rounded-full bg-violet  opacity-[0.06] blur-[140px]"></div>
      <div class="absolute bottom-[5%]  right-[5%]  w-[500px] h-[500px] rounded-full bg-gold    opacity-[0.05] blur-[120px]"></div>
      <div class="absolute top-[40%]    left-[50%]  w-[300px] h-[300px] rounded-full bg-pink-500 opacity-[0.04] blur-[90px]"></div>
    </div>

    <!-- Film-strip top + bottom edges -->
    <div class="absolute top-0    left-0 right-0 h-7 film-edge opacity-20"></div>
    <div class="absolute bottom-0 left-0 right-0 h-7 film-edge opacity-20"></div>

    <!-- Floating particles -->
    <div class="particle w-2 h-2 bg-violet-light" style="top:22%;left:8%;  --dur:7s;  --delay:0s;"></div>
    <div class="particle w-1 h-1 bg-gold"         style="top:65%;left:82%; --dur:9s;  --delay:2.5s;"></div>
    <div class="particle w-3 h-3 bg-violet"        style="top:38%;left:55%; --dur:11s; --delay:1.2s; opacity:0.2;"></div>
    <div class="particle w-1 h-1 bg-gold-light"    style="top:80%;left:25%; --dur:8s;  --delay:3s;"></div>

    <div class="relative max-w-7xl mx-auto px-6 lg:px-12 w-full">
      <div class="grid lg:grid-cols-2 gap-20 items-center">

        <!-- LEFT: Copy -->
        <div class="space-y-8" id="hero-left">

          <!-- Eyebrow -->
          <div class="flex items-center gap-3" id="hero-eyebrow">
            <div class="flex items-end gap-px h-3">
              <div class="wave-bar w-px bg-gold rounded-full" style="height:4px; --dur:1.0s;"></div>
              <div class="wave-bar w-px bg-gold rounded-full" style="height:10px;--dur:1.3s; --delay:0.1s;"></div>
              <div class="wave-bar w-px bg-gold rounded-full" style="height:6px; --dur:1.0s; --delay:0.2s;"></div>
            </div>
            <span class="text-xs font-semibold tracking-[0.22em] text-gold uppercase">AI Script Intelligence — Built for PocketFM</span>
          </div>

          <!-- H1 -->
          <h1 class="font-serif leading-[1.04] max-w-2xl" id="hero-h1"
              style="font-size: clamp(3rem, 5vw, 5.5rem);">
            The science behind<br/>
            <span class="gradient-text">stories that sell</span>
          </h1>

          <p class="text-muted text-lg max-w-md leading-relaxed font-light" id="hero-sub">
            Upload PocketFM ad scripts, connect real campaign data, and let AI decode exactly why some audiobook stories convert — and others don't.
          </p>

          <!-- CTAs -->
          <div class="flex flex-wrap gap-4" id="hero-ctas">
            <a href="/Tool" target="_blank"
               class="inline-flex items-center gap-2 bg-gold hover:bg-gold-light text-void font-semibold px-8 py-3.5 rounded-full transition-all duration-300 hover:scale-105">
              Analyze a Script
              <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </a>
            <a href="#how-it-works"
               class="inline-flex items-center gap-2 glass text-text font-medium px-8 py-3.5 rounded-full transition-all duration-300 hover:border-violet/30">
              See How It Works
            </a>
          </div>

          <!-- Mini stats -->
          <div class="flex gap-10 pt-6 border-t border-border" id="hero-stats">
            <div>
              <div class="font-serif text-2xl text-gold-light counter" data-target="5">5</div>
              <div class="text-xs text-muted mt-1">Analysis Dimensions</div>
            </div>
            <div>
              <div class="font-serif text-2xl text-gold-light counter" data-target="3">3</div>
              <div class="text-xs text-muted mt-1">AI Providers</div>
            </div>
            <div>
              <div class="font-serif text-2xl text-violet-light counter" data-target="4">4</div>
              <div class="text-xs text-muted mt-1">Scripts at Once</div>
            </div>
          </div>
        </div>

        <!-- RIGHT: Animated analysis card -->
        <div class="relative" id="hero-card">

          <!-- Glow behind card -->
          <div class="absolute inset-0 bg-violet opacity-[0.08] blur-3xl rounded-3xl scale-110 pointer-events-none"></div>

          <!-- Main dashboard card -->
          <div class="relative glass rounded-2xl overflow-hidden glow-violet">

            <!-- Title bar -->
            <div class="bg-gradient-to-r from-surface to-card px-5 py-3.5 flex items-center justify-between border-b border-border">
              <div class="flex items-center gap-1.5">
                <div class="w-3 h-3 rounded-full bg-red-500/80"></div>
                <div class="w-3 h-3 rounded-full bg-gold/80"></div>
                <div class="w-3 h-3 rounded-full bg-green-500/80"></div>
              </div>
              <span class="text-[11px] text-muted font-mono">story_analyzer — analysis complete</span>
              <div class="w-1.5 h-1.5 rounded-full bg-green-400 animate-pulse"></div>
            </div>

            <div class="p-6 space-y-5">

              <!-- Script label -->
              <div>
                <div class="text-[10px] text-muted uppercase tracking-widest mb-1">Script</div>
                <div class="font-medium text-sm">"The Haunted Mansion — 30s Hook Cut"</div>
              </div>

              <!-- 5 score rings -->
              <div class="grid grid-cols-5 gap-2">
                <!-- Hook -->
                <div class="flex flex-col items-center gap-1.5">
                  <div class="relative w-12 h-12">
                    <svg viewBox="0 0 40 40" class="w-full h-full -rotate-90">
                      <circle cx="20" cy="20" r="16" fill="none" stroke="#1D1A35" stroke-width="3.5"/>
                      <circle class="score-ring" cx="20" cy="20" r="16" fill="none" stroke="#C9973A" stroke-width="3.5" stroke-linecap="round" data-score="82"/>
                    </svg>
                    <span class="absolute inset-0 flex items-center justify-center text-[9px] font-bold text-gold">82</span>
                  </div>
                  <span class="text-[9px] text-muted text-center">Hook</span>
                </div>
                <!-- Pacing -->
                <div class="flex flex-col items-center gap-1.5">
                  <div class="relative w-12 h-12">
                    <svg viewBox="0 0 40 40" class="w-full h-full -rotate-90">
                      <circle cx="20" cy="20" r="16" fill="none" stroke="#1D1A35" stroke-width="3.5"/>
                      <circle class="score-ring" cx="20" cy="20" r="16" fill="none" stroke="#7C3AED" stroke-width="3.5" stroke-linecap="round" data-score="74"/>
                    </svg>
                    <span class="absolute inset-0 flex items-center justify-center text-[9px] font-bold text-violet-light">74</span>
                  </div>
                  <span class="text-[9px] text-muted text-center">Pacing</span>
                </div>
                <!-- Emotion -->
                <div class="flex flex-col items-center gap-1.5">
                  <div class="relative w-12 h-12">
                    <svg viewBox="0 0 40 40" class="w-full h-full -rotate-90">
                      <circle cx="20" cy="20" r="16" fill="none" stroke="#1D1A35" stroke-width="3.5"/>
                      <circle class="score-ring" cx="20" cy="20" r="16" fill="none" stroke="#EC4899" stroke-width="3.5" stroke-linecap="round" data-score="91"/>
                    </svg>
                    <span class="absolute inset-0 flex items-center justify-center text-[9px] font-bold text-pink-400">91</span>
                  </div>
                  <span class="text-[9px] text-muted text-center">Emotion</span>
                </div>
                <!-- CTA -->
                <div class="flex flex-col items-center gap-1.5">
                  <div class="relative w-12 h-12">
                    <svg viewBox="0 0 40 40" class="w-full h-full -rotate-90">
                      <circle cx="20" cy="20" r="16" fill="none" stroke="#1D1A35" stroke-width="3.5"/>
                      <circle class="score-ring" cx="20" cy="20" r="16" fill="none" stroke="#10B981" stroke-width="3.5" stroke-linecap="round" data-score="68"/>
                    </svg>
                    <span class="absolute inset-0 flex items-center justify-center text-[9px] font-bold text-emerald-400">68</span>
                  </div>
                  <span class="text-[9px] text-muted text-center">CTA</span>
                </div>
                <!-- Story -->
                <div class="flex flex-col items-center gap-1.5">
                  <div class="relative w-12 h-12">
                    <svg viewBox="0 0 40 40" class="w-full h-full -rotate-90">
                      <circle cx="20" cy="20" r="16" fill="none" stroke="#1D1A35" stroke-width="3.5"/>
                      <circle class="score-ring" cx="20" cy="20" r="16" fill="none" stroke="#F59E0B" stroke-width="3.5" stroke-linecap="round" data-score="88"/>
                    </svg>
                    <span class="absolute inset-0 flex items-center justify-center text-[9px] font-bold text-amber-400">88</span>
                  </div>
                  <span class="text-[9px] text-muted text-center">Story</span>
                </div>
              </div>

              <!-- Campaign metrics -->
              <div class="bg-surface rounded-xl p-4 space-y-2.5">
                <div class="text-[10px] text-muted uppercase tracking-widest mb-3">Campaign Performance</div>
                <div class="flex justify-between items-center">
                  <span class="text-xs text-muted">ThruPlay %</span>
                  <div class="flex items-center gap-2.5">
                    <div class="w-24 bg-border rounded-full h-1 overflow-hidden">
                      <div class="bar-fill bg-gold h-1 rounded-full" data-width="67"></div>
                    </div>
                    <span class="text-xs text-gold font-semibold w-8 text-right">67%</span>
                  </div>
                </div>
                <div class="flex justify-between items-center">
                  <span class="text-xs text-muted">CTR</span>
                  <div class="flex items-center gap-2.5">
                    <div class="w-24 bg-border rounded-full h-1 overflow-hidden">
                      <div class="bar-fill bg-violet-light h-1 rounded-full" data-width="42"></div>
                    </div>
                    <span class="text-xs text-violet-light font-semibold w-8 text-right">3.2%</span>
                  </div>
                </div>
                <div class="flex justify-between items-center">
                  <span class="text-xs text-muted">CPI</span>
                  <div class="flex items-center gap-2.5">
                    <div class="w-24 bg-border rounded-full h-1 overflow-hidden">
                      <div class="bar-fill bg-emerald-400 h-1 rounded-full" data-width="75"></div>
                    </div>
                    <span class="text-xs text-emerald-400 font-semibold w-8 text-right">12.4</span>
                  </div>
                </div>
              </div>

              <!-- AI verdict -->
              <div class="flex items-start gap-3 bg-gradient-to-r from-violet/8 to-gold/5 rounded-xl p-3.5 border border-violet/15">
                <div class="w-8 h-8 rounded-full bg-violet/20 flex items-center justify-center flex-shrink-0 mt-0.5">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none">
                    <path d="M12 2l2.4 7.4H22l-6.2 4.5 2.4 7.4L12 17l-6.2 4.3 2.4-7.4L2 9.4h7.6L12 2z" fill="#A855F7"/>
                  </svg>
                </div>
                <div>
                  <div class="text-xs font-semibold text-violet-light">Strong Performer</div>
                  <div class="text-[10px] text-muted leading-relaxed mt-0.5">Emotional arc peaks at 0:18 — aligns with highest retention drop-off point in funnel data.</div>
                </div>
              </div>

            </div>
          </div>

          <!-- Floating retention funnel mini-card -->
          <div class="absolute -top-5 -right-5 glass-gold rounded-xl p-3.5 w-40 hidden lg:block shadow-2xl">
            <div class="text-[10px] text-muted mb-2.5">Retention Funnel</div>
            <div class="flex gap-1 items-end h-10">
              <div class="flex-1 bg-violet   rounded-sm" style="height:100%"></div>
              <div class="flex-1 bg-violet-light rounded-sm opacity-80" style="height:78%"></div>
              <div class="flex-1 bg-gold/70  rounded-sm" style="height:56%"></div>
              <div class="flex-1 bg-gold/40  rounded-sm" style="height:36%"></div>
            </div>
            <div class="flex justify-between text-[8px] text-muted mt-1.5">
              <span>0%</span><span>25%</span><span>50%</span><span>75%+</span>
            </div>
          </div>

          <!-- Floating writer feedback badge -->
          <div class="absolute -bottom-5 -left-5 glass rounded-xl p-3 w-44 hidden lg:block shadow-2xl">
            <div class="flex items-center gap-2 mb-2">
              <div class="w-6 h-6 rounded-full bg-gold/20 flex items-center justify-center text-[9px] font-bold text-gold">W</div>
              <span class="text-[10px] text-muted">Writer Feedback</span>
            </div>
            <div class="text-[10px] text-text leading-relaxed">Strengthen the mid-section tension drop at line 8.</div>
          </div>

        </div>
      </div>
    </div>
  </section>


  <!-- ============================================================
       MARQUEE: Scrolling metrics ticker
  ============================================================ -->
  <section class="relative border-y border-border py-4 overflow-hidden">
    <div class="absolute inset-y-0 left-0  w-32 bg-gradient-to-r from-void to-transparent z-10 pointer-events-none"></div>
    <div class="absolute inset-y-0 right-0 w-32 bg-gradient-to-l from-void to-transparent z-10 pointer-events-none"></div>

    <div class="marquee-track">
      <!-- First copy -->
      <div class="flex gap-10 items-center pr-10 select-none">
        <span class="text-sm font-medium text-muted whitespace-nowrap">Hook Effectiveness</span>
        <span class="w-1 h-1 rounded-full bg-gold flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Pacing &amp; Rhythm</span>
        <span class="w-1 h-1 rounded-full bg-violet flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Emotional Arc</span>
        <span class="w-1 h-1 rounded-full bg-gold flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">CTA Clarity</span>
        <span class="w-1 h-1 rounded-full bg-violet flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Narrative Quality</span>
        <span class="w-1 h-1 rounded-full bg-gold flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">ThruPlay Rate</span>
        <span class="w-1 h-1 rounded-full bg-violet flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Click-Through Rate</span>
        <span class="w-1 h-1 rounded-full bg-gold flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Cost Per Install</span>
        <span class="w-1 h-1 rounded-full bg-violet flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Retention Funnel</span>
        <span class="w-1 h-1 rounded-full bg-gold flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Google Gemini</span>
        <span class="w-1 h-1 rounded-full bg-violet flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Groq Llama</span>
        <span class="w-1 h-1 rounded-full bg-gold flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Claude Haiku</span>
        <span class="w-1 h-1 rounded-full bg-violet flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Radar Chart</span>
        <span class="w-1 h-1 rounded-full bg-gold flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Excel Export</span>
        <span class="w-1 h-1 rounded-full bg-violet flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Script Comparison</span>
        <span class="w-1 h-1 rounded-full bg-gold flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Meta Ads Data</span>
        <span class="w-1 h-1 rounded-full bg-violet flex-shrink-0"></span>
      </div>
      <!-- Duplicate for seamless loop -->
      <div class="flex gap-10 items-center pr-10 select-none">
        <span class="text-sm font-medium text-muted whitespace-nowrap">Hook Effectiveness</span>
        <span class="w-1 h-1 rounded-full bg-gold flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Pacing &amp; Rhythm</span>
        <span class="w-1 h-1 rounded-full bg-violet flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Emotional Arc</span>
        <span class="w-1 h-1 rounded-full bg-gold flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">CTA Clarity</span>
        <span class="w-1 h-1 rounded-full bg-violet flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Narrative Quality</span>
        <span class="w-1 h-1 rounded-full bg-gold flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">ThruPlay Rate</span>
        <span class="w-1 h-1 rounded-full bg-violet flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Click-Through Rate</span>
        <span class="w-1 h-1 rounded-full bg-gold flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Cost Per Install</span>
        <span class="w-1 h-1 rounded-full bg-violet flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Retention Funnel</span>
        <span class="w-1 h-1 rounded-full bg-gold flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Google Gemini</span>
        <span class="w-1 h-1 rounded-full bg-violet flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Groq Llama</span>
        <span class="w-1 h-1 rounded-full bg-gold flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Claude Haiku</span>
        <span class="w-1 h-1 rounded-full bg-violet flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Radar Chart</span>
        <span class="w-1 h-1 rounded-full bg-gold flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Excel Export</span>
        <span class="w-1 h-1 rounded-full bg-violet flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Script Comparison</span>
        <span class="w-1 h-1 rounded-full bg-gold flex-shrink-0"></span>
        <span class="text-sm font-medium text-muted whitespace-nowrap">Meta Ads Data</span>
        <span class="w-1 h-1 rounded-full bg-violet flex-shrink-0"></span>
      </div>
    </div>
  </section>


  <!-- ============================================================
       FEATURES: Gapless Bento Grid
  ============================================================ -->
  <section id="features" class="py-40 px-6 lg:px-12 max-w-7xl mx-auto">

    <!-- Section intro -->
    <div class="mb-20">
      <h2 class="font-serif leading-[1.08] max-w-3xl reveal"
          style="font-size: clamp(2.4rem, 4vw, 4.5rem);">
        Five lenses on every
        <span class="heading-img" style="background-image: url('https://picsum.photos/seed/theater/200/100');"></span>
        story
      </h2>
      <p class="text-muted mt-5 max-w-lg text-lg font-light reveal">
        Each dimension scored 0–100 with evidence pulled directly from your script and correlated against real Meta Ads campaign data.
      </p>
    </div>

    <!-- Bento grid: 3 columns, dense fill -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4" style="grid-auto-flow: dense;">

      <!-- Card 1: Hook Effectiveness — col-span-2, row-span-1 -->
      <div class="md:col-span-2 glass rounded-2xl p-8 card-hover glow-gold relative overflow-hidden group">
        <div class="absolute top-0 right-0 w-48 h-48 bg-gold opacity-[0.06] rounded-full blur-3xl group-hover:opacity-[0.1] transition-opacity pointer-events-none"></div>
        <div class="relative">
          <div class="flex items-start justify-between mb-6">
            <div class="w-11 h-11 rounded-xl bg-gold/10 flex items-center justify-center">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#C9973A" stroke-width="2">
                <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>
              </svg>
            </div>
            <span class="font-serif text-4xl font-bold text-gold">82</span>
          </div>
          <h3 class="text-xl font-semibold mb-2">Hook Effectiveness</h3>
          <p class="text-muted text-sm leading-relaxed max-w-sm">
            The critical first 3 seconds. AI evaluates your opening for pattern interrupts, curiosity gaps, and genre-specific emotional triggers that keep listeners from skipping.
          </p>
          <!-- Animated waveform bar chart -->
          <div class="flex items-end gap-1 mt-6 h-14 opacity-70">
            <div class="flex-1 bg-gold/25 rounded-t-sm" style="height:38%"></div>
            <div class="flex-1 bg-gold/40 rounded-t-sm" style="height:62%"></div>
            <div class="flex-1 bg-gold/35 rounded-t-sm" style="height:50%"></div>
            <div class="flex-1 bg-gold    rounded-t-sm" style="height:100%"></div>
            <div class="flex-1 bg-gold/75 rounded-t-sm" style="height:82%"></div>
            <div class="flex-1 bg-gold/55 rounded-t-sm" style="height:65%"></div>
            <div class="flex-1 bg-gold/40 rounded-t-sm" style="height:48%"></div>
            <div class="flex-1 bg-gold/25 rounded-t-sm" style="height:33%"></div>
            <div class="flex-1 bg-gold/15 rounded-t-sm" style="height:22%"></div>
          </div>
          <div class="text-[10px] text-muted mt-1.5">Audio intensity timeline — peaks at hook moment</div>
        </div>
      </div>

      <!-- Card 2: Emotional Arc — col-span-1, row-span-2 -->
      <div class="md:row-span-2 glass rounded-2xl overflow-hidden card-hover relative group flex flex-col">
        <!-- Background image layer -->
        <div class="absolute inset-0 opacity-[0.07] group-hover:opacity-[0.12] transition-opacity pointer-events-none">
          <img src="https://picsum.photos/seed/storytelling/400/700" class="w-full h-full object-cover" style="filter: grayscale(1) contrast(1.2) brightness(0.7);" alt="" />
        </div>
        <div class="relative flex flex-col h-full p-8">
          <div class="w-11 h-11 rounded-xl bg-pink-500/10 flex items-center justify-center mb-5">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#EC4899" stroke-width="2">
              <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/>
            </svg>
          </div>
          <h3 class="text-xl font-semibold mb-3">Emotional Arc</h3>
          <p class="text-muted text-sm leading-relaxed flex-1">
            Maps the listener's full emotional journey. Identifies tension peaks, release moments, and deep-connection triggers that drive long-term retention in audiobook funnels.
          </p>

          <!-- SVG arc visualization -->
          <div class="mt-6">
            <svg viewBox="0 0 200 90" class="w-full" preserveAspectRatio="none">
              <defs>
                <linearGradient id="arcGrad" x1="0%" y1="0%" x2="100%" y2="0%">
                  <stop offset="0%"   stop-color="#EC4899" stop-opacity="0.2"/>
                  <stop offset="50%"  stop-color="#EC4899" stop-opacity="0.9"/>
                  <stop offset="100%" stop-color="#7C3AED" stop-opacity="0.4"/>
                </linearGradient>
                <linearGradient id="arcFill" x1="0%" y1="0%" x2="0%" y2="100%">
                  <stop offset="0%"   stop-color="#EC4899" stop-opacity="0.15"/>
                  <stop offset="100%" stop-color="#EC4899" stop-opacity="0"/>
                </linearGradient>
              </defs>
              <!-- Fill area -->
              <path d="M 0 80 Q 40 65 60 35 Q 80 12 100 22 Q 120 32 140 16 Q 162 4 185 28 L 200 45 L 200 90 L 0 90 Z"
                    fill="url(#arcFill)"/>
              <!-- Arc line -->
              <path d="M 0 80 Q 40 65 60 35 Q 80 12 100 22 Q 120 32 140 16 Q 162 4 185 28 L 200 45"
                    fill="none" stroke="url(#arcGrad)" stroke-width="2.5" stroke-linecap="round"/>
              <!-- Peak dots -->
              <circle cx="100" cy="22" r="3.5" fill="#EC4899"/>
              <circle cx="140" cy="16" r="4.5" fill="#EC4899" opacity="0.85"/>
              <!-- Annotation -->
              <line x1="140" y1="16" x2="140" y2="5" stroke="#EC4899" stroke-width="1" stroke-dasharray="2,2" opacity="0.5"/>
              <text x="145" y="9" font-size="6" fill="#EC4899" opacity="0.8" font-family="Outfit">peak</text>
            </svg>
            <div class="flex justify-between text-[9px] text-muted mt-1">
              <span>Open</span><span>Mid</span><span>Close</span>
            </div>
          </div>

          <div class="mt-5 font-serif text-5xl font-bold text-pink-400">91</div>
        </div>
      </div>

      <!-- Card 3: Pacing — col-span-1 -->
      <div class="glass rounded-2xl p-7 card-hover relative overflow-hidden group">
        <div class="absolute bottom-0 right-0 w-32 h-32 bg-violet opacity-[0.06] rounded-full blur-2xl pointer-events-none"></div>
        <div class="relative">
          <div class="w-11 h-11 rounded-xl bg-violet/10 flex items-center justify-center mb-4">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#7C3AED" stroke-width="2">
              <circle cx="12" cy="12" r="10"/>
              <polyline points="12 6 12 12 16 14"/>
            </svg>
          </div>
          <h3 class="text-lg font-semibold mb-2">Pacing</h3>
          <p class="text-muted text-xs leading-relaxed">Story rhythm and beat timing — where the narrative breathes and where it rushes past the listener.</p>
          <!-- Speed meter visual -->
          <div class="mt-4 flex gap-1 items-end h-8">
            <div class="flex-1 bg-violet/20 rounded-sm" style="height:30%"></div>
            <div class="flex-1 bg-violet/35 rounded-sm" style="height:55%"></div>
            <div class="flex-1 bg-violet/55 rounded-sm" style="height:75%"></div>
            <div class="flex-1 bg-violet    rounded-sm" style="height:100%"></div>
            <div class="flex-1 bg-violet/70 rounded-sm" style="height:85%"></div>
            <div class="flex-1 bg-violet/45 rounded-sm" style="height:60%"></div>
          </div>
          <div class="font-serif text-4xl font-bold text-violet-light mt-4">74</div>
        </div>
      </div>

      <!-- Card 4: CTA Clarity — col-span-1 -->
      <div class="glass rounded-2xl p-7 card-hover relative overflow-hidden group">
        <div class="absolute bottom-0 left-0 w-32 h-32 bg-emerald-500 opacity-[0.05] rounded-full blur-2xl pointer-events-none"></div>
        <div class="relative">
          <div class="w-11 h-11 rounded-xl bg-emerald-500/10 flex items-center justify-center mb-4">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2">
              <path d="M5 12h14M12 5l7 7-7 7"/>
            </svg>
          </div>
          <h3 class="text-lg font-semibold mb-2">CTA Clarity</h3>
          <p class="text-muted text-xs leading-relaxed">How compellingly the script converts listener intent into action — measured against install and click-through rates.</p>
          <!-- Clarity gauge -->
          <div class="mt-4 relative h-2 bg-border rounded-full overflow-hidden">
            <div class="absolute inset-y-0 left-0 rounded-full bg-gradient-to-r from-emerald-500/50 to-emerald-400" style="width:68%"></div>
          </div>
          <div class="flex justify-between text-[9px] text-muted mt-1">
            <span>0</span><span>50</span><span>100</span>
          </div>
          <div class="font-serif text-4xl font-bold text-emerald-400 mt-3">68</div>
        </div>
      </div>

      <!-- Card 5: Narrative Quality — col-span-3, full-width -->
      <div class="md:col-span-3 glass rounded-2xl p-8 card-hover relative overflow-hidden group">
        <!-- Cinematic BG -->
        <div class="absolute inset-0 opacity-[0.06] pointer-events-none">
          <img src="https://picsum.photos/seed/cinema/1400/250" class="w-full h-full object-cover"
               style="filter: grayscale(1) contrast(1.1); mix-blend-mode: luminosity;" alt="" />
        </div>
        <div class="relative flex flex-col md:flex-row items-start md:items-center gap-8">
          <div class="flex-1">
            <div class="flex items-center gap-3 mb-4">
              <div class="w-11 h-11 rounded-xl bg-amber-500/10 flex items-center justify-center">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#F59E0B" stroke-width="2">
                  <path d="M12 2l2.4 7.4H22l-6.2 4.5 2.4 7.4L12 17l-6.2 4.3 2.4-7.4L2 9.4h7.6L12 2z"/>
                </svg>
              </div>
              <h3 class="text-xl font-semibold">Overall Narrative Quality</h3>
            </div>
            <p class="text-muted text-sm leading-relaxed max-w-2xl">
              A holistic score considering story structure, genre conventions, character depth, and how well the ad narrative mirrors the in-app audiobook experience. The most comprehensive predictor of long-term listener retention and install quality.
            </p>
            <!-- Tag pills -->
            <div class="flex flex-wrap gap-2 mt-5">
              <span class="text-[11px] bg-amber-500/8  border border-amber-500/15 rounded-full px-3 py-1 text-amber-400/80">Story Structure</span>
              <span class="text-[11px] bg-amber-500/8  border border-amber-500/15 rounded-full px-3 py-1 text-amber-400/80">Genre Conventions</span>
              <span class="text-[11px] bg-violet/8     border border-violet/15     rounded-full px-3 py-1 text-violet-light/80">Character Depth</span>
              <span class="text-[11px] bg-violet/8     border border-violet/15     rounded-full px-3 py-1 text-violet-light/80">Listener Retention</span>
            </div>
          </div>
          <div class="flex-shrink-0 flex items-center gap-8">
            <div class="text-right">
              <div class="font-serif text-7xl font-bold text-amber-400">88</div>
              <div class="text-xs text-muted mt-1">Overall Score</div>
            </div>
            <div class="w-px h-20 bg-border hidden md:block"></div>
            <div class="space-y-1.5 text-right hidden md:block">
              <div class="text-[10px] text-muted uppercase tracking-widest">Verdict</div>
              <div class="text-sm font-semibold text-emerald-400">Top Performer</div>
              <div class="text-xs text-muted">Top 15% of scripts</div>
              <div class="text-[10px] text-gold mt-2">Recommended for scale</div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </section>


  <!-- ============================================================
       HOW IT WORKS: Sticky left + scrolling right steps
  ============================================================ -->
  <section id="how-it-works" class="py-40 bg-surface relative overflow-hidden">
    <div class="absolute inset-0 pointer-events-none">
      <div class="absolute top-1/2 left-1/4 w-96 h-96 bg-violet opacity-[0.05] rounded-full blur-[100px]"></div>
    </div>

    <div class="max-w-7xl mx-auto px-6 lg:px-12">
      <div class="flex flex-col lg:flex-row gap-16">

        <!-- Sticky left -->
        <div class="lg:w-1/3 lg:sticky lg:top-28 lg:self-start">
          <h2 class="font-serif leading-tight reveal"
              style="font-size: clamp(2.4rem, 4vw, 4.5rem);">
            How it<br/><span class="gradient-text">works</span>
          </h2>
          <p class="text-muted mt-4 text-base leading-relaxed reveal">
            Three steps from raw script to actionable creative insight. No complex setup required beyond your performance data.
          </p>

          <!-- Step progress dots -->
          <div class="flex gap-2 mt-8 reveal" id="step-dots">
            <div class="w-6 h-2 rounded-full bg-gold transition-all duration-300"  data-step="0"></div>
            <div class="w-2 h-2 rounded-full bg-border transition-all duration-300" data-step="1"></div>
            <div class="w-2 h-2 rounded-full bg-border transition-all duration-300" data-step="2"></div>
          </div>

          <!-- Radar chart radar preview -->
          <div class="mt-10 glass rounded-xl p-5 reveal">
            <div class="text-xs text-muted mb-3">Script Comparison Radar</div>
            <svg viewBox="0 0 160 140" class="w-full max-w-[200px] mx-auto">
              <!-- Concentric pentagons -->
              <polygon points="80,10 148,55 122,120 38,120 12,55" fill="none" stroke="#1D1A35" stroke-width="1"/>
              <polygon points="80,28 128,63 108,108 52,108 32,63" fill="none" stroke="#1D1A35" stroke-width="1"/>
              <polygon points="80,46 108,71 94,96 66,96 52,71" fill="none" stroke="#1D1A35" stroke-width="1"/>
              <!-- Axis lines -->
              <line x1="80" y1="10"  x2="80"  y2="120" stroke="#1D1A35" stroke-width="0.5"/>
              <line x1="80" y1="65"  x2="148" y2="55"  stroke="#1D1A35" stroke-width="0.5"/>
              <line x1="80" y1="65"  x2="122" y2="120" stroke="#1D1A35" stroke-width="0.5"/>
              <line x1="80" y1="65"  x2="38"  y2="120" stroke="#1D1A35" stroke-width="0.5"/>
              <line x1="80" y1="65"  x2="12"  y2="55"  stroke="#1D1A35" stroke-width="0.5"/>
              <!-- Data polygon 1 (gold) -->
              <polygon
                points="80,18 138,59 110,112 50,112 20,59"
                fill="rgba(201,151,58,0.12)" stroke="#C9973A" stroke-width="1.5"
                class="radar-poly"/>
              <!-- Data polygon 2 (violet) -->
              <polygon
                points="80,30 120,64 100,100 60,100 38,64"
                fill="rgba(124,58,237,0.10)" stroke="#7C3AED" stroke-width="1.5"
                class="radar-poly" style="animation-delay:1.5s"/>
              <!-- Axis labels -->
              <text x="76" y="8"   font-size="7" fill="#5A5478" font-family="Outfit" text-anchor="middle">Hook</text>
              <text x="152" y="55" font-size="7" fill="#5A5478" font-family="Outfit" text-anchor="start">Pacing</text>
              <text x="124" y="126" font-size="7" fill="#5A5478" font-family="Outfit" text-anchor="middle">CTA</text>
              <text x="36"  y="126" font-size="7" fill="#5A5478" font-family="Outfit" text-anchor="middle">Story</text>
              <text x="4"   y="55"  font-size="7" fill="#5A5478" font-family="Outfit" text-anchor="start">Emot.</text>
            </svg>
            <div class="flex gap-3 justify-center mt-3">
              <div class="flex items-center gap-1.5"><div class="w-3 h-0.5 bg-gold rounded"></div><span class="text-[10px] text-muted">Script A</span></div>
              <div class="flex items-center gap-1.5"><div class="w-3 h-0.5 bg-violet rounded"></div><span class="text-[10px] text-muted">Script B</span></div>
            </div>
          </div>
        </div>

        <!-- Scrolling steps -->
        <div class="lg:w-2/3 space-y-6">

          <!-- Step 01 -->
          <div class="step-card glass rounded-2xl p-8">
            <div class="flex items-start gap-6">
              <div class="w-12 h-12 rounded-xl bg-gold/10 border border-gold/20 flex items-center justify-center flex-shrink-0">
                <span class="font-serif font-bold text-gold text-lg">01</span>
              </div>
              <div class="flex-1">
                <h3 class="text-xl font-semibold mb-3">Upload Your Performance Data</h3>
                <p class="text-muted text-sm leading-relaxed mb-5">
                  Drop your Meta Ads Excel file. The tool reads ThruPlay %, CTR, CPI, and spend data automatically per ad set. Then connect Google Drive to fetch scripts — or paste them manually as a fallback.
                </p>
                <!-- File mockup -->
                <div class="bg-surface rounded-xl border border-border border-dashed p-4 flex items-center gap-3">
                  <div class="w-9 h-9 rounded-lg bg-gold/10 flex items-center justify-center">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#C9973A" stroke-width="2">
                      <path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M17 8l-5-5-5 5M12 3v12"/>
                    </svg>
                  </div>
                  <div class="flex-1">
                    <div class="text-xs font-medium">master_data.xlsx</div>
                    <div class="text-[10px] text-muted">12 ad sets &bull; 47 scripts &bull; 3.2 MB</div>
                  </div>
                  <div class="flex items-center gap-1.5">
                    <div class="w-1.5 h-1.5 rounded-full bg-emerald-400"></div>
                    <span class="text-[10px] text-emerald-400">Loaded</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Step 02 -->
          <div class="step-card glass rounded-2xl p-8">
            <div class="flex items-start gap-6">
              <div class="w-12 h-12 rounded-xl bg-violet/10 border border-violet/20 flex items-center justify-center flex-shrink-0">
                <span class="font-serif font-bold text-violet-light text-lg">02</span>
              </div>
              <div class="flex-1">
                <h3 class="text-xl font-semibold mb-3">Choose AI Provider &amp; Analyze</h3>
                <p class="text-muted text-sm leading-relaxed mb-5">
                  Select 1–4 scripts and pick your AI provider. The system reads each script alongside its campaign data and evaluates it across all five narrative dimensions simultaneously.
                </p>
                <!-- AI provider pills -->
                <div class="flex flex-wrap gap-2">
                  <div class="flex items-center gap-2 bg-blue-500/8 border border-blue-500/15 rounded-full px-3.5 py-1.5">
                    <div class="w-4 h-4 rounded-full bg-gradient-to-br from-blue-400 to-blue-600 flex items-center justify-center text-[8px] font-bold text-white">G</div>
                    <span class="text-xs text-blue-300 font-medium">Google Gemini</span>
                    <span class="text-[10px] text-muted bg-emerald-500/10 text-emerald-400 px-1.5 py-0.5 rounded-full">Free</span>
                  </div>
                  <div class="flex items-center gap-2 bg-orange-500/8 border border-orange-500/15 rounded-full px-3.5 py-1.5">
                    <div class="w-4 h-4 rounded-full bg-gradient-to-br from-orange-400 to-red-500 flex items-center justify-center text-[8px] font-bold text-white">L</div>
                    <span class="text-xs text-orange-300 font-medium">Groq Llama</span>
                    <span class="text-[10px] text-muted bg-emerald-500/10 text-emerald-400 px-1.5 py-0.5 rounded-full">Free</span>
                  </div>
                  <div class="flex items-center gap-2 bg-violet/8 border border-violet/15 rounded-full px-3.5 py-1.5">
                    <div class="w-4 h-4 rounded-full bg-gradient-to-br from-violet to-violet-light flex items-center justify-center text-[8px] font-bold text-white">C</div>
                    <span class="text-xs text-violet-light font-medium">Claude Haiku</span>
                    <span class="text-[10px] text-muted bg-amber-500/10 text-amber-400 px-1.5 py-0.5 rounded-full">Paid</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Step 03 -->
          <div class="step-card glass rounded-2xl p-8">
            <div class="flex items-start gap-6">
              <div class="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center flex-shrink-0">
                <span class="font-serif font-bold text-emerald-400 text-lg">03</span>
              </div>
              <div class="flex-1">
                <h3 class="text-xl font-semibold mb-3">Receive Deep Creative Insight</h3>
                <p class="text-muted text-sm leading-relaxed mb-5">
                  Get scored analysis across all 5 dimensions, a full "Why It Performed" narrative, retention funnel correlations, radar chart comparisons across scripts, writer-specific feedback, and a downloadable Excel report for your team.
                </p>
                <div class="grid grid-cols-2 gap-3">
                  <div class="flex items-center gap-2.5 bg-emerald-500/8 border border-emerald-500/12 rounded-xl px-4 py-2.5">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="2">
                      <path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M7 10l5 5 5-5M12 15V3"/>
                    </svg>
                    <span class="text-xs text-emerald-400 font-medium">Excel Export</span>
                  </div>
                  <div class="flex items-center gap-2.5 bg-violet/8 border border-violet/12 rounded-xl px-4 py-2.5">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#A855F7" stroke-width="2">
                      <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/>
                    </svg>
                    <span class="text-xs text-violet-light font-medium">Open Source</span>
                  </div>
                  <div class="flex items-center gap-2.5 bg-gold/8 border border-gold/12 rounded-xl px-4 py-2.5">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#C9973A" stroke-width="2">
                      <path d="M18 20V10M12 20V4M6 20v-6"/>
                    </svg>
                    <span class="text-xs text-gold font-medium">Radar Chart</span>
                  </div>
                  <div class="flex items-center gap-2.5 bg-pink-500/8 border border-pink-500/12 rounded-xl px-4 py-2.5">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#EC4899" stroke-width="2">
                      <path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2M9 11a4 4 0 100-8 4 4 0 000 8zM23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/>
                    </svg>
                    <span class="text-xs text-pink-300 font-medium">Writer Feedback</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  </section>


  <!-- ============================================================
       HORIZONTAL ACCORDION: Audiobook genres / use cases
  ============================================================ -->
  <section class="py-40 px-6 lg:px-12 max-w-7xl mx-auto">
    <div class="mb-16">
      <h2 class="font-serif leading-tight max-w-2xl reveal"
          style="font-size: clamp(2.2rem, 3.5vw, 4rem);">
        Built for every<br/>PocketFM genre
      </h2>
      <p class="text-muted mt-4 max-w-md text-base font-light reveal">
        Whether it's horror, romance, thriller, or drama — the same five-lens analysis adapts to genre-specific narrative conventions.
      </p>
    </div>

    <div class="flex gap-2 h-80 reveal" id="accordion">
      <!-- Horror -->
      <div class="accordion-item glass rounded-2xl relative overflow-hidden group" style="min-width:60px;">
        <div class="absolute inset-0 opacity-20 group-hover:opacity-35 transition-opacity">
          <img src="https://picsum.photos/seed/horror/400/600" class="w-full h-full object-cover"
               style="filter: grayscale(0.6) contrast(1.3) brightness(0.5);" alt="" />
        </div>
        <div class="absolute inset-0 bg-gradient-to-t from-void via-transparent to-transparent opacity-70"></div>
        <div class="relative h-full flex flex-col justify-end p-5">
          <!-- Rotated label (always visible) -->
          <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 group-hover:opacity-0 transition-opacity">
            <span class="text-xs font-semibold text-text/60 tracking-widest" style="writing-mode:vertical-rl; text-orientation:mixed; transform:rotate(180deg)">Horror</span>
          </div>
          <!-- Expanded content -->
          <div class="acc-content">
            <h4 class="text-base font-semibold text-text mb-1 whitespace-nowrap">Horror &amp; Thriller</h4>
            <p class="text-xs text-muted whitespace-nowrap">Tension pacing, dread buildup, jump-cut timing analysis</p>
          </div>
        </div>
      </div>

      <!-- Romance -->
      <div class="accordion-item glass rounded-2xl relative overflow-hidden group" style="min-width:60px;">
        <div class="absolute inset-0 opacity-20 group-hover:opacity-35 transition-opacity">
          <img src="https://picsum.photos/seed/romance/400/600" class="w-full h-full object-cover"
               style="filter: saturate(0.5) contrast(1.1) brightness(0.5);" alt="" />
        </div>
        <div class="absolute inset-0 bg-gradient-to-t from-void via-transparent to-transparent opacity-70"></div>
        <div class="relative h-full flex flex-col justify-end p-5">
          <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 group-hover:opacity-0 transition-opacity">
            <span class="text-xs font-semibold text-text/60 tracking-widest" style="writing-mode:vertical-rl; text-orientation:mixed; transform:rotate(180deg)">Romance</span>
          </div>
          <div class="acc-content">
            <h4 class="text-base font-semibold text-text mb-1 whitespace-nowrap">Romance &amp; Drama</h4>
            <p class="text-xs text-muted whitespace-nowrap">Emotional resonance, intimacy arc, vulnerability scoring</p>
          </div>
        </div>
      </div>

      <!-- Crime -->
      <div class="accordion-item glass rounded-2xl relative overflow-hidden group" style="min-width:60px;">
        <div class="absolute inset-0 opacity-20 group-hover:opacity-35 transition-opacity">
          <img src="https://picsum.photos/seed/crime/400/600" class="w-full h-full object-cover"
               style="filter: grayscale(0.7) contrast(1.2) brightness(0.45);" alt="" />
        </div>
        <div class="absolute inset-0 bg-gradient-to-t from-void via-transparent to-transparent opacity-70"></div>
        <div class="relative h-full flex flex-col justify-end p-5">
          <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 group-hover:opacity-0 transition-opacity">
            <span class="text-xs font-semibold text-text/60 tracking-widest" style="writing-mode:vertical-rl; text-orientation:mixed; transform:rotate(180deg)">Crime</span>
          </div>
          <div class="acc-content">
            <h4 class="text-base font-semibold text-text mb-1 whitespace-nowrap">Crime &amp; Mystery</h4>
            <p class="text-xs text-muted whitespace-nowrap">Hook density, clue-reveal pacing, suspense sustain</p>
          </div>
        </div>
      </div>

      <!-- Fantasy -->
      <div class="accordion-item glass rounded-2xl relative overflow-hidden group" style="min-width:60px;">
        <div class="absolute inset-0 opacity-20 group-hover:opacity-35 transition-opacity">
          <img src="https://picsum.photos/seed/fantasy/400/600" class="w-full h-full object-cover"
               style="filter: saturate(0.4) contrast(1.15) brightness(0.4);" alt="" />
        </div>
        <div class="absolute inset-0 bg-gradient-to-t from-void via-transparent to-transparent opacity-70"></div>
        <div class="relative h-full flex flex-col justify-end p-5">
          <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 group-hover:opacity-0 transition-opacity">
            <span class="text-xs font-semibold text-text/60 tracking-widest" style="writing-mode:vertical-rl; text-orientation:mixed; transform:rotate(180deg)">Fantasy</span>
          </div>
          <div class="acc-content">
            <h4 class="text-base font-semibold text-text mb-1 whitespace-nowrap">Fantasy &amp; Sci-Fi</h4>
            <p class="text-xs text-muted whitespace-nowrap">World-building immersion speed, wonder triggers, lore hooks</p>
          </div>
        </div>
      </div>

      <!-- Comedy -->
      <div class="accordion-item glass rounded-2xl relative overflow-hidden group" style="min-width:60px;">
        <div class="absolute inset-0 opacity-20 group-hover:opacity-35 transition-opacity">
          <img src="https://picsum.photos/seed/comedy/400/600" class="w-full h-full object-cover"
               style="filter: saturate(0.3) contrast(1.1) brightness(0.45);" alt="" />
        </div>
        <div class="absolute inset-0 bg-gradient-to-t from-void via-transparent to-transparent opacity-70"></div>
        <div class="relative h-full flex flex-col justify-end p-5">
          <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 group-hover:opacity-0 transition-opacity">
            <span class="text-xs font-semibold text-text/60 tracking-widest" style="writing-mode:vertical-rl; text-orientation:mixed; transform:rotate(180deg)">Comedy</span>
          </div>
          <div class="acc-content">
            <h4 class="text-base font-semibold text-text mb-1 whitespace-nowrap">Comedy &amp; Slice-of-Life</h4>
            <p class="text-xs text-muted whitespace-nowrap">Rhythm breaks, relatable beat timing, warmth quotient</p>
          </div>
        </div>
      </div>
    </div>
  </section>


  <!-- ============================================================
       SCRUBBING TEXT REVEAL: "Why This Matters"
  ============================================================ -->
  <section id="why" class="py-48 px-6 max-w-5xl mx-auto">
    <p id="scrub-text" class="font-serif text-center leading-[1.35]"
       style="font-size: clamp(1.8rem, 3.5vw, 4rem);">
      <span class="scrub-word">Every</span>
      <span class="scrub-word"> second</span>
      <span class="scrub-word"> of</span>
      <span class="scrub-word"> your</span>
      <span class="scrub-word"> audio</span>
      <span class="scrub-word"> ad</span>
      <span class="scrub-word"> is</span>
      <span class="scrub-word"> a</span>
      <span class="scrub-word text-gold"> creative</span>
      <span class="scrub-word text-gold"> decision.</span>
      <span class="scrub-word"> Stop</span>
      <span class="scrub-word"> shipping</span>
      <span class="scrub-word"> on</span>
      <span class="scrub-word"> instinct.</span>
      <span class="scrub-word"> Start</span>
      <span class="scrub-word text-violet-light"> knowing</span>
      <span class="scrub-word text-violet-light"> why</span>
      <span class="scrub-word text-violet-light"> stories</span>
      <span class="scrub-word text-violet-light"> work.</span>
    </p>
  </section>


  <!-- ============================================================
       CTA SECTION
  ============================================================ -->
  <section id="cta" class="py-40 px-6 relative overflow-hidden">
    <div class="absolute inset-0 bg-gradient-to-b from-void via-surface/80 to-void pointer-events-none"></div>
    <div class="absolute inset-0 pointer-events-none">
      <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[700px] h-[700px] rounded-full bg-violet opacity-[0.08] blur-[130px]"></div>
      <div class="absolute top-1/3 right-1/4 w-[300px] h-[300px] rounded-full bg-gold opacity-[0.05] blur-[80px]"></div>
    </div>

    <div class="relative max-w-4xl mx-auto text-center">
      <!-- Film-reel icon -->
      <div class="flex justify-center mb-8 reveal">
        <div class="w-16 h-16 glass rounded-2xl flex items-center justify-center glow-violet">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#A855F7" stroke-width="1.5">
            <circle cx="12" cy="12" r="10"/>
            <circle cx="12" cy="12" r="3"/>
            <circle cx="12" cy="5"  r="1.5" fill="#A855F7" stroke="none"/>
            <circle cx="12" cy="19" r="1.5" fill="#A855F7" stroke="none"/>
            <circle cx="5"  cy="12" r="1.5" fill="#A855F7" stroke="none"/>
            <circle cx="19" cy="12" r="1.5" fill="#A855F7" stroke="none"/>
          </svg>
        </div>
      </div>

      <h2 class="font-serif leading-tight mb-6 reveal"
          style="font-size: clamp(2.5rem, 5vw, 5.5rem);">
        Ready to decode your<br/>
        <span class="gradient-text">best stories?</span>
      </h2>

      <p class="text-muted text-lg max-w-xl mx-auto mb-10 font-light reveal">
        Open source, AI-powered, and built specifically for PocketFM's creative and performance marketing teams.
      </p>

      <div class="flex flex-col sm:flex-row gap-4 justify-center reveal">
        <a href="/Tool" target="_blank"
           class="inline-flex items-center justify-center gap-2.5 bg-gold hover:bg-gold-light text-void font-bold px-10 py-4 rounded-full text-base transition-all duration-300 hover:scale-105">
          Analyze a Script
          <svg width="18" height="18" viewBox="0 0 16 16" fill="none"><path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
        </a>
        <a href="#features"
           class="inline-flex items-center justify-center gap-2 glass text-text font-medium px-10 py-4 rounded-full text-base hover:border-violet/30 transition-all duration-300">
          Explore Features
        </a>
      </div>

      <!-- Stack badges -->
      <div class="flex flex-wrap items-center justify-center gap-3 mt-12 reveal">
        <span class="text-xs text-muted">Built with</span>
        <span class="glass px-3 py-1.5 rounded-full text-xs font-medium text-text/70">Python</span>
        <span class="glass px-3 py-1.5 rounded-full text-xs font-medium text-text/70">Streamlit</span>
        <span class="glass px-3 py-1.5 rounded-full text-xs font-medium text-text/70">Google Gemini</span>
        <span class="glass px-3 py-1.5 rounded-full text-xs font-medium text-text/70">Groq Llama</span>
        <span class="glass px-3 py-1.5 rounded-full text-xs font-medium text-violet-light/80">Claude Haiku</span>
        <span class="glass px-3 py-1.5 rounded-full text-xs font-medium text-gold/80">Google Drive API</span>
        <span class="glass px-3 py-1.5 rounded-full text-xs font-medium text-text/70">Meta Ads Data</span>
      </div>
    </div>
  </section>


  <!-- ============================================================
       FOOTER
  ============================================================ -->
  <footer class="border-t border-border py-16 px-6 lg:px-12">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-start md:items-center justify-between gap-10">
      <!-- Brand -->
      <div>
        <div class="flex items-center gap-2 mb-3">
          <div class="flex items-end gap-px h-4">
            <div class="wave-bar w-px bg-gold rounded-full" style="height:5px;  --dur:1.0s;"></div>
            <div class="wave-bar w-px bg-gold rounded-full" style="height:12px; --dur:1.3s; --delay:0.1s;"></div>
            <div class="wave-bar w-px bg-gold rounded-full" style="height:8px;  --dur:1.0s; --delay:0.2s;"></div>
          </div>
          <span class="font-semibold text-text tracking-wide">StoryAnalyzer</span>
        </div>
        <p class="text-muted text-sm">AI-powered script intelligence for PocketFM.</p>
        <p class="text-muted/40 text-xs mt-1">Python &bull; Streamlit &bull; Multi-AI &bull; Open Source</p>
      </div>

      <!-- Links -->
      <div class="flex flex-wrap gap-8 text-sm text-muted">
        <a href="#features"     class="hover:text-text transition-colors duration-200">Features</a>
        <a href="#how-it-works" class="hover:text-text transition-colors duration-200">How It Works</a>
        <a href="#why"          class="hover:text-text transition-colors duration-200">Why It Matters</a>
        <a href="__GH__" target="_blank"
           class="hover:text-text transition-colors duration-200">GitHub</a>
      </div>

      <!-- Right — Developer Credit -->
      <div class="text-right">
        <div class="text-xs text-muted/40 mb-2">Made for PocketFM — 2025</div>
        <div class="flex items-center justify-end gap-2">
          <!-- Slack icon -->
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" style="color:#A855F7; flex-shrink:0;">
            <path d="M5.042 15.165a2.528 2.528 0 0 1-2.52 2.523A2.528 2.528 0 0 1 0 15.165a2.527 2.527 0 0 1 2.522-2.52h2.52v2.52zM6.313 15.165a2.527 2.527 0 0 1 2.521-2.52 2.527 2.527 0 0 1 2.521 2.52v6.313A2.528 2.528 0 0 1 8.834 24a2.528 2.528 0 0 1-2.521-2.522v-6.313zM8.834 5.042a2.528 2.528 0 0 1-2.521-2.52A2.528 2.528 0 0 1 8.834 0a2.528 2.528 0 0 1 2.521 2.522v2.52H8.834zM8.834 6.313a2.528 2.528 0 0 1 2.521 2.521 2.528 2.528 0 0 1-2.521 2.521H2.522A2.528 2.528 0 0 1 0 8.834a2.528 2.528 0 0 1 2.522-2.521h6.312zM18.956 8.834a2.528 2.528 0 0 1 2.522-2.521A2.528 2.528 0 0 1 24 8.834a2.528 2.528 0 0 1-2.522 2.521h-2.522V8.834zM17.688 8.834a2.528 2.528 0 0 1-2.523 2.521 2.527 2.527 0 0 1-2.52-2.521V2.522A2.527 2.527 0 0 1 15.165 0a2.528 2.528 0 0 1 2.523 2.522v6.312zM15.165 18.956a2.528 2.528 0 0 1 2.523 2.522A2.528 2.528 0 0 1 15.165 24a2.527 2.527 0 0 1-2.52-2.522v-2.522h2.52zM15.165 17.688a2.527 2.527 0 0 1-2.52-2.523 2.526 2.526 0 0 1 2.52-2.52h6.313A2.527 2.527 0 0 1 24 15.165a2.528 2.528 0 0 1-2.522 2.523h-6.313z" fill="currentColor"/>
          </svg>
          <a href="__SLACK__" target="_blank" rel="noopener"
             style="font-size:12px; color: #E5C068; font-weight:600; text-decoration:none; font-family:'Outfit',sans-serif;
                    text-shadow: 0 0 12px rgba(229,192,104,0.4); transition: all 0.2s;"
             onmouseover="this.style.color='#fff'; this.style.textShadow='0 0 20px rgba(229,192,104,0.8)';"
             onmouseout="this.style.color='#E5C068'; this.style.textShadow='0 0 12px rgba(229,192,104,0.4)';">
            Mayank Mandal
          </a>
        </div>
        <div class="text-[10px] text-muted/30 mt-1">Designed &amp; Developed &middot; PocketFM</div>
      </div>
    </div>
  </footer>


  <!-- ============================================================
       VANILLA JS — replaces GSAP
  ============================================================ -->
  <script>
    // ---------- Cursor spotlight ----------
    const spotlight = document.getElementById('spotlight');
    document.addEventListener('mousemove', e => {
      spotlight.style.left = e.clientX + 'px';
      spotlight.style.top  = e.clientY + 'px';
    });

    // ---------- Score ring animation ----------
    function animateScoreRings() {
      document.querySelectorAll('.score-ring[data-score]').forEach(ring => {
        const score  = parseInt(ring.dataset.score);
        const circ   = 2 * Math.PI * 16; // r=16 => 100.53
        const offset = circ * (1 - score / 100);
        ring.style.strokeDasharray  = circ;
        ring.style.strokeDashoffset = offset;
      });
    }
    setTimeout(animateScoreRings, 600);

    // ---------- Bar fill animation ----------
    function animateBars() {
      document.querySelectorAll('.bar-fill[data-width]').forEach(bar => {
        bar.style.width = bar.dataset.width + '%';
      });
    }
    setTimeout(animateBars, 800);

    // ---------- Counter — just set target value ----------
    document.querySelectorAll('.counter[data-target]').forEach(el => {
      el.textContent = el.dataset.target;
    });

    // ---------- IntersectionObserver for .reveal elements ----------
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -60px 0px' });

    document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

    // ---------- IntersectionObserver for .step-card elements ----------
    const stepObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry, idx) => {
        if (entry.isIntersecting) {
          const delay = Array.from(document.querySelectorAll('.step-card')).indexOf(entry.target) * 100;
          setTimeout(() => {
            entry.target.classList.add('revealed');
          }, delay);
          stepObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll('.step-card').forEach(el => stepObserver.observe(el));

    // ---------- IntersectionObserver for bento .card-hover elements ----------
    const bentoObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry, idx) => {
        if (entry.isIntersecting) {
          const cards = Array.from(document.querySelectorAll('#features .card-hover'));
          const delay = (cards.indexOf(entry.target) % 3) * 80;
          setTimeout(() => {
            entry.target.classList.add('revealed');
          }, delay);
          bentoObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.05, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll('#features .card-hover').forEach(el => bentoObserver.observe(el));

    // ---------- Step progress dots update ----------
    const dots = document.querySelectorAll('#step-dots [data-step]');
    const stepDotObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const stepCards = Array.from(document.querySelectorAll('.step-card'));
          const i = stepCards.indexOf(entry.target);
          if (i >= 0) {
            dots.forEach((d, di) => {
              d.style.background = di === i ? '#C9973A' : '#1D1A35';
              d.style.width      = di === i ? '24px'   : '8px';
            });
          }
        }
      });
    }, { threshold: 0.5 });

    document.querySelectorAll('.step-card').forEach(el => stepDotObserver.observe(el));

    // ---------- Navbar shrink on scroll ----------
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
      if (window.scrollY > 60) {
        navbar.style.background = 'rgba(6,4,15,0.92)';
      } else {
        navbar.style.background = '';
      }
    }, { passive: true });
  </script>

</body>
</html>"""

HTML = HTML_TEMPLATE.replace("__SLACK__", SLACK).replace("__GH__", GH)

st.components.v1.html(HTML, height=930, scrolling=True)
