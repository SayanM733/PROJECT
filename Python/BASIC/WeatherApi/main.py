import requests
import json
import win32com.client as wincom

city = input("Enter the city name ")
speak = wincom.Dispatch("SAPI.SpVoice")

url = f"https://api.weatherapi.com/v1/current.json?key=8efb2194e4394361bb4160131230409&q={city}"

r = requests.get(url)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

speak.Speak(f"The current weather in {city} is {w} degrees")