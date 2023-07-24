import streamlit as st
import pandas as pd
import os
import seaborn as sns

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

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
                    'tmin',
                    'tmax',
                    'prcp',
                    'snow',
                    'wdir',
                    'wspd',
                    'pres']
    return df[column_order]

def main():

    st.title('RRGCC Running Data')

    data_dir = 'csv/run/rrgcc/rrgcc_loops/'

    csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    selected_file = st.selectbox('Select:', csv_files, index=0)

    if selected_file:
        file_path = os.path.join(data_dir, selected_file)
        run_data = load_data(file_path)
        run_data = reorder_columns(df=run_data)

        st.subheader('List of Runs:')
        # run_data = reorder_columns(run_data)
        st.dataframe(run_data)
        st.write(run_data.describe())
        st.caption('Combined run/weather data for RRGCC runs')

    st.title('RRGCC Run Viewer')

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