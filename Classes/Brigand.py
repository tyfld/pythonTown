from .Humain import Humain
from .Dame import Dame

class Brigand(Humain):
    def __init__(self, nom, boisson_pref="tord-boyaux", look="méchant", prime=100):
        super().__init__(nom, boisson_pref)
        self.__look = look
        self.__dames_enlevées = 0
        self.__prime = prime
        self.__en_prison = False

    def se_presenter(self):
        return super().se_presenter()
    
    def quelEstTonNom(self):
        return f"{ super().quelEstTonNom()} le {self.__look}"
    
    def kidnapper(self, dame):
        if isinstance(dame, Dame) and dame.est_libre:
            self.__dames_enlevées += 1
            print(f"{self.quelEstTonNom()} kidnappe {dame.quelEstTonNom()}  !")
            self.parle(f"Ah ah ! {dame.quelEstTonNom()}, tu es mienne désormais !")
            dame.se_faire_enlever()

    def connaitre_prime(self):
        return self.__prime
    
    def emprisonner(self, sherif):
        pass
            