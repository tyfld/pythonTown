from .Humain import Humain
from .Dame import Dame
from .Sherif import Sherif

class Brigand(Humain):
    def __init__(self, nom, boisson_pref="tord-boyaux", look="méchant", prime=100):
        super().__init__(nom, boisson_pref)
        self.__look = look
        self.__dames_enlevées = 0
        self.__prime = prime
        self.__en_prison = False

    def se_presenter(self):
        super().se_presenter()
        self.parle(f"J'ai l'air {self.__look} et j'ai déjà kidnappé {self.__dames_enlevées} dames !")
        self.parle(f"Ma tête est mise à prix à {self.__prime} !")
    
    def quelEstTonNom(self):
        return f"{ super().quelEstTonNom()} le {self.__look}"
    
    def kidnapper(self, dame):
        if isinstance(dame, Dame) and dame.est_libre:
            self.__dames_enlevées += 1
            print(f"{self.quelEstTonNom()} kidnappe {dame.quelEstTonNom()}  !")
            self.parle(f"Ah ah ! {dame.quelEstTonNom()}, tu es mienne désormais !")
            dame.se_faire_enlever()

    def avoir_prime(self):
        return self.__prime
    
    def emprisonner(self, sherif):
        if isinstance(sherif, Sherif):
            self.__en_prison = True
            self.parle(f"Damned, je suis fait ! {sherif.quelEstTonNom()}, tu m'as eu !")

    def manger(self, aliment):
        print(f"{self.quelEstTonNom()} mange du {aliment} avec bruyamment.")
            