import discord
from discord import client
from discord import voice_client
from discord import colour
from discord.ext import commands, tasks
import random
from itertools import cycle
# import cog
# import youtube_dl
import praw
import music
from io import BytesIO
from PIL import Image,ImageFont,ImageDraw
import time
import datetime
from PIL import Image, ImageEnhance

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())
client.remove_command('help')
status = cycle(['Murdering game haters!!', 'Printing("Hello world")', 'Gta5 :D', 'FIFA!'])




@client.event
async def on_ready():
    print('We Have logged in as {0.user}'.format(client))
    # client.load_extension('dismusic')
    change_status.start()







@client.event
async def on_message(message):
    #On ping
    if f'<@!{client.user.id}>' in message.content:
        embed = discord.Embed(title='Want Something!!', colour=discord.Colour.dark_grey())
        embed.add_field(name='Want Some Help!', value='```Type !help for some help```')
        embed.set_image(url='https://c.tenor.com/1vtM0MVvOg4AAAAd/when-ping-ping.gif')
        await message.channel.send(embed=embed)
        return
    await client.process_commands(message)



@client.event
async def on_member_join(ctx, member):
    embed = discord.Embed(title=f"{member} just showed up!!", colour=discord.Colour.dark_gold())
    await ctx.send(embed=embed)
    role = discord.utils.get(ctx.guild.roles, name = "{New Boi}") 
    await ctx.add_roles(role)




@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title='Invalid Command Please Enter a Valid Command!', colour=discord.Colour.dark_gold())
        embed.add_field(name="Want help?", value='```!help```')
        await ctx.send(embed=embed)




@client.event
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title='Please Enter the Required Argument!', colour=discord.Colour.dark_gold())
        await ctx.send(embed=embed)



@client.command()
async def hi(ctx):
            async with ctx.channel.typing():
                responses = ['Hello',
                            'whats going on',
                            'You disturbed me']
                await ctx.send(random.choice(responses))






@client.command(case_insensitive=True)
async def say(ctx, saymsg=None):
            async with ctx.channel.typing():
                if saymsg==None:
                    await ctx.send('Please Add a message to say!')

                sayEmbed = discord.Embed(title=f"{ctx.author.name} Say's", color= discord.Color.blue(), description=f"{saymsg}")
                sayEmbed.timestamp = ctx.message.created_at
                await ctx.send(embed=sayEmbed)







@client.command()
async def bye(ctx):
            async with ctx.channel.typing():
                    await ctx.send('Bye\n''https://tenor.com/view/feels-cry-tears-upset-emotional-gif-5342266')






@client.command()
async def ping(ctx):
            async with ctx.channel.typing():
                embed = discord.Embed(title="Ping", colour=0x3498db,)
                embed.add_field(name="pong", value=round(client.latency * 1000))
                await ctx.send(embed=embed)







@client.command(aliases=['8ball', 'ball'])
async def _8ball(ctx, *, question):
            async with ctx.channel.typing():
                responses = ['It is Certain.',
                            'it is decidely so.',
                            'You may rely on it',
                            'Ask again later'
                            'Bruh']
                await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')






@client.command()
async def clear(ctx, amount=6):
            async with ctx.channel.typing():
                await ctx.channel.purge(limit=amount)






@client.command()
async def kick(ctx, memeber : discord.Member, *, reason=None):
    await memeber.kick(reason=reason)






@client.command()
async def ban(ctx, memeber : discord.Member, *, reason=None):
    await memeber.ban(reason=reason)






@client.command(help="To unban people")
async def unban(ctx, *, user=None):

    try:
        user = await commands.converter.UserConverter().convert(ctx, user)
    except:
        await ctx.send("USER NOT FOUND!!")
        return

    try:
        bans = tuple(ban_entry.user for ban_entry in await ctx.guild.bans())
        if user in bans:
            await ctx.guild.unban(user)
        else:
            await ctx.send(F"{user.mention} is not in Banned List!!")
            return

    except Exception as e:
        await ctx.send(f"Error: {e} User unbanned")
        return







