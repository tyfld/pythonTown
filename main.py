from Classes.Brigand import Brigand
from Classes.Cowboy import Cowboy
from Classes.Dame import Dame
from Classes.Barman import Barman
from Classes.Sherif import Sherif

if __name__ == "__main__":
    brigand = Brigand("Bill","tord-boyaux")
    cowboy = Cowboy("John", "whisky")
    dame = Dame("Daisy","rouge","lait")
    barman = Barman("Tony", "Tony", "vin")
    sherif = Sherif("Robert", "wisky")


#Notre scénario
brigand.se_presenter()
cowboy.se_presenter()
dame.se_presenter()
dame.changer_de_robe("jaune")
print()
brigand.kidnapper(dame)
cowboy.tirer(brigand)
cowboy.liberer(dame)

print()
brigand.se_presenter()
cowboy.se_presenter()

print()
barman.se_presenter()
barman.servir(cowboy)

print()
sherif.se_presenter()
sherif.rechercher(brigand)
sherif.coffrer(brigand)
sherif.se_presenter()
dame.manger("salade")