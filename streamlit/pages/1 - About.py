import streamlit as st
from Home import *

def main():
    st.set_page_config(page_title='RRGCC Running and Weather Data',
                       page_icon= ':runner:',
                       layout='wide',
                       initial_sidebar_state='expanded')

    about_content = load_markdown_file('streamlit/pages/md/About.md')

    st.markdown(about_content, unsafe_allow_html=True)

if __name__ == '__main__':
    main()