import streamlit as st
import pandas as pd
import os


def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def main():

    st.title('RRGCC Running Data')

    data_dir = 'csv/run/rrgcc/rrgcc_loops/'

    csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    selected_file = st.selectbox('Select:', csv_files, index=0)

    if selected_file:
        file_path = os.path.join(data_dir, selected_file)
        run_data = load_data(file_path)

        st.subheader('Run Previews')
        st.dataframe(run_data)

        st.subheader('Run Summaries')
        st.write(run_data.describe())

    st.title('Folium Map Viewer')

    map_dir = 'maps/'

    map_files = [f for f in os.listdir(map_dir) if f.endswith('html')]

    selected_map = st.selectbox('Select a Map:', map_files, index=0)

    if selected_map:
        map_path = os.path.join(map_dir, selected_map)

        with open(map_path, 'r') as f:
            map_html = f.read()

        st.components.v1.html(map_html, width=800, height=600)
    

if __name__ == '__main__':
    main()