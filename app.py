import handlers.client
import modules.start, modules.ping, modules.timeNow, modules.talkback, modules.forecast, modules.prayerTime

bot = handlers.client.bot
TOKEN = handlers.client.TOKEN



with bot as yuki:
  yuki.add_event_handler(modules.start.start)

with bot as yuki:
  yuki.add_event_handler(modules.ping.ping)

with bot as yuki:
  yuki.add_event_handler(modules.timeNow.whatTime)

# talkback
with bot as yuki:
  yuki.add_event_handler(modules.talkback.greetingsHalo)
  yuki.add_event_handler(modules.talkback.greetingsHai)
  yuki.add_event_handler(modules.talkback.salam)


with bot as yuki:
  yuki.add_event_handler(modules.forecast.forecastWeather)


with bot as yuki:
  yuki.add_event_handler(modules.prayerTime.jadwalSolat)
  

bot.start(bot_token=TOKEN)
print("bot running")
bot.run_until_disconnected()