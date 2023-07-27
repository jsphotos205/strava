import streamlit as st
from Home import *

def main():

    page_config = Page_Config()
    page_config.set_page_config()
    
    strava_api_content = load_markdown_file('streamlit/pages/md/Strava_API.md')

    st.markdown(strava_api_content, unsafe_allow_html=True)

if __name__ == '__main__':
    main()