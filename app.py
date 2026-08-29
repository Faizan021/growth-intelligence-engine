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
    page_title="Fintech & Crypto Lifecycle OS | Regulated Digital Assets",
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
    <div class="status-badge">\U0001F7E2 Production Lifecycle OS &bull; Regulated European Digital Assets &bull; Braze Architecture</div>
    <div class="hero-title">\U0001F4B0 Fintech & Crypto CRM Lifecycle Operating System</div>
    <div class="hero-subtitle">
        An end-to-end lifecycle automation architecture modeled on regulated European wealthtech apps: Automating the Demo-to-Real Money transition, 3-step KYC verification, recurring Sparpläne, Limit Order triggers, and In-App Message Feeds (Content Cards).
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

# 6 Clean Tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "\U0001F680 1. Demo Mode & 3-Step KYC (Cases 1 & 2)",
    "\U0001F4C8 2. 'Savings Plan' (Sparplan) DCA Engine (Cases 3 & 6)",
    "\U0001F4A5 3. Volatility Alerts & Trading Rules (Cases 4 & 5)",
    "\U0001F465 4. Trader RFM & Whale VIP Hub (Cases 9 & 10)",
    "\U0001F4E8 5. In-App Message Center & Referrals (Cases 7 & 8)",
    "\U0001F517 6. Native Liquid & Event Webhook Dispatcher"
])

