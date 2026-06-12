import streamlit as st
import requests

st.set_page_config(
    page_title="SmartPrice AI",
    page_icon="🏠",
    layout="centered"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    /* ── Reset & base ── */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: #0F1923;
    }

    /* ── Hide Streamlit chrome ── */
    #MainMenu, footer, header { visibility: hidden; }
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
        max-width: 560px !important;
    }

    /* ── Hero header ── */
    .hero {
        text-align: center;
        padding: 2.5rem 1.5rem 2rem;
        margin-bottom: 0.5rem;
    }
    .hero-badge {
        display: inline-block;
        background: rgba(255, 153, 51, 0.12);
        border: 1px solid rgba(255, 153, 51, 0.3);
        color: #FF9933;
        font-size: 0.7rem;
        font-weight: 600;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        padding: 0.35rem 0.9rem;
        border-radius: 999px;
        margin-bottom: 1.2rem;
    }
    .hero-title {
        font-size: 2.6rem;
        font-weight: 800;
        color: #F7F4EF;
        line-height: 1.1;
        margin: 0 0 0.6rem;
        letter-spacing: -0.03em;
    }
    .hero-title span {
        color: #FF9933;
    }
    .hero-sub {
        font-size: 0.95rem;
        color: #7A8B9A;
        font-weight: 400;
        margin: 0;
    }

    /* ── Card ── */
    .form-card {
        background: #1A2535;
        border: 1px solid rgba(255,255,255,0.07);
        border-radius: 20px;
        padding: 2rem 2rem 1.5rem;
        margin-bottom: 1.2rem;
    }
    .card-section-label {
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #4A6080;
        margin-bottom: 1.1rem;
    }

    /* ── Labels ── */
    .stTextInput label,
    .stNumberInput label {
        color: #9AAFC0 !important;
        font-size: 0.8rem !important;
        font-weight: 500 !important;
        letter-spacing: 0.02em !important;
    }

    /* ── Input fields ── */
    .stTextInput input,
    .stNumberInput input {
        background: #0F1923 !important;
        border: 1.5px solid rgba(255,255,255,0.1) !important;
        border-radius: 10px !important;
        color: #F7F4EF !important;
        font-size: 0.95rem !important;
        font-weight: 500 !important;
        padding: 0.6rem 0.85rem !important;
        transition: border-color 0.2s !important;
    }
    .stTextInput input:focus,
    .stNumberInput input:focus {
        border-color: #FF9933 !important;
        box-shadow: 0 0 0 3px rgba(255,153,51,0.12) !important;
    }

    /* ── Stepper arrows ── */
    .stNumberInput button {
        background: rgba(255,255,255,0.05) !important;
        border: none !important;
        color: #9AAFC0 !important;
        border-radius: 6px !important;
    }
    .stNumberInput button:hover {
        background: rgba(255,153,51,0.15) !important;
        color: #FF9933 !important;
    }

    /* ── Predict button ── */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #FF9933 0%, #E07B1A 100%) !important;
        color: #0F1923 !important;
        font-weight: 700 !important;
        font-size: 1rem !important;
        letter-spacing: 0.04em !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.85rem 1.5rem !important;
        cursor: pointer !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 4px 20px rgba(255,153,51,0.25) !important;
    }
    .stButton > button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 8px 28px rgba(255,153,51,0.4) !important;
    }
    .stButton > button:active {
        transform: translateY(0) !important;
    }

    /* ── Result card ── */
    .result-card {
        background: linear-gradient(135deg, #1A2535 0%, #1F2E40 100%);
        border: 1px solid rgba(255, 153, 51, 0.25);
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        animation: slideUp 0.4s ease;
        margin-top: 1rem;
    }
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(16px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    .result-label {
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #4A6080;
        margin-bottom: 0.5rem;
    }
    .result-price {
        font-size: 3rem;
        font-weight: 800;
        color: #FF9933;
        letter-spacing: -0.04em;
        line-height: 1;
        margin: 0.2rem 0;
    }
    .result-unit {
        font-size: 0.85rem;
        color: #7A8B9A;
        margin-top: 0.4rem;
    }
    .result-divider {
        height: 1px;
        background: rgba(255,255,255,0.07);
        margin: 1.2rem 0;
    }
    .result-meta {
        display: flex;
        justify-content: center;
        gap: 1.5rem;
        flex-wrap: wrap;
    }
    .meta-item {
        text-align: center;
    }
    .meta-value {
        font-size: 0.9rem;
        font-weight: 700;
        color: #C8D8E8;
    }
    .meta-key {
        font-size: 0.68rem;
        color: #4A6080;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-top: 0.1rem;
    }

    /* ── Error card ── */
    .error-card {
        background: rgba(220, 60, 60, 0.08);
        border: 1px solid rgba(220, 60, 60, 0.25);
        border-radius: 12px;
        padding: 1rem 1.25rem;
        color: #FF7070;
        font-size: 0.85rem;
        margin-top: 1rem;
    }

    /* ── Footer ── */
    .footer {
        text-align: center;
        color: #2E3E50;
        font-size: 0.72rem;
        margin-top: 2.5rem;
        letter-spacing: 0.03em;
    }

    /* ── Column gap tweak ── */
    [data-testid="column"] {
        padding: 0 0.3rem !important;
    }
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-badge">✦ AI-Powered Valuation</div>
    <h1 class="hero-title">Smart<span>Price</span> AI</h1>
    <p class="hero-sub">Enter property details to get an instant market estimate</p>
</div>
""", unsafe_allow_html=True)

# ── Form card ─────────────────────────────────────────────
st.markdown('<div class="form-card">', unsafe_allow_html=True)
st.markdown('<div class="card-section-label">📍 Property Details</div>', unsafe_allow_html=True)

location = st.text_input("Location", placeholder="e.g. Whitefield, Bangalore")
sqft = st.number_input("Total Area (sq ft)", min_value=100.0, value=1000.0, step=50.0)

col1, col2, col3 = st.columns(3)
with col1:
    bhk = st.number_input("BHK", min_value=1, value=2, step=1)
with col2:
    bath = st.number_input("Bathrooms", min_value=1, value=2, step=1)
with col3:
    balcony = st.number_input("Balconies", min_value=0, value=1, step=1)

st.markdown('</div>', unsafe_allow_html=True)

# ── Predict button ────────────────────────────────────────
predict = st.button("⚡  Estimate Price")

# ── Result ────────────────────────────────────────────────
if predict:
    if not location.strip():
        st.markdown('<div class="error-card">⚠️ Please enter a location to continue.</div>', unsafe_allow_html=True)
    else:
        payload = {
            "location": location,
            "total_sqft": sqft,
            "bath": bath,
            "balcony": balcony,
            "bhk": bhk
        }
        try:
            response = requests.post(
                "http://127.0.0.1:8000/predict-house",
                json=payload,
                timeout=10
            )
            response.raise_for_status()
            result = response.json()
            price = result["predicted_price_lakhs"]

            st.markdown(f"""
            <div class="result-card">
                <div class="result-label">Estimated Market Value</div>
                <div class="result-price">₹{price}</div>
                <div class="result-unit">Lakhs &nbsp;·&nbsp; Indian Rupees</div>
                <div class="result-divider"></div>
                <div class="result-meta">
                    <div class="meta-item">
                        <div class="meta-value">{location.title()}</div>
                        <div class="meta-key">Location</div>
                    </div>
                    <div class="meta-item">
                        <div class="meta-value">{int(sqft):,} sq ft</div>
                        <div class="meta-key">Area</div>
                    </div>
                    <div class="meta-item">
                        <div class="meta-value">{bhk} BHK</div>
                        <div class="meta-key">Configuration</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        except requests.exceptions.ConnectionError:
            st.markdown('<div class="error-card">⚠️ Could not reach the prediction server. Make sure it\'s running on port 8000.</div>', unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f'<div class="error-card">⚠️ {str(e)}</div>', unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────
st.markdown('<div class="footer">SmartPrice AI &nbsp;·&nbsp; Powered by Machine Learning</div>', unsafe_allow_html=True)