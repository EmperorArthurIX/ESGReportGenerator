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
generate_doc = st.sidebar.button(label="Generate Document")
# download_doc = st.sidebar.button(label = "Download Generated Document")


# Variables
queryString = "Write an ESG report for the company {} based on data from {} to {}"
# if orgString and startDate and endDate and PSID and PSIDTS:
# queryString.format(orgString, startDate.year, endDate.year)

# Query Output
st.header("Search Query")
st.subheader("Your search query looks like this:")
st.write(queryString.format(orgString, startDate.year, endDate.year))

if orgString and startDate and endDate and PSID and PSIDTS:
    from LLMUtils import BardAPIConsumer
    llm = BardAPIConsumer(PSID=PSID, PSIDTS=PSIDTS)
    st.write(llm.get_report_text(queryString.format(
        orgString, startDate.year, endDate.year)))
    if generate_doc:
        llm.export_word(llm.get_report_text(
            queryString.format(orgString, startDate.year, endDate.year)))
        with open("report.docx", 'r+') as file:
            if st.download_button("Download Generated Document", file_name='report.docx', data=file):
                # st.download_button()
                st.success("Downloading File!")