# -------------------------------------------------------------
# TAB 1: Demo Mode & 3-Step KYC Funnel (Cases 1 & 2)
# -------------------------------------------------------------
with tab1:
    st.markdown("### \U0001F680 Use Cases 1 & 2: Demo Mode Transition & 3-Step KYC Recovery")
    st.caption("Case Study: Moving users from 'Demo Mode' exploration into 'Real-Money Trading' by recovering the 3-step verification funnel.")

    st.markdown("""
    <div class="hero-container" style="padding: 1.25rem 1.5rem; margin-top: 0.5rem; margin-bottom: 1.5rem; background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);">
        <h4 style="color: #f8fafc; margin-bottom: 0.35rem;">⚡ Real App Architecture: The Demo-to-Real Money Funnel</h4>
        <p style="color: #cbd5e1; font-size: 0.92rem; line-height: 1.6; margin-bottom: 0;">
            <em>"New signups enter the app in <strong>Demo Mode</strong>. When they tap 'Buy' or 'Deposit', trading is locked behind a <strong>3-Step Verification Funnel</strong> (1. Personal Data &rarr; 2. Tax ID Questions &rarr; 3. Document/VideoIdent). This engine tracks granular drop-offs at each step to deploy targeted recovery nudges."</em>
        </p>
    </div>
    """, unsafe_allow_html=True)

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
            title="Funnel Conversion: From Demo Mode to Real-Money Verified Trader",
            template="plotly_white",
            margin=dict(l=20, r=20, t=40, b=20)
        )
        st.plotly_chart(fig_funnel, use_container_width=True)

    with col_k2:
        st.markdown("#### 📋 Funnel Breakdown & Micro-Drop Interventions")
        st.dataframe(kyc_df[['funnel_stage', 'drop_off_pct', 'primary_drop_reason']], use_container_width=True, height=320)

    st.markdown("""
    <div class="glass-card" style="border-left: 4px solid #3b82f6; background: #eff6ff; padding: 1.25rem;">
        <h5 style="color: #1e40af; margin-bottom: 0.5rem; font-size: 1rem;">🔬 The 3 Tailored Recovery Interventions:</h5>
        <div style="font-size: 0.88rem; color: #1e3a8a; line-height: 1.6;">
            <p><strong>• Step 1 &rarr; Step 2 Drop-off (Missing Tax ID):</strong> Nudge with reassurance: <em>'Don't have your Steuer-ID handy? You can add it later—complete Step 3 to unlock trading today!'</em></p>
            <p><strong>• Step 2 &rarr; Step 3 Drop-off (VideoIdent Friction):</strong> Hour 2 Push: <em>'🔒 Your trading wallet is 80% ready. Complete the final 5-minute ID check so you can place your first trade.'</em></p>
            <p style="margin-bottom: 0;"><strong>• Day 3 Cross-Device Handoff (Camera Fallback):</strong> Send a secure SMS magic link for Desktop/Laptop webcam verification if mobile lighting fails.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------
# TAB 2: 'Savings Plan' (Sparplan) DCA Engine (Cases 3 & 6)
# -------------------------------------------------------------
with tab2:
    st.markdown("### \U0001F4C8 Use Cases 3 & 6: 'Savings Plan' (Sparplan) DCA Adoption & Milestones")
    st.caption("Case Study: Driving adoption of the dedicated 'Savings plan' tab (`New savings plan +`) under the Orders menu.")

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
            <p><strong>• 48h Post-1st Trade Nudge:</strong> <em>'Take the stress out of watching price charts. Set up an automated €50/month Bitcoin Sparplan with zero extra order fees.'</em></p>
            <p style="margin-bottom: 0;"><strong>• Milestone Gamification:</strong> Celebrates 3-month streaks with in-app badges, reinforcing steady wealth-building habits.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------
# TAB 3: Volatility Alerts & Trading Rules (Cases 4 & 5)
# -------------------------------------------------------------
with tab3:
    st.markdown("### \U0001F4A5 Use Cases 4 & 5: Volatility Alerts & Automated Limit Order Triggers")
    st.caption("Case Study: Connecting market swings and automated Limit/Stop trading rules with strict 24h frequency governance.")

    v_data = pd.DataFrame([
        {"asset": "Bitcoin (BTC)", "price_change_24h": "+7.4%", "trigger_action": "✅ BUY DIP / RALLY PUSH", "cooling_status": "Eligible (Last touch 36h ago)", "rule_type": "Market Swing"},
        {"asset": "Ethereum (ETH)", "price_change_24h": "-6.1%", "trigger_action": "✅ DCA BUY ALERT PUSH", "cooling_status": "Eligible (Last touch 48h ago)", "rule_type": "Market Dip"},
        {"asset": "Solana (SOL)", "price_change_24h": "+12.8%", "trigger_action": "✅ LIMIT ORDER EXECUTED", "cooling_status": "Transactional (Immediate)", "rule_type": "Limit Buy Rule Triggered"},
        {"asset": "Cardano (ADA)", "price_change_24h": "+3.1%", "trigger_action": "🛑 SUPPRESSED (Sub-threshold)", "cooling_status": "Blocked (Change < 5%)", "rule_type": "Watchlist Only"}
    ])
    st.dataframe(v_data, use_container_width=True)

    st.markdown("""
    <div class="glass-card" style="border-left: 4px solid #f59e0b; background: #fffbeb; padding: 1.25rem;">
        <h5 style="color: #92400e; margin-bottom: 0.5rem; font-size: 1rem;">🛡️ Automated Trading Rule & Volatility Mechanics:</h5>
        <ul style="font-size: 0.88rem; color: #78350f; line-height: 1.6; margin-bottom: 0;">
            <li><strong>Limit Order Execution Alerts:</strong> Instant push confirmation when a user's target buy price triggers while they sleep: <em>'🎯 Your Limit Order executed: Bought 0.05 BTC at €64,000.'</em></li>
            <li><strong>24h Cooling Rule:</strong> Promotional price swings are capped at max 2 alerts/day to maintain < 0.15% push opt-out rates.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------------
# TAB 4: Trader RFM & Whale VIP Hub (Cases 9 & 10)
# -------------------------------------------------------------
with tab4:
    st.markdown("### \U0001F465 Use Cases 9 & 10: Trader RFM Clustering & Whale VIP Management")
    st.caption("Case Study: Preventing 60-day trader churn and providing white-glove VIP execution for high-volume traders (>€25k vol).")

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

# -------------------------------------------------------------
# TAB 5: In-App Message Center & Referrals (Cases 7 & 8)
# -------------------------------------------------------------
with tab5:
    st.markdown("### \U0001F4E8 Use Cases 7 & 8: In-App Message Center (Content Cards) & €30 Referral Engine")
    st.caption("Case Study: Managing persistent in-app notifications (Content Cards) and scaling viral €30 ETH referral loops.")

    m_col1, m_col2 = st.columns(2)
    with m_col1:
        st.markdown("""
        <div class="glass-card" style="border-left: 4px solid #3b82f6; background: #eff6ff;">
            <h5 style="color: #1e40af; margin-bottom: 0.35rem;">📬 Native In-App Message Inbox (Braze Content Cards)</h5>
            <p style="font-size: 0.88rem; color: #1e3a8a; line-height: 1.5;">
                Powers the native message feed (envelope icon with red notification badge) to store persistent updates: annual tax certificates (Steuerbescheinigung), new coin listings, and security notices without intrusive popups.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with m_col2:
        st.markdown("""
        <div class="glass-card" style="border-left: 4px solid #10b981; background: #f0fdf4;">
            <h5 style="color: #065f46; margin-bottom: 0.35rem;">🎁 The 'Invite Friends & Get €30 in ETH' Loop</h5>
            <p style="font-size: 0.88rem; color: #064e3b; line-height: 1.5;">
                Triggered immediately after a user completes their 1st month Sparplan streak: Displays a 1-click WhatsApp share card to invite friends, unlocking €30 in ETH for both when the friend places their first trade.
            </p>
        </div>
        """, unsafe_allow_html=True)

# -------------------------------------------------------------
# TAB 6: Native Liquid & Event Webhook Dispatcher
# -------------------------------------------------------------
with tab6:
    st.markdown("### \U0001F517 Native Liquid & Event Webhook Dispatcher")
    st.caption("Production Liquid syntax pulling live crypto prices & portfolio balances into dynamic push and email payloads.")

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
