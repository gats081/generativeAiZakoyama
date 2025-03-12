import discord
import config
import random

intents = discord.Intents.all()
client = discord.Client(intents=intents)

# Bot起動時に呼び出される関数
@client.event
async def on_ready():
    print("Ready!")

# メッセージの検知
@client.event
async def on_message(message):
    # 自身が送信したメッセージには反応しない
    if message.author == client.user:
        return
    if message.content.startswith('おもち'):
	    await message.channel.send('もちもち')
        
# Bot起動
client.run(config.DISCORD_TOKEN)
