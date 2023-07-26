import streamlit as st

def centered_header(text):
    st.markdown(f"<h1 style='text_align: center;'>{text}</h1>", unsafe_allow_html=True)

def centered_subheader(text):
    """Custom function to display a centered-aligned subheader."""
    st.markdown(f"<h2 style='text-align: center;'>{text}</h2>", unsafe_allow_html=True)

def load_markdown_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def set_page_config(page_title, page_icon):
    return ('RRGCC Running and Weather', ':runner:')

def main():

    set_page_config(page_title=True, page_icon=True)

    header_path = 'images/rrgcc.png'
    st.image(header_path, use_column_width=True, width=100)

    centered_header('Running and Weather Data Analysis')
    centered_subheader('on RRGCC operated land')

    st.sidebar.success('Select a demo above.')

    home_content = load_markdown_file('streamlit/pages/md/Home.md')
    st.markdown(home_content, unsafe_allow_html=True)
    
if __name__ == '__main__':
    main()