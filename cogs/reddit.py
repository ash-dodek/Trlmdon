import discord
from discord.ext import commands
import requests,os
import os.path

class reddit(commands.Cog):

    def __init__(self,client):
        self.client=client
    @commands.Cog.listener()
    async def on_ready(self):
        print("Loaded Reddit")
    
    @commands.command()
    async def reddit(self,ctx,*,url):
        if os.path.exists("audio.mp3") == True:
            os.remove("audio.mp3")
        if os.path.exists("video.mp4") == True:
            os.remove("video.mp4")
        if os.path.exists("output.mp4") == True:
            os.remove("output.mp4")
        
        url = url[:-1]+".json"
        # title = random_post["data"]["title"]
        r = requests.get(url,headers={"User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"})
        data = r.json()[0]
        video_url = data["data"]['children'][0]['data']['secure_media']['reddit_video']['fallback_url']
        audio_url = "https://v.redd.it/"+video_url.split("/")[3]+"/DASH_audio.mp4"
        with open("video.mp4","wb") as f:
            g = requests.get(video_url,stream=True)
            f.write(g.content)
        with open("audio.mp3","wb") as f:
            g = requests.get(audio_url,stream=True)
            f.write(g.content)
        os.system("ffmpeg -i video.mp4 -i audio.mp3 -c copy output.mp4")
        # file = discord.File("misc.py", filename="misc.py")
        await ctx.send(file=discord.File("output.mp4"))
        os.remove("audio.mp3")
        os.remove("video.mp4")
        os.remove("output.mp4")
        # await ctx.send("Done")
        # await ctx.send("h")



def setup(client):
    client.add_cog(reddit(client))








