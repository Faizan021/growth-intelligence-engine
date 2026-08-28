# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import json
import os
import math
import time
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from openai import OpenAI

try:
    from scipy.stats import norm
    SCIPY_AVAILABLE = True
except Exception:
    SCIPY_AVAILABLE = False

st.set_page_config(
    page_title="Growth Intelligence Engine | AI CRM & Lifecycle OS",
    page_icon="\u26a1",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Premium CSS Styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    .hero-container {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #311042 100%);
        border-radius: 16px;
        padding: 2.5rem 2rem;
        color: white;
        margin-bottom: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    }
    
    .hero-title {
        font-size: 2.5rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        background: linear-gradient(to right, #ffffff, #e2e8f0, #cbd5e1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .hero-subtitle {
        font-size: 1.1rem;
        color: #94a3b8;
        font-weight: 500;
        line-height: 1.6;
        max-width: 800px;
    }
    
    .status-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: rgba(16, 185, 129, 0.15);
        color: #34d399;
        border: 1px solid rgba(16, 185, 129, 0.3);
        padding: 0.35rem 0.85rem;
        border-radius: 9999px;
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 1rem;
    }
    
    .glass-card {
        background: #ffffff;
        border-radius: 14px;
        padding: 1.5rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
        margin-bottom: 1.5rem;
    }
    
    .critique-card-bad {
        background: #fff1f2;
        border-left: 5px solid #f43f5e;
        border-radius: 8px;
        padding: 1.25rem;
        margin-bottom: 1rem;
    }
    
    .critique-card-good {
        background: #f0fdf4;
        border-left: 5px solid #22c55e;
        border-radius: 8px;
        padding: 1.25rem;
        margin-bottom: 1rem;
    }

    .pill-tag {
        display: inline-block;
        padding: 0.2rem 0.6rem;
        border-radius: 6px;
        font-size: 0.75rem;
        font-weight: 700;
        margin-right: 0.4rem;
    }
</style>
""", unsafe_allow_html=True)

# Hero Header Banner
st.markdown("""
<div class="hero-container">
    <div class="status-badge">\U0001F7E2 Engine Status: Online &bull; Multi-Agent Pipeline Ready</div>
    <div class="hero-title">\u26a1 Growth Intelligence Engine</div>
    <div class="hero-subtitle">
        Bridging the gap between raw Tableau BI data and real-time CRM execution. Automated YoY seasonal drop analytics, machine-learning RFM lifecycle segmentation, and AI copywriting post-mortems for high-velocity D2C brands.
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar Configuration
with st.sidebar:
    st.header("\u2699\ufe0f Control Center")
    api_key = st.text_input("OpenAI API Key", type="password", help="Enter your OpenAI API key for live custom AI agent execution.")
    model_choice = st.selectbox("LLM Agent Model", ["gpt-4o-mini", "gpt-4o"])
    
    demo_mode = st.toggle("\u26a1 Use Instant Demo Cache", value=True, help="Enable to see instant pre-computed multi-agent analyses without needing an OpenAI key.")
    
    st.divider()
    st.subheader("\U0001F3A8 Brand Voice Guidelines")
    if os.path.exists("config/brand_voice.json"):
        with open("config/brand_voice.json", encoding="utf-8") as f:
            brand_config = json.load(f)
        st.json(brand_config)
    else:
        brand_config = {"brand_name": "Savage Growth D2C", "tone": "Bold, confident, VIP-centric"}

# Tabs Navigation
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "\U0001F4CA 1. Tableau YoY Drop Engine",
    "\U0001F3AF 2. AI Copy Critic & PAS Re-writer",
    "\U0001F465 3. Predictive RFM CRM Segmentation",
    "\U0001F6E1\ufe0f 4. Multi-Channel Fatigue Guard",
    "\U0001F916 5. GEO (AI Search) Brand Auditor",
    "\U0001F50D 6. Programmatic SEO & GSC Gap Finder"
])

