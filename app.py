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

st.set_page_config(
    page_title="Fintech & Crypto Lifecycle OS | Open-Source CRM Architecture",
    page_icon="\U0001F4B0",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
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
        font-size: 2.2rem;
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
    <div class="status-badge">\U0001F7E2 Open-Source Fintech & Crypto Lifecycle Architecture &bull; Braze / Dittofeed &bull; Twenty CRM</div>
    <div class="hero-title">\U0001F4B0 Fintech & Crypto CRM Lifecycle Operating System</div>
    <div class="hero-subtitle">
        An open-source lifecycle automation architecture for European regulated crypto platforms and wealthtech apps. Automating 10 critical lifecycle stages: KYC onboarding recovery, recurring 'Sparplan' adoption, volatility alerts, staking updates, and BaFin/GDPR deliverability governance.
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
    if os.path.exists("config/fintech_brand_voice.json"):
        with open("config/fintech_brand_voice.json", encoding="utf-8") as f:
            brand_config = json.load(f)
        st.json(brand_config)
    else:
        brand_config = {"brand_name": "Regulated Wealthtech App", "tone": "Trustworthy, BaFin-compliant"}

# 6 Comprehensive Tabs Covering the 10 Core Use Cases
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "\U0001F680 1. KYC & Deposit Activation (Use Cases 1 & 2)",
    "\U0001F4C8 2. 'Sparplan' DCA & Milestones (Use Cases 3 & 6)",
    "\U0001F4A5 3. Volatility Alerts & Staking Yields (Use Cases 4 & 5)",
    "\U0001F465 4. Trader RFM & Whale VIP Hub (Use Cases 9 & 10)",
    "\U0001F4C4 5. Tax Reports & Feature Drops (Use Cases 7 & 8)",
    "\U0001F517 6. Open-Source CRM & Liquid Engine (Dittofeed & Twenty)"
])

