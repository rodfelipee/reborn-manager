import os
import discord
from discord.ext import commands


server_id = 1047502406189068379
intents = discord.Intents.default()
intents.members = True
token = ''

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    client = commands.Bot(command_prefix='/',intents=intents)
    client.remove_command('help')

    for filename in os.listdir('./utils'):
        if filename.endswith('.py'):
            client.load_extension(f'./utils.{filename[:-3]}')

    @client.event
    async def on_ready(self):
        print(f'Logged in as {client.user}')
        await client.change_presence(activity=discord.Game(name=f'The Indomitable Human Spirit'))

    @client.command(name='ping')
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

    

client = MyClient()
client.run(token)



