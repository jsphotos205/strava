# RRGCC Running Data

---

The Red River Gorge Climbers Colition ([RRGCC](https://rrgcc.org/)) owns and operates nearly 1,150 acres of land in Lee County, Kentucky near the outdoor mecca of the Red River Gorge. 

Some of these properties include the Pendergrass-Muray Recreational Preserve ([PMRP](https://rrgcc.org/rrg-info/pmrp/)) and Bald Rock Recreational Preserve ([BRRP](https://rrgcc.org/rrg-info/brrp/)). These preserves are mainly used for rock climbing but host endless miles of trails for hiking and excellent trail running for all experience levels. 

To better showcase the trail running in the area I have processed data from Strava to collect a variety of running metrics to create a dashboard. Along with Strava data, I have merged historical weather data for the area for better comparative analysis between the user's past run attempts of similar routes to weather data for performance review.

---

### Running data :

---

##### Strava API :

* Distance
  * Miles
* Time
  * Moving Time in Minutes
  * Moving Time in Hours
* Speed
  * Average Speed
  * Maximum Speed
  * Minimum Speed
* Elevation
  * Total Elevation Gain
  * Highest Elevation
  * Lowest Elevation
* Personal Records
* Location
  * Decoded Google Polyline
    * Latitude
    * Longitude

---

### Weather data :

---

Historical weather data for the RRGCC areas in Lee County, KY obtained from the [Meteostat](https://dev.meteostat.net/ "Meteostat Dev Page") python library.

##### Nearest Weater Station : Jackson Carroll Airport

* Temperature
  * Temperature Max
  * Temperature Minimium
  * Temperature Average
* Precipitation
* Snowfall
* Wind Directrion
* Wind Speed
* Pressure

---

##### Future Development :

Develop an app that uses decoded Google Polyline to better direct Local Search and Rescue responders to climber's locations in case of severe injuries.

* Create Dataframe of climbing area locations and names to be accessed quickly in emergency response.
* Plot paths to crag locations for better directions and navigation of RRGCC land for First Responders.

Use run data for running events, fund-raisers, and trail days for furtue RRGCC event planning.

* Develop an app for random run selection for individual or team running events
* Acquire user data for times and local leaderboards for running loops.

---

###### Data Analysis 2 Final Project - Code Kentucky
