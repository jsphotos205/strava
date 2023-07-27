# Mapping with Folium

Following is a walkthrough of using the Folium library to map decoded Google Polyline.

The original file can be found on [GitHub](https://github.com/jsphotos205/strava "GitHub link") as a python file under the name [mapping.py](https://github.com/jsphotos205/strava/blob/main/mapping.py "Github link"). We are using .csv files that were processed in the [strava_api.ipynb](https://github.com/jsphotos205/strava/blob/main/strava_api.ipynb "Github link") Jupyter Notebook located in the same GitHub repo.

---

First we want to import all required libraries into the python script. The 'literal_eval' funciton from the 'ast' (Abstract Syntax Trees) module is used to safely evaluate and conver a string containing a Python literal or container to display its corresponding data type.

```python
import pandas as pd
import folium
from ast import literal_eval
import os
```

Next we want to read in the .csv files that were created using the [strava_api.ipynb](https://github.com/jsphotos205/strava/blob/main/strava_api.ipynb "Github link") into pandas DataFrames for each respecting loop and run.

```python
all_pmrp = pd.read_csv('csv/run/rrgcc/all_pmrp.csv')
all_lode = pd.read_csv('csv/run/rrgcc/all_lode.csv')
only_lode = pd.read_csv('csv/run/rrgcc/only_lode.csv')
all_sore_heel = pd.read_csv('csv/run/rrgcc/all_sore_heel.csv')
only_sore_heel = pd.read_csv('csv/run/rrgcc/only_sore_heel.csv')
all_drive_by = pd.read_csv('csv/run/rrgcc/all_drive_by.csv')
only_drive_by = pd.read_csv('csv/run/rrgcc/only_drive_by.csv')
only_arena_loop = pd.read_csv('csv/run/rrgcc/only_arena.csv')
```

For effiency I wrote a function that contains all mapping capabilities to use on the run_data. First it iterates over each row in the run_data and then extracts the latitude and longitude values from the 'start_latlng' column to be used for setting a start location for the folium Map. We can then modify the map with some markers and popup capabilites for start/finish information.

```python
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
```

In the same function we iterate over the rows again and pull out the 'decoded_polyline'. Within the 'decoded_polyline' column we extract the list of latitude and longitude coordinates for each run. Using this polyline variable we then create a folium FeatureGroup to hold the polyline information. We can then use the folium Polyline capability to add each individual latitude and longitude to the FeatureGroup and then add to the folium Map. We also save the map information as a .html file to be later used in the Streamlit app.

```python
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
```

Finally, we can now input the run_data to the mapping function to create beautiful and interactive maps for further route exploration and mapping.

```python
#Create an interactive map for all the running data provided to the function
PMRP_Map(all_pmrp, 'all_pmrp')
PMRP_Map(all_lode, 'all_lode')
PMRP_Map(only_lode, 'only_lode')
PMRP_Map(all_sore_heel, 'all_sore_heel')
PMRP_Map(only_sore_heel, 'only_sore_heel')
PMRP_Map(all_drive_by, 'all_drive_by')
PMRP_Map(only_drive_by, 'only_drive_by')
PMRP_Map(only_arena_loop, 'only_arena')
```
