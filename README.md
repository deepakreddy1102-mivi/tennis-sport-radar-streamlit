# Tennis SportRadar Analytics Dashboard

A fully interactive analytics dashboard built using **Streamlit**, designed to analyze global tennis competition data sourced from **SportRadar**.

🔗 **Live App**:  
https://tennis-sport-radar-app-jjb8xifzy7oxws3et8dp67.streamlit.app/

---

## Project Overview

This project provides insights into tennis competitions across different:
- Tournament categories
- Match types
- Gender categories

The dashboard supports dynamic filtering, summary KPIs, and visual analysis while handling edge cases gracefully when no data matches selected filters.

---

## Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **Matplotlib**
- **MySQL** (used during data extraction phase)
- **GitHub**
- **Streamlit Cloud**

---

## Data Pipeline

1. Raw tennis competition data extracted from **MySQL**
2. Data exported to **CSV** format for cloud deployment
3. Streamlit app reads data directly from CSV
4. Filters dynamically update tables, KPIs, and charts

---

## Dashboard Features

- Interactive sidebar filters:
  - Tournament Category
  - Match Type
  - Gender Category
- Data preview table
- KPI summary:
  - Total Competitions
  - Match Types count
  - Tournament Categories count
- Visual analysis:
  - Match Type Distribution
  - Tournament Category Distribution
  - Gender Category Distribution
- Graceful handling of empty filter results

---

## Deployment

The application is deployed on **Streamlit Cloud** and automatically updates when changes are pushed to the GitHub repository.

---
