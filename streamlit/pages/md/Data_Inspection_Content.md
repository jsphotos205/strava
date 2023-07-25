# Inspecting and Cleaning Activities Data

### Following is the source code I used for digging further into the data that was collected from the Strava API.

Looking to where the data could be cleaned:

* Columns that void of information due to no use of heart monitor or watch that tracks health data as such.
  * Could have further development if data was present.
* Personally not interested in the social-networking side of Strava
  * i.e. photos, kudos, etc.
* Noticed that column values 'location_city' and 'location_stat' actually contained no location information.
  * Location information can be acquired via Google Polyline information which is found in the 'map' column
    * [Google Polyline](https://developers.google.com/maps/documentation/utilities/polylineutility "Google Polyline Developers Page")
    * Explained further on the next page.

```python
all_strava_activites.head()
all_strava_activites_columns = all_strava_activites.columns.to_list()
all_strava_activites_columns

# Define the columns to drop from the DataFrame
columns_to_drop = ['athlete',
                   'resource_state', 
                   'sport_type', 
                   'workout_type',
                   'location_city',
                   'location_state',
                   'location_country', 
                   'kudos_count', 
                   'comment_count', 
                   'athlete_count', 
                   'photo_count', 
                   'trainer', 
                   'commute', 
                   'manual', 
                   'private',
                   'visibility', 
                   'flagged', 
                   'gear_id', 
                   'has_heartrate', 
                   'heartrate_opt_out', 
                   'display_hide_heartrate_option', 
                   'from_accepted_tag', 
                   'total_photo_count', 
                   'has_kudoed', 
                   'average_watts', 
                   'kilojoules',
                   'achievement_count',
                   'device_watts',
                   'upload_id_str',
                   'upload_id',
                   'external_id', 
                   'suffer_score']

# Drop the specified columns from the DataFrame
all_strava_activites.drop(columns=columns_to_drop, inplace=True)

columns = all_strava_activites.columns.to_list()

columns
```

## Creating a Pandas Datframe for just the activity of Running

Filter the data where the column 'type' is equal to 'Run'

```python
run_data = all_strava_activites.loc[all_strava_activites['type'] == 'Run']

# Reset the index of the DataFrame after filtering
run_data.reset_index(drop=True, inplace=True)
```

## Conversions

* Calculate miles, minutes, and hours
* Column 'distance' is in meters
* Column 'moving_time' is in seconds

```python
# Calculate and add new columns, 'distance_miles', 'moving_time_minutes', and 'moving_time_hours, rounded to 2 decimal places
run_data['distance_miles'] = round(run_data.loc[:,('distance')] * 0.00062137119, 2)
run_data['moving_time_minutes'] = round(run_data.loc[:,('moving_time')] / 60, 2)
run_data['moving_time_hours'] = round(run_data.loc[:,('moving_time')] / 3600, 2)
```

```python
# Calculate averages for miles and time
average_distance_miles = round(run_data['distance_miles'].mean(), 2)
print("Average Distance (miles):", average_distance_miles)
average_time_minutes = round(run_data['moving_time_minutes'].mean(), 2)
print("Average Time Ran (minutes):", average_time_minutes)

# Calculate distance for longest run
max_distance_ran = round(run_data['distance_miles'].max(), 2)
print("Longest Run:", max_distance_ran, "miles")

# Calculate total time ran
max_duration_mintues = round(run_data['moving_time_minutes'].max(), 2)
max_duration_hours = round(run_data['moving_time_hours'].max(), 2)
print("Longest Duration:", max_duration_mintues,"minutes. Converted to hours:", max_duration_hours)

# Calculate total miles ran
total_distance_miles = round(run_data['distance'].sum() * 0.00062137119, 2)
print("Total Distance Covered to the date (miles):", total_distance_miles)
```
