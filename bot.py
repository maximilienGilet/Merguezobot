import discord
import random
import re
import requests
from bs4 import BeautifulSoup
import os

command = os.environ.get('MERGUEZ_COMMAND', "!merguez")
motoplanete = 'https://www.motoplanete.com'
searchPath = "/researchFicheMoto.php"

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if "https://www.leboncoin.fr/motos/" in message.content:
            count = int(random.random()*10)
            if count == 1:
                await message.channel.send('Dégage avec ta merde !')

        if message.content.startswith(command):
            search = message.content.replace(command, "")
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
                    await message.channel.send(motoplanete + link['href'])
                    if not os.environ.get('MERGUEZ_DISABLE_DETAILS') == "true" :
                        details = requests.get(motoplanete + link['href'])
                        if details.ok:
                            detailsSoup = BeautifulSoup(details.text)
                            chassis = re.sub(' +',' ',detailsSoup.find_all(class_="assise")[0].text.strip())
                            moteur = re.sub(' +',' ',detailsSoup.find_all(class_="moteur")[0].text.strip())
                            await message.channel.send(os.linesep.join([s for s in chassis.splitlines() if s]))
                            await message.channel.send(os.linesep.join([s for s in moteur.splitlines() if s]))
                        else:
                            await message.channel.send("J'ai pas plus d'infos")
                else:
                    await message.channel.send("J'ai pas trouvé, dégage avec ta merde")
            else:
                await message.channel.send("Ça a planté chef")


client = MyClient()

discord_key = os.environ.get('MERGUEZ_DISCORD_SECRET_KEY')
if discord_key:
    client.run(discord_key)
else: 
    print("You must set the MERGUEZ_DISCORD_SECRET_KEY environment variable with the Discord secret key of your bot")
