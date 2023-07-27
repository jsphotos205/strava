import pandas as pd
import ydata_profiling as yprof
import streamlit as st
import os
from Home import Page_Config


from streamlit_pandas_profiling import st_profile_report


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
                    # 'snow',
                    # 'wdir',
                    'wspd',
                    'pres']
    return df[column_order]

def main():
    
    page_config = Page_Config()
    page_config.set_page_config()
    
    st.title('Summary Report:')
    
    data_dir = 'csv/run/rrgcc'
    csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    selected_file = st.selectbox(':runner: Select a Loop for Summary Report:', csv_files, index=0)

    selected_run_name = None

    if selected_file != 'Default':

        def pandas_report():
            file_path = os.path.join(data_dir, selected_file)
            selected_file_name = selected_file.rstrip('.csv')
            run_data = load_data(file_path)
            run_data = reorder_columns(df=run_data)

            if run_data is not None:
                profile = yprof.ProfileReport(run_data)
                st.title(f'{selected_file_name} Report :')
                profile = st_profile_report(profile)
                return(profile)
            else:
                st.write('Error : Failed to load data from the csv file')
        pandas_report()

if __name__ == '__main__':
    main()