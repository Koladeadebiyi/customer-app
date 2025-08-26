import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(
    page_title="🛒 Customer Recommendation System",
    page_icon="🛍️",
    layout="wide"
)

# Load Data
customer_features_with_clusters = pd.read_csv("customer_features_with_clusters.csv")
top_products_per_cluster = pd.read_csv("top_products_per_cluster.csv")

# Title
st.title("🛍️ Smart Customer Recommendations")

# Select Customer
customer_id = st.selectbox(
    "Select Customer ID",
    customer_features_with_clusters['CustomerID'].unique()
)

# Find customer’s cluster
cluster = customer_features_with_clusters.loc[
    customer_features_with_clusters['CustomerID'] == customer_id, 
    'Cluster'
].values[0]

# Show customer info in a "card" style
col1, col2 = st.columns(2)
with col1:
    st.metric("Customer ID", customer_id)
with col2:
    st.metric("Cluster", cluster)

# Recommended Products
st.subheader("✨ Recommended Products for this Cluster")
recs = top_products_per_cluster[top_products_per_cluster['Cluster'] == cluster]

if recs.empty:
    st.warning("⚠️ No products found for this cluster.")
else:
    st.dataframe(
        recs[['StockCode', 'Description', 'Quantity']],  # ✅ fixed column name
        use_container_width=True
    )
