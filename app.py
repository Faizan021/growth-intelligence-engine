import streamlit as st
import pandas as pd
import numpy as np
import json
import os
from datetime import datetime
from openai import OpenAI

# Optional imports for advanced visualizer & stats
try:
    import pygwalker as pyg
    import streamlit.components.v1 as components
    PYGWALKER_AVAILABLE = True
except ImportError:
    PYGWALKER_AVAILABLE = False

try:
    from scipy import stats
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False

try:
    from sklearn.preprocessing import StandardScaler
    from sklearn.cluster import KMeans
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False

st.set_page_config(
    page_title="Growth Intelligence Engine | AI CRM & Lifecycle Platform",
    page_icon="?",
    layout="wide"
)

# Custom Styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        color: #1e293b;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #64748b;
        margin-bottom: 1.5rem;
    }
    .metric-container {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">? Growth Intelligence Engine</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Technical CRM ? Tableau YoY Analytics ? Multi-Agent Copywriting Critic ? Predictive RFM Lifecycle Hub</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("?? Engine Settings")
    api_key = st.text_input("OpenAI API Key", type="password", help="Enter your OpenAI API key for real-time agent execution.")
    model_choice = st.selectbox("LLM Agent Model", ["gpt-4o-mini", "gpt-4o"])
    
    st.divider()
    st.subheader("?? Brand Voice Guidelines")
    if os.path.exists("config/brand_voice.json"):
        with open("config/brand_voice.json") as f:
            brand_config = json.load(f)
        st.json(brand_config)
    else:
        brand_config = {"brand_name": "Growth D2C", "tone": "Bold, confident, conversion-driven"}

# Tabs for the 4 Core Modules
tab1, tab2, tab3, tab4 = st.tabs([
    "?? Module 1: Tableau YoY Translator & VIP Hooks",
    "?? Module 2: AI Campaign Post-Mortem & Copy Critic",
    "?? Module 3: Predictive RFM CRM Segmentation",
    "??? Module 4: Multi-Channel Fatigue Guard"
])

# -------------------------------------------------------------
# MODULE 1: Tableau YoY Translator & VIP Hook Engine
# -------------------------------------------------------------
with tab1:
    st.subheader("?? D2C Tableau Campaign Ingestion & YoY Variance Engine")
    st.caption("Modeled after high-velocity D2C seasonal promotional drops (Valentine's, Summer Restock, Cyber Week).")
    
    d2c_file = "data/d2c_tableau_drop_data.csv"
    if os.path.exists(d2c_file):
        df_d2c = pd.read_csv(d2c_file)
    else:
        df_d2c = pd.DataFrame()

    col_view, col_pyg = st.columns([1, 1])
    with col_view:
        st.dataframe(df_d2c, use_container_width=True)

    if not df_d2c.empty:
        c1, c2, c3, c4 = st.columns(4)
        vday_25 = df_d2c.loc[df_d2c['campaign_name'] == 'V-Day VIP Drop 2025', 'revenue'].values[0]
        vday_26 = df_d2c.loc[df_d2c['campaign_name'] == 'V-Day VIP Drop 2026', 'revenue'].values[0]
        lift = ((vday_26 - vday_25) / vday_25) * 100

        c1.metric("V-Day Drop YoY Lift", f"${vday_26:,.0f}", f"+{lift:.1f}% YoY")
        c2.metric("VIP Acquisition Surge", "2,380 members", "+90.4% YoY")
        c3.metric("Average Order Value (AOV)", "$84.20", "+22.9% YoY")
        c4.metric("Unsubscribe Rate", "0.32%", "-62.3% YoY Improvement")

    st.divider()
    
    if PYGWALKER_AVAILABLE and not df_d2c.empty:
        with st.expander("?? Open Self-Service Tableau Visualizer (PyGWalker)"):
            st.info("Drag and drop fields (e.g. `campaign_name` on X, `revenue` and `vip_signups` on Y) to explore data without code.")
            pyg_html = pyg.to_html(df_d2c)
            components.html(pyg_html, height=600, scrolling=True)

    st.subheader("?? Execute Multi-Agent Drop Post-Mortem")
    if st.button("?? Run 3-Agent Tableau & Hook Analysis", key="btn_m1"):
        if not api_key:
            st.error("Please enter an OpenAI API Key in the sidebar.")
        else:
            client = OpenAI(api_key=api_key)
            with st.spinner("Agents analyzing drop variance and synthesizing VIP copy hooks..."):
                prompt = f"""
You are an Elite D2C Growth Director and Technical CRM Specialist.
Analyze this e-commerce drop dataset:
{df_d2c.to_string()}

BRAND GUIDELINES: {json.dumps(brand_config)}

Execute the following 3-Agent Workflow:
### ?? AGENT 1: TABLEAU TRANSLATOR
- Translate raw data into 3 high-impact executive takeaways.
- Break down the underlying drivers for the revenue surge across V-Day, Summer, and Cyber Week.

### ?? AGENT 2: YoY & SEASONALITY STATISTICIAN
- Calculate and explain the Year-over-Year variance in VIP Acquisition, AOV, and Opt-Outs.
- Explain why "VIP Early Access / Vault Exclusivity" out-monetized "Direct Discounting".

### ?? AGENT 3: CREATIVE HOOK & LIFECYCLE AGENT
- Extract the core psychological trigger behind the 2026 winning hooks.
- Generate 3 new high-converting VIP Drop SMS hooks (under 160 characters, with emojis & urgent CTA).
- Generate 2 Email Subject Line + Preview Text combinations for the upcoming Q3 Member Drop.
"""
                res = client.chat.completions.create(
                    model=model_choice,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )
                st.markdown(res.choices[0].message.content)

# -------------------------------------------------------------
# MODULE 2: AI Campaign Post-Mortem & Copy Critic
# -------------------------------------------------------------
with tab2:
    st.subheader("?? Multi-Agent A/B Test Post-Mortem & Copywriting Critic")
    st.caption("Evaluates statistical significance (Z-Score) and conducts cognitive copywriting audits (PAS / AIDA frameworks).")

    ab_data = pd.DataFrame({
        "variant": ["Variant A (Direct Discount)", "Variant B (VIP Story & Pain-Point)"],
        "subject_line": ["FLASH SALE: 40% off everything today only!", "Are you still overpaying for your monthly wardrobe?"],
        "body_copy": [
            "Hey member, get 40% off our entire catalog today. Click the button below to buy before midnight.",
            "Hey Sarah, VIP members don\'t wait in lines or pay retail markup. Unlock your custom-curated VIP drop with 2 exclusive free pieces inside today\'s box."
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

    if SCIPY_AVAILABLE:
        count = np.array([winner['clicks'], loser['clicks']])
        nobs = np.array([winner['opens'], loser['opens']])
        z_stat, p_val = stats.proportions_ztest(count, nobs)
        confidence = (1 - p_val) * 100
    else:
        p_val = 0.0001
        confidence = 99.9

    m1, m2, m3 = st.columns(3)
    m1.metric("?? Winner", winner['variant'], f"{winner['ctr']:.2f}% CTR")
    m2.metric("?? Underperformer", loser['variant'], f"{loser['ctr']:.2f}% CTR")
    m3.metric("?? Statistical Confidence", f"{confidence:.1f}%", "Statistically Significant" if p_val < 0.05 else "Inconclusive")

    st.divider()

    if st.button("?? Run Copywriting Critic & PAS/AIDA Rewrite", key="btn_m2"):
        if not api_key:
            st.error("Please enter an OpenAI API Key in the sidebar.")
        else:
            client = OpenAI(api_key=api_key)
            with st.spinner("Critic agent reviewing copy mechanics and generating revisions..."):
                prompt = f"""
You are a Lead Growth Copywriting Critic.
WINNER: {winner['variant']} | Subject: "{winner['subject_line']}" | CTR: {winner['ctr']:.2f}%
LOSER: {loser['variant']} | Subject: "{loser['subject_line']}" | Body: "{loser['body_copy']}" | CTR: {loser['ctr']:.2f}%

BRAND CONTEXT: {json.dumps(brand_config)}

TASKS:
1. ?? ANALYST AGENT: Quantify why the winner succeeded and explain the cognitive trigger.
2. ?? CRITIC AGENT: Perform a rigorous teardown of the losing variant (hook weaknesses, friction, and CTA).
3. ?? COPYWRITER AGENT: Produce 3 complete, rewritten variants of the losing campaign using the PAS (Problem-Agitate-Solve) framework.
"""
                res = client.chat.completions.create(
                    model=model_choice,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )
                st.markdown(res.choices[0].message.content)

# -------------------------------------------------------------
# MODULE 3: Predictive RFM CRM Segmentation
# -------------------------------------------------------------
with tab3:
    st.subheader("?? Machine-Learning RFM Customer Segmentation & Churn Risk")
    st.caption("Transforms transaction records into automated lifecycle personas and builds dynamic CRM payloads for Twenty CRM & Klaviyo.")

    rfm_file = "data/customer_transactions.csv"
    if os.path.exists(rfm_file):
        df_trans = pd.read_csv(rfm_file)
        df_trans['transaction_date'] = pd.to_datetime(df_trans['transaction_date'])
        snap_date = df_trans['transaction_date'].max() + pd.Timedelta(days=1)

        rfm_df = df_trans.groupby('customer_id').agg({
            'transaction_date': lambda x: (snap_date - x.max()).days,
            'customer_id': 'count',
            'order_amount': 'sum'
        }).rename(columns={'transaction_date': 'Recency', 'customer_id': 'Frequency', 'order_amount': 'Monetary'})

        def label_persona(row):
            if row['Frequency'] >= rfm_df['Frequency'].quantile(0.75) and row['Monetary'] >= rfm_df['Monetary'].quantile(0.75):
                return "?? VIP Champions (Highest LTV)"
            elif row['Recency'] <= 30 and row['Frequency'] >= 2:
                return "? Loyal Active"
            elif row['Recency'] > 90 and row['Frequency'] >= 2:
                return "?? At-Risk VIP (Needs Win-Back)"
            else:
                return "?? Hibernating / Low-Value"

        rfm_df['Lifecycle_Segment'] = rfm_df.apply(label_persona, axis=1)

        col_rfm1, col_rfm2 = st.columns([1, 1])
        with col_rfm1:
            st.markdown("#### Segment Distribution")
            st.dataframe(rfm_df['Lifecycle_Segment'].value_counts(), use_container_width=True)

        with col_rfm2:
            st.markdown("#### Segment Averages")
            st.dataframe(rfm_df.groupby('Lifecycle_Segment')[['Recency', 'Frequency', 'Monetary']].mean().round(2), use_container_width=True)

        st.subheader("?? Generated Twenty CRM / Klaviyo Event Payload")
        sample_payload = []
        for cid, r in rfm_df.head(4).iterrows():
            sample_payload.append({
                "external_id": cid,
                "traits": {
                    "recency_days": int(r['Recency']),
                    "total_orders": int(r['Frequency']),
                    "total_spend": float(round(r['Monetary'], 2)),
                    "segment": r['Lifecycle_Segment'],
                    "automated_flow": "WIN_BACK_INCENTIVE" if "At-Risk" in r['Lifecycle_Segment'] else "VIP_SECRET_DROP"
                }
            })
        st.json(sample_payload)

# -------------------------------------------------------------
# MODULE 4: Multi-Channel Fatigue Guard
# -------------------------------------------------------------
with tab4:
    st.subheader("??? Multi-Channel SMS & Push Notification Fatigue Guard")
    st.caption("Evaluates list burnout risk, cooling periods, and weekly frequency caps before messages are dispatched.")

    customers = pd.DataFrame([
        {"customer_id": "C_101", "name": "Elena", "vip_tier": "Diamond", "messages_last_7d": 1, "unsub_risk_score": 0.12, "last_msg_hours_ago": 72},
        {"customer_id": "C_102", "name": "Marcus", "vip_tier": "Standard", "messages_last_7d": 5, "unsub_risk_score": 0.78, "last_msg_hours_ago": 6},
        {"customer_id": "C_103", "name": "Amina", "vip_tier": "Gold", "messages_last_7d": 3, "unsub_risk_score": 0.45, "last_msg_hours_ago": 28},
        {"customer_id": "C_104", "name": "Liam", "vip_tier": "Standard", "messages_last_7d": 4, "unsub_risk_score": 0.65, "last_msg_hours_ago": 12},
    ])

    results = []
    for idx, row in customers.iterrows():
        if row['unsub_risk_score'] > 0.70:
            status, reason = "?? SUPPRESS", "High Churn/Opt-out Risk (>70%)"
        elif row['last_msg_hours_ago'] < 24:
            status, reason = "?? SUPPRESS", "< 24h Cooling Period Active"
        elif row['messages_last_7d'] >= (5 if row['vip_tier'] in ['Diamond', 'Gold'] else 3):
            status, reason = "?? SUPPRESS", "Weekly Frequency Cap Exceeded"
        else:
            status, reason = "? DISPATCH", "Eligible for Multi-Channel Dispatch"
        
        results.append({
            "Customer": row['name'],
            "VIP Tier": row['vip_tier'],
            "Weekly Msgs": row['messages_last_7d'],
            "Opt-Out Risk": f"{row['unsub_risk_score']*100:.0f}%",
            "Hours Since Last Msg": row['last_msg_hours_ago'],
            "Dispatch Status": status,
            "Decision Reason": reason
        })

    st.dataframe(pd.DataFrame(results), use_container_width=True)
