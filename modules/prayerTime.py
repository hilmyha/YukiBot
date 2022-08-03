import datetime
import requests

from telethon import events
from datetime import datetime


@events.register(events.NewMessage(pattern='#pray', forwards=False))
async def jadwalSolat(event):
  try:
    # In this way, if the user send , new york will be selected as the CITY
    msg = event.message.text
    after_command = msg.split(" ")[1:]
    city = ' '.join(after_command)

    # day func
    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    currentYear = datetime.now().year

    base_url = f'https://api.myquran.com/v1'
    cari_url = base_url + '/sholat/kota/cari/' + city

    # Get response and parse it to JSON format
    response = requests.get(cari_url)
    json_jadwal = response.json()

    # If we get a good response, we send a specific message
    if json_jadwal['status'] != False:
      # id to translate searched country
      idlokasi = json_jadwal['data'][0]['id']

      complete_url = base_url + '/sholat/jadwal/' + idlokasi + '/' + str(currentYear) + "/" + str(currentMonth) + "/" + str(currentDay)
      
      # Get response and parse it to JSON format
      response = requests.get(complete_url)
      json_jadwal = response.json()
    
      # If we get a good response, we send a specific message
      if json_jadwal['status'] != False:
        
        getToday = json_jadwal['data']['jadwal']['tanggal']
        getCity = json_jadwal['data']['lokasi']
        getCountry = json_jadwal['data']['daerah']

        jadwalImsak = json_jadwal['data']['jadwal']['imsak']
        jadwalSubuh = json_jadwal['data']['jadwal']['subuh']
        jadwalDzuhur = json_jadwal['data']['jadwal']['dzuhur']
        jadwalAshar = json_jadwal['data']['jadwal']['ashar']
        jadwalMaghrib = json_jadwal['data']['jadwal']['maghrib']
        jadwalIsya = json_jadwal['data']['jadwal']['isya']

      text = "🕌 Prayer times for the region <i><b>" + str(getCity) + " (" + str(getCountry) + ")</b></i>\n\n"
      textJadwal = "<pre>"+\
          str(getCity) + " (" + str(getToday) + ")" +\
          "\n\nImsak    : " + str(jadwalImsak)+\
          "\nSubuh    : " + str(jadwalSubuh)+\
          "\nDzuhur   : " + str(jadwalDzuhur)+\
          "\nAshar    : " + str(jadwalAshar)+\
          "\nMaghrib  : " + str(jadwalMaghrib)+\
          "\nIsya     : " + str(jadwalIsya)+\
          "</pre>"+\
          "\n\nSource: http://api.banghasan.com"


      await event.respond(text, parse_mode="HTML")
      await event.respond(textJadwal, parse_mode="HTML")
    else:
      text = "I couldn't find the city named " + city + " in my database"
      await event.respond(text, parse_mode="HTML")
  except:
    await event.respond( "Insert a city after the #pray command!", parse_mode="HTML")
    return