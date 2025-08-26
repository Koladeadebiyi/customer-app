import streamlit as st
import pandas as pd

# ========================
# 1. Load Your Data
# ========================
try:
    customer_features_with_clusters = pd.read_csv("customer_features_with_clusters.csv")
    top_products_per_cluster = pd.read_csv("top_products_per_cluster.csv")
except FileNotFoundError as e:
    st.error(f"❌ File not found: {e}")
    st.stop()

# ========================
# 2. Build Streamlit Interface
# ========================
st.title("🛒 Customer Recommendation System")

# Debugging: show samples
st.write("✅ Customer data sample:", customer_features_with_clusters.head())
st.write("✅ Products data sample:", top_products_per_cluster.head())

# Let user select customer
customer_id = st.selectbox(
    "Select Customer ID",
    customer_features_with_clusters['CustomerID'].unique()
)

# Find customer’s cluster
cluster = customer_features_with_clusters.loc[
    customer_features_with_clusters['CustomerID'] == customer_id, 
    'Cluster'
].values[0]

st.write(f"Customer **{customer_id}** belongs to **Cluster {cluster}**")

# Show recommended products
st.subheader("Recommended Products for this Cluster")
recs = top_products_per_cluster[top_products_per_cluster['Cluster'] == cluster]

if recs.empty:
    st.warning("⚠️ No products found for this cluster.")
else:
    st.table(recs[['StockCode', 'Description', 'Quantity']])
