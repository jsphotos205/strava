import streamlit as st
from streamlit.components.v1 import html

def load_markdown_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def main():

    st.title('About')

    about_content = load_markdown_file('streamlit/pages/md/About.md')

    st.markdown(about_content, unsafe_allow_html=True)

if __name__ == '__main__':
    main()