# RRGCC Running Data

After merging the weather data and run data earlier in the [strava_api.ipynb](https://github.com/jsphotos205/strava/blob/main/strava_api.ipynb "strava_api.ipynb link") we aim to go further into the Strava run_data to only collect runs from RRGCC land.

* For this particular project I want to focus on RRGCC owned and operated land
  * Most common local running location for my runs
* Highlight the running opportunities on climber owned land
  * Showcase different loops and routes

---

**Filter the run data for RRGCC land and different running loops and routes :**

```python
all_pmrp_run = run_data[run_data['name'].str.contains('PMRP', case=False, na=False)]
all_rrg_run = run_data[run_data['name'].str.contains('RRG', case=False, na=False)]
all_sore_heel = run_data[run_data['name'].str.contains('Sore Heel', case=False, na=False)]
all_lode_loop = run_data[run_data['name'].str.contains('Lode Loop', case=False, na=False)]
all_drive_by = run_data[run_data['name'].str.contains('Drive By Loop', case=False,na=False)]
```

**Filter the run data for strict instances of running loops :**

```python
only_lode_loop = run_data[run_data['name'].str.contains(r'^PMRP : Lode Loop$', case=False)]
only_sore_heel_loop = run_data[run_data['name'].str.contains(r'^PMRP : Sore Heel Loop$', case=False)]
only_drive_by_loop = run_data[run_data['name'].str.contains(r'^PMRP : Drive By Loop$', case=False)]
```

**Set csv path and save csv files :**

```python
base_path = 'csv/run/'
rrgcc_path = 'csv/run/rrgcc/'

all_run_path = f'{base_path}all_run.csv'
all_rrg_path = f'{base_path}all_rrg.csv'

all_pmrp_path = f'{rrgcc_path}all_pmrp.csv'

all_sore_heel_path = f'{rrgcc_path}all_sore_heel.csv'
all_lode_path = f'{rrgcc_path}all_lode.csv'
all_drive_by_path = f'{rrgcc_path}all_drive_by.csv'

only_sore_heel_path = f'{rrgcc_path}only_sore_heel.csv'
only_lode_path = f'{rrgcc_path}only_lode.csv'
only_drive_by_path = f'{rrgcc_path}only_drive_by.csv'

weather_data_csv_path = 'csv/weather/only_weather_data.csv'

run_data.to_csv(all_run_path, index=False)
all_pmrp_run.to_csv(all_pmrp_path, index=False)
all_rrg_run.to_csv(all_rrg_path, index=False)
all_sore_heel.to_csv(all_sore_heel_path, index=False)
only_sore_heel_loop.to_csv(only_sore_heel_path, index=False)
all_lode_loop.to_csv(all_lode_path, index=False)
only_lode_loop.to_csv(only_lode_path, index=False)
all_drive_by.to_csv(all_drive_by_path, index=False)
only_drive_by_loop.to_csv(only_drive_by_path, index=False)

weather_data.to_csv(weather_data_csv_path, index=True)
```

Now that the data is processed and saved as a .csv file it is easily explored and accessed via a Streamlit app.

You can explore the Streamlit app code [here](https://github.com/jsphotos205/strava/tree/main/streamlit "streamlit code in Github")
