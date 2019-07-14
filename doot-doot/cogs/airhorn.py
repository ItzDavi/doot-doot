import discord
import random
import asyncio
from discord.ext import commands

async def play_file(ctx, filename):
    voice_channel = ctx.author.voice.channel
    print(f'{str(ctx.author)} is in {voice_channel}')
    try:
        voice_channel = await voice_channel.connect()
    except Exception as e:
        voice_channel.disconnect()
        ctx.send("Exception occured, automatic process " +
        "atempted to repair it, please try again. | " + str(e))

    # There is a 1 in 100th chance that it
    # will do a rickroll instead of the desired sound
    randomChance = random.randint(1, 100)
    if randomChance == 1:
        source = discord.FFmpegPCMAudio("sounds/rickroll.mp3")
    else:
        source = discord.FFmpegPCMAudio(filename)

    voice_channel.play(source, after=lambda: print("played doot"))

    await ctx.send(":thumbsup: played the effect")
    while voice_channel.is_playing():
        await asyncio.sleep(1)

    voice_channel.stop()

    await voice_channel.disconnect()


class airhorn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def doot(self, ctx):
        """Doots the horn."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "sounds/airhorn.mp3")

    @commands.command()
    @commands.guild_only()
    async def bazinga(self, ctx):
        """Plays bazinga effect."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "sounds/bazinga.mp3")

    @commands.command()
    @commands.guild_only()
    async def justdoit(self, ctx):
        """Tells you to just do it."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "sounds/justdoit.mp3")

    @commands.command()
    @commands.guild_only()
    async def clap(self, ctx):
        """Just some clapping."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "sounds/clap.mp3")

    @commands.command()
    @commands.guild_only()
    async def oof(self, ctx):
        """Roblox oof."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "sounds/oof.mp3")

    @commands.command()
    @commands.guild_only()
    async def nope(self, ctx):
        """Nope."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "sounds/nope.mp3")

    @commands.command()
    @commands.guild_only()
    async def suspence(self, ctx):
        """Sudden suspence."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "sounds/suddensus.mp3")

    @commands.command()
    @commands.guild_only()
    async def sad(self, ctx):
        """Plays sad music."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "sounds/sadmusic.mp3")

    @commands.command()
    @commands.guild_only()
    async def fail(self, ctx):
        """Plays fail sound."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "sounds/fail.mp3")

    @commands.command()
    @commands.guild_only()
    async def gay(self, ctx):
        """HA GAY."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "sounds/hagay.mp3")


    @commands.command()
    @commands.guild_only()
    async def no(self, ctx):
        """Says no."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "no.mp3")

    @commands.command()
    @commands.guild_only()
    async def godno(self, ctx):
        """plays No god no."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "godno.mp3")

    @commands.command()
    @commands.guild_only()
    async def dootstorm(self, ctx):
        """plays sands storm but with doot."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "dootstorm.mp3")

    @commands.command()
    @commands.guild_only()
    async def WTF(self, ctx):
        """plays Bish WTF."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "WTF.mp3")

    @commands.command()
    @commands.guild_only()
    async def fuckedup(self, ctx):
        """it was at this moment he knew he fucked up."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "fuckedup.mp3")

    @commands.command()
    @commands.guild_only()
    async def ohno(self, ctx):
        """oh no no no."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "ohno.mp3")

    @commands.command()
    @commands.guild_only()
    async def ohhh(self, ctx):
        """ohhhhhhh."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "ohhh.mp3")

    @commands.command()
    @commands.guild_only()
    async def thuglife(self, ctx):
        """thug life."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "thuglife.mp3")

    @commands.command()
    @commands.guild_only()
    async def horn(self, ctx):
        """DJ horn."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "djhorn.mp3")


    @commands.command()
    @commands.guild_only()
    async def phintro(self, ctx):
        """Scare the s### out of your friends."""
        if not ctx.author.voice:
            await ctx.send("You are not in a voice channel.")
        else:
            await play_file(ctx, "phintro.mp3")

def setup(bot):
    bot.add_cog(airhorn(bot))
