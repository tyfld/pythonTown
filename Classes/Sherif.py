from .Humain import Humain
from .Brigand import Brigand

class Sherif(Humain):
    def __init__(self, nom, boisson_pref="wisky", adjectif="honnête"):
        super().__init__(nom, boisson_pref, adjectif)
        self.__brigands_coffres = 0

    def se_presenter(self):
        super().se_presenter()
        self.parle(f"Je suis quelqu'un d'{self.__adjectif} et j'ai déjà coffré {self.__brigands_coffres} brigands !")

    def quelEstTonNom(self):
        return f"Shérif {super().quelEstTonNom()}"
    
    def coffrer(self, brigand):
        if isinstance(brigand, Brigand) and not brigand.__en_prison:
            from .Cowboy import Cowboy # Import du cowboy delayée poour éviter une erreur d'import circulaire
            self.__brigands_coffres += 1
            self.parle(f"Au nom de la loi, je vous arrête !")
            brigand.emprisonner(self)

    def rechercher(self, brigand):
        if isinstance(brigand, Brigand) and not brigand.__en_prison:
            self.parle(f"OYER OYER BRAVE GENS !!! {brigand.avoir_prime} à qui arrêtera {brigand.quelEstTonNom} mort ou vif !")