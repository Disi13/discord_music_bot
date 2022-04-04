import discord

client = discord.Client()

@client.event
async def on_message(message):
    message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("привет"):
        await message.channel.send("Ну, привет, " + str(message.author).partition('#')[0] + "!")

client.run('OTYwMTI3MjE3MzkwNzQ3NzAw.Ykl6Jg.U8juphY7QcDiavypX6b59u07m44')
