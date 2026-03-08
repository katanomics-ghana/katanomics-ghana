import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

st.set_page_config(page_title="Katanomics Portfolio", layout="wide", page_icon="🏗️")

# Custom CSS for IMANI-level polish
st.markdown("""
<style>
.main-header {font-size: 3rem; color: #1f77b4; font-weight: 700;}
.error-banner {font-size: 1.5rem; font-weight: 600;}
.metric-col {background-color: #f8f9fa; padding: 1rem; border-radius: 10px;}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🏗️ KATANOMICS TRIPLE PORTFOLIO v3.0</h1>', unsafe_allow_html=True)
st.markdown('<p class="error-banner">❌ GH¢1.3T MOBILIZATION BLACK HOLE</p>', unsafe_allow_html=True)

# Data
@st.cache_data
def load_data():
    return pd.DataFrame({
        'Project': ['Pwalugu Dam', 'Saglemi Housing', 'GH¢104B Roads'],
        'Contracts': [895, 200, 104000],
        'Paid': [11.9, 200, 30000],
        'Delivery': [0, 1506, 20],
        'Status': ['0 DAMS', 'SHELLS ONLY', 'CRISIS'],
        'Action': ['PPDA AUDIT', 'HALT MOU', 'PAC SUMMON']
    })

df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filter Projects")
selected_projects = st.sidebar.multiselect("Select projects:", df['Project'].tolist(), default=df['Project'].tolist())

filtered_df = df[df['Project'].isin(selected_projects)]

# KPI Row 1: Core Metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    total_contracts = filtered_df['Contracts'].sum()
    st.metric("Total Contracts", f"GH¢{total_contracts:,.0f}M", delta="100% overpaid")
with col2:
    st.metric("Mobilization Paid", f"GH¢{filtered_df['Paid'].sum():,.0f}M")
with col3:
    delivery_rate = filtered_df['Delivery'].sum() / total_contracts * 100 if total_contracts > 0 else 0
    st.metric("Delivery Rate", f"{delivery_rate:.1f}%", delta=f"-{100-delivery_rate:.1f}%")
with col4:
    st.metric("Projects in Crisis", len(filtered_df), delta="+3")

# Row 2: Interactive Charts
col5, col6 = st.columns([2,1])

with col5:
    st.subheader("🏭 Mobilization vs Delivery Black Hole")
    fig = px.bar(filtered_df, 
                x='Project', 
                y=['Contracts', 'Paid', 'Delivery'],
                title="Budget → Payment → ZERO Delivery Pattern",
                barmode='group',
                color_discrete_map={'Contracts': '#ff4444', 'Paid': '#ffaa00', 'Delivery': '#00aa44'})
    fig.update_layout(height=500, showlegend=True)
    st.plotly_chart(fig, use_container_width=True)

with col6:
    st.subheader("⚠️ Project Status")
    fig2 = px.pie(filtered_df, names='Status', 
                  title="All Projects Failing",
                  color_discrete_sequence=['#ff4444', '#ff8800', '#ffaa00'])
    fig2.update_traces(textposition='inside', textinfo='percent+label')
    fig2.update_layout(height=300)
    st.plotly_chart(fig2, use_container_width=True)

# Row 3: Action Cards
st.subheader("✅ PAC Action Items")
action_cols = st.columns(len(filtered_df))
for idx, (_, row) in enumerate(filtered_df.iterrows()):
    with action_cols[idx]:
        st.error(f"**{row['Project']}**")
        st.metric("Status", row['Status'])
        if st.button(f"📋 {row['Action']}", key=f"action_{idx}"):
            st.success(f"✅ {row['Action']} assigned to PAC agenda")

# Row 4: Raw Data + Export
with st.expander("📊 Detailed Data & Methodology", expanded=False):
    st.dataframe(filtered_df, use_container_width=True)
    
    csv = filtered_df.to_csv(index=False)
    st.download_button("💾 Download PAC Brief (CSV)", csv, "katanomics_pac_brief.csv")

st.markdown("---")
st.markdown("**🏛️ Katanomics Collective** | *Diagnostic engine for Ghana's infrastructure crisis*")
