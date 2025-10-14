from telethon import TelegramClient, events

api_id = 123456
api_hash = "abcd1234"

client = TelegramClient("userbot", api_id, api_hash)

@client.on(events.NewMessage(pattern="/ping"))
async def handler(event):
    await event.respond("pong")

client.start()
client.run_until_disconnected()
