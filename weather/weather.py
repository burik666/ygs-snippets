#!/usr/bin/env python3
import urllib
import urllib.request
import json
import argparse

# https://openweathermap.org/weather-conditions
icons = {
        # clear sky
        "01d": "<span font=\"Font Awesome 5 Free Solid\">\uf185</span>",
        "01n": "<span font=\"Font Awesome 5 Free Solid\">\uf186</span>",
        # few clouds
        "02d": "<span font=\"Font Awesome 5 Free Solid\">\uf6c4</span>",
        "02n": "<span font=\"Font Awesome 5 Free Solid\">\uf6c3</span>",
        # scattered clouds
        "03d": "<span font=\"Font Awesome 5 Free Solid\">\uf0c2</span>",
        "03n": "<span font=\"Font Awesome 5 Free Solid\">\uf0c2</span>",
        # broken clouds
        "04d": "<span font=\"Font Awesome 5 Free Solid\">\uf0c2</span>",
        "04n": "<span font=\"Font Awesome 5 Free Solid\">\uf0c2</span>",
        # shower rain
        "09d": "<span font=\"Font Awesome 5 Free Solid\">\uf740</span>",
        "09n": "<span font=\"Font Awesome 5 Free Solid\">\uf740</span>",
        # rain
        "10d": "<span font=\"Font Awesome 5 Free Solid\">\uf743</span>",
        "10n": "<span font=\"Font Awesome 5 Free Solid\">\uf73c</span>",
        # thunderstorm
        "11d": "<span font=\"Font Awesome 5 Free Solid\">\uf2dc</span>",
        "11n": "<span font=\"Font Awesome 5 Free Solid\">\uf2dc</span>",
        # snow
        "13d": "<span font=\"Font Awesome 5 Free Solid\">\uf2dc</span>",
        "13n": "<span font=\"Font Awesome 5 Free Solid\">\uf037</span>",
        # mist
        "50d": "<span font=\"Font Awesome 5 Free Solid\">\uf037</span>",
        "50n": "<span font=\"Font Awesome 5 Free Solid\">\uf037</span>",
        }

parser = argparse.ArgumentParser()
parser.add_argument("-apikey", metavar="key", required=True, help="openweathermap apikey")
parser.add_argument("-city", metavar="city", required=True,  help="city")
parser.add_argument("-units", metavar="units", default="metric", choices=["metric", "imperial"], help="units []")
args = parser.parse_args()

req = {
        "appid": args.apikey,
        "units": args.units,
        "q": args.city,
        }
r = urllib.request.urlopen("https://api.openweathermap.org/data/2.5/weather?"+ urllib.parse.urlencode(req))
resp = json.loads(r.read())
print(json.dumps([{
    "full_text":icons[resp["weather"][0]["icon"]]+" "+str(resp["main"]["temp"])+"\u00b0",
    "_temp": resp["main"]["temp"],
    "markup": "pango",
    }]))
