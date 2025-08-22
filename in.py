import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Supermarket Sales Tracker", layout="wide")
st.title("🛒 Supermarket Daily Sales Tracker")

# Initialize session state
if "sales" not in st.session_state:
    st.session_state.sales = pd.DataFrame(columns=["Product", "Quantity", "Price", "Revenue"])

# ---- Sales Form ----
with st.form(key="sales_form"):
    st.subheader("Add a Sale")
    product = st.text_input("Product")
    quantity = st.number_input("Quantity", min_value=1, step=1)
    price = st.number_input("Price", min_value=0.0, step=0.5)
    submitted = st.form_submit_button("Add Sale")

    if submitted and product:
        revenue = quantity * price
        new_row = {"Product": product, "Quantity": quantity, "Price": price, "Revenue": revenue}
        st.session_state.sales = pd.concat([st.session_state.sales, pd.DataFrame([new_row])], ignore_index=True)
        st.success(f"✅ Added {product} (Qty: {quantity}, Price: {price}) → Revenue: {revenue}")

# ---- Sales Records ----
st.subheader("📊 Sales Records")
st.dataframe(st.session_state.sales, use_container_width=True)

# ---- Summary ----
if not st.session_state.sales.empty:
    total_revenue = st.session_state.sales["Revenue"].sum()
    total_items = st.session_state.sales["Quantity"].sum()
    st.metric("Total Revenue", f"${total_revenue:,.2f}")
    st.metric("Total Items Sold", total_items)

    # ---- Charts ----
    col1, col2 = st.columns(2)

    with col1:
        fig = px.bar(st.session_state.sales, x="Product", y="Revenue", color="Product",
                     title="Revenue by Product", text="Revenue")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig2 = px.pie(st.session_state.sales, names="Product", values="Revenue", title="Revenue Share by Product")
        st.plotly_chart(fig2, use_container_width=True)
