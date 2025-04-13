import streamlit as st

# Business details
managing_director = "Muhammad Tariq Mahboob"
name = "Tech Solutions"
year_of_establishment = 2010
number_of_employees = 50
revenue_in_dollars = 10000
is_profitable = True

# Streamlit App
st.title("🚀 Business Overview 🚀")

# Adding content with color and icons
st.markdown(f"<h3 style='color:blue;'>👨‍💼 Managing Director: {managing_director}</h3>", unsafe_allow_html=True)
st.markdown(f"<p style='color:green; font-weight:950;'><b>🏢 Business Name:</b> {name}</p>", unsafe_allow_html=True)
st.markdown(f"<p style='color:purple; font-weight:900;'><b>📅 Year of Establishment:</b> {year_of_establishment}</p>", unsafe_allow_html=True)
st.markdown(f"<p style='color:orange; font-weight:900;'><b>👥 Number of Employees:</b> {number_of_employees}</p>", unsafe_allow_html=True)
st.markdown(f"<p style='color:teal; font-weight:900;'><b>💰 Revenue in Dollars:</b> ${revenue_in_dollars}</p>", unsafe_allow_html=True)
st.markdown(f"<p style='color:red; font-weight:900;'><b>📈 Is the Business Profitable?</b> {is_profitable}</p>", unsafe_allow_html=True)