import streamlit as st
from Home import Page_Config
from Home import load_markdown_file

def main():

    page_config = Page_Config()
    page_config.set_page_config()

    mapping_content = load_markdown_file('streamlit/pages/md/Mapping.md')
    st.markdown(mapping_content, unsafe_allow_html=True)

if __name__ == '__main__':
    main()