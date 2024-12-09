from .Humain import Humain

class Dame(Humain):
    def __init__(self, nom, couleur_robe, boisson_pref="lait"):
        super().__init__(nom, boisson_pref)
        self.__couleur_robe = couleur_robe
        self.__est_captive = False

    def se_presenter(self):
        super().se_presenter()
        self.parle(f"Avez-vous remarqué ma belle robe {self.__couleur_robe} ? Je l'adore tellement !")
    
    def quelEstTonNom(self):
        return f"Miss {super().quelEstTonNom()}"
    
    def se_faire_enlever(self):
        if self.est_libre():
            self.__est_captive = True
            print(f"{self.quelEstTonNom()} hurle : Aaaah ! Au secours !")

    def se_faire_liberer(self, cowboy):
        if self.__est_captive and hasattr(cowboy, 'quelEstTonNom'):
            self.__est_captive = False
            self.parle(f"Merci {cowboy.quelEstTonNom()} de m'avoir sauvée !")

    def est_libre(self):
        return not self.__est_captive
    
    def changer_de_robe(self, nouvelle_couleur):
        self.__couleur_robe = nouvelle_couleur
        self.parle(f"Regarder la nouvelle robe que j'ai acheté ! Elle est magnifique en {self.__couleur_robe} !")

    def manger(self, aliment):
        print(f"{self.quelEstTonNom()} mange une {aliment} avec élégance.")