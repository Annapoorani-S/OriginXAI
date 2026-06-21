import streamlit as st
import ai_engine
from prompts import (
    BRANDING_PROMPT,
    MARKET_PROMPT,
    COMPETITOR_PROMPT,
    DECISION_PROMPT
)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="OriginX AI",
    page_icon="🌍",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main {
    background-color: #F7F8FC;
}

/* Title */
.title {
    font-size: 42px;
    font-weight: 800;
    color: #6C5CE7;
}

.subtitle {
    font-size: 18px;
    color: #444;
    margin-bottom: 20px;
}

/* Card */
.card {
    background: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.08);
    margin-bottom: 15px;

    /* FIX TEXT VISIBILITY */
    color: #111 !important;
    font-size: 15px;
    line-height: 1.6;
}

/* Button */
.stButton>button {
    background-color: #6C5CE7;
    color: white;
    padding: 0.6rem 1.2rem;
    border-radius: 8px;
    border: none;
    font-weight: 600;
}

.stButton>button:hover {
    background-color: #00D2D3;
    color: black;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<div class="title">🌍 OriginX AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI Product Intelligence & Global Decision Engine</div>', unsafe_allow_html=True)

st.markdown("---")

# ---------------- INPUT SECTION ----------------
with st.container():
    st.markdown("### 📦 Product Details")

    col1, col2 = st.columns(2)

    with col1:
        product = st.text_input("Product Name")

    with col2:
        country = st.text_input("Target Country")

    description = st.text_area("Product Description", height=120)

    generate = st.button("🚀 Analyze Product", use_container_width=True)

st.markdown("---")

# ---------------- OUTPUT ----------------
if generate:

    if not product or not description or not country:
        st.warning("Please fill all fields before generating insights.")
        st.stop()

    tab1, tab2, tab3, tab4 = st.tabs([
        "🧠 Brand Strategy",
        "📊 Market Analysis",
        "⚔️ Competitor Analysis",
        "📈 Decision Engine"
    ])

    # ---------------- BRAND ----------------
    with tab1:
        with st.spinner("Generating brand strategy..."):
            prompt = BRANDING_PROMPT.format(
                product=product,
                description=description,
                country=country
            )
            result = ai_engine.generate_response(prompt)

            st.markdown(
                f"<div class='card'><pre style='white-space: pre-wrap;'>{result}</pre></div>",
                unsafe_allow_html=True
            )

    # ---------------- MARKET ----------------
    with tab2:
        with st.spinner("Analyzing market..."):
            prompt = MARKET_PROMPT.format(
                product=product,
                description=description,
                country=country
            )
            result = ai_engine.generate_response(prompt)

            st.markdown(
                f"<div class='card'><pre style='white-space: pre-wrap;'>{result}</pre></div>",
                unsafe_allow_html=True
            )

    # ---------------- COMPETITOR ----------------
    with tab3:
        with st.spinner("Analyzing competitors..."):
            prompt = COMPETITOR_PROMPT.format(
                product=product,
                description=description,
                country=country
            )
            result = ai_engine.generate_response(prompt)

            st.markdown(
                f"<div class='card'><pre style='white-space: pre-wrap;'>{result}</pre></div>",
                unsafe_allow_html=True
            )

    # ---------------- DECISION ENGINE ----------------
    with tab4:
        with st.spinner("Calculating decision score..."):
            prompt = DECISION_PROMPT.format(
                product=product,
                description=description,
                country=country
            )
            result = ai_engine.generate_response(prompt)

            st.markdown(
                f"<div class='card'><pre style='white-space: pre-wrap;'>{result}</pre></div>",
                unsafe_allow_html=True
            )