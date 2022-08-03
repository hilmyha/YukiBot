from telethon import events, utils


# bot talkback
@events.register(events.NewMessage(pattern='halo', forwards=False))
@events.register(events.NewMessage(pattern='Halo', forwards=False))
@events.register(events.NewMessage(pattern='hallo', forwards=False))
@events.register(events.NewMessage(pattern='Hallo', forwards=False))
async def greetingsHalo(event):
  sender = await event.get_sender()
  name = utils.get_display_name(sender)
  
  # Define the text and send the message
  text = "Halo juga, " + name + " ada yang bisa saya bantu? to use bot command #start"
  await event.respond(text, parse_mode="HTML")

@events.register(events.NewMessage(pattern='hai', forwards=False))
@events.register(events.NewMessage(pattern='Hai', forwards=False))
async def greetingsHai(event):
  sender = await event.get_sender()
  name = utils.get_display_name(sender)
  
  # Define the text and send the message
  text = "Hai juga, " + name + " ada yang bisa saya bantu? to use bot command #start"
  await event.respond(text, parse_mode="HTML")

@events.register(events.NewMessage(pattern='Assalaamualaikum', forwards=False))
@events.register(events.NewMessage(pattern='assalaamualaikum', forwards=False))
async def salam(event):
  sender = await event.get_sender()
  name = utils.get_display_name(sender)
  
  # Define the text and send the message
  text = "Waalaikumsalaam, " + name + "? ada yang bisa saya bantu? to use bot command #start"
  await event.respond(text, parse_mode="HTML")