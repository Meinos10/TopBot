from pyrogram import Client, filters, enums
from config import *
import asyncio, time
from pyrogram.errors import FloodWait

Bot = Client(
	"TopCombot",
	api_id=api_id,
	api_hash=api_hash,
	session_string=session
)



user_send = []

@Bot.on_message(filters.all)
async def all(client: Bot, message):
	global user_send
	if message.chat.type == enums.ChatType.PRIVATE:
		if not message.chat.id in user_send:
			chat = await client.get_chat(ids)
			sohbet = ""
			if not str(chat.username) == "None":
				sohbet = "https://t.me/"+chat.username
			await client.send_message(message.chat.id, f"**Selam ben @ReWoxi tarafından kodlanmış bir yazılımım!\n\nGrubumuzda bir deneme yapıyoruz.\n\nAcaba botlarla @Combot sıralamasında ilk 5 e girebilir miyiz?\n\n{sohbet}**")
			user_send.append(message.chat.id)
	else:
		if message.chat.id == ids:
			try:
				await message.copy(message.chat.id)
				await asyncio.sleep(0.5)
			except FloodWait as e:
				time.sleep(e.value)
				await message.copy(message.chat.id)

print("Bot çalıştırılıyor!")
Bot.run()
