import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

st.set_page_config(page_title="Katanomics Portfolio", layout="wide", page_icon="🏗️")

# Professional CSS
st.markdown("""
<style>
.main-header {font-size: 3rem; color: #1f77b4; font-weight: 700;}
.error-banner {font-size: 1.5rem; font-weight: 600; color: #d32f2f;}
.metric-col {background-color: #f8f9fa; padding: 1rem; border-radius: 10px;}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🏗️ KATANOMICS TRIPLE PORTFOLIO v3.1</h1>', unsafe_allow_html=True)
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

# Sidebar
st.sidebar.header("🔍 Filter")
selected = st.sidebar.multiselect("Projects:", df['Project'].tolist(), default=df['Project'].tolist())
filtered_df = df[df['Project'].isin(selected)]

# KPIs
col1, col2, col3, col4 = st.columns(4)
total_c = filtered_df['Contracts'].sum()
with col1: st.metric("Contracts", f"GH¢{total_c:,.0f}M")
with col2: st.metric("Paid", f"GH¢{filtered_df['Paid'].sum():,.0f}M") 
with col3: st.metric("Delivery", f"{filtered_df['Delivery'].sum():,.0f}")
with col4: st.metric("Crisis Projects", len(filtered_df))

# CHARTS WITH PROFESSIONAL COLORS
col5, col6 = st.columns([3,1])

with col5:
    st.subheader("🏭 Mobilization Black Hole")
    fig = px.bar(filtered_df, 
                x='Project', 
                y=['Contracts', 'Paid', 'Delivery'],
                barmode='group',
                color_discrete_map={
                    'Contracts': '#d32f2f',  # Deep red
                    'Paid': '#f57c00',       # Burnt orange
                    'Delivery': '#388e3c'    # Forest green
                })
    fig.update_layout(height=450, showlegend=True)
    st.plotly_chart(fig, use_container_width=True)

with col6:
    st.subheader("⚠️ Status")
    fig2 = px.pie(filtered_df, names='Status', 
                  color_discrete_sequence=['#d32f2f', '#f57c00'])
    fig2.update_traces(textposition='inside')
    fig2.update_layout(height=300)
    st.plotly_chart(fig2, use_container_width=True)

# Actions
st.subheader("✅ PAC Actions")
cols = st.columns(len(filtered_df))
for i, (_, row) in enumerate(filtered_df.iterrows()):
    with cols[i]:
        st.error(row['Project'])
        if st.button(row['Action'], key=f"btn_{i}"):
            st.success(f"✅ {row['Action']} queued")

# Data
with st.expander("📊 Data"):
    st.dataframe(filtered_df)
    st.download_button("💾 CSV", filtered_df.to_csv().encode(), "katanomics.csv")

st.markdown("**🏛️ Katanomics Collective** | Ghana infrastructure accountability")
