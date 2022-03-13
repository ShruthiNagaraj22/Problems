import requests
from twilio.rest import Client
from twilio.http.http_client import  TwilioHttpClient
import os

account_sid = "ACb6a42986a64625a1dbe17066ad5dc198"
auth_token = "a1347c4fbb75bd4775b61924d099e0b7"

params = {
    "lat" : 49.006889,
    "lon" : 8.403653,
    "exclude" : "current,minutely,daily",
    "appid" : "f20e9367eec765eaafd033c53f94c2cd"
}

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https' : os.environ['https_proxy']}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=params)
response.raise_for_status()

weather_data = response.json()
#print(weather_data["hourly"][0]["weather"][0]["id"])

weather_slice = weather_data["hourly"][:12]    # Slicing first 12 hours data (n-1)
#print(weather_slice)

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    #print("Bring an umbrella")
    client = Client(account_sid, auth_token, http_client= proxy_client)
    message = client.messages \
        .create(
        body="Hola! It's going to rain today. Remember to bring an ☂",
        from_='+-----------',
        to='+49 ---- ----'
    )

print(message.status)