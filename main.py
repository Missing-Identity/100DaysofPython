import requests
from twilio.rest import Client

#  Stripped of all the keys as it was uploaded to Github. Add later if needed.

api_key = ""
my_lat = 17.385044
my_long = 78.486671

twillio_accid = ""
twillio_authtoken = ""

parameters = {
    "lat": my_lat,
    "lon": my_long,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
print(response)
response_json = response.json()
hourly_data = response_json["hourly"]
next_twelve_hour_id_list = []
rain_possibility = False

for i in range(12):
    weather_id = hourly_data[i]["weather"][0]["id"]
    next_twelve_hour_id_list.append(weather_id)
    if weather_id < 800:
        rain_possibility = True
if rain_possibility:
    print("rain")
    client = Client(twillio_accid, twillio_authtoken)

    message = client.messages \
        .create(body="Unmilan here, reminding you to take an umbrella!", from_='', to='')  # Numbers removed
    print(message.status)
