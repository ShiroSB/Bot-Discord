from asyncio import events
from dis import disco
from email import message
from http import client
from sqlite3 import connect
import discord
from importlib import reload
from discord.ext import commands
import youtube_dl
import DiscordUtils
import os

TOKEN = open("TOKEN","r").read()

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Hay una canción en curso, si quieres poner otro usa primero el comando $stop")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
        await ctx.send("Se a desconectado manualmente al bot.")
    else:
        await ctx.send("El bot no esta en ningun canal.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
        await ctx.send("Se a pausado el video/canción.")
    else:
        await ctx.send("No hay ninguna cancion en curso.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
        await ctx.send("Se a reanudado el video/canción.")
    else:
        await ctx.send("La canción no esta pausado.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

@client.command(name='info', help='Ask person for feedback')
async def roll(ctx):

    embed=discord.Embed(title="Index", url="https://i.imgur.com/dyo7xtM.png", description="A continuación se desplegaran las opciones del Bot, reacciona con el emoji adecuado a lo que quieras hacer", color=0xFF5733)
    embed.set_thumbnail(url="https://i.imgur.com/dyo7xtM.png")
    embed.add_field(name="1️⃣ Escuchar Musica", value="Funcionalidad para escuchar muscia", inline=False)
    embed.add_field(name="2️⃣ Manual Programación", value="Manual de consulta sobre lenguajes de programación", inline=False)
    embed.add_field(name="3️⃣ Enviar Ticket", value="Si tienes alguna duda envia un ticket", inline=False)
    await ctx.send(embed=embed)

    message = await ctx.send('Opciones')

    one = '1️⃣'
    two = '2️⃣'
    three = '3️⃣'

    await message.add_reaction(one)
    await message.add_reaction(two)
    await message.add_reaction(three)

    def check(reaction, user):
        return user == ctx.author and str(
            reaction.emoji) in [one, two, three]

    member = ctx.author

    while True:

            reaction, user = await client.wait_for("reaction_add", timeout=10.0, check=check)

            if str(reaction.emoji) == one:

                embed = discord.Embed(
                title = 'Musica',
                url="https://youtube.com", 
                description= 'Funciones del bot',
                colour= discord.Colour.red()
                )
                embed.add_field(name="!play", value="Comando + link de youtube", inline=False)
                embed.add_field(name="!pause", value="Pausa el video", inline=False)
                embed.add_field(name="!resume", value="Reanuda el video", inline=False)
                embed.add_field(name="!leave", value="Que el bot abandone el canal", inline=False)   
                await ctx.send(embed=embed)

            if str(reaction.emoji) == two:

                #Pagina 1
                embed1 = discord.Embed(color=ctx.author.color).add_field(name="Pagina 1", value="XXXX")
                embed1.add_field(name="comando", value="Descripcion", inline=False)
                embed1.add_field(name="comando", value="Descripcion", inline=False)
                embed1.add_field(name="comando", value="Descripcion", inline=False)
                embed1.add_field(name="comando", value="Descripcion", inline=False)

                #Pagina 2
                embed2 = discord.Embed(color=ctx.author.color).add_field(name="Pagina 2", value="XXXX")
                embed2.add_field(name="comando", value="Descripcion", inline=False)
                embed2.add_field(name="comando", value="Descripcion", inline=False)
                embed2.add_field(name="comando", value="Descripcion", inline=False)

                #Pagina 3
                embed3 = discord.Embed(color=ctx.author.color).add_field(name="Pagina 3", value="XXXX")
                embed3.add_field(name="comando", value="Descripcion", inline=False)
                embed3.add_field(name="comando", value="Descripcion", inline=False)
                embed3.add_field(name="comando", value="Descripcion", inline=False)

                paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
                paginator.add_reaction('⏮️', "first")
                paginator.add_reaction('⏪', "back")
                paginator.add_reaction('🔐', "lock")
                paginator.add_reaction('⏩', "next")
                paginator.add_reaction('⏭️', "last")
                embeds = [embed1, embed2, embed3]

                await paginator.run(embeds)

            if str(reaction.emoji) == three:
                embed = discord.Embed(
                title = 'Tickets',
                url="https://youtube.com", 
                description= 'Funciones del bot',
                colour= discord.Colour.red()
                )   
                await ctx.send(embed=embed)
    
client.run(TOKEN)
