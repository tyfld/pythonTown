from Classes.Brigand import Brigand
from Classes.Cowboy import Cowboy
from Classes.Dame import Dame
from Classes.Barman import Barman
from Classes.Sherif import Sherif

from os import system, name
from time import sleep

# Fonction pour clear le terminal
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

# sleep for 2 seconds after printing output
sleep(2)


if __name__ == "__main__":

    dame_prologue1 = Dame("Juliette","vert","lait")
    dame_prologue2 = Dame("Lisa","vert","lait")

    brigand = Brigand("Bill","tord-boyaux")
    cowboy = Cowboy("John", "whisky")
    barman = Barman("Tony", "Tony", "vin")

    dame1 = Dame("Marie","bleu","lait")
    dame2 = Dame("Véronica","jaune","lait")
    dame = Dame("Daisy","rouge","lait")

    sherif = Sherif("Robert", "wisky")

#Notre scénario
clear()
print(f"Dans une ville non loin de Python Town, un brigand semait la terreur en kidnappant de nombreuses dames.")
sleep(2)
brigand.kidnapper(dame_prologue1)
brigand.kidnapper(dame_prologue2)
brigand.se_presenter()
print(f"Le brigand venait de kidnapper deux belles dames !")
print(f"Mais il ne pouvait pas agir ainsi sans subir les conséquences.")
print(f"Un vaillant cowboy arriva et tira sur le vilain brigand :")
cowboy.tirer(brigand)
cowboy.se_presenter()
cowboy.parle(f"N'ayez crainte, mes demoiselles ! Je vais vous libérer.")
print(f"S'écria le cowboy. Il réussit à sauver Miss Juliette.")
cowboy.liberer(dame)
sleep(2)
print(f"Malheureusement, le brigand réussit à prendre la fuite...")
sleep(5)
print(f"Le cowboy se retrouva à Python Town et décida de se rendre au bar le plus proche.")
print(f"A l'intérieur se trouvaient le barman et trois dames en pleine conversation.")
cowboy.parle(f"Bonjour, barman, un whisky, s'il vous plaît.")
barman.se_presenter()
barman.servir(cowboy)
cowboy.boire()
print(f"Notre brave cowboy décida de boire son verre silencieusement et d'écouter les dames parler.")
sleep(2)
dame1.changer_de_robe("rose")
dame1.parle(f"Je l'ai achetée dans la boutique d'à côté !")
dame.parle(f"Oh, elle te va si bien, Miss Marie !")
dame2.parle(f"D'ailleurs, avez-vous entendu parler de ce qui s'est passé dans la ville voisine ? Les pauvres...")
dame.parle(f"Nous n'avons rien à craindre, mes amies, notre shérif ferait fuir n'importe quel brigand !")
sleep(2)
print(f"Le cowboy se leva et sortit du bar, bien décidé à retrouver ce bandit.")
print(f"Il alla voir le shérif de la ville pour lui fournir les informations qu'il avait.")
sleep(2)
sherif.se_presenter()
sherif.parle(f"Ah, donc tu as déjà rencontré ce scélérat ? J'ai entendu parler de ses méfaits.")
cowboy.parle(f"Oui, en effet ! Est-ce que je peux compter sur vous pour l'arrêter ?")
sherif.parle(f"Mais bien sûr ! C'est mon devoir après tout.")
sleep(2)
print(f"Soudain, un cri se fit entendre. Les deux hommes coururent pour voir ce qui se passait.")
brigand.kidnapper(dame)
print(f"Le brigand venait de kidnapper Miss Daisy !")
brigand.parle(f"Ah ah ! Vous ne m'attraperez jamais !")
print(f"Les deux hommes essayèrent d'intervenir, mais il était trop tard... Le brigand s'était enfui, emportant la belle Daisy avec lui.")
sleep(2)
print(f"Le lendemain, le shérif décida de plaquer des avis de recherche partout dans la ville.")
sherif.rechercher(brigand)
print(f"Soudain, il aperçut le brigand passer et se jeta sur lui. Pendant ce temps, le cowboy en profita pour libérer la dame.")
cowboy.liberer(dame)
dame.parle(f"Vous êtes mon héros !")
sherif.coffrer(brigand)
print(f"Le brigand étant enfin sous les barreaux, Miss Daisy invita ses deux sauveurs au bar pour les remercier.")
dame.manger("salade")
cowboy.manger("côte de porc")
sherif.manger("poulet")
print(f"Le calme régna sur Python Town.")