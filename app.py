
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
from pathlib import Path

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="HeatSense — Urban Heat Intelligence",
    page_icon="🌡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# PATHS & DATA
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "heatsense_model.pkl"
DATA_PATH = BASE_DIR / "weather_data.csv"
METADATA_PATH = BASE_DIR / "model_metadata.json"

model = joblib.load(MODEL_PATH)

weather_data = pd.read_csv(DATA_PATH)
weather_data["time"] = pd.to_datetime(weather_data["time"])

with open(METADATA_PATH, "r") as f:
    metadata = json.load(f)

# ============================================================
# GLOBAL CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 5% 0%, rgba(0, 212, 255, 0.13), transparent 28%),
        radial-gradient(circle at 95% 5%, rgba(124, 58, 237, 0.16), transparent 30%),
        radial-gradient(circle at 50% 100%, rgba(16, 185, 129, 0.06), transparent 30%),
        #050811;
    color: #F8FAFC;
}

.block-container {
    max-width: 1380px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

/* Hide Streamlit chrome */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* ---------- HERO ---------- */

.hero {
    padding: 34px 36px;
    border-radius: 28px;
    border: 1px solid rgba(255,255,255,0.10);
    background:
        linear-gradient(135deg,
            rgba(255,255,255,0.075),
            rgba(255,255,255,0.025));
    backdrop-filter: blur(22px);
    box-shadow:
        0 30px 80px rgba(0,0,0,0.35),
        inset 0 1px rgba(255,255,255,0.08);
    margin-bottom: 25px;
}

.brand {
    font-size: 2.9rem;
    font-weight: 800;
    letter-spacing: -2px;
    margin: 0;
}

.gradient-text {
    background: linear-gradient(90deg,#38BDF8,#818CF8,#C084FC);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.tagline {
    margin-top: 8px;
    color: #94A3B8;
    font-size: 1rem;
}

.online {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    margin-top: 18px;
    padding: 7px 13px;
    border-radius: 999px;
    background: rgba(16,185,129,0.10);
    border: 1px solid rgba(16,185,129,0.25);
    color: #6EE7B7;
    font-size: 0.76rem;
    font-weight: 700;
    letter-spacing: 0.5px;
}

.dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #34D399;
    box-shadow: 0 0 12px #34D399;
}

/* ---------- CARDS ---------- */

.card {
    border-radius: 24px;
    padding: 25px;
    border: 1px solid rgba(255,255,255,0.085);
    background: rgba(255,255,255,0.045);
    backdrop-filter: blur(20px);
    box-shadow:
        0 20px 55px rgba(0,0,0,0.20),
        inset 0 1px rgba(255,255,255,0.05);
}

.card-title {
    font-size: 1.05rem;
    font-weight: 700;
    margin-bottom: 4px;
}

.card-subtitle {
    color: #64748B;
    font-size: 0.82rem;
    margin-bottom: 18px;
}

/* ---------- RISK ---------- */

.risk-card {
    text-align: center;
    padding: 32px 20px;
    border-radius: 26px;
    background:
        radial-gradient(circle at 50% 0%, rgba(239,68,68,0.13), transparent 55%),
        rgba(255,255,255,0.045);
    border: 1px solid rgba(255,255,255,0.09);
}

.risk-label {
    color: #94A3B8;
    font-size: 0.72rem;
    letter-spacing: 2px;
    font-weight: 700;
    text-transform: uppercase;
}

.risk-value {
    font-size: 3.7rem;
    line-height: 1;
    font-weight: 800;
    margin: 15px 0 10px;
    letter-spacing: -2px;
}

.risk-confidence {
    color: #CBD5E1;
    font-size: 0.9rem;
}

.risk-high {
    color: #FB7185;
    text-shadow: 0 0 35px rgba(251,113,133,0.25);
}

.risk-moderate {
    color: #FBBF24;
    text-shadow: 0 0 35px rgba(251,191,36,0.20);
}

.risk-low {
    color: #34D399;
    text-shadow: 0 0 35px rgba(52,211,153,0.20);
}

/* ---------- METRICS ---------- */

.metric-card {
    padding: 20px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.07);
    background: rgba(255,255,255,0.035);
}

.metric-value {
    font-size: 1.65rem;
    font-weight: 800;
}

