import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Trader Behavior vs Market Sentiment Dashboard")

# Load data
data = pd.read_csv("data/merged_data.csv")

# recreate features if not saved
data["sentiment_group"] = data["sentiment"].replace({
    "Extreme Fear": "Fear",
    "Extreme Greed": "Greed"
})

data["position_type"] = data["Direction"].apply(
    lambda x: "Long" if "Long" in x else ("Short" if "Short" in x else "Other")
)
st.sidebar.header("Filters")

sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment",
    data["sentiment_group"].unique(),
    default=data["sentiment_group"].unique()
)

filtered = data[data["sentiment_group"].isin(sentiment_filter)]

# ---- Sentiment Distribution ----

st.subheader("Trade Distribution by Sentiment")

fig, ax = plt.subplots()
sns.countplot(x="sentiment_group", data=filtered, ax=ax)

st.pyplot(fig)

# ---- PnL vs Sentiment ----

st.subheader("PnL Distribution by Sentiment")

fig, ax = plt.subplots()
sns.boxplot(x="sentiment_group", y="Closed PnL", data=filtered, ax=ax)

st.pyplot(fig)

# ---- Trade Size vs Sentiment ----

st.subheader("Trade Size by Sentiment")

fig, ax = plt.subplots()
sns.boxplot(x="sentiment_group", y="Size USD", data=filtered, ax=ax)

st.pyplot(fig)