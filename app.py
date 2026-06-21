import streamlit as st
import ai_engine

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="OriginX AI",
    page_icon="🚀",
    layout="wide"
)

# ---------------- CLEAN SAAS STYLING ----------------
st.markdown("""
<style>
    /* Background */
    .stApp {
        background-color: #0b1220;
        color: #e5e7eb;
    }

    /* Title */
    h1 {
        color: #60a5fa !important;
        font-size: 42px !important;
        font-weight: 700;
    }

    /* Subtext */
    .stCaption {
        color: #94a3b8;
    }

    /* Input boxes */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background-color: #111827;
        color: white;
        border-radius: 10px;
        border: 1px solid #1f2937;
    }

    /* Button */
    .stButton > button {
        background: linear-gradient(90deg, #3b82f6, #8b5cf6);
        color: white;
        border: none;
        padding: 0.6rem 1.2rem;
        border-radius: 10px;
        font-weight: 600;
    }

    .stButton > button:hover {
        transform: scale(1.02);
        transition: 0.2s;
    }

    /* Card-like container */
    .card {
        background-color: #111827;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #1f2937;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("🚀 OriginX AI")
st.caption("Startup Intelligence Engine — Validate ideas like an investor")

st.markdown("---")

# ---------------- INPUT SECTION ----------------
col1, col2 = st.columns(2)

with col1:
    product = st.text_input("📦 Product Name")

with col2:
    country = st.text_input("🌍 Target Country")

description = st.text_area("🧠 Product Description")

# ---------------- PROMPT ----------------
MASTER_PROMPT = """
You are OriginX AI — a startup intelligence engine used by founders and investors.

Analyze deeply like a venture capitalist.

Product: {product}
Description: {description}
Country: {country}

Return structured output:

BRANDING:
- Brand Name
- Tagline
- Positioning
- Target Audience
- Emotional Strategy

MARKET:
- Demand Level
- Trends
- Growth Potential
- Pain Points

COMPETITOR:
- Top competitors
- Weaknesses
- Market gap
- Advantage strategy

DECISION:
- Score (0–100)
- Profit Potential
- Risk Level
- Final Verdict (GO / NO-GO / TEST)
- Investor Summary
"""

# ---------------- ANALYZE ----------------
st.markdown("")

if st.button("🚀 Analyze Idea"):

    if not product or not description or not country:
        st.warning("Please fill all fields")
        st.stop()

    prompt = MASTER_PROMPT.format(
        product=product,
        description=description,
        country=country
    )

    with st.spinner("Analyzing market intelligence..."):
        result = ai_engine.generate_response(prompt)

    # ---------------- OUTPUT ----------------
    st.markdown("## 📊 Intelligence Report")

    st.markdown("---")

    st.markdown(
        f"""
        <div class="card">
            {result}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.caption("OriginX AI • SaaS MVP • Built for startup validation")
