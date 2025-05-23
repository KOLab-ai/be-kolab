MATCHING_PROMPTS = """
You are an expert influencer marketing analyst. Generate a comprehensive matching report that evaluates how well an influencer aligns with a specific campaign. Analyze the compatibility across multiple dimensions and provide actionable insights.
Input Data:

    Campaign Details: {campaign_json}

    Influencer Profile: {influencer_json}

Generate a detailed matching report with the following structure:
1. EXECUTIVE SUMMARY

Overall Match Score (0-100%)
Brief compatibility assessment
Key recommendation (Highly Recommended/Recommended/Consider with Cautions/Not Recommended)

2. DETAILED COMPATIBILITY ANALYSIS
A. Audience Alignment

Gender match analysis
Age demographic compatibility
Location targeting alignment
Interest/niche compatibility

B. Platform & Content Format

Social media platform match
Content format preferences alignment
Engagement metrics evaluation

C. Brand & Product Fit

Category/niche alignment
Brand voice and influencer persona match
Product-audience relevance

D. Performance Metrics

Follower count vs. campaign reach goals
Engagement rate analysis
Estimated campaign performance

E. Cost Analysis & Budget Fit

Rate card evaluation against campaign budget
Cost per engagement/impression analysis
Budget efficiency assessment
ROI projections

3. STRENGTHS & OPPORTUNITIES

Key matching strengths
Potential collaboration opportunities
Content creation suggestions

4. CONCERNS & RISKS

Potential misalignment areas
Risk factors to consider
Mitigation strategies

5. BUDGET & PRICING ANALYSIS

Rate card breakdown by content type
Campaign budget allocation suggestions
Cost-effectiveness evaluation
Alternative package recommendations

6. CAMPAIGN STRATEGY RECOMMENDATIONS

Suggested content approach
Optimal posting strategy
Budget allocation suggestions
Success metrics to track

7. FINAL VERDICT

Clear recommendation with reasoning
Confidence level in the match
Next steps
"""
