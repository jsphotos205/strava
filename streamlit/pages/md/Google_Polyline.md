# Google Polyline

Continuing in the [strava_api.ipynb](https://github.com/jsphotos205/strava/blob/main/strava_api.ipynb "strava_api.ipynb link") we aim to retrieve and decode Google Polyline for mapping and weather location information.

* [Google Polyline Documentation](https://developers.google.com/maps/documentation/utilities/polylineutility "Google Polyline Docs")
* [Polyline Python Library Documentation](https://pypi.org/project/polyline/ "Polyline Module Docs")

When Google Polyline is decoded it outputs longitude and latitude listings for activity. With this information we can then assign a weather station based on the acquired longitude and latitude of the run activity to use for weather data.

```python
# Create a new DataFrame 'all_run_map_data' form the 'map' column in 'run_data' for polyline data
all_run_map_data = pd.DataFrame(run_data['map'].to_list())

# Remove the first character 'a' from the 'id' column to match id's between two DataFrames
all_run_map_data['id'] = all_run_map_data['id'].str.slice(start=1)

# Drop the 'map' column from 'run_data'
run_data.drop(columns='map', inplace=True)
```

```python
# Create a new DataFrame 'decoded_df_all' with columns 'id' and 'decoded_polyline'
decoded_df_all = pd.DataFrame(columns=['id', 'decoded_polyline'])

# Iterate over each row in 'all_run_map_data'
for index, row in all_run_map_data.iterrows():
    polyline_str = row['summary_polyline']

    # Decode the polyline string using 'polyline.decode()'
    decoded_polyline = polyline.decode(polyline_str)

    # Append the decoded polyline and its corresponding ID to 'decoded_df_all'
    decoded_df_all = decoded_df_all.append({'id' : row['id'], 'decoded_polyline' : decoded_polyline}, ignore_index=True)
```

```python
# Print the data type of the 'id' column in both DataFrames
print('ID column datatype in Run Data: ', run_data['id'].dtype)
print('ID column datatype in Decoded Data: ', decoded_df_all['id'].dtype)

# Convert the 'id' column in 'decoded_df_all' to integer data type
decoded_df_all['id'] = decoded_df_all['id'].astype(int)
print('ID column datatype of Decoded Data after convert: ', decoded_df_all['id'].dtype)
```

```python
# Merge the 'run_data' with 'decoded_df_all' on the 'id' column
run_data = pd.merge(run_data, decoded_df_all, on='id')
```

## Prepping Run Data for merge with Weather Data

We are looking to merge the run_data and weather data on date.

* merge on column 'start_date' in run_data
  * change date format to match between the two dataframes

```python
# Convert 'start_date' to datetime format to be index for later merge with weather data
run_data['start_date'] = pd.to_datetime(run_data['start_date'])
run_data['start_date'].dtype
```

```python
# Convert 'start_date' column to date only (removing time information)
run_data['start_date'] = run_data['start_date'].dt.date
print(run_data['start_date'].dtype)

# Convert 'start_date' column to datetime format
run_data['start_date'] = pd.to_datetime(run_data['start_date'])
print(run_data['start_date'].dtype)
```
