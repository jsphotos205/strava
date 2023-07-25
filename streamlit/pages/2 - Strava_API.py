import streamlit as st
from Home import *

def main():
    
    strava_api_content = load_markdown_file('streamlit/pages/md/Strava_API.md')

    st.markdown(strava_api_content, unsafe_allow_html=True)

if __name__ == '__main__':
    main()