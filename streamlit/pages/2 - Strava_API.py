import streamlit as st
from Home import *

def main():

    st.set_page_config(page_title='RRGCC Running and Weather Data : Strava API',
                       page_icon= ':runner:')
    
    strava_api_content = load_markdown_file('streamlit/pages/md/Strava_API.md')

    st.markdown(strava_api_content, unsafe_allow_html=True)

if __name__ == '__main__':
    main()