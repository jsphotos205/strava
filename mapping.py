import pandas as pd
import folium
from ast import literal_eval
import os

pmrp_run = pd.read_csv('csv/run/rrgcc/rrgcc_combined_loops/pmrp_run_data.csv')
lode_loop = pd.read_csv('csv/run/rrgcc/rrgcc_combined_loops/lode_loop_data.csv')
only_lode_loop = pd.read_csv('csv/run/rrgcc/rrgcc_loops/only_lode_loop.csv')
sore_heel_loop = pd.read_csv('csv/run/rrgcc/rrgcc_combined_loops/sore_heel_data.csv')
only_sore_heel_loop = pd.read_csv('csv/run/rrgcc/rrgcc_loops/only_sore_heel_loop.csv')
drive_by_loop = pd.read_csv('csv/run/rrgcc/rrgcc_combined_loops/drive_by_data.csv')
only_drive_by_loop = pd.read_csv('csv/run/rrgcc/rrgcc_loops/only_drive_by_loop.csv')

def PMRP_Map(df, map_name):

    for index, row in df.iterrows():

        row = literal_eval(row['start_latlng'])
        # print(row)
        lat, lng = row[0], row[1]
        # print(lat, lng)
        lat = float(lat)
        lng = float(lng)

        m = folium.Map(location=[lat, lng],
                       zoom_start=15)

        tool_tip = 'Click For Start / Finish Location'
        folium.Marker(location=[lat,lng],
                      popup=f'<i>Start / Finish: {lat},{lng}<i>',
                      icon=folium.Icon(color='darkblue',
                                       icon_color='white',
                                       icon='fa-person-running',
                                       prefix='fa'),
                      tooltip=tool_tip).add_to(m)
    
    for index, row in df.iterrows():
            
        polyline = literal_eval(row['decoded_polyline'])

        feature_group = folium.FeatureGroup()

        folium.PolyLine(locations=polyline, color='red').add_to(feature_group)

        feature_group.add_to(m)
        
        map_file_name = f'{map_name}.html'
        map_path = os.path.join('maps', map_file_name)
        m.save(map_path)
        
    return(m)

PMRP_Map(pmrp_run, 'all_pmrp')
PMRP_Map(lode_loop, 'all_lode_loops')
PMRP_Map(only_lode_loop, 'only_lode_loop')
PMRP_Map(sore_heel_loop, 'all_sore_heel_loops')
PMRP_Map(only_sore_heel_loop, 'only_sore_heel_loop')
PMRP_Map(drive_by_loop, 'all_drive_by_loops')
PMRP_Map(only_drive_by_loop, 'only_drive_by_loop')