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
                    'tmax',
                    'tmin',
                    'prcp',
                    'snow',
                    'wdir',
                    'wspd',
                    'pres']
    return df[column_order]

def highlight_max_values(val, df):
    max_distance = val == df['distance_miles'].max()
    max_speed = val == df['max_speed'].max()
    max_avg_speed = val == df['average_speed'].max()
    max_tmax = val == df['tmax'].max()
    max_tmin = val == df['tmin'].max()
    max_prcp = val == df['prcp'].max()

    background_color = 'background-color : red'

    max_distance_style = f'{background_color}' if max_distance else ''
    max_speed_style = f'{background_color}' if max_speed else ''
    max_avg_speed_style = f'{background_color}' if max_avg_speed else ''
    max_tmax_style =f'{background_color}' if max_tmax else ''
    max_tmin_style = f'{background_color}' if max_tmin else ''
    max_prcp_style = f'{background_color}' if max_prcp else ''

    return f'{max_distance_style}; {max_speed_style}; {max_avg_speed_style}; {max_tmax_style}; {max_tmin_style} {max_prcp_style}'

def main():

    header_path = 'images/rrgcc.png'
    st.image(header_path, use_column_width=True, width=100)

    st.title(':red[Running] and :blue[Weather] Data Analysis')
    

    data_dir = 'csv/run/rrgcc'

    csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    selected_file = st.selectbox('Select Run(s):', csv_files, index=0)

    selected_run_name = None

    if selected_file:

        file_path = os.path.join(data_dir, selected_file)
        selected_file = selected_file.rstrip('.csv')
        run_data = load_data(file_path)
        run_data = reorder_columns(df=run_data)
        run_data_styled = run_data.style.applymap(highlight_max_values, subset=['distance_miles', 'max_speed', 'average_speed', 'tmax', 'prcp'], df=run_data)

        st.subheader(f'{selected_file}:')
        st.dataframe(run_data)
        st.caption(f'Combined run/weather data for {selected_file} runs.')

        st.subheader(f'Describe {selected_file}:')
        st.write(run_data.describe())
        st.caption('Run Data Description')

        st.subheader(f'Max values:')
        st.dataframe(run_data_styled)
        st.caption(f'Max values of {selected_file} highlighted')

    st.title(f'{selected_file} Map:')

    map_dir = 'maps/'

    map_files = [f for f in os.listdir(map_dir) if f.startswith(selected_file) and f.endswith('.html')]

    if map_files:
        selected_map = map_files[0]
        map_path = os.path.join(map_dir, selected_map)

        with open(map_path, 'r') as f:
            map_html = f.read()

        st.components.v1.html(map_html, width=800, height=600)
    

if __name__ == '__main__':
    main()