#import all required libraries
import pandas as pd
import folium
from ast import literal_eval
import os

#read all csv files generated from the strava_api.ipynb into this mapping function
all_pmrp = pd.read_csv('csv/run/rrgcc/all_pmrp.csv')
all_lode = pd.read_csv('csv/run/rrgcc/all_lode.csv')
only_lode = pd.read_csv('csv/run/rrgcc/only_lode.csv')
all_sore_heel = pd.read_csv('csv/run/rrgcc/all_sore_heel.csv')
only_sore_heel = pd.read_csv('csv/run/rrgcc/only_sore_heel.csv')
all_drive_by = pd.read_csv('csv/run/rrgcc/all_drive_by.csv')
only_drive_by = pd.read_csv('csv/run/rrgcc/only_drive_by.csv')
only_arena_loop = pd.read_csv('csv/run/rrgcc/only_arena.csv')

def PMRP_Map(df, map_name):
    #iterate over each row in the DataFrame 'df'
    for index, row in df.iterrows():
        # Extract the latitude and longitude values from the 'start_latlng' column
        row = literal_eval(row['start_latlng'])
        lat, lng = row[0], row[1]
        # convert latitude and longitude values to floats
        lat = float(lat)
        lng = float(lng)
        # create a folium Map centered at the give latitude and longitude with a zoom level of 15
        m = folium.Map(location=[lat, lng],
                       zoom_start=15)
        #Tooltip text to be displayed when hovering over the marker
        tool_tip = 'Click For Start / Finish Location'
        #Add a marker to the map at the given latitude and longitude with a popup showing the coordinates
        #The marker icon is a person running on a dark blue background
        folium.Marker(location=[lat,lng],
                      popup=f'<i>Start / Finish: {lat},{lng}<i>',
                      icon=folium.Icon(color='darkblue',
                                       icon_color='white',
                                       icon='fa-person-running',
                                       prefix='fa'),
                      tooltip=tool_tip).add_to(m)
    #Iterate over each row in the DataFrame 'df' again
    for index, row in df.iterrows():
        #Extract the list of latitude and longitude coordinates from the 'decoded_polyline' column   
        polyline = literal_eval(row['decoded_polyline'])
        # Create a folium FeatureGroup to hold the polyline
        feature_group = folium.FeatureGroup()
        #Add the polyline to the FeatureGroup with the color 'red'
        folium.PolyLine(locations=polyline, color='red').add_to(feature_group)
        #Add the FeatureGroup to the main map 'm'
        feature_group.add_to(m)
        #Generate the filename for the map and define the path for saving the map
        map_file_name = f'{map_name}.html'
        map_path = os.path.join('maps', map_file_name)
        #Save the map as an html file
        m.save(map_path)
    #return the final map
    return(m)

#Create an interactive map for all the running data provided to the function
PMRP_Map(all_pmrp, 'all_pmrp')
PMRP_Map(all_lode, 'all_lode')
PMRP_Map(only_lode, 'only_lode')
PMRP_Map(all_sore_heel, 'all_sore_heel')
PMRP_Map(only_sore_heel, 'only_sore_heel')
PMRP_Map(all_drive_by, 'all_drive_by')
PMRP_Map(only_drive_by, 'only_drive_by')
PMRP_Map(only_arena_loop, 'only_arena')