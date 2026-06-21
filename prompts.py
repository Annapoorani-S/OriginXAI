BRANDING_PROMPT = """
You are a global branding expert.

Product:
{product}

Description:
{description}

Target Country:
{country}

Generate:

1. Brand Name
2. Tagline
3. Brand Story
4. Target Audience
5. Positioning Statement
6. 10 Marketing Ideas

Format clearly in markdown.
"""


MARKET_PROMPT = """
You are a market research analyst.

Product:
{product}

Description:
{description}

Target Country:
{country}

Generate:

1. Market Potential Score (1-10)
2. Demand Trend
3. Customer Segments
4. Opportunities
5. Risks
6. Pricing Suggestion

Format clearly in markdown.
"""


COMPETITOR_PROMPT = """
You are a competitive intelligence expert.

Product:
{product}

Description:
{description}

Target Country:
{country}

Generate:

1. Main Competitors
2. Their Strengths
3. Their Weaknesses
4. Market Gaps
5. Differentiation Strategy

Format clearly in markdown.
"""


DECISION_PROMPT = """
You are a startup investment and export decision expert.

Analyze the product and give a structured decision report.

Product:
{product}

Description:
{description}

Target Country:
{country}

Return STRICTLY in this format:

# Market Score (0-100)
# Demand Level (Low / Medium / High)
# Competition Level (Low / Medium / High)
# Export Difficulty (Low / Medium / High)
# Profit Potential (Low / Medium / High)

# Recommendation
(Should the user proceed or avoid this product?)

# Key Risks
- Risk 1
- Risk 2
- Risk 3

# Top 3 Improvement Suggestions
- Point 1
- Point 2
- Point 3
"""