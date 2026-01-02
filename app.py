import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Tennis SportRadar Analytics",
    layout="wide"
)

st.title("🎾 Tennis SportRadar Analytics")

# ---------------- Load Data (CSV ONLY) ----------------
@st.cache_data
def load_data():
    return pd.read_csv("competitions.csv")

try:
    df = load_data()
    st.success("Data loaded successfully from CSV!")
except Exception as e:
    st.error(f"Failed to load data: {e}")
    st.stop()

# ---------------- Sidebar Filters ----------------
st.sidebar.header("🧩 Filter Competitions")

tournament_options = ["All"] + sorted(df["tournament_category"].dropna().unique().tolist())
match_type_options = ["All"] + sorted(df["match_type"].dropna().unique().tolist())
gender_options = ["All"] + sorted(df["gender_category"].dropna().unique().tolist())

selected_tournament = st.sidebar.selectbox("Tournament Category", tournament_options)
selected_match_type = st.sidebar.selectbox("Match Type", match_type_options)
selected_gender = st.sidebar.selectbox("Gender Category", gender_options)

# ---------------- Apply Filters ----------------
filtered_df = df.copy()

if selected_tournament != "All":
    filtered_df = filtered_df[filtered_df["tournament_category"] == selected_tournament]

if selected_match_type != "All":
    filtered_df = filtered_df[filtered_df["match_type"] == selected_match_type]

if selected_gender != "All":
    filtered_df = filtered_df[filtered_df["gender_category"] == selected_gender]

# ---------------- Data Preview ----------------
st.subheader("📋 Competitions Data Preview")
st.dataframe(filtered_df.head(50), use_container_width=True)

# ---------------- Summary ----------------
st.subheader("📊 Summary")

col1, col2, col3 = st.columns(3)
col1.metric("Total Competitions", len(filtered_df))
col2.metric("Match Types", filtered_df["match_type"].nunique())
col3.metric("Tournament Categories", filtered_df["tournament_category"].nunique())

# ---------------- Visual Analysis ----------------
st.subheader("📈 Visual Analysis")

# Match Type Distribution
st.markdown("### Match Type Distribution")
match_counts = filtered_df["match_type"].value_counts()
fig, ax = plt.subplots()
match_counts.plot(kind="bar", ax=ax)
ax.set_xlabel("Match Type")
ax.set_ylabel("Count")
st.pyplot(fig)

# Tournament Category Distribution (Top 10)
st.markdown("### Top 10 Tournament Categories")
tournament_counts = filtered_df["tournament_category"].value_counts().head(10)
fig, ax = plt.subplots()
tournament_counts.plot(kind="bar", ax=ax)
ax.set_xlabel("Tournament Category")
ax.set_ylabel("Count")
st.pyplot(fig)

# Gender Category Distribution
st.markdown("### Gender Category Distribution")
gender_counts = filtered_df["gender_category"].value_counts()
fig, ax = plt.subplots()
gender_counts.plot(kind="bar", ax=ax)
ax.set_xlabel("Gender Category")
ax.set_ylabel("Count")
st.pyplot(fig)
