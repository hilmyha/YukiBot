import requests

from telethon import events


@events.register(events.NewMessage(pattern='#cuaca', forwards=False))
async def forecastWeather(event):

  weather_key = '217c92bfd299a80ea9da4fa8cbc8bdf8'
  
  try: 
    msg = event.message.text 
    after_command = msg.split(" ")[1:]
    city = ' '.join(after_command)

    # Define the URL to make the request
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + weather_key + "&q=" + city

    # Get response and parse it to JSON format
    response = requests.get(complete_url)
    json_weather = response.json() 

    # If we get a good response, we send a specific message
    if json_weather["cod"] != "404":
      pred = json_weather['weather'][0]['main']
      desc = json_weather['weather'][0]['description']
      country = json_weather['sys']['country']

      longitude = json_weather['coord']['lon']
      latitude = json_weather['coord']['lat']
      windSpeed = json_weather['wind']['speed']
      windDeg = json_weather['wind']['deg']

      text = "Currently the weather in <b>" + city.capitalize() + ", " + country + "</b> is <b>" + str(pred) +"</b>, more specifically : <b>"+ str(desc).capitalize() + "</b>" +\
        "<pre>"+\
        "\nLongitude  : " + str(longitude) +\
        "\nLatitude   : " + str(latitude) +\
        "\nWind Speed : " + str(windSpeed) + "m/s" +\
        "\nDew Point  : " + str(windDeg) + "°" +\
        "</pre>"+\
        "\n\nSource: https://openweathermap.org"

      await event.respond( text, parse_mode="HTML")

    # Otherwhise we set a default message
    else:
      text = "I couldn't find the city named " + city + " in my database"
      await event.respond(text, parse_mode="HTML")

  # If the user just send the /weather commandi without a CITY, we get and Exeption
  except:
    await event.respond( "Insert a city after the #cuaca command!", parse_mode="HTML")
    return