@client.command()
async def help(ctx):
            async with ctx.channel.typing():
                embed = discord.Embed(
                    title='LetCodingBegin', 
                    description='Coder and a gamer bot!!',
                    color = discord.Color.blue()
                )

                embed.set_footer(text='Help!!')
                embed.set_thumbnail(url='https://cdna.artstation.com/p/assets/images/images/024/715/012/large/pinkuoir-esidisi2.jpg?1583300397')
                embed.set_image(url='https://cdna.artstation.com/p/assets/images/images/024/715/012/large/pinkuoir-esidisi2.jpg?1583300397')
                embed.set_author(name='Gamingismylife')
                embed.add_field(name='kick', value='Kick user', inline=False)
                embed.add_field(name='ban', value='Ban user', inline=True)
                embed.add_field(name='unban', value='Unbans user', inline=True)
                embed.add_field(name='clear', value='Clears chat', inline=True)
                embed.add_field(name='ping', value='Shows ping', inline=True)
                embed.add_field(name='hi', value='Find it out', inline=True)
                embed.add_field(name='Bye', value='Find it out', inline=True)
                embed.add_field(name='Avatar', value='Shows the Avatar', inline=False)
                embed.add_field(name='Join', value='Joins the voice channel',inline=True)
                embed.add_field(name='leave', value='Leaves the voice channel',inline=True)
                embed.add_field(name='whois', value='Shows Genral Information', inline=True)
                embed.add_field(name='help', value='Shows this message', inline=True)
                embed.add_field(name='meme', value='Shows a random meme!',inline=False)
                embed.add_field(name='Wanted', value='to make someone wanted',inline=True)
                embed.add_field(name='say', value='Says What you Wish!',inline=True)
                embed.add_field(name='crime', value='Set Bounty on someones',inline=True)
                embed.add_field(name='play', value='Plays music',inline=True)
                embed.add_field(name='pause', value='pauses the music',inline=False)
                embed.add_field(name='resume', value='resumes the music',inline=True)
                embed.add_field(name='slap', value='Slaps Someones',inline=True)
                embed.add_field(name='kill', value='To kill someone',inline=False)
                embed.add_field(name='kiss', value='To kiss someone',inline=True)
                embed.add_field(name='poll', value='To add up a Poll',inline=True)
                embed.add_field(name='thank', value='To thank someone',inline=True)
                embed.add_field(name='Poke', value='To poke somone',inline=True)
                await ctx.send(embed=embed)


@client.command(aliases=['user', 'info'])
@commands.has_permissions(kick_members=True)
async def whois(ctx,member : discord.Member):
        async with ctx.channel.typing():
            embed = discord.Embed(Title=member.name , description = member.mention, color= discord.Color.red())
            embed.add_field(name = "ID", value=member.id, inline=True)
            await ctx.send(embed=embed)


@client.command()
async def avatar(ctx, member : discord.Member = None):
    async with ctx.channel.typing():
            if member is None:
                embed = discord.Embed(title="This command is used like this: ```!avatar [member]```", colour=0x3498db, timestamp=ctx.message.created_at)
                await ctx.send(embed=embed)
                return

            else:
                embed2 = discord.Embed(title=f"{member}'s Avatar!", colour=0x3498db, timestamp=ctx.message.created_at)
                embed2.add_field(name="Animated?", value=member.is_avatar_animated())
                embed2.set_image(url=member.avatar_url)
                await ctx.send(embed=embed2)



@client.command(pass_context=True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send('Please Join A Voice Channel')


@client.command(pass_context = True)
async def lv(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        user = ctx.message.author.name
        embed = discord.Embed(title='I left the voice channel.', colour=discord.Colour.blue)
        embed.add_field(name="On the request of", value=f"{user}")
        await ctx.send(embed=embed)
    else:
        await ctx.send('I am not in a voice channel.')



@client.command()
async def meme(ctx):
    async with ctx.channel.typing():
        reddit = praw.Reddit(client_id='U_ZcqYupoZNt6T7i4nmqTw',
    client_secret='ZE2xblFizUBtvYQpG5mjgRGW9z_hqg',
    user_agent='Memes :D')
    
    memes_subbmissions = reddit.subreddit('memes').hot()
    post_to_pick = random.randint(1, 1000)
    for i in range(0, post_to_pick):
        subbmission = next(x for x in memes_subbmissions if not x.stickied)
    await ctx.send(subbmission.url)


@client.command()
async def wanted(ctx, user: discord.Member = None):
        async with ctx.channel.typing():
            if user == None:
                user = ctx.author

        wanted = Image.open("Wanted.jpg")

        asset = user.avatar_url_as(size = 1024)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((500, 560))
        wanted.paste(pfp, (80, 210))

        wanted.save("profile.jpg")

        await ctx.send(file = discord.File("profile.jpg"))





client.lava_nodes = [
    {
        'host': 'lava.link',
        'port': 80,
        'rest_uri': f"http://lava.link:80",
        'identifier' : 'MAIN',
        'password' : 'anything',
        'region' : 'singapore'
    }
]




@client.command()
async def crime(ctx, user: discord.Member = None):
    async with ctx.channel.typing():
            if user == None:
                user = ctx.author

    crime = Image.open("Criminal.jpg")

    asset = user.avatar_url_as(size=1024)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((320,320))
    crime.paste(pfp, (360, 90))

    crime.save("crime.jpg")

    await ctx.send(file=discord.File("crime.jpg"))



@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))




