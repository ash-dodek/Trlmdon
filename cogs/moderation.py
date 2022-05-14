# from dis import disco
import discord
from discord.ext import commands
# from pyparsing import col

# from main import embed

class moderation(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.Cog.listener()
    async def on_ready(self):
        print("=>Loaded moderation")        

    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error, commands.MissingPermissions):
            permEm = discord.Embed(description="You don't have enough permission execute that command :x:")
            await ctx.send(embed=permEm)

    @commands.command(case_insensitive=True)
    @commands.has_permissions(ban_members = True)
    async def kick(self,ctx, member:commands.MemberConverter,*, reason=None):
        kickEmbed = discord.Embed(title="You got kicked.",description=f"You were **kicked** from {member.guild.name}\n**Reason**: {reason}",color=0x00ffea)
        kickEmbed.set_footer(text=f"Action done by: {ctx.author}")
        await member.send(embed=kickEmbed)
        kickChannelEmbed = discord.Embed(description=f"***Kicked <@{member.id}>\nReason: {reason}***",color=0x00ffea) 
        kickChannelEmbed.set_footer(text=f"Action done by: {ctx.author}")
        await ctx.send(embed = kickChannelEmbed)
        await member.kick(reason=reason)


    
    @commands.command(case_insensitive=True)
    @commands.has_permissions(ban_members = True)
    async def ban(self,ctx, member:commands.MemberConverter,*, reason=None):
        banEmbed = discord.Embed(description=f"**Successfully banned** {member.mention}\n**Reason:** {reason}",color=0xfff700)
        banEmbed.set_footer(text = f"Banned by {ctx.author}")
        userEmbed = discord.Embed(title="You were banned.",description=f"**You were banned from {member.guild.name}**\n**Reason: ** {reason}",color=0xfff700)
        userEmbed.set_footer(text=f"Action done by: {ctx.author}")
        await ctx.send(embed= banEmbed)
        await member.send(embed=userEmbed)
        await member.ban(reason =reason)



    @commands.command(case_insensitive=True)
    @commands.has_permissions(ban_members = True)
    async def unban(self,ctx,*, member:discord.User):
        banned_users = await ctx.guild.bans()
        for ban_entry in banned_users:
            user = ban_entry.user
            ubEmbed = discord.Embed(description=f"**Unbanned {member.mention}, say them to rejoin!**",color=0x56f740)
            ubEmbed.set_footer(text=f"Action done by: {ctx.author}")
            await ctx.send(embed = ubEmbed)
            await ctx.guild.unban(member)
            return

    @commands.command(case_insensitive=True)
    @commands.has_permissions(ban_members=True)
    async def warn(self,ctx, member:commands.MemberConverter,*,reason):
        if reason != "":
            warnEmbed = discord.Embed(title="You recieved a warning", description=f"You were warned in {member.guild.name}\n**Reason:** {reason} ")
            warnEmbed.set_footer(text=f"Action taken by: {ctx.author}")
            await member.send(embed=warnEmbed)
            cm = discord.Embed(description=f"**Warned** {member.mention}\n**Reason:** {reason}",color=0x39fc03)
            cm.set_footer(text=f"Action taken by: {ctx.author}")
            await ctx.send(embed=cm)
        else:
            resEmbed = discord.Embed(description="Please provide a valid reason")
            await ctx.send(embed=resEmbed)


        # else:
        #     embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        #     await ctx.send(embed=embed)

#ERRORS---------------------------------------------------------------------
    @kick.error
    async def kick_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            failEm=discord.Embed(description="Invalid syntax, make sure you have mentioned the user you want to kick") 
            await ctx.send(embed=failEm)

        elif isinstance(error, commands.MemberNotFound):
            x=discord.Embed(description="The mentioned user cannot be found")
            await ctx.send(embed=x)
    @ban.error
    async def ban_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            failEm=discord.Embed(description="Invalid syntax, make sure you have mentioned the user you want to ban") 
            await ctx.send(embed=failEm)

        elif isinstance(error, commands.MemberNotFound):
            x=discord.Embed(description="The mentioned user cannot be found")
            await ctx.send(embed=x)
    @unban.error
    async def unban_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            failEm=discord.Embed(description="Invalid syntax, make sure you have mentioned the user you want to unban") 
            await ctx.send(embed=failEm)

        elif isinstance(error, commands.MemberNotFound):
            failEm=discord.Embed(description="The mentioned user cannot be found") 
            await ctx.send(embed=failEm)

def setup(client):
    client.add_cog(moderation(client))