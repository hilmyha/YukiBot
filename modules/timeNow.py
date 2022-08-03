from telethon import events
from datetime import date


@events.register(events.NewMessage(pattern='#time', forwards=False))
async def whatTime(event):
  
  # Define the text and send the message
  thisDay = date.today()
  text = "Received! Day and time: \n"+\
    "<pre>"+\
    str(thisDay.strftime('%A')) + ", " + str(thisDay)+\
    "</pre>"
  await event.respond(text, parse_mode="HTML")