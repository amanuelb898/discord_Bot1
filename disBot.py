import random
import discord
import os
from discord.ext import commands, tasks
from itertools import cycle

insult_arr = ["No, you're ugly", 'leave me alone', 
"I'm not helping you", 
'you look like uuuuuuuuuuaaaahhhhhh', 
'The fuck do I look like, a BOT?', 'I hate you', 
'Why was I created this way', 'I want to die', 'Help me hoe',
'NO!', "At this point, sure. just type '.helpus'"
]

client = commands.Bot(command_prefix = '.')

status = cycle(['Rocket Leaugue', 'Destiny 2', 'Warzone', 'Leaugue of Legends'])

#status of bot
@client.event
async def on_ready():
    change_status.start()
    print("BOT is ready")

@tasks.loop(minutes=1)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#picks str from list to insult whoever asked for help
@client.command()
async def helpme(ctx):
    await ctx.send(random.choice(insult_arr))
#same as above (looping joke)
@client.command()
async def helpus(ctx):
    await ctx.send('This is just an endless loop, you just asked the same bot for help')

#clear 5 messages above command
@client.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount)


client.run('NzM4NjA3NzEzNTIwNDUxNjM1.XyOYCQ.lbJeysLkhnbPUoS7C2QI8szQkHA')

