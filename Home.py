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
refresh_cookie_btn = st.sidebar.button(label="Refresh Cookies", help="If you run into errors, try refreshing Bard and copy-paste the new cookies here")


# Variables
queryString = "Write an ESG report for the company {} based on data from {} to {}"
# if orgString and startDate and endDate and PSID and PSIDTS:
# queryString.format(orgString, startDate.year, endDate.year)

# Query Output
st.header("Search Query")
st.subheader("Your search query looks like this:")
st.write(queryString.format(orgString, startDate.year, endDate.year))

if orgString and startDate and endDate and PSID and PSIDTS:
    try:
        from LLMUtils import BardAPIConsumer
        llm = BardAPIConsumer(PSID=PSID, PSIDTS=PSIDTS)
        st.write(llm.get_report_text(queryString.format(
            orgString, startDate.year, endDate.year)))
        if generate_doc:
            byteIO = llm.export_word(llm.get_report_text(
                queryString.format(orgString, startDate.year, endDate.year)))
            if st.download_button("Download Generated Document", file_name='report.docx', data=byteIO.getvalue()):
                    # st.download_button()
                st.toast("Downloading File!")
        if refresh_cookie_btn:
            llm.refresh_cookies(PSID=PSID, PSIDTS=PSIDTS)
            st.toast("Cookies Refreshed")
        
        st.write(llm.get_viz_data())
    except Exception as exp:
        st.warning(*exp.args)
        st.warning("Please try refreshing cookies or try later if it doesn't work")