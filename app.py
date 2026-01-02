import streamlit as st
import pandas as pd
import os

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="Tennis SportRadar Analytics",
    layout="wide"
)

st.title("🎾 Tennis SportRadar Analytics")

# ---------------------------------
# Data Loading (CLOUD SAFE)
# ---------------------------------
DATA_FILE = "competitions.csv"

if not os.path.exists(DATA_FILE):
    st.error("❌ competitions.csv not found. Please ensure it exists in the repository.")
    st.stop()

df = pd.read_csv(DATA_FILE)

st.success("✅ Data loaded successfully!")

# ---------------------------------
# Sidebar Filters
# ---------------------------------
st.sidebar.header("🧩 Filter Competitions")

tournament_options = ["All"] + sorted(df["tournament_category"].dropna().unique().tolist())
match_type_options = ["All"] + sorted(df["match_type"].dropna().unique().tolist())
gender_options = ["All"] + sorted(df["gender_category"].dropna().unique().tolist())

selected_tournament = st.sidebar.selectbox("Tournament Category", tournament_options)
selected_match_type = st.sidebar.selectbox("Match Type", match_type_options)
selected_gender = st.sidebar.selectbox("Gender Category", gender_options)

# ---------------------------------
# Apply Filters
# ---------------------------------
filtered_df = df.copy()

if selected_tournament != "All":
    filtered_df = filtered_df[filtered_df["tournament_category"] == selected_tournament]

if selected_match_type != "All":
    filtered_df = filtered_df[filtered_df["match_type"] == selected_match_type]

if selected_gender != "All":
    filtered_df = filtered_df[filtered_df["gender_category"] == selected_gender]

# ---------------------------------
# Data Preview
# ---------------------------------
st.subheader("📋 Competitions Data Preview")
st.dataframe(filtered_df.head(20), use_container_width=True)

# ---------------------------------
# Summary Section
# ---------------------------------
st.subheader("📊 Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Competitions", filtered_df.shape[0])

with col2:
    st.metric("Match Types", filtered_df["match_type"].nunique())

with col3:
    st.metric("Tournament Categories", filtered_df["tournament_category"].nunique())

# ---------------------------------
# Visual Analysis
# ---------------------------------
st.subheader("📈 Visual Analysis")

# Match Type Distribution
st.markdown("### Match Type Distribution")
match_type_counts = (
    filtered_df["match_type"]
    .value_counts()
    .reset_index()
)
match_type_counts.columns = ["Match Type", "Count"]
st.bar_chart(match_type_counts.set_index("Match Type"))

# Tournament Category Distribution
st.markdown("### Tournament Category Distribution")
tournament_counts = (
    filtered_df["tournament_category"]
    .value_counts()
    .reset_index()
)
tournament_counts.columns = ["Tournament Category", "Count"]
st.bar_chart(tournament_counts.set_index("Tournament Category"))

# Top 10 Tournament Categories
st.markdown("### 🏆 Top 10 Tournament Categories")
top_tournaments = (
    filtered_df["tournament_category"]
    .value_counts()
    .head(10)
    .reset_index()
)
top_tournaments.columns = ["Tournament Category", "Count"]
st.bar_chart(top_tournaments.set_index("Tournament Category"))

# Gender Category Distribution
st.markdown("### 👥 Gender Category Distribution")
gender_counts = (
    filtered_df["gender_category"]
    .value_counts()
    .reset_index()
)
gender_counts.columns = ["Gender", "Count"]
st.bar_chart(gender_counts.set_index("Gender"))

# ---------------------------------
# Footer
# ---------------------------------
st.markdown("---")
st.caption("📊 Tennis SportRadar Analytics Dashboard | Built with Streamlit")