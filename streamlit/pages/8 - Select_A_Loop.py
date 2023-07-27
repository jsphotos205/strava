import streamlit as st
import pandas as pd
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from Home import Page_Config

st.set_option('deprecation.showPyplotGlobalUse', False)

class Temp_Graphs:

    def create_temperature_graphs(self, df):
        if len(df) > 1:
            fig, axes = plt.subplots(2, 2, figsize=(12, 10))
            fig.suptitle('Temperature vs. Running Performance')

            sns.scatterplot(ax=axes[0, 0], data=df, x='tavg', y='moving_time_minutes')
            axes[0, 0].set_xlabel('Average Temperature (°F)')
            axes[0, 0].set_ylabel('Moving Time (minutes)')

            sns.scatterplot(ax=axes[0, 1], data=df, x='tavg', y='average_speed')
            axes[0, 1].set_xlabel('Average Temperature (°F)')
            axes[0, 1].set_ylabel('Average Speed (mph)')

            sns.scatterplot(ax=axes[1, 0], data=df, x='tavg', y='max_speed')
            axes[1, 0].set_xlabel('Average Temperature (°F)')
            axes[1, 0].set_ylabel('Max Speed (mph)')

            sns.scatterplot(ax=axes[1, 1], data=df, x='tavg', y='total_elevation_gain')
            axes[1, 1].set_xlabel('Average Temperature (°F)')
            axes[1, 1].set_ylabel('Total Elevation Gain (feet)')

            plt.tight_layout()
            st.pyplot(fig)
        elif len(df) == 1:
            st.write('Only one entry for loop, cannot create temperature comparison graph for loop.')
        else:
            st.write('No run data.')

# @st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# @st.cache_data
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

def highlight_max_values(val, df):

    max_minutes = val == df['moving_time_minutes'].max()
    max_distance = val == df['distance_miles'].max()
    max_speed = val == df['max_speed'].max()
    max_avg_speed = val == df['average_speed'].max()
    max_elevation_gain = val == df['total_elevation_gain'].max()
    max_elevation = val == df['elev_high'].max()
    max_elevation_low = val == df['elev_low'].max()
    max_pr_count = val == df['pr_count'].max()
    max_tavg = val == df['tavg'].max()
    max_tmax = val == df['tmax'].max()
    max_tmin = val == df['tmin'].max()
    max_prcp = val == df['prcp'].max()
    max_wspd = val == df['wspd'].max()
    max_pres = val == df['pres'].max()

    max_background_color = 'background-color : red'

    max_minutes_style = f'{max_background_color}' if max_minutes else ''
    max_distance_style = f'{max_background_color}' if max_distance else ''
    max_speed_style = f'{max_background_color}' if max_speed else ''
    max_avg_speed_style = f'{max_background_color}' if max_avg_speed else ''
    max_elevation_gain_style = f'{max_background_color}' if max_elevation_gain else ''
    max_elevation_style = f'{max_background_color}' if max_elevation else ''
    max_elevation_low_style = f'{max_background_color}' if max_elevation_low else ''
    max_pr_count_style =f'{max_background_color}' if max_pr_count else ''
    max_tavg_style =f'{max_background_color}' if max_tavg else ''
    max_tmax_style =f'{max_background_color}' if max_tmax else ''
    max_tmin_style = f'{max_background_color}' if max_tmin else ''
    max_prcp_style = f'{max_background_color}' if max_prcp else ''
    max_wspd_style = f'{max_background_color}' if max_wspd else ''
    max_pres_style = f'{max_background_color}' if max_pres else ''

    return f'{max_minutes_style}; {max_distance_style}; {max_speed_style}; {max_avg_speed_style}; {max_elevation_gain_style}; {max_elevation_style}; {max_elevation_low_style}; {max_pr_count_style}; {max_tavg_style}; {max_tmax_style}; {max_tmin_style}; {max_prcp_style}; {max_wspd_style}; {max_pres_style}'