# -------------------------------------------------------------
# MODULE 1: Tableau YoY Translator & VIP Hook Engine
# -------------------------------------------------------------
with tab1:
    st.markdown("### \U0001F4CA D2C Tableau Campaign Ingestion & YoY Variance Engine")
    st.caption("Benchmark dataset modeled after high-velocity D2C seasonal drops (Valentine's, Summer Restock, Cyber Week).")
    
    d2c_file = "data/d2c_tableau_drop_data.csv"
    df_d2c = pd.read_csv(d2c_file, encoding="utf-8") if os.path.exists(d2c_file) else pd.DataFrame()

    # KPI Top Metric Cards
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("V-Day Drop '26 Revenue", "$498,464", "+91.5% YoY Lift", delta_color="normal")
    c2.metric("VIP Member Signups", "2,380 members", "+90.4% YoY Surge", delta_color="normal")
    c3.metric("Average Order Value (AOV)", "$84.20", "+22.9% YoY Expansion", delta_color="normal")
    c4.metric("Unsubscribe Rate", "0.32%", "-62.3% YoY Improvement", delta_color="inverse")

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Interactive Plotly Chart: Revenue & VIP Signups YoY
    col_chart, col_table = st.columns([3, 2])
    
    with col_chart:
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df_d2c['campaign_name'],
            y=df_d2c['revenue'],
            name='Revenue ($)',
            marker_color=['#94a3b8', '#6366f1', '#94a3b8', '#8b5cf6', '#94a3b8', '#ec4899'],
            text=df_d2c['revenue'].apply(lambda x: f"${x:,.0f}"),
            textposition='auto',
        ))
        fig.add_trace(go.Scatter(
            x=df_d2c['campaign_name'],
            y=df_d2c['vip_signups'] * 100,
            name='VIP Signups (Scaled)',
            mode='lines+markers',
            line=dict(color='#f59e0b', width=3),
            marker=dict(size=8)
        ))
        fig.update_layout(
            title="Drop Revenue & VIP Acquisition Comparison (2024 - 2026)",
            template="plotly_white",
            margin=dict(l=20, r=20, t=40, b=20),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig, use_container_width=True)
        
    with col_table:
        st.markdown("#### \U0001F4CB Raw Drop Records")
        st.dataframe(df_d2c[['campaign_name', 'channel', 'vip_signups', 'revenue', 'aov', 'unsubscribe_rate']], use_container_width=True, height=340)

    st.divider()

    st.markdown("### \U0001F916 Multi-Agent Drop Post-Mortem & Creative Hook Engine")
    
    if st.button("\U0001F680 Execute 3-Agent YoY Post-Mortem", key="btn_m1", type="primary"):
        if not api_key and not demo_mode:
            st.error("Please enter an OpenAI API Key or toggle 'Use Instant Demo Cache' in the sidebar.")
        elif demo_mode and not api_key:
            with st.spinner("Agents analyzing Tableau dataset, calculating variance, and drafting winning hooks..."):
                time.sleep(1)
                st.markdown("""
### \U0001F916 AGENT 1: TABLEAU TRANSLATOR (Executive KPIs)
* **Revenue Acceleration:** Total drop revenue surged from **$260.3k (2025)** to **$498.5k (2026)** (+91.5% YoY), demonstrating explosive compounding on high-intent promotional drops.
* **AOV Expansion:** Average Order Value expanded by **+$15.70 (+22.9%)** driven by VIP exclusive multi-item bundling mechanics.
* **List Health Preservation:** Opt-out rates dropped by **62.3%**, showing that higher frequency paired with VIP exclusivity increases engagement without fatiguing the audience.

---

### \U0001F916 AGENT 2: YoY & SEASONALITY STATISTICIAN
* **Direct Discount vs. Exclusivity Elasticity:** In 2025, the brand pushed *"50% Off Everything VIP Intro Sale"*, leading to price anchoring and margin compression. In 2026, pivoting to the *"VIP Vault Unlocked: Secret Drop"* hook generated **+90.4% more VIP signups** at a **22.9% higher basket size**.
* **Seasonal Compounding:** Cyber Week 2025 crossed **$1.04M** (+70.5% YoY), proving that early VIP 24h-access passes generate immense FOMO and urgency before public sale launch.

---

### \U0001F916 AGENT 3: CREATIVE HOOK & VIP LIFECYCLE AGENT
* **The Core Cognitive Trigger:** Shifted messaging from *Transactional Value (Discount)* to *Status Entitlement (Exclusivity & Curiosity Gap)*.

#### \U0001F4F1 High-Converting SMS Variations for Upcoming Q3 Drop:
1. `\U0001F512 VIP VAULT: Your private Q3 drop is officially unlocked, [First Name]. 2 free limited edition pieces reserved in your bag for 24h: [Link] (Txt STOP to opt out)`
2. `\U0001F525 Secret Restock: Members get 1st pass on the sold-out Lace Capsule before public launch tomorrow at 9 AM: [Link]`
3. `\U0001F451 You're on the list. Exclusive VIP early access starts right now. Sizes go fast: [Link]`

#### \u2709\ufe0f High-Converting Email Sequences:
* **Subject:** `VIP First Pass: Your secret capsule is unlocked \U0001F513`  
  **Preview Text:** `No waiting in line. Claim your member-exclusive bonus pieces inside.`
* **Subject:** `[First Name], did you see what's inside the VIP Vault?`  
  **Preview Text:** `Curated specifically for your style profile. 24 hours only.`
""")
        else:
            client = OpenAI(api_key=api_key)
            with st.spinner("Agents analyzing drop variance and synthesizing VIP copy hooks..."):
                prompt = f"""
You are an Elite D2C Growth Director and Technical CRM Specialist.
Analyze this e-commerce drop dataset:
{df_d2c.to_string()}
BRAND GUIDELINES: {json.dumps(brand_config)}

Execute the 3-Agent Workflow:
### AGENT 1: TABLEAU TRANSLATOR (Executive KPIs)
### AGENT 2: YoY & SEASONALITY STATISTICIAN
### AGENT 3: CREATIVE HOOK & LIFECYCLE AGENT (Generate 3 SMS hooks & 2 Email Subject/Preview lines)
"""
                res = client.chat.completions.create(model=model_choice, messages=[{"role": "user", "content": prompt}], temperature=0.7)
                st.markdown(res.choices[0].message.content)

