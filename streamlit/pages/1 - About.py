import streamlit as st
from Home import Page_Config
from Home import load_markdown_file

def main():
    # st.set_page_config(page_title='RRGCC Running and Weather Data', 
    #                    page_icon=':runner:', 
    #                    layout='wide',
    #                    initial_sidebar_state='expanded')    
    page_config = Page_Config()
    page_config.set_page_config()

    about_content = load_markdown_file('streamlit/pages/md/About.md')

    st.markdown(about_content, unsafe_allow_html=True)

if __name__ == '__main__':
    main()