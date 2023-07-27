import streamlit as st
from Home import *

def main():
    page_config = Page_Config()
    page_config.set_page_config()

    mapping_content = load_markdown_file('streamlit/pages/md/Mapping.md')
    mapping_content

if __name__ == '__main__':
    main()