@client.command()
async def slap(ctx, member : discord.Member = None):
    async with ctx.channel.typing():
                    if member is None:
                        embed = discord.Embed(title="This command is used like this: ```!slap [member]```", colour=0x3498db, timestamp=ctx.message.created_at)
                        await ctx.send(embed=embed)
                        return
                    else:
                        embed = discord.Embed(title=f'{ctx.author.name} Slapped {member}', colour=discord.Color.blue())

                        embed.set_image(url='https://media0.giphy.com/media/gSIz6gGLhguOY/giphy.gif?cid=ecf05e47rsgnzrfxnpl7idl8n22xllxp8ff11ekw36fthlpq&rid=giphy.gif&ct=g')

                        await ctx.send(embed=embed)



@client.command()
async def poll(ctx, *, question=None):
        async with ctx.channel.typing():
            if question == None:
                await ctx.send('```Please add a question```')
            else:
                icon_url = ctx.author.avatar_url 
        
            pollEmbed = discord.Embed(title = "New Poll!", description = f"{question}")
        
            pollEmbed.set_footer(text = f"Poll given by {ctx.author}", icon_url = ctx.author.avatar_url)
        
            pollEmbed.timestamp = ctx.message.created_at 
        
            await ctx.message.delete()
        
            poll_msg = await ctx.send(embed = pollEmbed)
        
            await poll_msg.add_reaction("⬆️")
            await poll_msg.add_reaction("⬇️")



@client.command()
async def kill(ctx, member: discord.Member = None):
        async with ctx.channel.typing():
            if member == None:
                embed = discord.Embed(title='Please Add A Member Name!', colour=discord.Colour.dark_gold())
                await ctx.send(embed=embed)
            else:
                username = ctx.message.author.name
                timestamp=ctx.message.created_at
                embed = discord.Embed(title='New Kill!')
                embed.add_field(name='Killer', value=f'{username}')
                embed.add_field(name='Killed', value=f'{member}')
                embed.set_image(url='https://64.media.tumblr.com/8a3155edac398dee8b97b3ff2d0bffa6/tumblr_nopurcuyZ01u7gt7ro1_r1_400.gifv')
                await ctx.send(embed=embed)


@client.command()
async def kiss(ctx, member: discord.Member = None):
        async with ctx.channel.typing():
            if member == None:
                embed = discord.Embed(title='Please add someone to kiss!', colour=discord.Colour.dark_gold())
                await ctx.send(embed=embed)
            else:
                username = ctx.message.author.name
                embed = discord.Embed(title='Kiss detected!!')
                embed.add_field(name='Kisser', value=f'{username}')
                embed.add_field(name='Kissed', value=f'{member}')
                embed.set_image(url='http://www.reactiongifs.com/wp-content/uploads/2013/11/1106.gif')
                await ctx.send(embed=embed)




@client.command()
async def poke(ctx, member: discord.Member = None):
    async with ctx.channel.typing():
        if member == None:
            embed = discord.Embed(title='Hey! add someone to poke!', colour=discord.Color.dark_gold())
            embed.add_field(name='!poke ```member```')
            await ctx.send(embed=embed)
        else:
            user = ctx.message.author.name
            embed = discord.Embed(title='That was a Hard One!!', colour=discord.Colour.dark_blue())
            embed.add_field(name=f'{user} Poked!', value=f'{member}')
            embed.set_image(url='https://c.tenor.com/7dl2wy-8ePUAAAAM/poke-im-not-poking-you.gif')
            await ctx.send(embed=embed)



@client.command()
async def thank(ctx, member: discord.Member = None):
    async with ctx.channel.typing():
        if member == None:
            embed = discord.Embed(title='Hey! add someone to Thank!', colour=discord.Color.dark_gold())
            embed.add_field(name='!thank ```member```')
            await ctx.send(embed=embed)
        else:
            user = ctx.message.author.name
            embed = discord.Embed(title='Thanks For Thanks!', colour=discord.Colour.dark_gold())
            embed.add_field(name='Thanker!!', value=f'{user}')
            embed.add_field(name='Thanks To!!', value=f'{member}')
            embed.set_image(url='https://c.tenor.com/jJITWKXdHdIAAAAM/dog-bark.gif')
            await ctx.send(embed=embed)





client.run('YOUR_SECRET_HERE_I_AINT_UPLOADING_MINE')