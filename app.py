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
    page_title="Fintech & Crypto CRM Lifecycle Engine | Regulated Digital Assets",
    page_icon="\U0001F4B0",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Fintech / Regulated European Exchange Group Digital theme)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    html, body, [class*="css"] { font-family: 'Plus Jakarta Sans', sans-serif; }
    
    .hero-container {
        background: linear-gradient(135deg, #0a192f 0%, #1e3a8a 50%, #0f766e 100%);
        border-radius: 16px;
        padding: 2.5rem 2rem;
        color: white;
        margin-bottom: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2);
    }
    
    .hero-title {
        font-size: 2.3rem;
        font-weight: 800;
        letter-spacing: -0.03em;
        background: linear-gradient(to right, #ffffff, #93c5fd, #6ee7b7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .hero-subtitle {
        font-size: 1.05rem;
        color: #cbd5e1;
        font-weight: 500;
        line-height: 1.6;
        max-width: 850px;
    }
    
    .status-badge {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: rgba(16, 185, 129, 0.2);
        color: #6ee7b7;
        border: 1px solid rgba(16, 185, 129, 0.4);
        padding: 0.35rem 0.85rem;
        border-radius: 9999px;
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        margin-bottom: 1rem;
    }

    .glass-card {
        background: #ffffff;
        border-radius: 14px;
        padding: 1.5rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Header Banner
st.markdown("""
<div class="hero-container">
    <div class="status-badge">\U0001F7E2 Regulated European Fintech &bull; Crypto & Wealthtech Lifecycle Engine &bull; Braze Architecture</div>
    <div class="hero-title">\U0001F4B0 Fintech Crypto CRM & Lifecycle Automation Platform</div>
    <div class="hero-subtitle">
        Automated customer journeys for regulated retail crypto trading. Minimizing KYC drop-off, scaling recurring 'Sparplan' adoption, executing volatility-triggered Braze Canvases, and enforcing BaFin/GDPR deliverability governance.
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("\u2699\ufe0f Engine Settings")
    api_key = st.text_input("OpenAI API Key", type="password", help="Enter OpenAI key for live agent execution.")
    model_choice = st.selectbox("LLM Agent Model", ["gpt-4o-mini", "gpt-4o"])
    demo_mode = st.toggle("\u26a1 Use Instant Demo Cache", value=True)
    
    st.divider()
    st.subheader("\U0001F3A8 Compliance & Brand Guidelines")
    if os.path.exists("config/bison_brand_voice.json"):
        with open("config/bison_brand_voice.json", encoding="utf-8") as f:
            brand_config = json.load(f)
        st.json(brand_config)
    else:
        brand_config = {"brand_name": "Regulated Wealthtech Exchange", "tone": "Trustworthy, BaFin-compliant"}

# 5 Core Fintech CRM Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "\U0001F680 1. KYC Drop-Off Recovery (Braze Canvas)",
    "\U0001F4C8 2. 'Sparplan' DCA Adoption Engine",
    "\U0001F4A5 3. Volatility Alerts & Frequency Guard",
    "\U0001F465 4. Crypto Trader RFM Clustering",
    "\U0001F517 5. Braze Liquid & Connected Content"
])

# -------------------------------------------------------------
# TAB 1: KYC Onboarding & Drop-Off Recovery
# -------------------------------------------------------------
with tab1:
    st.markdown("### \U0001F680 KYC & Identity Verification Recovery: 'The Locked Wallet' Mechanism")
    st.caption("Case Study: How Regulated Wealthtech Exchange recovers users stuck in the 'Restricted Read-Only Mode' before BaFin VideoIdent verification.")

    st.markdown("""
    <div class="hero-container" style="padding: 1.25rem 1.5rem; margin-top: 0.5rem; margin-bottom: 1.5rem; background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);">
        <h4 style="color: #f8fafc; margin-bottom: 0.35rem;">⚡ Fintech Reality: The 'Restricted Read-Only' App State</h4>
        <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6; margin-bottom: 0;">
            <em>"When users sign up, they can explore live crypto charts and market news in <strong>Read-Only Mode</strong>, but trading is locked behind BaFin identity verification. Rather than generic 'Please verify' nags, we use the <strong>Endowed Progress Effect</strong> and <strong>Cross-Device VideoIdent Handoffs</strong> to recover 28.4% of abandoned accounts."</em>
        </p>
    </div>
    """, unsafe_allow_html=True)

    kyc_df = pd.read_csv("data/bison_kyc_funnel.csv")
    
    col_k1, col_k2 = st.columns([3, 2])
    with col_k1:
        fig_funnel = go.Figure(go.Funnel(
            y=kyc_df['funnel_stage'],
            x=kyc_df['users_completed'],
            textinfo="value+percent initial",
            marker=dict(color=["#3b82f6", "#f43f5e", "#f59e0b", "#10b981", "#8b5cf6"])
        ))
        fig_funnel.update_layout(
            title="Regulated Wealthtech Exchange Acquisition Funnel: From Restricted Mode to Verified Trader",
            template="plotly_white",
            margin=dict(l=20, r=20, t=40, b=20)
        )
        st.plotly_chart(fig_funnel, use_container_width=True)

    with col_k2:
        st.markdown("#### 📋 Funnel Friction & Behavioral Interventions")
        st.dataframe(kyc_df[['funnel_stage', 'drop_off_pct', 'primary_drop_reason']], use_container_width=True, height=320)

    st.markdown("""
    <div class="glass-card" style="border-left: 4px solid #3b82f6; background: #eff6ff; padding: 1.25rem;">
        <h5 style="color: #1e40af; margin-bottom: 0.5rem; font-size: 1rem;">🔬 The 3 Creative KYC Recovery Triggers (Braze Canvas):</h5>
        <div style="font-size: 0.88rem; color: #1e3a8a; line-height: 1.6;">
            <p><strong>1. Hour 2 — 'The Reserved Account & Endowed Progress Hook' (Push):</strong><br>
            Instead of <em>'Verify your ID'</em>, the push frames progress: <em>'🔒 Your Regulated Wealthtech Exchange trading wallet is 80% ready. Tap to finish the final 2-minute ID step so you can lock in your first trade.'</em></p>
            <p><strong>2. Day 1 — 'Market Movement Opportunity Hook' (Email):</strong><br>
            If Bitcoin or Ethereum moves >3%, trigger dynamic email: <em>'BTC moved +4.2% today. Complete verification in 1 tap so you're ready for the next market entry.'</em> (Highlights Regulated European Exchange Group's bank-level security).</p>
            <p style="margin-bottom: 0;"><strong>3. Day 3 — 'Cross-Device Web/Desktop Handoff' (SMS Magic Link):</strong><br>
            Many users drop off because their mobile webcam or lighting fails during VideoIdent. We send a secure SMS magic-link allowing them to complete verification on desktop with a passport/ID card in under 3 minutes.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------
# TAB 2: 'Sparplan' DCA Recurring Savings Adoption
# -------------------------------------------------------------
with tab2:
    st.markdown("### \U0001F4C8 'Sparplan' (DCA Recurring Savings) Adoption: The Stress-Free Trader")
    st.caption("Case Study: Converting volatile spot traders into automated monthly Bitcoin/Ethereum savings plans (Dollar-Cost Averaging).")

    st.markdown("""
    <div class="hero-container" style="padding: 1.25rem 1.5rem; margin-top: 0.5rem; margin-bottom: 1.5rem; background: linear-gradient(135deg, #064e3b 0%, #0f172a 100%);">
        <h4 style="color: #f8fafc; margin-bottom: 0.35rem;">⚡ Creative Lifecycle Concept: 'Eliminate Market Anxiety'</h4>
        <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6; margin-bottom: 0;">
            <em>"Spot crypto buyers get exhausted watching 1-minute candlestick charts and second-guessing market dips. 48h after their 1st trade, Braze triggers a <strong>personalized DCA Backtest Simulator</strong> showing that automated recurring buys outperform 78% of emotional retail day-traders."</em>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Interactive DCA Simulation vs Spot Trading
    col_dca1, col_dca2 = st.columns([3, 2])
    with col_dca1:
        months_sim = ["Month 1", "Month 3", "Month 6", "Month 9", "Month 12", "Month 18", "Month 24"]
        dca_growth = [100, 320, 680, 1150, 1720, 3100, 4850]
        manual_volatile = [100, 180, 90, 420, 310, 850, 1920]

        fig_dca = go.Figure()
        fig_dca.add_trace(go.Scatter(
            x=months_sim, y=dca_growth,
            mode='lines+markers', name='💎 Regulated Wealthtech Exchange Automated Sparplan (DCA)',
            line=dict(color='#10b981', width=3), marker=dict(size=8)
        ))
        fig_dca.add_trace(go.Scatter(
            x=months_sim, y=manual_volatile,
            mode='lines+markers', name='📉 Emotional Spot Trading (High Churn)',
            line=dict(color='#f43f5e', width=2, dash='dash'), marker=dict(size=6)
        ))
        fig_dca.update_layout(
            title="Portfolio Value Simulation (€): Automated Sparplan vs. Emotional Trading",
            yaxis_title="Simulated Portfolio (€)",
            template="plotly_white",
            margin=dict(l=20, r=20, t=40, b=20),
            legend=dict(orientation="h", yanchor="top", y=-0.15, xanchor="center", x=0.5)
        )
        st.plotly_chart(fig_dca, use_container_width=True)

    with col_dca2:
        st.markdown("#### 🎯 Sparplan Adoption Metrics")
        st.metric("Sparplan Adoption Lift", "38.2%", "+14.5% YoY via DCA Nudges")
        st.metric("12-Month LTV Multiplier", "3.8x higher LTV", "Recurring auto-deposit volume")
        st.metric("90-Day Churn Reduction", "14.2% Churn", "-70.8% vs Manual Spot Traders", delta_color="inverse")

    st.markdown("""
    <div class="glass-card" style="border-left: 4px solid #10b981; background: #f0fdf4; padding: 1.25rem;">
        <h5 style="color: #065f46; margin-bottom: 0.5rem; font-size: 1rem;">🔬 The 3 Creative Sparplan Retention Hooks:</h5>
        <div style="font-size: 0.88rem; color: #064e3b; line-height: 1.6;">
            <p><strong>1. 'The Backtested Visualizer' (Email / In-App 48h Post-Trade):</strong><br>
            <em>'If you saved €50/month in Bitcoin since 2021, your portfolio would be +142% today with zero chart-watching stress. Set up your auto-Sparplan in 2 taps.'</em></p>
            <p><strong>2. 'Zero Extra Order Fees' Angle:</strong><br>
            Highlights that Regulated Wealthtech Exchange charges no additional transaction surcharge on recurring Sparplan executions compared to traditional brokers.</p>
            <p style="margin-bottom: 0;"><strong>3. Gamified Savings Streaks:</strong><br>
            Sends in-app milestone celebrations (e.g., <em>'🔥 3-Month Sparplan Streak Completed: You've automatically accumulated 0.015 BTC'</em>), locking in high retention.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)


# -------------------------------------------------------------
# TAB 3: Volatility Alerts & Frequency Guard
# -------------------------------------------------------------
with tab3:
    st.markdown("### \U0001F4A5 Market Volatility Price Alerts & Deliverability Guard")
    st.caption("Case Study: Capitalizing on Bitcoin/Ethereum ±5% market swings while enforcing strict 24h cooling periods to prevent app uninstalls.")

    v_data = pd.DataFrame([
        {"asset": "Bitcoin (BTC)", "price_change_24h": "+7.4%", "trigger_action": "✅ BUY DIP / RALLY PUSH", "cooling_status": "Eligible (Last touch 36h ago)", "portfolio_relevance": "User holds BTC"},
        {"asset": "Ethereum (ETH)", "price_change_24h": "-6.1%", "trigger_action": "✅ DCA BUY ALERT PUSH", "cooling_status": "Eligible (Last touch 48h ago)", "portfolio_relevance": "User holds ETH"},
        {"asset": "Solana (SOL)", "price_change_24h": "+12.8%", "trigger_action": "🛑 SUPPRESSED (Cooldown)", "cooling_status": "Blocked (< 12h since last push)", "portfolio_relevance": "User does NOT hold SOL"},
        {"asset": "Cardano (ADA)", "price_change_24h": "+3.1%", "trigger_action": "🛑 SUPPRESSED (Sub-threshold)", "cooling_status": "Blocked (Change < 5%)", "portfolio_relevance": "User watchlist only"}
    ])
    st.dataframe(v_data, use_container_width=True)

    st.markdown("""
    <div class="glass-card" style="border-left: 4px solid #f59e0b; background: #fffbeb; padding: 1.25rem;">
        <h5 style="color: #92400e; margin-bottom: 0.5rem; font-size: 1rem;">🛡️ BaFin & User Experience Governance Rules:</h5>
        <ul style="font-size: 0.88rem; color: #78350f; line-height: 1.6; margin-bottom: 0;">
            <li><strong>Portfolio-Relevance Filtering:</strong> Users only receive volatility alerts for coins they actually hold in their trading account or have added to their active Watchlist.</li>
            <li><strong>24-Hour Cooldown Cap:</strong> Maximum 2 price alert push notifications per 24 hours per user to maintain < 0.15% opt-out rates.</li>
            <li><strong>Non-Promotional Neutral Tone:</strong> Alerts present factual market movements without speculative hype (strictly BaFin-compliant).</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------
# TAB 4: Crypto Trader RFM Clustering
# -------------------------------------------------------------
with tab4:
    st.markdown("### \U0001F465 Crypto Trader Lifecycle Segmentation (RFM)")
    st.caption("Case Study: Tailoring CRM communication by Trading Recency (Days), Monthly Frequency (Trades), and Monetary Volume (€).")

    df_rfm = pd.read_csv("data/crypto_trader_rfm.csv")
    
    def classify_crypto_persona(row):
        vol = row['total_trading_volume_eur']
        rec = row['recency_days_since_trade']
        spar = row['sparplan_active']
        
        if vol >= 5000 and rec <= 14:
            return "👑 VIP Active Whales (>€5k Volume)"
        elif str(spar) == "True":
            return "💎 Steady 'Sparplan' HODLers (Recurring LTV)"
        elif rec > 60:
            return "⚠️ Dormant Inactive Traders (Needs Win-Back)"
        else:
            return "⚡ Active Casual Traders"

    df_rfm['Trader_Segment'] = df_rfm.apply(classify_crypto_persona, axis=1)

    fig_crypto_rfm = px.scatter(
        df_rfm.head(500),
        x="recency_days_since_trade",
        y="total_trading_volume_eur",
        size="monthly_trades",
        color="Trader_Segment",
        color_discrete_map={
            "👑 VIP Active Whales (>€5k Volume)": "#8b5cf6",
            "💎 Steady 'Sparplan' HODLers (Recurring LTV)": "#10b981",
            "⚠️ Dormant Inactive Traders (Needs Win-Back)": "#f43f5e",
            "⚡ Active Casual Traders": "#3b82f6"
        },
        title="Crypto & Wealthtech Trader RFM Distribution (Recency vs. Trading Volume €)"
    )
    fig_crypto_rfm.update_layout(template="plotly_white", margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig_crypto_rfm, use_container_width=True)

# -------------------------------------------------------------
# TAB 5: Braze Liquid & Connected Content
# -------------------------------------------------------------
with tab5:
    st.markdown("### \U0001F517 Braze Liquid Templating & Connected Content Live Engine")
    st.caption("Case Study: Pulling live real-time crypto prices & personal portfolio balance securely into push and email payloads via API.")

    sample_liquid_payload = '''{% connected_content https://api.bisonapp.de/v1/market/prices :save btc_market %}
{% assign btc_change = btc_market.bitcoin.change_24h | default: 0 %}

{% if {{${user_attribute_sparplan_active}}} == true %}
  Subject: 💎 Your monthly Bitcoin Sparplan was executed successfully, {{${first_name} | default: "Trader"}}!
  Body: Hi {{${first_name}}}, your automated €{{${user_attribute_monthly_dca_amount}}} investment bought {{btc_market.bitcoin.purchased_sats}} sats at €{{btc_market.bitcoin.current_price_eur}}.
{% else %}
  Subject: 📈 Bitcoin is {{ btc_change }}% in the last 24h — Automate your savings with Automated Crypto Sparplan (DCA)
  Body: Hi {{${first_name}}}, avoid timing the market. Turn on recurring weekly buys with 0 extra fees.
{% endif %}'''

    st.code(sample_liquid_payload, language="liquid")
    st.info("💡 **Technical Advantage:** Proves hands-on mastery of **Braze Connected Content, conditional Liquid branching, and fallback logic** for fintech CRM setups.")
