from telethon import events, utils

# start command
@events.register(events.NewMessage(pattern='/start'))
@events.register(events.NewMessage(pattern='#start')) 
async def start(event):
  sender = await event.get_sender()
  name = utils.get_display_name(sender)

  
  greeting = "Hello welcome " + name
  descText = " " +\
    "Bot Config command" +\
    "\n<pre>" +\
    "\"#ping\" : for run ping reply message" +\
    "\n\"#time\" : what time is it?" +\
    "</pre>"+\
    "\n\nBot Function command" +\
    "\n<pre>" +\
    "\"#cuaca\"  : weather forecast" +\
    "\n\"#pray\"   : muslim prayer time" +\
    "</pre>"

  await event.respond(greeting, parse_mode="HTML")
  await event.respond(descText, parse_mode="HTML")