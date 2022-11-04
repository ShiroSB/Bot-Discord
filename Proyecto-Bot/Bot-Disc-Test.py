from asyncio import events
from dis import disco
from email import message
from http import client
from sqlite3 import connect
import discord
from importlib import reload


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
TOKEN = open("TOKEN","r").read()

@client.event
async def on_connect():
    print("Online")

@client.event
async def on_message(message):
    if message.content.startswith("!Pbot"):
        await message.channel.send("It Works")
    if message.content.startswith("!Pinfo"):
        await message.channel.send("Si quieres ver las opciones reacciona con un ✅")

    # if message.content.startswith('Si quieres ver las opciones reacciona con un ✅'):
    #     await message.add_reaction('✅')

@client.event
async def on_reaction_add(reaction, user):
  if reaction.emoji == '✅':
        
        embed = discord.Embed(
        title = 'Index',
        url="https://discordpy.readthedocs.io/en/stable/", 
        description= 'A continuación se desplegaran las opciones del Bot, reacciona con el emoji adecuado a lo que quieras hacer',
        colour= discord.Colour.red()
    )
        embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1350600904299393030/kBhYfrIu_400x400.jpg")
        embed.add_field(name="1️⃣ Escuchar Musica ", value="Funcionalidad para escuchar muscia", inline=False)
        embed.add_field(name="2️⃣ Manual Programación ", value="Manual de consulta sobre lenguajes de programación", inline=False)
        embed.add_field(name="3️⃣ Enviar Ticket ", value="Si tienes alguna duda envia un ticket", inline=False)
        
        await reaction.message.channel.send(embed=embed)

  elif reaction.emoji == '1️⃣':
        embed = discord.Embed(
        title = 'Bot Musica',
        url="https://youtube.com", 
        description= 'Funciones del bot',
        colour= discord.Colour.purple()
    )
        embed.add_field(name="Comandos:", value="Pplay --> Reproducir canción \n Pstop --> Parar canción", inline=False)
        await reaction.message.channel.send(embed=embed)
#       async def act_musica():
#         print(1)
#
#	    music_bot.run(act_musica())


client.run(TOKEN)