.metric-label {
    color: #64748B;
    font-size: 0.75rem;
    margin-top: 5px;
}

/* ---------- SECTION ---------- */

.section {
    margin-top: 30px;
    margin-bottom: 14px;
}

.section h2 {
    font-size: 1.45rem;
    letter-spacing: -0.5px;
    margin-bottom: 2px;
}

.section p {
    color: #64748B;
    font-size: 0.84rem;
}

/* ---------- BUTTON ---------- */

.stButton > button {
    width: 100%;
    height: 48px;
    border-radius: 14px;
    border: 1px solid rgba(56,189,248,0.30);
    background: linear-gradient(90deg,#0EA5E9,#6366F1);
    color: white;
    font-weight: 800;
    letter-spacing: 0.3px;
    box-shadow: 0 10px 30px rgba(59,130,246,0.20);
    transition: all 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 14px 38px rgba(59,130,246,0.30);
}

/* ---------- INPUTS ---------- */

div[data-baseweb="input"],
div[data-baseweb="select"] {
    border-radius: 12px;
}

label {
    color: #CBD5E1 !important;
    font-size: 0.82rem !important;
}

/* ---------- DIVIDER ---------- */

.glow-divider {
    height: 1px;
    margin: 28px 0;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(56,189,248,0.35),
        rgba(129,140,248,0.35),
        transparent
    );
}

/* ---------- FOOTER ---------- */

