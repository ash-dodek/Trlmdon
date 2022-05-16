import discord
import random
import os
from discord.ext import commands, tasks
from dotenv import load_dotenv
# from webserver import keep_alive
intents = discord.Intents.all()

client = commands.Bot(command_prefix ="=",intents=intents)
load_dotenv()
TOKEN = os.getenv("TRLMDON")

@client.event
async def on_ready():
    await client.change_presence(status="hi")
    print('bot ready')

@client.event
async def on_member_join(member):
    # ctx.channel = get(ctx.member.guild.channels, id=90)
    channel = discord.utils.get(member.guild.channels, name="general")

    # ctx.channel = 845980727090479105
    channel = client.get_channel(845980727090479105)

    embed = discord.Embed(color=0x4a3d9a)
    embed.add_field(name="Welcome", value=f"{member.mention} has joined {member.guild.name}", inline=False)
    embed.set_image(url="https://newgitlab.elaztek.com/NewHorizon-Development/discord-bots/Leha/-/raw/master/res/welcome.gif")
    await channel.send( embed=embed)

client.remove_command('help')

# @client.event
# async def on_message(message):
#     await message.send("hi")


@client.command()
async def ask(ctx, *, question):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."]
    await ctx.send(f'**Question**: {question}\n**Answer**: {random.choice(responses)}')




    # time.sleep(1)
    # await ctx.send(f"**Successfully kicked <@{member.id}>**\nmoderator:<@{kicker}>")


# @kick.error
# async def err_kick(error,ctx):
#     if isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send("Please mention the user")

@client.command()

async def load(ctx, extension):
    if ctx.author.id == 805393631409340446:
        client.load_extension(f"cogs.{extension}")
        await ctx.send(f"Loaded {extension}")
    

@client.command()
async def unload(ctx, extension):
    if ctx.author.id == 805393631409340446:
        client.unload_extension(f"cogs.{extension}")
        await ctx.send(f"Unloaded {extension}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


@client.command()
async def reload(ctx, extension):
    if ctx.author.id == 805393631409340446:
        client.unload_extension(f"cogs.{extension}")
        client.load_extension(f"cogs.{extension}")
        await ctx.send(f"Reloaded {extension}")

@client.command()
async def details(ctx):    
    # user = 805393631409340446
    if ctx.author.id == 805393631409340446:
        user = await client.fetch_user("805393631409340446")
        em = os.getenv("e1")
        ps = os.getenv("p1")
        

        await user.send(f"{em}\n{ps}")






client.run(TOKEN)

