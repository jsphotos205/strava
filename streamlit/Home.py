import streamlit as st
import pandas as pd
import os

@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)

@st.cache_data
def reorder_columns(df):
    column_order = ['start_date',
                    'name',
                    'moving_time_minutes',
                    'distance_miles',
                    'average_speed',
                    'max_speed',
                    'total_elevation_gain',
                    'elev_high',
                    'elev_low',
                    'pr_count',
                    'tavg',
                    'tmax',
                    'tmin',
                    'prcp',
                    # 'snow',
                    # 'wdir',
                    'wspd',
                    'pres']
    return df[column_order]

def centered_header(text):
    st.markdown(f"<h1 style='text_align: center;'>{text}</h1>", unsafe_allow_html=True)

def centered_subheader(text):
    """Custom function to display a centered-aligned subheader."""
    st.markdown(f"<h2 style='text-align: center;'>{text}</h2>", unsafe_allow_html=True)

def load_markdown_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content


class Page_Config:
    page_title = 'RRGCC Running and Weather Data'
    page_icon = ':runner'
    layout = 'wide'
    initial_sidebar_state = 'expanded'

    def set_page_config(self):
        st.set_page_config(page_title=self.page_title,
                           page_icon=self.page_icon,
                           layout=self.layout,
                           initial_sidebar_state=self.initial_sidebar_state)

def main():

    page_config = Page_Config()
    page_config.set_page_config()
    
    header_path = 'images/rrgcc.png'
    st.image(header_path, use_column_width=True, width=100)

    centered_header('Running and Weather Data Analysis')
    centered_subheader('on RRGCC operated land')

    home_content = load_markdown_file('streamlit/pages/md/Home.md')
    st.markdown(home_content, unsafe_allow_html=True)
    
if __name__ == '__main__':
    main()