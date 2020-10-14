import requests
import json
from win10toast import ToastNotifier

r = requests.get("https://coronavirus-19-api.herokuapp.com/all")

data = r.json()
text = f"Confirmed Cases : {data['cases']} \nDeaths : {data['deaths']} \nRecovered : {data['recovered']}"

toast = ToastNotifier()
toast.show_toast("Covid-19 Tracker",text, duration=20)