# -------------------------------------------------------------
# TAB 1: KYC Onboarding & Deposit Activation (Cases 1 & 2)
# -------------------------------------------------------------
with tab1:
    st.markdown("### \U0001F680 Use Cases 1 & 2: KYC Drop-Off Recovery & First SEPA Deposit")
    st.caption("Case Study: Recovering the 41.8% drop-off during BaFin-mandated VideoIdent verification and activating 1st SEPA deposits.")

    kyc_df = pd.read_csv("data/crypto_kyc_funnel.csv")
    
    col_k1, col_k2 = st.columns([3, 2])
    with col_k1:
        fig_funnel = go.Figure(go.Funnel(
            y=kyc_df['funnel_stage'],
            x=kyc_df['users_completed'],
            textinfo="value+percent initial",
            marker=dict(color=["#3b82f6", "#f43f5e", "#f59e0b", "#10b981", "#8b5cf6"])
        ))
        fig_funnel.update_layout(
            title="Customer Acquisition Funnel: From Restricted Mode to Verified Trader",
            template="plotly_white",
            margin=dict(l=20, r=20, t=40, b=20)
        )
        st.plotly_chart(fig_funnel, use_container_width=True)

    with col_k2:
        st.markdown("#### 📋 Funnel Friction & Automated Interventions")
        st.dataframe(kyc_df[['funnel_stage', 'drop_off_pct', 'primary_drop_reason']], use_container_width=True, height=320)

    st.markdown("""
    <div class="glass-card" style="border-left: 4px solid #3b82f6; background: #eff6ff; padding: 1.25rem;">
        <h5 style="color: #1e40af; margin-bottom: 0.5rem; font-size: 1rem;">🔬 The 3 Core Activation Triggers (Braze / Dittofeed Canvas):</h5>
        <div style="font-size: 0.88rem; color: #1e3a8a; line-height: 1.6;">
            <p><strong>• Use Case 1 (Hour 2 - Push Notification):</strong> <em>'🔒 Your trading wallet is 80% ready. Tap to finish quick 2-min verification and claim your allocated wallet address.'</em> (Deep-links directly to VideoIdent SDK).</p>
            <p><strong>• Use Case 1 (Day 3 - SMS Desktop Handoff):</strong> Send a secure SMS magic link allowing users to complete verification on desktop with a webcam if mobile lighting fails.</p>
            <p style="margin-bottom: 0;"><strong>• Use Case 2 (Day 1 Post-KYC - First Deposit Activation):</strong> Nudge verified users with an instant SEPA guide highlighting €0 deposit fees and €15 welcome trading bonus.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------
# TAB 2: 'Sparplan' DCA & Milestones (Cases 3 & 6)
# -------------------------------------------------------------
with tab2:
    st.markdown("### \U0001F4C8 Use Cases 3 & 6: Automated 'Sparplan' (DCA) & Milestone Celebrations")
    st.caption("Case Study: Converting volatile spot traders into automated monthly crypto savings plans (Dollar-Cost Averaging) and gamifying milestones.")

    col_dca1, col_dca2 = st.columns([3, 2])
    with col_dca1:
        months_sim = ["Month 1", "Month 3", "Month 6", "Month 9", "Month 12", "Month 18", "Month 24"]
        dca_growth = [100, 320, 680, 1150, 1720, 3100, 4850]
        manual_volatile = [100, 180, 90, 420, 310, 850, 1920]

        fig_dca = go.Figure()
        fig_dca.add_trace(go.Scatter(
            x=months_sim, y=dca_growth,
            mode='lines+markers', name='💎 Automated Crypto Sparplan (DCA)',
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
        st.markdown("#### 🎯 Sparplan Adoption & LTV Metrics")
        st.metric("Sparplan Adoption Rate", "38.2%", "+14.5% YoY via DCA Nudges")
        st.metric("12-Month LTV Multiplier", "3.8x higher LTV", "Recurring auto-deposit volume")
        st.metric("90-Day Churn Reduction", "14.2% Churn", "-70.8% vs Manual Spot Traders", delta_color="inverse")

    st.markdown("""
    <div class="glass-card" style="border-left: 4px solid #10b981; background: #f0fdf4; padding: 1.25rem;">
        <h5 style="color: #065f46; margin-bottom: 0.5rem; font-size: 1rem;">🔬 Behavioral Habit Formation:</h5>
        <div style="font-size: 0.88rem; color: #064e3b; line-height: 1.6;">
            <p><strong>• Use Case 3 (48h Post-Trade - The Stress-Free Sparplan):</strong> <em>'Take the stress out of market timing. Set up an automated €50/month Bitcoin Sparplan with zero extra order fees.'</em></p>
            <p style="margin-bottom: 0;"><strong>• Use Case 6 (Milestone Gamification):</strong> When a user accumulates their first €1,000 or 0.1 BTC, trigger celebratory in-app confetti cards and streak badges to reinforce positive investing habits.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------
# TAB 3: Volatility Alerts & Staking Yields (Cases 4 & 5)
# -------------------------------------------------------------
with tab3:
    st.markdown("### \U0001F4A5 Use Cases 4 & 5: Market Volatility Push Alerts & Staking Payouts")
    st.caption("Case Study: Capitalizing on Bitcoin/Ethereum ±5% market swings and weekly staking yield distributions.")

    v_data = pd.DataFrame([
        {"asset": "Bitcoin (BTC)", "price_change_24h": "+7.4%", "trigger_action": "✅ BUY DIP / RALLY PUSH", "cooling_status": "Eligible (Last touch 36h ago)", "portfolio_relevance": "User holds BTC"},
        {"asset": "Ethereum (ETH)", "price_change_24h": "-6.1%", "trigger_action": "✅ DCA BUY ALERT PUSH", "cooling_status": "Eligible (Last touch 48h ago)", "portfolio_relevance": "User holds ETH"},
        {"asset": "Solana (SOL)", "price_change_24h": "+12.8%", "trigger_action": "🛑 SUPPRESSED (Cooldown)", "cooling_status": "Blocked (< 12h since last push)", "portfolio_relevance": "User does NOT hold SOL"},
        {"asset": "Cardano (ADA)", "price_change_24h": "+3.1%", "trigger_action": "🛑 SUPPRESSED (Sub-threshold)", "cooling_status": "Blocked (Change < 5%)", "portfolio_relevance": "User watchlist only"}
    ])
    st.dataframe(v_data, use_container_width=True)

    st.markdown("""
    <div class="glass-card" style="border-left: 4px solid #f59e0b; background: #fffbeb; padding: 1.25rem;">
        <h5 style="color: #92400e; margin-bottom: 0.5rem; font-size: 1rem;">🛡️ Use Cases 4 & 5 Automation Mechanics:</h5>
        <ul style="font-size: 0.88rem; color: #78350f; line-height: 1.6; margin-bottom: 0;">
            <li><strong>Use Case 4 (Volatility Alerts):</strong> Automated webhook checks coin movements every 15m. Alerts only trigger for assets the user holds or watches, with a strict <strong>24h cooling cap (max 2 pushes/day)</strong>.</li>
            <li><strong>Use Case 5 (Staking Yield Payouts):</strong> Weekly automated push/email notifying users of accrued rewards: <em>'💎 You earned €4.80 in Ethereum staking rewards this week. Your rewards have been automatically reinvested.'</em></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------
# TAB 4: Trader RFM & Whale VIP Hub (Cases 9 & 10)
# -------------------------------------------------------------
with tab4:
    st.markdown("### \U0001F465 Use Cases 9 & 10: Trader RFM Clustering & Whale VIP Management")
    st.caption("Case Study: Preventing 60-day trader churn and providing white-glove VIP management for high-volume traders (>€25k vol).")

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
        title="Trader RFM Distribution (Recency vs. Trading Volume €)"
    )
    fig_crypto_rfm.update_layout(template="plotly_white", margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig_crypto_rfm, use_container_width=True)

    st.markdown("""
    <div class="glass-card" style="border-left: 4px solid #8b5cf6; background: #faf5ff; padding: 1.25rem;">
        <h5 style="color: #6b21a8; margin-bottom: 0.5rem; font-size: 1rem;">🔬 Targeted Retention & VIP Strategies:</h5>
        <div style="font-size: 0.88rem; color: #4c1d95; line-height: 1.6;">
            <p><strong>• Use Case 9 (60-Day Dormant Win-Back):</strong> Personalized market recap email: <em>'Here is what happened in the crypto market while you were away + Your portfolio valuation update.'</em></p>
            <p style="margin-bottom: 0;"><strong>• Use Case 10 (High-Volume Whale Concierge):</strong> Automatically flags users with >€25k volume to receive reduced trading spread rebates and personal VIP Telegram/Email concierge support.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------
# TAB 5: Tax Reports & Feature Drops (Cases 7 & 8)
# -------------------------------------------------------------
with tab5:
    st.markdown("### \U0001F4C4 Use Cases 7 & 8: Annual Tax Reports & New Asset Listings")
    st.caption("Case Study: Delivering high-engagement German tax certificates (Steuerbescheinigung) and launching new tradable assets.")

    t_col1, t_col2 = st.columns(2)
    with t_col1:
        st.markdown("""
        <div class="glass-card" style="border-left: 4px solid #3b82f6; background: #eff6ff;">
            <h5 style="color: #1e40af; margin-bottom: 0.35rem;">📄 Use Case 8: Annual Tax Report Ready (Steuerbescheinigung)</h5>
            <p style="font-size: 0.88rem; color: #1e3a8a; line-height: 1.5;">
                In Germany, crypto tax calculation is a major friction point. In January, an automated email and in-app card notifies users that their 1-click PDF tax report is ready for the Finanzamt, generating <strong>68.4% open rates</strong>.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with t_col2:
        st.markdown("""
        <div class="glass-card" style="border-left: 4px solid #10b981; background: #f0fdf4;">
            <h5 style="color: #065f46; margin-bottom: 0.35rem;">🚀 Use Case 7: New Asset Listing & Educational Carousels</h5>
            <p style="font-size: 0.88rem; color: #064e3b; line-height: 1.5;">
                When listing a new crypto asset (e.g. Solana, Cardano), Braze triggers an educational lookbook explaining fundamentals, staking options, and BaFin regulatory status, driving a <strong>+42% 1st-week volume surge</strong>.
            </p>
        </div>
        """, unsafe_allow_html=True)

# -------------------------------------------------------------
# TAB 6: Open-Source Architecture (Dittofeed & Twenty CRM)
# -------------------------------------------------------------
with tab6:
    st.markdown("### \U0001F517 Open-Source CRM Architecture & Liquid Templating Engine")
    st.caption("Live integration schemas for open-source self-hosted platforms (Dittofeed, Twenty CRM, Novu, Formbricks).")

    st.markdown("""
    <div class="glass-card" style="border-left: 4px solid #0f766e; background: #f0fdfa; padding: 1.25rem;">
        <h5 style="color: #0f766e; margin-bottom: 0.5rem; font-size: 1rem;">🐙 Open-Source Stack Powering This Architecture:</h5>
        <ul style="font-size: 0.88rem; color: #134e4a; line-height: 1.6; margin-bottom: 0;">
            <li><strong>Dittofeed (<code>github.com/dittofeed/dittofeed</code>):</strong> Self-hosted Braze alternative ensuring zero PII customer data leaves the regulated EU VPC.</li>
            <li><strong>Twenty CRM (<code>github.com/twentyhq/twenty</code>):</strong> GraphQL-first CRM for managing trader accounts, KYC statuses, and VIP tiers.</li>
            <li><strong>Novu (<code>github.com/novuhq/novu</code>):</strong> Multi-channel push and in-app notification infrastructure for real-time volatility alerts.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### 🔗 Dynamic Liquid Event Template:")
    sample_liquid_payload = '''{% connected_content https://api.regulated-exchange.eu/v1/market/prices :save btc_market %}
{% assign btc_change = btc_market.bitcoin.change_24h | default: 0 %}

{% if {{${user_attribute_sparplan_active}}} == true %}
  Subject: 💎 Your monthly Bitcoin Sparplan was executed successfully, {{${first_name} | default: "Trader"}}!
  Body: Hi {{${first_name}}}, your automated €{{${user_attribute_monthly_dca_amount}}} investment bought {{btc_market.bitcoin.purchased_sats}} sats at €{{btc_market.bitcoin.current_price_eur}}.
{% else %}
  Subject: 📈 Bitcoin is {{ btc_change }}% in the last 24h — Automate your savings with our Sparplan
  Body: Hi {{${first_name}}}, avoid timing the market. Turn on recurring weekly buys with 0 extra fees.
{% endif %}'''

    st.code(sample_liquid_payload, language="liquid")
