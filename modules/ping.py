import time

from telethon import events


# bot feature config
@events.register(events.NewMessage(pattern='#ping', forwards=False))
async def ping(event):
    s = time.time()
    message = await event.reply('Pong!')
    d = time.time() - s
    await message.edit(f'Pong! __(reply memerlukan waktu {d:.2f} s)__')