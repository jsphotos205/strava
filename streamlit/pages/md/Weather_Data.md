# Weather Data

Continuing working with the [strava_api.ipynb](https://github.com/jsphotos205/strava/blob/main/strava_api.ipynb "strava_api.ipynb link") we will use latitude and longitude information collected from the run data to determine location for weather data.

We will be accessing historic weather data via weather stations in closest proximity to RRGCC land using the Meteostat python library. Meteostat is an excellent python library which gives developers a simple interface for historic weather data. With many failed attempts to access weather data via [NOAA](https://www.weather.gov/documentation/services-web-api "NOAA's API Documentation")'s API I have found Meteostat to be an easier and more user friendly option.

You can read more about Meteostat uses and developer information here:

* [Meteostat Developers Site](https://dev.meteostat.net/ "Meteostat Dev Site")

We will access weather station location data with latitude and longitude information from run_data column 'start_latlng'

We will limit the historic weather data to dates that only apply to the earliest run to now.

* Obtain the earliest run in the run_data by finding the last entry in the column 'start_date' and set that to our start option for the weather data.
* Use datetime.now() to get current date to ensure data is up to date

---

**Get first entry of row to access lat and lon values :**

```python
coords = run_data['start_latlng'].loc[0]
```

**Extracting the latitude and lon from the coords tuple :**

```python
lat = coords[0]
lon = coords[1]
```

**Use last entry in run data as start date for weather model :**

```python
start = pd.to_datetime(run_data['start_date'].iloc[-1])
```

**Use datetime.now() to get current date to ensure data is up to date :**

```python-repl
end = datetime.now()
model = True
```

**Use meteostat Stations() instance to acquire information for nearest weather station to run location :**

```python
stations = Stations()
stations = stations.nearby(lat=lat, lon=lon)
weather_station = stations.fetch(1)
```

**Use meteostat Daily() instance to acquire weather data based on the start date of the oldest run and ending to current date :**

```python
data = Daily(weather_station.iloc[:], start, end, model)
data = data.normalize()
data = data.fetch()
```

**Create DataFrame for weather_data :**

```python
weather_data = pd.DataFrame(data)
```

**Convert 'tavg', 'tmin', and 'tmax' from Celsius to Fahrenheit and round to 2 decimal places :**

```python
weather_data['tavg'] = weather_data.apply(lambda x : round((9/5)*x['tavg']+32,2), axis=1)
weather_data['tmin'] = weather_data.apply(lambda x : round((9/5)*x['tmin']+32,2), axis=1)
weather_data['tmax'] = weather_data.apply(lambda x : round((9/5)*x['tmax']+32,2), axis=1)
```

**Convert the 'wspd' column from km/h to mph and round to 2 decimal places :**

```python
weather_data['wspd'] = weather_data.apply(lambda x : round(x['wspd'] * 0.621371, 2), axis=1)
```

**Drop 'wpgt' and 'tsun' because columns contian no data :**

```python
weather_data = weather_data.drop(['wpgt', 'tsun'], axis=1)
```

**Merge 'run_data' and 'weather_data' based on the 'start_date' column in 'run_data', index 'weather_data' using an inner join :**

```python
run_data = run_data.merge(weather_data, left_on='start_date', right_index=True, how='inner')
```

**Calculate the mean value for 'tavg', 'tmin', 'tmax', 'wspd', and 'pres' :**

```python
temp_mean = run_data['tavg'].mean()
tmin_mean = run_data['tmin'].mean()
tmax_mean = run_data['tmax'].mean()
wspd_mean = run_data['wspd'].mean()
pres_mean = run_data['pres'].mean()
```

**Use mean to fill NaN values :**

```python
run_data['tavg'].fillna(int(temp_mean), inplace=True)
run_data['tmin'].fillna(int(tmin_mean), inplace=True)
run_data['tmax'].fillna(int(tmax_mean), inplace=True)
run_data['wspd'].fillna(int(wspd_mean), inplace=True)
run_data['pres'].fillna(int(pres_mean), inplace=True)
```

**Fill NaN with 0.0 value :**

```python
run_data['prcp'].fillna(0.0, inplace=True)
run_data['snow'].fillna(0.0, inplace=True)
run_data['wdir'].fillna(0.0, inplace=True)
```
