from .Humain import Humain

class Barman(Humain):
    def __init__(self, nom, nom_bar=None, boisson_pref="vin"):
        super().__init__(nom, boisson_pref)
        self.__nom_bar = nom_bar

    def se_presenter(self):
        super().se_presenter()
        self.parle(f"Bienvenue dans mon bar : Chez '{self.__nom_bar}', coco.")

    def quelEstTonNom(self):
        return super().quelEstTonNom()
    
    def servir(self, humain):
        if isinstance(humain, Humain):
            self.parle(f"Tenez {humain.quelEstTonNom()}, voici un verre de {humain.quelleEstTaBoissonPref()}, coco.")

    def manger(self, aliment):
        print(f"{self.quelEstTonNom()} grignote du {aliment} entre deux services.")