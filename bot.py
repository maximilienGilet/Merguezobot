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

cpList = [
"""
V a toi:v: je vois beaucoup de commentaires négatifs, sérieux vous pouvez pas juste être gentil ?! Vous pourissez le groupe. Les pseudos motards qui roule "beaucoup'' sauf : quand il fait un peu gris, quand il fait en dessous de 20°C, quand il y a un peut de vents (sûrement par peur de tomber) quand il y a deux gouttes de pluie.. en hiver n'en parlons pas parce que juste l'idée de monté sur la moto même à l'arrêt vous vous chié dessus et c'est bizarrement les même qui ne répondent pas quand on leurs fait un V ou qui passe à côté quand on est en panne pff aucune solidarité motards vous me dégoûté.. bref, quand on vous souhaite une bonne journée, une bonne soirée ou autre, on répond un truc du genre "à toi aussi :v:" bande de con.
Les kassos qui vont re venir faire des copiés collé, vous êtes apte pour la maternelle, félicitations.
""",
"""
Ahah quelle magnifique mentalité :thumbsup::thumbsup:
Donc c’est quoi vos critères d’une bonne moto ? Un truc qui passe les 300, un ratio Puissance/Poids > 1 et un motard en combi capote ? :joy::joy:
Que tu roules en Harley, SR1000RR ou Tmax, tu fais un faux pas tu finis en bouillit, et peu importe avec quel deux roues tu roules, tu n’auras pas marqué sur ta pierre tombale « ce playboy roulait à 300km/h en SR1000RR ». On prend tous les mêmes risques, on se doit tous le respect :fist: Peu importe si certaines têtes de cons sont plus attirées par un type de bécane, il ne faut pas généraliser. Pisse et lauve:v:
""",
"""
mdrr franchement faudrait changer le nom du groupe pck vous avez rien de progressiste et agréables ici
""",
"""
A2 moi ? serieusement ^^ haha on me l avait pas sortie celle la depuis looooongtemps :slight_smile: demande a mes potes si je suis A2 tu vas voir les reponses que tu vas te prendre XD rien que la semaine passee j ai niquer des 125 avec ma MT07 full donc chuuuuut ferme la A2 de merde car oui toi tu m as tout l air d un bon A2 de merde car souvent vous etes frustrer de ne pas ACCELERER :slight_smile: ses agreable de se faire une pointe à 190 ou une arsouille avec des vrais biker hein? tu peux pas repondre car tu ne sais pas ce que c ou alors tu le sais mais tu as du taper dans ta barre de recherche "Arsouille Dans les Ardennes" ou "Vitesse max MT07" pour comprendre ce que c etait mdddrrr !! c est grave quoiquil en soit.... pour revenir a moi, je pense que je suis le mec le moins A2 de ma bande de 11 meilleurs amis pas psk j ai eu le plus de PV pour exssé de vitesse mais psk j ai eu les plus jolie femme en SDS que mes amis :smile: ses pas moi qui le dit, ses eux qui commente sous mes photos insta "trop belle la fille que t'as arsouille avec hier en autoroute notamment!" donc apres si tu veux que sa parte plus loin sa peut partir vraiment loin donc OKLM hahaha on verra si tu parles encore de A2 de merde mdddrrr pk insulter qd on est soi meme A2 tu me feras toujour marrer!!
""",
"""
Ahah tu m'affiches sur ton groupe? La règle de base c'est de cacher le nom, c'est juste la base. Je pensais être sur moto île de france, j'avais pas vu que j'étais sur neurchi de motocyclette, mais à priori il y a tellement peu d'ambiance dans ce groupe que ta publication de mon com est la publi la plus likée :joy::joy: Bref supprime tu serais un brave gars, déjà que ta bravoure est limitée par cacher ta gueule avec une visseuse et changer de nom :joy::joy::joy:
""",
"""
Du coup toutes les personnes qui ont une voiture savent comment se fait une vidange et comment on change ses injecteurs ? Ou c'est drôle parce-que c'est une moto ?
La mécanique n'intéresse pas tous les utilisateurs.
Un peu comme toi avec l'utilisation d'un smartphone ou d'un PC je suppose par exemple....
""",
"""
Killian Kf 2k, grand, GRAND max 2,5 si elle brille comme un phare. Et encore ptain.
3k, tu peux retourner le problème dans tous les sens, c’est pas le prix même dans la conjoncture actuelle. Ça s’en approche même pas.
T’auras toujours des mecs pour les mettre à ce prix, parce qu’ils savent qu’il y aura toujours, même s’il faut attendre un peu, un gars gentil pour l’acheter à ce prix, en tablant entre autres sur le fait que 3k pour une moto, dans l’absolu ça va c’est pas cher.
Clinique ou pas, kmage faible ou pas, c’est une putain de ZZR, sur aucune planète au monde ça vaut 3k.
Regarde dans les commentaires des mecs qui en ont chopé pour 3x moins que ça dans le même état avec un cligno à changer.
Faut arrêter de tout le temps vouloir défendre les gentils juste parce qu’ils sont du côté des gentils.
Qu’il trouve que nos commentaires ne sont « pas sensés ni intelligents » uniquement parce qu’ils vont pas dans son sens, bon ben il est jeune et il a des œillères de 3 mètres carrés qui lui coupent l’objectivité qu’est ce que tu veux que je te dise.
Moi aussi si je m’étais fait enfler ça me ferait chier de l’admettre, et pour de vrai en plus.
Mais c’est une putain de Kawasaki ZZR les enfants, allo du bateau, ici les côtes, on a plus de signal.
Je m’en branle de l’état, on vent pas une clio 2 à prix d’or juste parce qu’elle a pas de rayure putain.
C’est quasiment le prix de ma Ducati 900 SS que j’ai achetée avec l’équivalent d’une deuxième moto en pièces détachées (et c’était y’a même pas deux ans), allô, on se réveille, youhou.
Tain j’ai l’impression de lire les super héros du clavier qui volent au secours des opprimés de type « oui t’es obèse morbide mais non t’inquiète tu es magnifique comme ça mais non t’es pas an mauvaise santé #bodypositive ».
""",
"""
En fait on va pas refaire le débat sur l'équipement, chaqun est libre de ses choix. Mais si on a un peu de cerveau et d'esprit critique global rouler sans équipement c'est juste favoriser les chiffres actuel. En effet si ce monsieur tombe ça sera quasiment a coup sûr un accident corporel, et il viendra gonfler les chiffres déjà ahurissant de la sécurité routière. Alors que avec juste une veste plus chaussure haute il diminue carrément le risque d'avoir un truc cassé comme un coude ou une épaule ce qui reclasse cet accident en un accident matériel. Donc chaqun fait ce qu'il veux mais si on a un minimum d'esprit motard on s'équipe pour nous, pour convaincre les autres de s'équiper pour eux et aussi pour tout le monde afin que les mesures débile cessent de fleurir pour endiguer la progression des dits chiffres
Voilà bisous :hearts:
""",
"""
salut :v:
Oui dès que s'installe un débat les gens s'enflamment et oublient la courtoisie et le respect qui devrait être la norme dans une discussion.

Et je te rejoins sur le fait que la solidarité motarde périclite avec le temps :confused:

C'est fou le nombre de moto qui ne sont plus présente sur les routes des que le temps est gris :joy:

Enfin bref et sinon tu roule dans quel coin toi ? :v:
""",
"""
écoute si tu avais lus mon message je dis en préambule que je prône la liberté individuelle. Mais après si tu veux pas rouler sous la pluie c'est ton choix, la moto doit rester un plaisir donc si tu aime pas être mouillé ou que ce n'est pas ton délire de partir qu'importe le temps c'est ta vie. 
Et concernant l'équipement je suis seulement attristé par ceux qui vont arsouiller sans équipement, les petits trajets j'en ai fait aussi sans équipement.
 Mais de toute façon la moto c'est à mon sens une histoire d'humilité et de remise en question. 
En conclusion de la question le la famille des motards, c'est la solidarité et le respect qui importe, par exemple ne pas laisser un deux roue en galère sur le bord de la route et proposer son aide ça c'est être motard :v:

Bisous à toi et tu peux aussi essayer d'étoffer tes commentaires en proposant de nouvelles idées pour alimenter le débat :ok_hand:
""",
"""
pareils commentaire non constructif  .
Et te prends pas pour dieu car je le suis pas et toi non plus sinon tu ferais pas le pinguoin sur une mobylette que tu maîtrise pas. 
Car si tu étais si fort tu ferai pas ton rigolo a parlé mais plutôt a roulé. Ça fait 30 ans que je roule donc je vais pas recevoir de leçon d'un gamin qui chier dans son froque il y a encore 2 ans . Sur ceux au plaisir gamin . A si quand tu auras roulé autant que moi tu reviendra me parler. Bisous gamin.
""",
"""
Pas be soin d’être irrespectueux si ça vous emmerde de voir ma caisse bah vous me bloquez et basta j’ai pas besoin de voir vos vieux commentaires irrespectueux
""",
"""
Maxime mais frère t'es con ou quoi? le mec a une assurance complète et dans deux jours il a une caisse!!!! moi j'ai 20 ans et j'ai rien d'autre j'ai perdu ma caisse et moi alors dans l'histoire? "Tu as ruiné leur seul moyen de transport" et moi? dans l'histoire? le mien? J'ai niqué ma voiture, la leurs je m'en fous...eux ils ont une caisse dans un ou deux jours, moi pas !
""",
"""
Salut les bikers je suis moi même motard. Mais je comprends les automobilistes qui aime pas les motos. J'étais en voiture à Verigné entre briollay et Tiercé quand je me suis fait doublé par un abrutie en moto, route limitée à 70 se taré nous a doublé à plus de 150  et je suis jentil. Ligne continue passé de l'autre côté du haricot avec des passages piétons de l'on vois au dernier moment. Toi qui roule comme ça je pense savoir qui tu es. Et que tu habite dans les hauts de cheffes. Si tu lis se message ai le courage de répondre. J'étais là 306 verte que ta doublé comme un con
""",
"""
Ici tous le monde critique les 206 en elle même alors que le plus gros problème c'est souvent les propriétaires, a vrai dire une 206 avec une bonne prepa et bah c'est pas si dégueu, avec une vraie bonne prepa complete y'a sûrement moyen de calmer des golf en virage. Allez bisous sur le petou
""",
"""
de qui la grosse daube pardon excuse moi tu parler de toi et t'es copains avec vos commentaires inutiles avant de parler où critiqués derrière un ordinateur on apprend a balayé devant ça porte je savais pas que c'était un groupe pour des hommes qui ont un complexe d'infériorité sur ceux bonne journée
""",
"""Tu as pas du rouler beaucoup en ducati pour dire qu'il n'y a aucune performance... Certe elle reste difficile à piloter bien plus que les jap mais en même temp piloter une ducati sa se mérite et surtout tu apprend à piloter avec pas comme les jap ou n'importe qui peu enchaîner des tours dire que c'est une moto à caractère banal loll okkkk bein loue en un va rouler avec autre que sur le parking de lidl et tu reviendra nous dire qu'une ducat sa a un caractère banal et je finirai pour ta science que ducati n'es pa plus fragile qu'une autre la preuve en es en wsbk sur une saison ils ont passé moin de moteur que toutes les autres marques après certe les entretients sont plus minutieux et si tu es subgenre chaouie je fou la clé et je démarre je m'en bas les balls de l'huile et l'entretient oui effectivement sa reste une moto problématique mais dans se cas la question à se posé es plutôt de savoir qui es le problème la moto avec un entretient minutieux ou toi qui achète une moto sans prendre en compte se qu'elle a besoin ?

20mkm uniquement de circuit ( sauf les 1200km de rodage) et la seul panne à était le capteur de pression atmosphériques que j'ai cassé moi en démontent les polis pour l'entretien hivernale..  Donc fragile non je crois pas
""",
"""
Ce qui est le plus angoissant ce sont vos commentaires désobligeant, on dirait des collégiens en train de passer leur BsR. Je suis sur que les trois quart ne se permettrait pas en face de la personne. Vous êtes vraiment des tocards sans savoir vivre.
Pas étonnant que les motards passent pour des boloss regardez comment vous vous parlez entre vous
""",
"""
Sans rigoler.

Je pratique la motocyclette depuis maintenant 6 ans, de la mécanique en parallèle depuis 7 ans, faut pas me faire chier moi.

Ainsi que la piste depuis 4 ans, 1m87 pour 86 kg

J'ai une vitesse de fou, et des réflexes identiques à ma vitesse. J'ai juste à l'attendre qu'il y ait une ligne droite, rétrograder et lui donner un grand coup d'accélérateur. Je le lâcherai pas à la moindre erreur, la voiture est finie. T'auras toujours des puceaux d'ici pour penser que c'est impossible. Rien n'est impossible avec de la volonté déjà les amis, et de 2) c'est pas avec votre moto de lâche que vous allez faire quoi que ce soit.

N'importe quel homme un minimum entraîné peut doubler une voiture dans le sinueux. Dans les cols c'est pas forcément plus compliqué ça demande juste de la technique.
""",
"""
enfants de 19kg, mawashigueri, tourne retourne, couteau jaune, coupe en cubes, marmite rouge, feu vif et voila, c'est prêt, donne aux cochons
""",
"""
Je rage des prix des Daytona, je rage des gens qui disent que les petites cylindrées c'est nul, je rage sur moi-même, je rage contre les Twingo et les fiat 500, je rage contre mon ex, je rage contre les MT-07 sauf celles de Bob, je rage du charisme du Tronchet, je rage du chien du Guido, je rage quand on dit chocolatine, je rage quand on me dit comment faire des quiches lorraines (cc Gαuvαin )
""",
"""
La violence du pilotage :smirk::heart_eyes: et ce bruit ? La première raison pour laquelle je passe le permis moto : faire de la piste ayant soif de vitesse et d'adrénaline :smirk::sweat_smile: deja que sur route en moto école je penche fort j'accélère quelques peu fort par moment je suis pas trop fait pour rouler sur route ouverte, chacun son profil de conduite :sweat_smile: au moins je me mettrais pas en danger sur piste, ou beaucoup moins :sweat_smile: et je pourrai ouvrir les gaz en grand sans risquer ma peau et celle des autres usagers :wink:
""",
"""
Rien à foutre ! Moi je roule en Monter 620ie :smirk: Pat'patrouille, pom'potes et Rock'n'rol... j'ai mon namoureuse qui roule aussi mais j'aime trop notre club house,le kif de ce faire ''sucer'' avec un Candy'up à la main par une invitée...je mate pas vos portraits ni mp,quand tu es à 50 bornes de panam les clubs sa circule...ont a ce qui faut sans Facebook...:wink:
"""
]

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
    brief="Un CP au hasard"
)
async def cp(ctx):
    await ctx.channel.send(random.choice(cpList))

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