.footer {
    text-align: center;
    color: #475569;
    font-size: 0.75rem;
    padding-top: 35px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# HELPERS
# ============================================================

def season_from_month(month):
    if month in [3, 4, 5]:
        return "Summer"
    elif month in [6, 7, 8, 9]:
        return "Monsoon"
    elif month in [10, 11]:
        return "Post-Monsoon"
    else:
        return "Winter"


def make_features(
    temperature,
    humidity,
    precipitation,
    wind,
    radiation,
    date,
    hour
):
    month = date.month
    day = date.day
    day_of_year = date.timetuple().tm_yday
    season = season_from_month(month)

    return pd.DataFrame([{
        "temperature_2m": temperature,
        "relative_humidity_2m": humidity,
        "precipitation": precipitation,
        "wind_speed_10m": wind,
        "shortwave_radiation": radiation,
        "hour": hour,
        "day": day,
        "month": month,
        "day_of_year": day_of_year,
        "season_Monsoon": int(season == "Monsoon"),
        "season_Post-Monsoon": int(season == "Post-Monsoon"),
        "season_Summer": int(season == "Summer"),
        "season_Winter": int(season == "Winter")
    }])


def risk_class(temp):
    if temp < metadata["low_threshold"]:
        return "Low"
    elif temp < metadata["high_threshold"]:
        return "Moderate"
    return "High"


def risk_class_style(risk):
    if risk == "High":
        return "risk-high"
    elif risk == "Moderate":
        return "risk-moderate"
    return "risk-low"


# ============================================================
# SESSION STATE
# ============================================================

if "prediction" not in st.session_state:
    st.session_state.prediction = None

# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

<div class="brand">
<span class="gradient-text">HeatSense</span>
</div>

<div class="tagline">
Urban Heat Intelligence powered by Machine Learning
</div>

<div class="online">
<span class="dot"></span>
AI MODEL ONLINE
</div>

</div>
""", unsafe_allow_html=True)

# ============================================================
# INPUT + PREDICTION
# ============================================================

left, right = st.columns([1.05, 1], gap="large")

with left:

    st.markdown("""
    <div class="card">
    <div class="card-title">Environmental Conditions</div>
    <div class="card-subtitle">
    Configure the atmospheric conditions you want the model to evaluate.
    </div>
    """, unsafe_allow_html=True)

    temperature = st.slider(
        "Temperature",
        min_value=10.0,
        max_value=45.0,
        value=30.0,
        step=0.1,
        format="%.1f"
    )

    humidity = st.slider(
        "Relative Humidity",
        min_value=10,
        max_value=100,
        value=65,
        step=1,
        format="%d"
    )

    precipitation = st.number_input(
        "Precipitation",
        min_value=0.0,
        max_value=50.0,
        value=0.0,
        step=0.1,
        format="%.1f"
    )

    wind = st.slider(
        "Wind Speed",
        min_value=0.0,
        max_value=30.0,
        value=4.0,
        step=0.1,
        format="%.1f"
    )

    radiation = st.slider(
        "Solar Radiation",
        min_value=0.0,
        max_value=1200.0,
        value=500.0,
        step=10.0,
        format="%.0f"
    )

    col1, col2 = st.columns(2)

    with col1:
        selected_date = st.date_input(
            "Date",
            value=pd.Timestamp("2025-05-15").date()
        )

    with col2:
        selected_hour = st.slider(
            "Hour",
            min_value=0,
            max_value=23,
            value=14
        )

    analyze = st.button("⚡ ANALYZE HEAT RISK")

    st.markdown("</div>", unsafe_allow_html=True)

    if analyze:

        features = make_features(
            temperature,
            humidity,
            precipitation,
            wind,
            radiation,
            selected_date,
            selected_hour
        )

        prediction = model.predict(features)[0]
        probabilities = model.predict_proba(features)[0]

        class_probabilities = dict(
            zip(model.classes_, probabilities)
        )

        st.session_state.prediction = {
            "risk": prediction,
            "probabilities": class_probabilities
        }


with right:

    prediction = st.session_state.prediction

    if prediction is None:
        risk = risk_class(temperature)

        st.markdown(f"""
        <div class="risk-card">

        <div class="risk-label">
        CURRENT HEAT RISK
        </div>

        <div class="risk-value {risk_class_style(risk)}">
        {risk.upper()}
        </div>

        <div class="risk-confidence">
        Configure conditions and analyze the environment
        </div>

        </div>
        """, unsafe_allow_html=True)

    else:

        risk = prediction["risk"]
        probs = prediction["probabilities"]
        confidence = probs[risk] * 100

        st.markdown(f"""
        <div class="risk-card">

        <div class="risk-label">
        PREDICTED HEAT RISK
        </div>

        <div class="risk-value {risk_class_style(risk)}">
        {risk.upper()}
        </div>

        <div class="risk-confidence">
        Model confidence · <strong>{confidence:.1f}%</strong>
        </div>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        prob_df = pd.DataFrame({
            "Risk": list(probs.keys()),
            "Probability": [v * 100 for v in probs.values()]
        })

        st.markdown("""
        <div class="card">
        <div class="card-title">Risk Probability</div>
        <div class="card-subtitle">
        Probability distribution returned by the trained classifier.
        </div>
        """, unsafe_allow_html=True)

        st.bar_chart(
            prob_df.set_index("Risk"),
            y="Probability",
            height=190
        )

        st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# WHAT-IF SIMULATOR
# ============================================================

st.markdown("""
<div class="section">
<h2>🎛️ What-If Simulator</h2>
<p>Explore how changing environmental conditions affects the model's prediction.</p>
</div>
""", unsafe_allow_html=True)

sim1, sim2, sim3 = st.columns(3)

with sim1:
    sim_temp = st.slider(
        "Temperature Scenario",
        15.0, 45.0, temperature,
        0.5,
        key="sim_temp"
    )

with sim2:
    sim_humidity = st.slider(
        "Humidity Scenario",
        10, 100, humidity,
        1,
        key="sim_humidity"
    )

with sim3:
    sim_wind = st.slider(
        "Wind Scenario",
        0.0, 30.0, wind,
        0.5,
        key="sim_wind"
    )

sim_features = make_features(
    sim_temp,
    sim_humidity,
    precipitation,
    sim_wind,
    radiation,
    selected_date,
    selected_hour
)

sim_prediction = model.predict(sim_features)[0]
sim_probability = model.predict_proba(sim_features)[0]

sim_probs = dict(zip(model.classes_, sim_probability))
sim_confidence = sim_probs[sim_prediction] * 100

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div class="metric-card">
    <div class="metric-value">{sim_temp:.1f}°C</div>
    <div class="metric-label">SCENARIO TEMPERATURE</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="metric-card">
    <div class="metric-value">{sim_humidity}%</div>
    <div class="metric-label">SCENARIO HUMIDITY</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="metric-card">
    <div class="metric-value {risk_class_style(sim_prediction)}">
    {sim_prediction.upper()}
    </div>
    <div class="metric-label">
    SCENARIO RESULT · {sim_confidence:.1f}% CONF.
    </div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# HISTORICAL INTELLIGENCE
# ============================================================

st.markdown("""
<div class="section">
<h2>📊 Bengaluru Heat Intelligence</h2>
<p>Historical patterns derived from the 2020–2025 weather dataset.</p>
</div>
""", unsafe_allow_html=True)

hist1, hist2 = st.columns(2, gap="large")

with hist1:

    monthly = (
        weather_data
        .assign(month=weather_data["time"].dt.month)
        .groupby("month")["temperature_2m"]
        .mean()
    )

    monthly.index = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    st.markdown("""
    <div class="card">
    <div class="card-title">Average Temperature by Month</div>
    <div class="card-subtitle">
    Bengaluru's historical monthly temperature profile.
    </div>
    """, unsafe_allow_html=True)

    st.line_chart(monthly, height=280)

    st.markdown("</div>", unsafe_allow_html=True)


with hist2:

    hourly = (
        weather_data
        .assign(hour=weather_data["time"].dt.hour)
        .groupby("hour")["temperature_2m"]
        .mean()
    )

    st.markdown("""
    <div class="card">
    <div class="card-title">Temperature by Hour</div>
    <div class="card-subtitle">
    Average temperature pattern across the day.
    </div>
    """, unsafe_allow_html=True)

    st.line_chart(hourly, height=280)

    st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# KEY STATISTICS
# ============================================================

st.markdown("""
<div class="section">
<h2>⚡ Dataset Intelligence</h2>
<p>Quick statistics from the historical weather record.</p>
</div>
""", unsafe_allow_html=True)

years = weather_data["time"].dt.year

stats = [
    ("6", "YEARS OF WEATHER DATA"),
    (f"{len(weather_data):,}", "HOURLY OBSERVATIONS"),
    (f"{weather_data['temperature_2m'].max():.1f}°C", "HIGHEST RECORDED TEMP."),
    (f"{weather_data['temperature_2m'].mean():.1f}°C", "AVERAGE TEMPERATURE")
]

cols = st.columns(4)

for col, (value, label) in zip(cols, stats):
    with col:
        st.markdown(f"""
        <div class="metric-card">
        <div class="metric-value">{value}</div>
        <div class="metric-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)


# ============================================================
# MODEL PERFORMANCE
# ============================================================

st.markdown("""
<div class="section">
<h2>🧠 Model Performance</h2>
<p>Measured on held-out test data and time-series cross-validation.</p>
</div>
""", unsafe_allow_html=True)

m1, m2, m3 = st.columns(3)

metrics = [
    (f"{metadata['test_accuracy'] * 100:.2f}%", "TEST ACCURACY"),
    (f"{metadata['mean_time_series_cv_accuracy'] * 100:.2f}%", "TIME-SERIES CV"),
    (f"{metadata['cv_std'] * 100:.2f}%", "CV STD. DEV.")
]

for col, (value, label) in zip([m1, m2, m3], metrics):
    with col:
        st.markdown(f"""
        <div class="metric-card">
        <div class="metric-value">{value}</div>
        <div class="metric-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)


# ============================================================
# HOW IT WORKS
# ============================================================

st.markdown("""
<div class="section">
<h2>⚙️ How HeatSense Works</h2>
<p>From raw environmental conditions to machine-learning risk classification.</p>
</div>

<div class="card">

<div style="display:flex; justify-content:space-between; gap:15px; flex-wrap:wrap;">

<div>
<strong>01 · WEATHER DATA</strong><br>
<span style="color:#64748B;">
Temperature · Humidity · Wind · Rain · Solar Radiation
</span>
</div>

<div style="color:#38BDF8; font-size:25px;">→</div>

<div>
<strong>02 · FEATURE ENGINEERING</strong><br>
<span style="color:#64748B;">
Hour · Day · Month · Day of Year · Season
</span>
</div>

<div style="color:#818CF8; font-size:25px;">→</div>

<div>
<strong>03 · MACHINE LEARNING</strong><br>
<span style="color:#64748B;">
Logistic Regression classifier
</span>
</div>

<div style="color:#C084FC; font-size:25px;">→</div>

<div>
<strong>04 · HEAT RISK</strong><br>
<span style="color:#64748B;">
Low · Moderate · High
</span>
</div>

</div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="glow-divider"></div>

<div class="footer">
HeatSense · Urban Heat Intelligence<br>
Machine Learning powered environmental risk analysis
</div>
""", unsafe_allow_html=True)
