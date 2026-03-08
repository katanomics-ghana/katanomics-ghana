import streamlit as st

st.set_page_config(page_title="Katanomics Portfolio", layout="wide")

st.title("🏗️ KATANOMICS TRIPLE PORTFOLIO v2.0")
st.error("❌ GH¢1.3T MOBILIZATION BLACK HOLE")

tab1, tab2, tab3 = st.tabs(["🇬🇭 PWALUGU DAM", "🏘️ SAGLEMI", "🛣️ GH¢104B ROADS"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Contracts", "$895M")
        st.metric("Paid", "$11.9M")
    with col2:
        st.error("🚫 Status: 0 DAMS BUILT")
        st.success("✅ PPDA AUDIT NOW")

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Loan", "$200M")
        st.metric("Built", "1,506 shells")
    with col2:
        st.error("💸 Status: $115M MORE NEEDED")
        st.success("✅ HALT QUARM-LMI MOU")

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Contracts", "GH¢104B")
        st.metric("Budget", "GH¢30B")
    with col2:
        st.error("⚠️ Status: CONTRACTOR CRISIS")
        st.success("✅ PAC SUMMON MINISTERS")

st.markdown("---")
st.markdown("**Katanomics Collective** | Budget → Payment → 0 Delivery")
