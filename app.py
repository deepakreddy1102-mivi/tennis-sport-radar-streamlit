import streamlit as st
import pandas as pd
import mysql.connector
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
# MySQL Connection (LOCAL + CLOUD SAFE)
# ---------------------------------
def get_connection():
    """
    Uses Streamlit secrets in deployment
    Falls back to local credentials when running locally
    """
    try:
        conn = mysql.connector.connect(
            host=st.secrets["mysql"]["host"],
            user=st.secrets["mysql"]["user"],
            password=st.secrets["mysql"]["password"],
            database=st.secrets["mysql"]["database"],
            port=st.secrets["mysql"].get("port", 3306)
        )
        return conn
    except Exception:
        # LOCAL fallback (your system)
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Samsung987",   # ONLY used locally
            database="tennis_sport_radar"
        )
        return conn

try:
    conn = get_connection()
    st.success("Data loaded successfully from MySQL!")
except Exception as e:
    st.error(f"MySQL Connection Failed: {e}")
    st.stop()

# ---------------------------------
# Load Data
# ---------------------------------
query = """
SELECT
    competition_id,
    competition_name,
    match_type,
    tournament_category,
    gender_category
FROM competitions
"""

df = pd.read_sql(query, conn)

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
st.caption("📊 Tennis SportRadar Analytics Dashboard | Built with Streamlit & MySQL")