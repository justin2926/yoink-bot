import discord 
from discord.ext import commands

client = commands.Bot(command_prefix = '_')

modquestions = '1. Who is the best at PvP? \n 2. What is Puckyz KD? \n 3. Who is the creator of this server? \n 4. Why do you want to become a mod? \n 5. What will you bring to this server? \n 6. Answer the image below: \n https://cdn.discordapp.com/attachments/745105208258068521/745106130799296522/5b16ceae5e48ec1b008b460c.png'

# bot on
@client.event
async def on_ready():
    print('Ready!')

# member joined
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to Yoink Hub'
    )
    print(f'{member} has joined the server!')

# member left
@client.event
async def on_member_remove(member):
    await member.create_dm()
    await member.dm_channel.send(f'Byeeeeeeeeeee, have a great time!')
    print(f'{member} has left the server!')

# kick
@client.command()
@commands.has_role('Admin')
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    print(f'{member} has been kicked!')

# ban
@client.command()
@commands.has_role('The Boss')
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    print(f'{member} has been banned!')

# unban
@client.command()
@commands.has_role('Admin')
async def unban(ctx, member : discord.Member, *, reason=None):
    await member.unban(reason=reason)
    print(f'{member} has been unbanned!')

# test
@client.command()
@commands.has_role('The Boss')
async def verify(ctx, member : discord.Member):
    await ctx.send(f'{member}, please check your email for further instructions!')

# help
@client.command()
async def Help(ctx):
    await ctx.send('Work in progess!')

# mod application
@client.command()
async def modapply(ctx):
    await ctx.send(modquestions)

# commands
@client.command()
async def servercommands(ctx):
    await ctx.send('```_modapply, _servercommands, _Help```')

@client.command()
async def faq(ctx):
    await ctx.send('**1. Who is Puckyz?** \n Puckyz is the best bird in PL \n **What is Yoink Hub?** \n A discord server')

#  https://discord.com/api/oauth2/authorize?client_id=744686810738720818&permissions=8&scope=bot
client.run('TOKEN')
