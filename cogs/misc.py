import discord
from discord.ext import commands

class misc(commands.Cog):
    
    def __init__(self,client):
        self.client=client


    @commands.Cog.listener()
    async def on_ready(self):
        print("=>Loaded misc") 
    
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.id == 850655066725154856:
            return
        else:
            if "randi" in message.content:
                await message.reply("https://tenor.com/view/teri-ma-teri-maa-funny-funny-insult-salman-gif-21959029")
            # await message.channel.send()
            # print("")


    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def purge(self,ctx,amount:int):
        await ctx.channel.purge(limit=amount)

    
    @commands.command()
    async def embed(self,ctx):
        myEmbed = discord.Embed(title="Embed title", description="description of the embed",color=0x5b5bfc)
        await ctx.send(embed=myEmbed)


def setup(client):
    client.add_cog(misc(client))