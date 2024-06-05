import discord
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def kutu_oyunu(ctx):
    await ctx.send("Sana rastgele bir kutu oyunu önereceğim. Bununla zamanını kaliteli bir şekilde değerlendirebilirsin =)")
    hey = random.choice(os.listdir("C:/Users/Lenovo/Desktop/Python Pro/images"))
    with open(f"C:/Users/Lenovo/Desktop/Python Pro/images/{hey}" , "rb") as game:
        oyun = discord.File(game)
    await ctx.send(file = oyun)    

bot.run("GİZLİ TOKEN BURAYA")
