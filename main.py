import discord
import random
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import os
from discord.ext import commands, tasks
from dotenv import load_dotenv
# from webserver import keep_alive
intents = discord.Intents.all()

client = commands.Bot(command_prefix ="=",intents=intents)
load_dotenv()
TOKEN = os.getenv("TRLMDON")

async def scheduled_thing():
    channel = client.get_channel(963423479653347369)
    timedEmbed = discord.Embed(title="Art-event",description=f"So, this is an announcement related to the art event which was started in Trlmdon.\nWe decided to keep only one winner for this event and that is <@703092079626158130>, he scored `12.86` upvotes on an average which is the highest, **CONGRATS NEKO**, I still can't believe he drew these\nYou get <@&978763960088141906>")
    timedEmbed.add_field(name="Runner Ups",value="Runner ups for this event are:\n=>**Riruru** > 8.5 Average upvotes\n=>**Sumanshi** > 8 average upvotes\n=>Atlast-Alviya, Rico, Nesky, INFINITY, Kiwi these guys posted only one drawing so no average for them\nOnce again, congrats neko :D and thanks for participating y'all")
    await channel.send("@everyone",embed=timedEmbed)

@client.event
async def on_ready():
    await client.change_presence(status="hi")
    print('bot ready')

    scheduler = AsyncIOScheduler()
    scheduler.add_job(scheduled_thing, CronTrigger(hour=9,minute=30,second=0)) 
    scheduler.start()

@client.event
async def on_message(message):
    message. content = message. content. lower()
    await client.process_commands(message)

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
