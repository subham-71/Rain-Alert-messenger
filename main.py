import requests
import os
from twilio.rest import Client

account_sid = 'Your Twillio account sid'
auth_token = 'ur authourisation token'

api_key = "your api key from open weather map"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lon": "latitude of your place",
    "lat": "longitude of your place",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
# print(weather_slice)
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="It's going to rain today. Bring an umbrella",
            from_='dummy number created in twillo',
            to='your phone number'
        )

    print(message.status)
