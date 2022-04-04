import discord
import os

token = os.environ['discordToken']
client = discord.Client()

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("привет"):
        await message.channel.send("Ну, привет, " + str(message.author).partition('#')[0] + "!")

client.run(token)
