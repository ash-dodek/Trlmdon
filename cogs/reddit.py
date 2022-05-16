import discord
from discord.ext import commands
import ffmpeg
import requests,os
import os.path
def compress_video(video_full_path, output_file_name):
    # Reference: https://en.wikipedia.org/wiki/Bit_rate#Encoding_bit_rate
    min_audio_bitrate = 32000
    max_audio_bitrate = 256000
    target_size=5860
    probe = ffmpeg.probe(video_full_path)
    # Video duration, in s.
    duration = float(probe['format']['duration'])
    # Audio bitrate, in bps.
    audio_bitrate = float(next((s for s in probe['streams'] if s['codec_type'] == 'audio'), None)['bit_rate'])
    # Target total bitrate, in bps.
    target_total_bitrate = (target_size * 1024 * 8) / (1.073741824 * duration)

    # Target audio bitrate, in bps
    if 10 * audio_bitrate > target_total_bitrate:
        audio_bitrate = target_total_bitrate / 10
        if audio_bitrate < min_audio_bitrate < target_total_bitrate:
            audio_bitrate = min_audio_bitrate
        elif audio_bitrate > max_audio_bitrate:
            audio_bitrate = max_audio_bitrate
    # Target video bitrate, in bps.
    video_bitrate = target_total_bitrate - audio_bitrate

    i = ffmpeg.input(video_full_path)
    ffmpeg.output(i, os.devnull,
                **{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 1, 'f': 'mp4'}
                ).overwrite_output().run()
    ffmpeg.output(i, output_file_name,
                **{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 2, 'c:a': 'aac', 'b:a': audio_bitrate}
                ).overwrite_output().run()

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
        fSize=os.path.getsize("output.mp4")
        if fSize>7800000: 
            # print("")
            # await ctx.send("compressing")
            compress_video("output.mp4","output_compressed.mp4")
            await ctx.send(file=discord.File("output_compressed.mp4"))
            os.remove("output.mp4")
            os.remove("audio.mp3")
            os.remove("video.mp4")
            os.remove("output_compressed.mp4")
        else:
            await ctx.send(file=discord.File("output.mp4"))
            os.remove("output.mp4")
            os.remove("audio.mp3")
            os.remove("video.mp4")

        # file = discord.File("misc.py", filename="misc.py")
        # await ctx.send(file=discord.File("output.mp4"))
        # await ctx.send("Done")
        # await ctx.send("h")



def setup(client):
    client.add_cog(reddit(client))








