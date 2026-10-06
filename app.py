import streamlit as st
import time

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="AI Wellness Guardian",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #07111f;
    color: #f4f7fb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 4rem;
    max-width: 1200px;
}

/* Hide Streamlit default elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Hero */
.hero {
    padding: 70px 30px 60px 30px;
    text-align: center;
    border-radius: 28px;
    background: linear-gradient(135deg, #0c1b30, #102b43);
    border: 1px solid #203b55;
    margin-bottom: 45px;
}

.badge {
    display: inline-block;
    padding: 8px 18px;
    border-radius: 30px;
    background: #132b40;
    border: 1px solid #2b5877;
    color: #8ed8ff;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 1px;
}

.hero h1 {
    font-size: 52px;
    font-weight: 800;
    margin: 22px 0 12px 0;
    background: linear-gradient(90deg, #ffffff, #79d7ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    font-size: 19px;
    color: #b8c7d9;
    max-width: 800px;
    margin: auto;
    line-height: 1.7;
}

.quote {
    margin-top: 22px;
    color: #7fd8ff;
    font-size: 16px;
    font-weight: 600;
}

/* Section */
.section-title {
    font-size: 32px;
    font-weight: 800;
    margin-top: 55px;
    margin-bottom: 8px;
}

.section-subtitle {
    color: #91a4b8;
    font-size: 16px;
    margin-bottom: 25px;
}

/* Cards */
.card {
    background: #0c1a2a;
    border: 1px solid #1e354d;
    border-radius: 18px;
    padding: 25px;
    min-height: 170px;
}

.card h3 {
    margin-top: 8px;
    font-size: 20px;
}

.card p {
    color: #9fb1c4;
    line-height: 1.6;
}

.icon {
    font-size: 30px;
}

/* Pipeline */
.pipeline {
    background: #0b1928;
    border: 1px solid #20394f;
    border-radius: 20px;
    padding: 25px;
    text-align: center;
}

.pipeline-item {
    padding: 18px;
    background: #102438;
    border-radius: 14px;
    border: 1px solid #28465f;
    margin: 5px;
    font-weight: 600;
}

.arrow {
    color: #6fd5ff;
    font-size: 25px;
}

/* Dashboard */
.dashboard {
    background: #091827;
    border: 1px solid #28445c;
    border-radius: 24px;
    padding: 28px;
    margin-top: 20px;
}

.metric {
    background: #0f2235;
    border: 1px solid #23435c;
    border-radius: 15px;
    padding: 20px;
    text-align: center;
}

.metric-title {
    color: #8ea4b8;
    font-size: 13px;
}

.metric-value {
    font-size: 27px;
    font-weight: 800;
    margin-top: 8px;
}

/* Recommendation */
.recommend {
    background: linear-gradient(135deg, #102d38, #102438);
    border: 1px solid #286071;
    border-radius: 20px;
    padding: 28px;
}

.recommend h3 {
    color: #82e0ff;
}

/* Privacy */
.privacy {
    background: #0a1826;
    border: 1px solid #1e384f;
    border-radius: 20px;
    padding: 30px;
    margin-top: 20px;
}

.small {
    color: #879caf;
    font-size: 13px;
}

/* CTA */
.final-cta {
    text-align: center;
    padding: 60px 25px;
    margin-top: 60px;
    border-radius: 25px;
    background: linear-gradient(135deg, #0d2538, #122d42);
    border: 1px solid #28516c;
}

.final-cta h2 {
    font-size: 34px;
    margin-bottom: 15px;
}

.final-cta p {
    color: #a9bdcf;
    font-size: 17px;
}
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# HERO
# ---------------------------------------------------------
st.markdown("""
<div class="hero">

<div class="badge">AI • WELLNESS • REAL-TIME • NON-INVASIVE</div>

<h1>🧠 AI Wellness Guardian</h1>

<p>
Your AI-powered digital wellness companion that understands
your work patterns and helps you take better care of yourself.
</p>

<div class="quote">
“Your computer knows what you're doing. We help it understand how you're doing.”
</div>

</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# PROBLEM
# ---------------------------------------------------------
st.markdown("""
<div class="section-title">The Problem</div>
<div class="section-subtitle">
We spend hours working with screens, but most digital systems understand productivity — not human wellness.
</div>
""", unsafe_allow_html=True)

cols = st.columns(4)

problems = [
    ("🕒", "Long Screen Time", "Continuous screen exposure can increase the need for regular breaks."),
    ("👁️", "Visual Fatigue", "Blinking and eye-behavior changes can indicate possible fatigue."),
    ("⌨️", "Changing Work Patterns", "Typing rhythm and pauses can change as a person becomes tired or stressed."),
    ("🧠", "Hidden Signals", "Multiple small signals together can provide a better wellness picture.")
]

for col, item in zip(cols, problems):
    with col:
        st.markdown(f"""
        <div class="card">
            <div class="icon">{item[0]}</div>
            <h3>{item[1]}</h3>
            <p>{item[2]}</p>
        </div>
        """, unsafe_allow_html=True)


# ---------------------------------------------------------
# INNOVATION
# ---------------------------------------------------------
st.markdown("""
<div class="section-title">Our Innovation</div>
<div class="section-subtitle">
Instead of depending on one signal, AI Wellness Guardian combines multiple behavioral signals.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="pipeline">

<div style="display:flex; flex-wrap:wrap; justify-content:center; align-items:center;">

<div class="pipeline-item">📷 Face</div>
<div class="pipeline-item">👁️ Eyes</div>
<div class="pipeline-item">⌨️ Typing</div>
<div class="pipeline-item">🕒 Screen Time</div>

</div>

<div class="arrow">↓</div>

<div class="pipeline-item">
🤖 AI Feature Fusion Engine
</div>

<div class="arrow">↓</div>

<div style="display:flex; flex-wrap:wrap; justify-content:center;">

<div class="pipeline-item">😊 Mood</div>
<div class="pipeline-item">😴 Fatigue</div>
<div class="pipeline-item">🧘 Stress Indicators</div>
<div class="pipeline-item">🎯 Focus</div>

</div>

<div class="arrow">↓</div>

<div class="pipeline-item">
💡 Personalized Wellness Recommendation
</div>

</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# HOW IT WORKS
# ---------------------------------------------------------
st.markdown("""
<div class="section-title">How It Works</div>
<div class="section-subtitle">
Four passive signals are combined to estimate a user's current wellness state.
</div>
""", unsafe_allow_html=True)

cols = st.columns(4)

modules = [
    ("📷", "Face Analysis", "Facial expression patterns are analyzed to estimate possible emotional state."),
    ("👁️", "Eye Analysis", "Blinking and eye openness are used as possible fatigue indicators."),
    ("⌨️", "Typing Analysis", "Typing rhythm, pauses and keystroke dynamics are analyzed without storing typed content."),
    ("🕒", "Screen-Time Analysis", "Continuous work duration is tracked to identify when a break may be useful.")
]

for col, item in zip(cols, modules):
    with col:
        st.markdown(f"""
        <div class="card">
            <div class="icon">{item[0]}</div>
            <h3>{item[1]}</h3>
            <p>{item[2]}</p>
        </div>
        """, unsafe_allow_html=True)


# ---------------------------------------------------------
# LIVE DEMO
# ---------------------------------------------------------
st.markdown("""
<div class="section-title">Live Product Demo</div>
<div class="section-subtitle">
A preview of the AI Wellness Guardian monitoring dashboard.
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="dashboard">', unsafe_allow_html=True)

st.markdown("""
<h2>🧠 AI Wellness Guardian — LIVE</h2>
<p style="color:#8ea4b8;">
Monitoring wellness-related behavioral signals
</p>
""", unsafe_allow_html=True)

cols = st.columns(4)

metrics = [
    ("😊", "Current Mood", "Neutral"),
    ("👁️", "Eye Fatigue", "High"),
    ("🧘", "Stress Indicator", "Medium"),
    ("🎯", "Focus", "Medium")
]

for col, metric in zip(cols, metrics):
    with col:
        st.markdown(f"""
        <div class="metric">
            <div style="font-size:28px">{metric[0]}</div>
            <div class="metric-title">{metric[1]}</div>
            <div class="metric-value">{metric[2]}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

cols = st.columns(2)

with cols[0]:
    st.markdown("""
    <div class="metric">
        <div class="metric-title">WELLNESS SCORE</div>
        <div class="metric-value">78 / 100</div>
        <div class="small">Overall estimated wellness state</div>
    </div>
    """, unsafe_allow_html=True)

with cols[1]:
    st.markdown("""
    <div class="metric">
        <div class="metric-title">CONTINUOUS WORK TIME</div>
        <div class="metric-value">3h 48m / 4h</div>
        <div class="small">Break threshold approaching</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="recommend">

<h3>💡 AI Recommendation</h3>

<h2>Take a short screen break.</h2>

<p style="color:#a9bdcf;">
Your screen time is approaching the configured continuous-work limit,
while eye-fatigue indicators are elevated.
A short break, hydration and looking away from the screen may help.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ---------------------------------------------------------
# ACTION BUTTONS
# ---------------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    if st.button("🧘 TAKE A BREAK", use_container_width=True):
        st.success("Break mode activated. Step away from the screen for a few minutes.")

with c2:
    if st.button("💧 HYDRATION REMINDER", use_container_width=True):
        st.info("Reminder: Take a moment for hydration.")

with c3:
    if st.button("🎵 PLAY RELAXING MUSIC", use_container_width=True):
        st.info("Relaxing music recommendation activated.")


# ---------------------------------------------------------
# ANALYTICS
# ---------------------------------------------------------
st.markdown("""
<div class="section-title">Wellness Analytics</div>
<div class="section-subtitle">
A simple view of how wellness-related indicators can change during a work session.
</div>
""", unsafe_allow_html=True)

import pandas as pd

chart_data = pd.DataFrame({
    "Time": ["9 AM", "10 AM", "11 AM", "12 PM", "1 PM", "2 PM"],
    "Wellness": [82, 85, 79, 74, 70, 78]
})

st.line_chart(
    chart_data.set_index("Time"),
    height=300
)


# ---------------------------------------------------------
# RECOMMENDATION ENGINE
# ---------------------------------------------------------
st.markdown("""
<div class="section-title">Recommendation Engine</div>
<div class="section-subtitle">
AI doesn't just detect — it recommends an action.
</div>
""", unsafe_allow_html=True)

cols = st.columns(4)

recommendations = [
    ("👁️", "High Eye Fatigue", "Suggest a short screen break."),
    ("🧘", "Stress Indicators", "Suggest relaxation or calming music."),
    ("⌨️", "Typing Changes", "Suggest a short rest."),
    ("🕒", "Long Work Session", "Trigger a break reminder.")
]

for col, item in zip(cols, recommendations):
    with col:
        st.markdown(f"""
        <div class="card">
            <div class="icon">{item[0]}</div>
            <h3>{item[1]}</h3>
            <p>{item[2]}</p>
        </div>
        """, unsafe_allow_html=True)


# ---------------------------------------------------------
# MUSIC
# ---------------------------------------------------------
st.markdown("""
<div class="section-title">Personalized Music</div>
<div class="section-subtitle">
Optional music recommendations can be used to support relaxation and focus.
</div>
""", unsafe_allow_html=True)

music_cols = st.columns(3)

music = [
    ("🎧", "Focus Mode", "Instrumental & concentration music"),
    ("🌿", "Relax Mode", "Calm and relaxing music"),
    ("🌙", "Recovery Mode", "Slow music for a short reset")
]

for col, item in zip(music_cols, music):
    with col:
        st.markdown(f"""
        <div class="card">
            <div class="icon">{item[0]}</div>
            <h3>{item[1]}</h3>
            <p>{item[2]}</p>
        </div>
        """, unsafe_allow_html=True)


# ---------------------------------------------------------
# WHY DIFFERENT
# ---------------------------------------------------------
st.markdown("""
<div class="section-title">Why AI Wellness Guardian?</div>
<div class="section-subtitle">
More than a detector — a multimodal wellness assistant.
</div>
""", unsafe_allow_html=True)

cols = st.columns(5)

advantages = [
    ("🔗", "Multimodal", "Combines multiple signals."),
    ("⚡", "Real-Time", "Continuous wellness monitoring."),
    ("💡", "Action-Oriented", "Turns signals into recommendations."),
    ("🔒", "Privacy-Conscious", "Focuses on behavior, not private content."),
    ("💻", "Lightweight", "Designed for everyday laptops.")
]

for col, item in zip(cols, advantages):
    with col:
        st.markdown(f"""
        <div class="card">
            <div class="icon">{item[0]}</div>
            <h3>{item[1]}</h3>
            <p>{item[2]}</p>
        </div>
        """, unsafe_allow_html=True)


# ---------------------------------------------------------
# TECHNOLOGY
# ---------------------------------------------------------
st.markdown("""
<div class="section-title">Technology Stack</div>
<div class="section-subtitle">
Technologies that power the AI Wellness Guardian concept.
</div>
""", unsafe_allow_html=True)

tech = [
    "🐍 Python",
    "👁️ OpenCV",
    "🎯 MediaPipe",
    "🤖 Scikit-learn",
    "📊 Pandas",
    "🌐 Streamlit"
]

cols = st.columns(3)

for i, technology in enumerate(tech):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="pipeline-item" style="margin-bottom:12px;">
            {technology}
        </div>
        """, unsafe_allow_html=True)


# ---------------------------------------------------------
# PRIVACY
# ---------------------------------------------------------
st.markdown("""
<div class="section-title">Privacy First</div>

<div class="privacy">

<h2>🔒 We analyze behavior, not private content.</h2>

<p style="color:#a5b7c8;">
AI Wellness Guardian is designed with privacy-conscious principles.
</p>

<p>✓ No raw webcam footage needs to be stored.</p>
<p>✓ Typed content is not required for typing analysis.</p>
<p>✓ Only behavioral patterns are considered.</p>
<p>✓ Local processing can be used where possible.</p>
<p>✓ Monitoring remains user-controlled.</p>

</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# DISCLAIMER
# ---------------------------------------------------------
st.markdown("""
<div class="privacy">

<h3>⚠️ Important</h3>

<p class="small">
AI Wellness Guardian is a wellness-support prototype, not a medical
diagnostic system. Its outputs represent estimated wellness indicators
and should not be treated as medical conclusions.
</p>

</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# FINAL CTA
# ---------------------------------------------------------
st.markdown("""
<div class="final-cta">

<h2>Don't wait for burnout.</h2>

<p>
Let your computer remind you to take care of yourself.
</p>

<h2>🧠 AI Wellness Guardian</h2>

<p>
Your AI-powered digital wellness companion.
</p>

</div>
""", unsafe_allow_html=True)
