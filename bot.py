import discord
from discord import activity
from discord.ext import commands
import random
import re
import requests
from bs4 import BeautifulSoup
import os

motoplanete = 'https://www.motoplanete.com'
searchPath = "/researchFicheMoto.php"
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(
        activity=discord.Activity(type=discord.ActivityType.watching, name="les merguez à 1€ le cc sur leboncoin", url="https://www.leboncoin.fr/recherche?category=3&cubic_capacity=200-max&price=100-1500"),
        command_prefix="!",  # Change to desired prefix
        case_insensitive=True,  # Commands aren't case-sensitive
        intents=intents
    )

@bot.event
async def on_ready():
    print("I'm in !")
    print(bot.user)

@bot.event
async def on_member_join(member):
    print('member join')
    print(member)
    channel = discord.utils.get(member.guild.text_channels, name="gueuloir")
    await channel.send(f"""
{member.mention}
Faut qu’on remplisse le tableau :chart_with_upwards_trend: des membres pour envoyer :incoming_envelope:les carte d’adhésions mais tqt ces gratuit :moneybag::moneybag:
Donc nous avons besoins de:man_technologist::
Nom
Prénom
Taille :point_up_2_tone3:
Pointure :boot:(une photo de ton pied en vue de dessus,coter et dessous stp)
Analyse d’urine :toilet:
Photo de toutes les femmes + de 7/10 que tu connais :dancer_tone1:
""")

@bot.command(
    # ADDS THIS VALUE TO THE $HELP PING MESSAGE.
    help="Uses come crazy logic to determine if pong is actually the correct value or not.",
    # ADDS THIS VALUE TO THE $HELP MESSAGE.
    brief="Prints pong back to the channel."
)
async def ping(ctx): 
    await ctx.channel.send("pong ta mère")



@bot.command(
    help="Trouve une merguez sur motoplanete",
    brief="Trouve une merguez sur motoplanete, tu peux même mettre l'année !"
)
async def mergez(ctx, args):
    search = args
    searchData = {
        "nom": search
    }
    # find year in search
    match = re.match(r'.*(((19)|(20))[0-9]{2})', search)
    if match is not None:
        # Then it found a match!
        year = match.group(1)
        search = search.replace(year, "")
        searchData = {
            "nom": search,
            "annee": year
        }
    
    res = requests.post(motoplanete + searchPath, data = searchData)
    if res.ok:
        soup = BeautifulSoup(res.text)
        links = soup.find_all(class_="view")
        if len(links) > 0:
            link = links[0]
            await ctx.channel.send(motoplanete + link['href'])
            if not os.environ.get('MERGUEZ_DISABLE_DETAILS') == "true" :
                details = requests.get(motoplanete + link['href'])
                if details.ok:
                    detailsSoup = BeautifulSoup(details.text)
                    chassis = re.sub(' +',' ',detailsSoup.find_all(class_="assise")[0].text.strip())
                    moteur = re.sub(' +',' ',detailsSoup.find_all(class_="moteur")[0].text.strip())
                    await ctx.channel.send(os.linesep.join([s for s in chassis.splitlines() if s]))
                    await ctx.channel.send(os.linesep.join([s for s in moteur.splitlines() if s]))
                else:
                    await ctx.channel.send("J'ai pas plus d'infos")
        else:
            await ctx.channel.send("J'ai pas trouvé, dégage avec ta merde")
    else:
        await ctx.channel.send("Ça a planté chef") 


@bot.event
async def on_message(message): 

    # don't respond to ourselves
    if message.author == bot.user:
        return

    if "https://www.leboncoin.fr/motos/" in message.content:
        count = int(random.random()*10)
        if count == 1:
            await message.channel.send('Dégage avec ta merde !')

    # INCLUDES THE COMMANDS FOR THE BOT. WITHOUT THIS LINE, YOU CANNOT TRIGGER YOUR COMMANDS.
    await bot.process_commands(message)
    
    
discord_key = os.environ.get('MERGUEZ_DISCORD_SECRET_KEY')
if discord_key:
    bot.run(discord_key)

else: 
    print("You must set the MERGUEZ_DISCORD_SECRET_KEY environment variable with the Discord secret key of your bot")