def highlight_min_values(val, df): 
    
    min_minutes = val == df['moving_time_minutes'].min()
    min_distance = val == df['distance_miles'].min()
    min_speed = val == df['max_speed'].min()
    min_avg_speed = val == df['average_speed'].min()
    min_elevation_gain = val == df['total_elevation_gain'].min()
    min_elevation = val == df['elev_high'].min()
    min_elevation_low = val == df['elev_low'].min()
    min_pr_count = val == df['pr_count'].min()
    min_tavg = val == df['tavg'].min()
    min_tmax = val == df['tmax'].min()
    min_tmin = val == df['tmin'].min()
    min_prcp = val == df['prcp'].min()
    min_wspd = val == df['wspd'].min()
    min_pres = val == df['pres'].min()

    min_background_color = 'background-color : blue'

    min_minutes_style = f'{min_background_color}' if min_minutes else ''
    min_distance_style = f'{min_background_color}' if min_distance else ''
    min_speed_style = f'{min_background_color}' if min_speed else ''
    min_avg_speed_style = f'{min_background_color}' if min_avg_speed else ''
    min_elevation_gain_style = f'{min_background_color}' if min_elevation_gain else ''
    min_elevation_style = f'{min_background_color}' if min_elevation else ''
    min_elevation_low_style = f'{min_background_color}' if min_elevation_low else ''
    min_pr_count_style =f'{min_background_color}' if min_pr_count else ''
    min_tavg_style =f'{min_background_color}' if min_tavg else ''
    min_tmax_style =f'{min_background_color}' if min_tmax else ''
    min_tmin_style = f'{min_background_color}' if min_tmin else ''
    min_prcp_style = f'{min_background_color}' if min_prcp else ''
    min_wspd_style = f'{min_background_color}' if min_wspd else ''
    min_pres_style = f'{min_background_color}' if min_pres else ''

    return f' {min_minutes_style}; {min_distance_style}; {min_speed_style}; {min_avg_speed_style}; {min_elevation_gain_style}; {min_elevation_style}; {min_elevation_low_style}; {min_pr_count_style}; {min_tavg_style}; {min_tmax_style}; {min_tmin_style}; {min_prcp_style}; {min_wspd_style}; {min_pres_style}'

def main():
    
    page_config = Page_Config()
    page_config.set_page_config()

    data_dir = 'csv/run/rrgcc'

    csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    selected_file = st.selectbox(':runner: Select Run Data:', csv_files, index=0)

    selected_run_name = None

    if selected_file:

        subset = ['moving_time_minutes', 
                  'distance_miles', 
                  'max_speed', 
                  'average_speed', 
                  'total_elevation_gain', 
                  'elev_high', 
                  'elev_low', 
                  'pr_count', 
                  'tavg', 
                  'tmax', 
                  'tmin', 
                  'wspd', 
                  'prcp', 
                  'pres']

        file_path = os.path.join(data_dir, selected_file)
        selected_file_name = selected_file.rstrip('.csv')
        run_data = load_data(file_path)
        run_data = reorder_columns(df=run_data)
        run_data_max = run_data.style.applymap(highlight_max_values, subset=subset, df=run_data)
        run_data_min = run_data.style.applymap(highlight_min_values, subset=subset, df=run_data)


        st.subheader(f'{selected_file_name}:')
        st.dataframe(run_data)
        st.caption(f'Combined run/weather data for {selected_file_name} runs.')

        st.subheader(f'Describe {selected_file_name}:')
        st.write(run_data.describe())
        st.caption('Run Data Description')

        st.subheader(f'Max values:')
        st.dataframe(run_data_max)
        st.caption(f'Max values of {selected_file_name} highlighted in red')

        st.subheader(f'Min values:')
        st.dataframe(run_data_min)
        st.caption(f'Min values of {selected_file_name} highlighted in blue')

        st.title(f'{selected_file_name} Graphs:')
        
        if len(run_data) > 1:
            fig, ax = plt.subplots()
            sns.set_style(style='darkgrid')
            ax = sns.histplot(data=run_data,
                              x='distance_miles',
                              binwidth=.5)
            plt.xlabel('Distance (miles)')
            plt.ylabel('Number of Runs')
            plt.title(f'Mile Concentration of {selected_file_name} Run Data')
            st.pyplot(fig)
        else:
            st.write('Only one entry for this loop, cannot create histogram for loop.')

        temp_graphs = Temp_Graphs()
        temp_graphs.create_temperature_graphs(run_data)

    st.title(f'{selected_file_name} Map:')

    map_dir = 'maps/'

    map_files = [f for f in os.listdir(map_dir) if f.startswith(selected_file_name) and f.endswith('.html')]

    if map_files:
        selected_map = map_files[0]
        map_path = os.path.join(map_dir, selected_map)

        with open(map_path, 'r') as f:
            map_html = f.read()

        st.components.v1.html(map_html, width=800, height=400)

if __name__ == '__main__':
    main()