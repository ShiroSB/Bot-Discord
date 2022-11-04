import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
TOKEN = open("TOKEN","r").read()

@client.event
async def shutdown(ctx):
    await ctx.bot.logout()

@client.event
async def on_connect():
    print("Offline")

client.run(TOKEN)