import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px

# --- Page Config ---
st.set_page_config(page_title="Marketing Campaign Dashboard", layout="wide")

# --- Connect to MySQL ---
def load_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",          
        password="Bholu@0352",  
        database="marketing_campaign"
    )
    query = "SELECT * FROM customers"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

df = load_data()

# --- Dashboard Title ---
st.title("📊 Marketing Campaign Analysis Dashboard")

# --- Sidebar Filters ---
st.sidebar.header("Filters")
country = st.sidebar.selectbox("Select Country", df["Country"].unique())
education = st.sidebar.multiselect("Select Education Level", df["Education"].unique())
marital = st.sidebar.multiselect("Select Marital Status", df["Marital_Status"].unique())
income_range = st.sidebar.slider("Income Range", int(df["Income"].min()), int(df["Income"].max()))

# Apply filters
filtered_df = df[(df["Country"] == country) & (df["Income"] <= income_range)]
if education:
    filtered_df = filtered_df[filtered_df["Education"].isin(education)]
if marital:
    filtered_df = filtered_df[filtered_df["Marital_Status"].isin(marital)]

# --- KPI Metrics ---
st.subheader("Key Performance Indicators")
response_rate = filtered_df["Response"].mean() * 100
avg_spend = filtered_df["Total_Spend"].mean()
avg_visits = filtered_df["NumWebVisitsMonth"].mean()
avg_age = filtered_df["Age"].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Response Rate (%)", f"{response_rate:.2f}")
col2.metric("Average Spend", f"₹{avg_spend:,.0f}")
col3.metric("Avg Web Visits", f"{avg_visits:.2f}")
col4.metric("Average Age", f"{avg_age:.1f}")

# --- Layout: Charts side by side ---
colA, colB = st.columns(2)

with colA:
    st.subheader("Spending Patterns by Product")
    spend_cols = ["MntWines","MntFruits","MntMeatProducts","MntFishProducts","MntSweetProducts","MntGoldProds"]
    spend_data = filtered_df[spend_cols].mean().reset_index()
    spend_data.columns = ["Product","Avg Spend"]
    fig = px.bar(spend_data, x="Product", y="Avg Spend", color="Product",
                 text="Avg Spend", color_discrete_sequence=px.colors.qualitative.Set2)
    fig.update_traces(texttemplate='%{text:.1f}', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

with colB:
    st.subheader("Channel Usage")
    channel_cols = ["NumWebPurchases","NumCatalogPurchases","NumStorePurchases","NumDealsPurchases"]
    channel_data = filtered_df[channel_cols].mean().reset_index()
    channel_data.columns = ["Channel","Avg Purchases"]
    fig2 = px.pie(channel_data, names="Channel", values="Avg Purchases",
                  hole=0.4, color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig2, use_container_width=True)

# --- Campaign Performance ---
st.subheader("Campaign Performance")
campaign_cols = ["AcceptedCmp1","AcceptedCmp2","AcceptedCmp3","AcceptedCmp4","AcceptedCmp5","Response"]
campaign_data = filtered_df[campaign_cols].mean().reset_index()
campaign_data.columns = ["Campaign","AcceptanceRate"]
campaign_data["AcceptanceRate"] *= 100
fig3 = px.bar(campaign_data, x="Campaign", y="AcceptanceRate", color="Campaign",
              text="AcceptanceRate", color_discrete_sequence=px.colors.qualitative.Bold)
fig3.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
st.plotly_chart(fig3, use_container_width=True)

# --- Segment KPIs ---
st.subheader("Segment KPIs")
segment_summary = filtered_df.groupby("Marital_Status")[["Total_Spend","Response"]].mean().reset_index()
segment_summary["Response"] = segment_summary["Response"] * 100
st.dataframe(segment_summary)

# --- Age vs Spend Trend ---
st.subheader("Age vs Spend Trend")
fig4 = px.scatter(filtered_df, x="Age", y="Total_Spend", color="Response",
                  size="Income", hover_data=["Education","Marital_Status"],
                  template="plotly_white")
st.plotly_chart(fig4, use_container_width=True)

# --- Download Filtered Data ---
st.download_button(
    label="Download Filtered Data",
    data=filtered_df.to_csv(index=False).encode("utf-8"),
    file_name="filtered_customers.csv",
    mime="text/csv"
)