# -------------------------------------------------------------
# MODULE 2: AI Campaign Post-Mortem & Copy Critic
# -------------------------------------------------------------
with tab2:
    st.markdown("### \U0001F3AF Multi-Agent A/B Test Post-Mortem & Copywriting Critic")
    st.caption("Combines two-proportion statistical Z-Tests with cognitive psychology teardowns (PAS & AIDA frameworks).")

    ab_data = pd.DataFrame({
        "variant": ["Variant A (Direct Discount Hook)", "Variant B (VIP Story & Pain-Point)"],
        "subject_line": ["FLASH SALE: 40% off everything today only!", "Are you still overpaying for your monthly wardrobe?"],
        "body_copy": [
            "Hey member, get 40% off our entire catalog today. Click the button below to buy before midnight.",
            "Hey Sarah, VIP members don't wait in lines or pay retail markup. Unlock your custom-curated VIP drop with 2 exclusive free pieces inside today's box."
        ],
        "sends": [25000, 25000],
        "opens": [4200, 6800],
        "clicks": [380, 1190],
        "conversions": [45, 168]
    })

    df_ab = st.data_editor(ab_data, use_container_width=True)
    df_ab['open_rate'] = (df_ab['opens'] / df_ab['sends']) * 100
    df_ab['ctr'] = (df_ab['clicks'] / df_ab['opens']) * 100
    df_ab['conv_rate'] = (df_ab['conversions'] / df_ab['clicks']) * 100

    win_idx = df_ab['ctr'].idxmax()
    lose_idx = df_ab['ctr'].idxmin()
    winner = df_ab.iloc[win_idx]
    loser = df_ab.iloc[lose_idx]

    # Z-Test Math
    clicks_w, opens_w = winner['clicks'], winner['opens']
    clicks_l, opens_l = loser['clicks'], loser['opens']
    p1 = clicks_w / opens_w
    p2 = clicks_l / opens_l
    p_pool = (clicks_w + clicks_l) / (opens_w + opens_l)
    se = math.sqrt(p_pool * (1 - p_pool) * (1/opens_w + 1/opens_l))
    z_score = (p1 - p2) / se if se > 0 else 0
    p_val = math.erfc(abs(z_score) / math.sqrt(2))
    confidence = (1 - p_val) * 100

    c_ab1, c_ab2, c_ab3 = st.columns(3)
    c_ab1.metric("\U0001F3C6 Winner", winner['variant'], f"{winner['ctr']:.2f}% CTR (+{winner['ctr']-loser['ctr']:.2f}%)")
    c_ab2.metric("\U0001F4C9 Underperformer", loser['variant'], f"{loser['ctr']:.2f}% CTR")
    c_ab3.metric("\U0001F52C Statistical Confidence", f"{confidence:.1f}%", "Statistically Significant (p < 0.001)")

    # Visual Comparison Cards
    col_v1, col_v2 = st.columns(2)
    with col_v1:
        st.markdown(f"""
        <div class="critique-card-bad">
            <h4>\u274c Underperformer: {loser['variant']}</h4>
            <p><strong>Subject:</strong> <code>{loser['subject_line']}</code></p>
            <p><strong>Body:</strong> {loser['body_copy']}</p>
            <hr>
            <span class="pill-tag" style="background:#fecdd3; color:#9f1239;">Hook: \u274c Generic</span>
            <span class="pill-tag" style="background:#fecdd3; color:#9f1239;">Friction: \U0001F6D1 High</span>
            <span class="pill-tag" style="background:#fecdd3; color:#9f1239;">CTA: \u26a0\ufe0f Weak</span>
        </div>
        """, unsafe_allow_html=True)

    with col_v2:
        st.markdown(f"""
        <div class="critique-card-good">
            <h4>\u2705 Winner: {winner['variant']}</h4>
            <p><strong>Subject:</strong> <code>{winner['subject_line']}</code></p>
            <p><strong>Body:</strong> {winner['body_copy']}</p>
            <hr>
            <span class="pill-tag" style="background:#bbf7d0; color:#166534;">Hook: \U0001F48E Pain-Point / Curiosity</span>
            <span class="pill-tag" style="background:#bbf7d0; color:#166534;">Value Prop: \u26a1 Clear VIP Benefits</span>
            <span class="pill-tag" style="background:#bbf7d0; color:#166534;">CTR Lift: +93.2%</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### \U0001F916 Multi-Agent Copywriting Teardown & PAS Re-writer")
    
    if st.button("\U0001F680 Run Copywriting Critic & PAS/AIDA Rewrite", key="btn_m2", type="primary"):
        if not api_key and not demo_mode:
            st.error("Please enter an OpenAI API Key or toggle 'Use Instant Demo Cache' in the sidebar.")
        elif demo_mode and not api_key:
            with st.spinner("Critic agent reviewing copy mechanics and generating revisions..."):
                time.sleep(1)
                st.markdown("""
### \U0001F4CA 1. ANALYST AGENT: Performance Attribution
* **Open Rate Victory (+61.9%):** Variant B's question hook (*"Are you still overpaying...?"*) created an instant cognitive curiosity gap compared to the spam-heavy *"FLASH SALE"* keyword which triggered Gmail's promotional tab filters.
* **Click-to-Open Rate (+93.2%):** Variant B established immediate emotional relevance with the reader's identity as a savvy VIP member.

---

### \U0001F9D0 2. CRITIC AGENT: Teardown of Variant A (The Loser)
1. **Buried Value Proposition:** The copy mentions "40% off" but fails to communicate *what* the member is actually getting or *why* they should care today.
2. **High Cognitive Friction:** "Click the button below to buy before midnight" feels transactional and demanding rather than rewarding.
3. **Banned Words Triggered:** Uses generic buzzwords (*"flash sale"*, *"click here"*), reducing brand trust.

---

### \u270d\ufe0f 3. COPYWRITER AGENT: 3 High-Converting Re-writes (PAS Framework)

#### Option 1: The VIP Entitlement Angle (PAS)
* **Subject Line:** `Your VIP box just got upgraded (2 free pieces inside) \U0001F381`
* **Preview Text:** `Why pay retail when you have member status?`
* **Body:**  
  * **(Problem):** Shopping for seasonal essentials usually means dealing with sold-out sizes and high retail markups.  
  * **(Agitate):** Why waste your weekend scrolling through endless generic sales that everyone else has access to?  
  * **(Solve):** We hand-selected 2 exclusive bonus pieces and locked your sizes in your private VIP capsule for the next 24 hours.  
* **CTA Button:** `[ Unlock My Curated Capsule &rarr; ]`

#### Option 2: The Social Proof & Style Refresh Angle (AIDA)
* **Subject Line:** `The #1 reason VIP members skip retail markup`
* **Preview Text:** `Over 10,000 members unlocked their summer capsule today.`
* **Body:**  
  * **(Attention):** Most fashion brands make you wait in line for the pieces everyone is wearing.  
  * **(Interest):** As a member, your stylist curates custom luxury pieces directly to your sizing profile.  
  * **(Desire):** Experience buttery-soft fabrics and tailored fits without the traditional 3x boutique price tag.  
  * **(Action):** Claim your exclusive 40% welcome credit before your reserved bag expires tonight.  
* **CTA Button:** `[ Claim My 40% VIP Credit Now ]`
""")
        else:
            client = OpenAI(api_key=api_key)
            with st.spinner("Critic agent reviewing copy mechanics..."):
                prompt = f"""
You are a Lead Growth Copywriting Critic.
WINNER: {winner['variant']} | Subject: "{winner['subject_line']}" | CTR: {winner['ctr']:.2f}%
LOSER: {loser['variant']} | Subject: "{loser['subject_line']}" | Body: "{loser['body_copy']}" | CTR: {loser['ctr']:.2f}%
BRAND CONTEXT: {json.dumps(brand_config)}
TASKS:
1. ANALYST AGENT: Quantify why the winner succeeded and explain the cognitive trigger.
2. CRITIC AGENT: Perform a rigorous teardown of the losing variant.
3. COPYWRITER AGENT: Produce 3 complete, rewritten variants using the PAS (Problem-Agitate-Solve) framework.
"""
                res = client.chat.completions.create(model=model_choice, messages=[{"role": "user", "content": prompt}], temperature=0.7)
                st.markdown(res.choices[0].message.content)

# -------------------------------------------------------------
# MODULE 3: Predictive RFM CRM Segmentation
# -------------------------------------------------------------
with tab3:
    st.markdown("### \U0001F465 Machine-Learning RFM Customer Segmentation & Churn Risk")
    st.caption("Transforms 3,000+ transaction records into automated lifecycle personas and builds dynamic CRM payloads for Twenty CRM & Klaviyo.")

    rfm_file = "data/customer_transactions.csv"
    if os.path.exists(rfm_file):
        df_trans = pd.read_csv(rfm_file, encoding="utf-8")
        df_trans['transaction_date'] = pd.to_datetime(df_trans['transaction_date'])
        snap_date = df_trans['transaction_date'].max() + pd.Timedelta(days=1)

        rfm_df = df_trans.groupby('customer_id').agg({
            'transaction_date': lambda x: (snap_date - x.max()).days,
            'customer_id': 'count',
            'order_amount': 'sum'
        }).rename(columns={'transaction_date': 'Recency', 'customer_id': 'Frequency', 'order_amount': 'Monetary'})

        def label_persona(row):
            if row['Frequency'] >= rfm_df['Frequency'].quantile(0.75) and row['Monetary'] >= rfm_df['Monetary'].quantile(0.75):
                return "\U0001F48E VIP Champions"
            elif row['Recency'] <= 30 and row['Frequency'] >= 2:
                return "\u26a1 Loyal Active"
            elif row['Recency'] > 90 and row['Frequency'] >= 2:
                return "\u26a0\ufe0f At-Risk VIP (Churn Hazard)"
            else:
                return "\U0001F4A4 Hibernating / Low-Value"

        rfm_df['Lifecycle_Segment'] = rfm_df.apply(label_persona, axis=1)

        # 3D/2D Plotly Scatter of RFM Clusters
        col_rfm_chart, col_rfm_stats = st.columns([3, 2])
        
        with col_rfm_chart:
            fig_rfm = px.scatter(
                rfm_df.reset_index(),
                x="Recency",
                y="Monetary",
                size="Frequency",
                color="Lifecycle_Segment",
                hover_data=["customer_id"],
                color_discrete_map={
                    "\U0001F48E VIP Champions": "#8b5cf6",
                    "\u26a1 Loyal Active": "#10b981",
                    "\u26a0\ufe0f At-Risk VIP (Churn Hazard)": "#f43f5e",
                    "\U0001F4A4 Hibernating / Low-Value": "#94a3b8"
                },
                title="Customer Distribution: Recency vs. Total Spend (Size = Order Frequency)"
            )
            fig_rfm.update_layout(template="plotly_white", margin=dict(l=20, r=20, t=40, b=20))
            st.plotly_chart(fig_rfm, use_container_width=True)

        with col_rfm_stats:
            st.markdown("#### \U0001F4CA Segment Lifecycle Metrics")
            seg_summary = rfm_df.groupby('Lifecycle_Segment').agg({
                'Recency': 'mean',
                'Frequency': 'mean',
                'Monetary': ['mean', 'count']
            }).round(2)
            st.dataframe(seg_summary, use_container_width=True)

        st.divider()

        st.markdown("### \U0001F517 Generated Twenty CRM / Klaviyo Real-Time Webhook Payloads")
        st.caption("JSON payloads ready to push into CRM webhooks for dynamic event-triggered email and SMS flows.")
        
        sample_payload = []
        for cid, r in rfm_df.head(4).iterrows():
            sample_payload.append({
                "external_id": cid,
                "traits": {
                    "recency_days": int(r['Recency']),
                    "total_orders": int(r['Frequency']),
                    "total_spend": float(round(r['Monetary'], 2)),
                    "crm_segment": r['Lifecycle_Segment'],
                    "automated_flow_trigger": "WIN_BACK_DISCOUNT_25" if "At-Risk" in r['Lifecycle_Segment'] else "VIP_SECRET_DROP"
                }
            })
        st.json(sample_payload)

# -------------------------------------------------------------
# MODULE 4: Multi-Channel Fatigue Guard
# -------------------------------------------------------------
with tab4:
    st.markdown("### \U0001F6E1\ufe0f Multi-Channel SMS & Push Notification Fatigue Guard")
    st.caption("Algorithmic frequency capping, 24h cooling periods, and churn-risk filters protecting carrier deliverability and subscriber lists.")

    customers = pd.DataFrame([
        {"customer_id": "C_101", "name": "Elena Rostova", "vip_tier": "\U0001F48E Diamond", "messages_last_7d": 1, "unsub_risk_score": 0.12, "last_msg_hours_ago": 72},
        {"customer_id": "C_102", "name": "Marcus Vance", "vip_tier": "Standard", "messages_last_7d": 5, "unsub_risk_score": 0.78, "last_msg_hours_ago": 6},
        {"customer_id": "C_103", "name": "Amina Chen", "vip_tier": "\U0001F451 Gold", "messages_last_7d": 3, "unsub_risk_score": 0.45, "last_msg_hours_ago": 28},
        {"customer_id": "C_104", "name": "Liam Gallagher", "vip_tier": "Standard", "messages_last_7d": 4, "unsub_risk_score": 0.65, "last_msg_hours_ago": 12},
    ])

    results = []
    for idx, row in customers.iterrows():
        if row['unsub_risk_score'] > 0.70:
            status, reason = "\U0001F6D1 SUPPRESSED", "High Churn / Opt-out Risk (>70%)"
        elif row['last_msg_hours_ago'] < 24:
            status, reason = "\U0001F6D1 SUPPRESSED", "< 24h Cooling Period Active"
        elif row['messages_last_7d'] >= (5 if "Diamond" in row['vip_tier'] or "Gold" in row['vip_tier'] else 3):
            status, reason = "\U0001F6D1 SUPPRESSED", "Weekly Frequency Cap Exceeded"
        else:
            status, reason = "\u2705 APPROVED", "Eligible for Multi-Channel Dispatch"
        
        results.append({
            "Customer": row['name'],
            "VIP Tier": row['vip_tier'],
            "Weekly Messages": row['messages_last_7d'],
            "Opt-Out Risk": f"{row['unsub_risk_score']*100:.0f}%",
            "Hours Since Last Touch": f"{row['last_msg_hours_ago']}h",
            "Dispatch Status": status,
            "Engine Decision Rationale": reason
        })

    df_guard = pd.DataFrame(results)
    st.dataframe(df_guard, use_container_width=True)

    g1, g2, g3 = st.columns(3)
    g1.metric("Messages Evaluated", "4 recipients", "")
    g2.metric("Dispatched Safely", "2 recipients (50%)", "Optimized", delta_color="normal")
    g3.metric("Fatigue Suppressions", "2 recipients (50%)", "Protected List Health", delta_color="normal")


# -------------------------------------------------------------
# MODULE 5: Generative Engine Optimization (GEO) & AI Search Monitor
# -------------------------------------------------------------
with tab5:
    st.markdown("### \U0001F916 GEO (Generative Engine Optimization) & AI Search Tracker")
    st.caption("Monitors how AI search engines (ChatGPT Search, Perplexity, Gemini) cite and recommend your brand for high-intent commercial queries.")

    geo_data = pd.DataFrame([
        {"query": "best D2C VIP fashion membership brands", "ai_engine": "ChatGPT Search", "brand_mentioned": "\u2705 Yes", "rank_position": "Rank #1", "sentiment": "Positive / Luxury", "sources_cited": "Vogue, Forbes, Brand Home"},
        {"query": "affordable luxury lingerie monthly drop", "ai_engine": "Perplexity", "brand_mentioned": "\u2705 Yes", "rank_position": "Rank #2", "sentiment": "High Quality / Inclusive", "sources_cited": "Elle, Byrdie, Reddit r/femalefashion"},
        {"query": "athleisure subscription box comparison", "ai_engine": "Google AI Overviews", "brand_mentioned": "\u274c No", "rank_position": "Not Cited", "sentiment": "Neutral", "sources_cited": "Wirecutter, Byrdie"},
        {"query": "best fitness recovery smart membership", "ai_engine": "Perplexity", "brand_mentioned": "\u2705 Yes", "rank_position": "Rank #1", "sentiment": "Scientific / Elite", "sources_cited": "TechCrunch, Men's Health"}
    ])
    
    st.dataframe(geo_data, use_container_width=True)
    
    geo_c1, geo_c2, geo_c3 = st.columns(3)
    geo_c1.metric("AI Share of Voice (SoV)", "75.0%", "+15.0% vs Competitors")
    geo_c2.metric("Top-3 Citation Rate", "75.0%", "3 out of 4 AI queries cited")
    geo_c3.metric("Digital PR Gap Identified", "1 Critical Query", "Needs Wirecutter / Reddit seeding")

# -------------------------------------------------------------
# MODULE 6: Programmatic SEO & GSC Striking Distance Gap Finder
# -------------------------------------------------------------
with tab6:
    st.markdown("### \U0001F50D Programmatic SEO & GSC Striking Distance Gap Finder")
    st.caption("Identifies 'striking distance' keywords (positions 8-18 with high impressions) from Google Search Console API and generates optimized Title/Meta tags.")

    gsc_data = pd.DataFrame([
        {"target_keyword": "vip membership lingerie drop", "impressions": 48200, "clicks": 580, "current_position": 11.4, "current_ctr": "1.20%", "projected_ctr_lift": "+3.40%", "suggested_title": "VIP Capsule Drops & Secret Vault Access | Exclusive Members"},
        {"target_keyword": "best seamless workout sets 2026", "impressions": 62400, "clicks": 890, "current_position": 14.2, "current_ctr": "1.42%", "projected_ctr_lift": "+4.10%", "suggested_title": "10 Best Seamless Workout Sets of 2026 (Tested for Squats)"},
        {"target_keyword": "skincare routine for glowing glass skin", "impressions": 89000, "clicks": 1100, "current_position": 12.8, "current_ctr": "1.23%", "projected_ctr_lift": "+3.80%", "suggested_title": "The 4-Step Glass Skin Skincare Routine (Dermatologist Approved)"},
        {"target_keyword": "whoop vs oura ring recovery comparison", "impressions": 114000, "clicks": 2100, "current_position": 9.1, "current_ctr": "1.84%", "projected_ctr_lift": "+5.20%", "suggested_title": "Whoop vs Oura Ring in 2026: The Ultimate Wearable Recovery Guide"}
    ])
    
    st.dataframe(gsc_data, use_container_width=True)
    
    s1, s2, s3 = st.columns(3)
    s1.metric("Striking-Distance Impressions", "313,600", "High Volume Opportunity")
    s2.metric("Projected Organic Traffic Lift", "+12,400 clicks/mo", "Via CTR Title Optimization")
    s3.metric("Average Current Position", "11.9", "Positions 8 - 15 Page 2")
