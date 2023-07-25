import pandas as pd
import folium
from ast import literal_eval
import os

all_pmrp = pd.read_csv('csv/run/rrgcc/all_pmrp.csv')
all_lode = pd.read_csv('csv/run/rrgcc/all_lode.csv')
only_lode = pd.read_csv('csv/run/rrgcc/only_lode.csv')
all_sore_heel = pd.read_csv('csv/run/rrgcc/all_sore_heel.csv')
only_sore_heel = pd.read_csv('csv/run/rrgcc/only_sore_heel.csv')
all_drive_by = pd.read_csv('csv/run/rrgcc/all_drive_by.csv')
only_drive_by = pd.read_csv('csv/run/rrgcc/only_drive_by.csv')

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

PMRP_Map(all_pmrp, 'all_pmrp')
PMRP_Map(all_lode, 'all_lode')
PMRP_Map(only_lode, 'only_lode')
PMRP_Map(all_sore_heel, 'all_sore_heel')
PMRP_Map(only_sore_heel, 'only_sore_heel')
PMRP_Map(all_drive_by, 'all_drive_by')
PMRP_Map(only_drive_by, 'only_drive_by')