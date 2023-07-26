import streamlit as st
from Home import *

def main():
    
    rrgcc_content = load_markdown_file('streamlit/pages/md/RRGCC_Land.md')

    st.markdown(rrgcc_content, unsafe_allow_html=True)

if __name__ == '__main__':
    main()