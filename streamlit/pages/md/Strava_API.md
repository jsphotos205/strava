# Strava API

Following is a walkthrough of acquring and working with the Strava API.

The original file can be found on [GitHub](https://github.com/jsphotos205/strava "GitHub link") as a Jupyter Noterbook under the name [strava_api.ipynb](https://github.com/jsphotos205/strava/blob/main/strava_api.ipynb "strava_api.ipynb link")

## Strava account information:

In order to acquire use of the Strava API you must have an account with Strava. If you do not already have an account with Strava you can sign up here:

* [Strava](https://www.strava.com/ "Click Here!")

After you have gotten all set up with your account and have logged some runs you can now pull your activities data from the Strava API.

* [Strava Developer Docs Link](https://developers.strava.com/docs/reference/)

Use of a `.gitignore` file which ignores `secrets.py` this is where the strava_payload is to handle Strava API request

`secrets.py` values are as followed:

* client_id
* client_secret
* refresh_token
* grant_type
* f
  * used for request for .json

## Code for Strava API:

```python
# Import required modules
import requests
import urllib3
import secrets
import pandas as pd
import polyline
from datetime import datetime
from meteostat import Stations, Daily
```

I am not really sure why you have to have this in the code but found this as a workaround for operating with the Strava API.

```python
# Disable insecure request warnings from urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
```

## Make call to Strava API

An example of how the `secrets.py` file that holds the strava_payload and weather token information is as follows :

```python
strava_payload = {
    'client_id' : '102332',
    'client_secret' : '1e57r15k89kldk3657g9e253136gdj23d3nu75r5gh',
    'refresh_token' : 'gg5g73gs46828t56768af3e82e3e1d454c716a73',
    'grant_type' : 'refresh_token',
    'f' : 'json'
}

weather_token = 'FGiRfkFGHsRLDdypTFSqLzaXrbCfFFsyQ'
```

First we need to make a request to the Strava API for the activities information of the user. At the end of this api call we have a json file that contains all the users activities.

```python
auth_url = 'https://www.strava.com/oauth/token'
activities_url = 'https://www.strava.com/api/v3/athlete/activities'

# Request Strava Token
print('Requesting Strava token... \n')
res = requests.post(auth_url, data=secrets.strava_payload, verify=False)
strava_access_token = res.json()['access_token']

# Set the authorization header using the obtained access token
header = {'Authorization': 'Bearer ' + strava_access_token}

strava_requests_page_num = 1
all_activities = []

while True:
    # Prepare the parameters for paginated request
    strava_param = {'per_page' : 15, 'page' : strava_requests_page_num}
    # Send GET request to retrieve Strava activity data
    strava_dataset = requests.get(activities_url, headers=header, params=strava_param).json()

    if len(strava_dataset) == 0:
        print('breaking out of Strava while loop because the response is zero, indicating no more activities.')
        break

    if all_activities:
        print('all activities is populated')
        all_activities.extend(strava_dataset)

    else:
        print('all activities is NOT populated')
        all_activities = strava_dataset

    strava_requests_page_num += 1

print('Total Activities: ', len(all_activities))
```

## Creating Panda dataframe for all activites from Strava API

The current dataframe contains activites such as:

* Running
* Walking
* Hiking
* Biking
* etc.

```python
all_strava_activites = pd.DataFrame(data=all_activities)
```
