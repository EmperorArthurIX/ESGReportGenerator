import streamlit as st

st.set_page_config(page_title="ESG Report Generation",
                   layout="centered")

st.title("ESG Report Generation")

# Sidebar Configuration
st.sidebar.header("Search Parameters")
orgString = st.sidebar.text_input("Organisation", placeholder="Example & Sons")
startDate = st.sidebar.date_input(
    "Start Year", help="The starting year for the report data")
endDate = st.sidebar.date_input(
    "End Year", help="The closing year for the report data")
PSID = st.sidebar.text_input("Secure1_PSID Cookie", type="password")
PSIDTS = st.sidebar.text_input("Secure1_PSIDTS Cookie", type="password")

# Variables
queryString = "Write an ESG report for the company {} based on data from {} to {}"
# if orgString and startDate and endDate and PSID and PSIDTS:
# queryString.format(orgString, startDate.year, endDate.year)

# Query Output
st.header("Search Query")
st.subheader("Your search query looks like this:")
st.write(queryString.format(orgString, startDate.year, endDate.year))
