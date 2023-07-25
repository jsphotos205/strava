import streamlit as st
from Home import *

def main():

    google_polyline_content = load_markdown_file('streamlit/pages/md/Google_Polyline.md')

    st.markdown(google_polyline_content, unsafe_allow_html=True)
    

if __name__ == '__main__':
    main()