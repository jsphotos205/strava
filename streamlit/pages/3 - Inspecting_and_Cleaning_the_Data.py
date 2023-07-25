import streamlit as st
from Home import *

def main():

    data_inspection_content = load_markdown_file('streamlit/pages/md/Data_Inspection_Content.md')

    st.markdown(data_inspection_content, unsafe_allow_html=True)
    
if __name__ == '__main__':
    main()