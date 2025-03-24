# import home_page
# import patents_page
import LLM_page
import streamlit as st
import os

# Set the page configuration
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"


def main():
    # Page navigation
    # page = st.sidebar.selectbox("Select a page", ["Home Page", "Patents Page", "Drug Pipeline Page", "Clinical Trials Page", "LLM Chatbot"])

    # if page == "Home Page":
    #     home_page.home_page()
    # elif page == "Patents Page":
    #     patents_page.patents_page()
    # elif page == "Drug Pipeline Page":
    #     drug_pipeline_page.drug_pipeline_page()
    # elif page == "Clinical Trials Page":
    #     clinical_trials_page.clinicalTrials_page()
    # else:
        LLM_page.LLM_chatbot()

if __name__ == "__main__":
    main()
