import discord
from discord.ext import commands
from discord_slash import SlashCommnads
from discord_slash import SlashContext
import requests
import json
api_key = '77a79b9acc8e4bb8a4fa3b374444bf46'  # from https://twelvedata.com/
client = discord.Client()
TOKEN = 'OTg2MTY1NzU5MDY1NjAwMDQw.GfHcjs._Cd_S6BhbP-Vwi1mGgn9uQNKLPLdw4gGQeEVWY' #discord API Token
bot = commands.Bot(command_prefix='/', intents = discord.Intentes.all())
slash_client = SlashCommnad(bot,sync_commands=True)


@client.event
async def on_ready():
    print(f'Alert on!! as {client.user}')
    await client.change_presence(activity=discord.Game(name="Trading/Coding on Air... We are CTCL."))

@slash_client.slash(name="xau",description ="show current gold price")
async def gold(ctx:SlashContext):
    ticker = 'XAU/USD'
    url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
    data = requests.get(url).json()
    await ctx.send(content=str(data))




@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if message.content.startswith('/gold'):
        ticker = 'XAU/USD'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


    if message.content.startswith('/silver'):
        ticker = 'XAG/USD'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


# gold and silver


    if message.content.startswith('/audcad'):
        ticker = 'AUD/CAD'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


    if message.content.startswith('/audchf'):
        ticker = 'AUD/CHF'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))



    if message.content.startswith('/audjpy'):
        ticker = 'AUD/JPY'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


    if message.content.startswith('/audnzd'):
        ticker = 'AUD/NZD'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


    if message.content.startswith('/audusd'):
        ticker = 'AUD/USD'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


# complete AUD currency


    if message.content.startswith('/cadjpy'):
        ticker = 'CAD/JPY'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


    if message.content.startswith('/cadchf'):
        ticker = 'CAD/CHF'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


#complete CAD currency


    if message.content.startswith('/chfjpy'):
        ticker = 'CHF/JPY'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


#complete CHF currency


    if message.content.startswith('/euraud'):
        ticker = 'EUR/AUD'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


    if message.content.startswith('/eurcad'):
        ticker = 'EUR/CAD'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


    if message.content.startswith('/eurgbp'):
        ticker = 'EUR/GBP'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


    if message.content.startswith('/eurhuf'):
        ticker = 'EUR/HUF'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


    if message.content.startswith('/eurjpy'):
        ticker = 'EUR/JPY'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


    if message.content.startswith('/eurnzd'):
        ticker = 'EUR/NZD'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


    if message.content.startswith('/eurusd'):
        ticker = 'EUR/USD'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


#complete EUR currency


    if message.content.startswith('/gbpaud'):
        ticker = 'GBP/AUD'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


    if message.content.startswith('/gbpcad'):
        ticker = 'GBP/CAD'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


    if message.content.startswith('/gbpchf'):
        ticker = 'GBP/CAD'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


    if message.content.startswith('/gbphuf'):
        ticker = 'GBP/HUF'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


    if message.content.startswith('/gpbjpy'):
        ticker = 'GBP/JPY'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


    if message.content.startswith('/gbpnzd'):
        ticker = 'GBP/NZD'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


    if message.content.startswith('/gbpusd'):
        ticker = 'GBP/USD'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


#complete GBP currency


    if message.content.startswith('/nzdcad'):
        ticker = 'NZD/CAD'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


    if message.content.startswith('/nzdchf'):
        ticker = 'NZD/CHF'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


    if message.content.startswith('/nzdjpy'):
        ticker = 'NZD/JPY'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


    if message.content.startswith('/nzdusd'):
        ticker = 'NZD/USD'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


#complete NZD currency


    if message.content.startswith('/usdcad'):
        ticker = 'USD/CAD'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


    if message.content.startswith('/ucdchf'):
        ticker = 'USD/CHF'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))


    if message.content.startswith('/usdjpy'):
        ticker = 'USD/JPY'
        url = f'https://api.twelvedata.com/price?symbol={ticker}&apikey={api_key}'
        data = requests.get(url).json()
        await message.channel.send(str(data))

#complete USD currency      
        
client.run(TOKEN)
bot.run(TOKEN)


