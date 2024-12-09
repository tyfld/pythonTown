from .Humain import Humain
from .Dame import Dame
from .Brigand import Brigand

class Cowboy(Humain):
    def __init__(self, nom, boisson_pref="wisky", adjectif="vaillant"):
        super().__init__(nom, boisson_pref)
        self.__popularite = 0
        self.__adjectif = adjectif

    def se_presenter(self):
        super().se_presenter()
        self.parle(f"Les habitants disent que je suis {self.__adjectif}. Ma côte de popularité est à {self.__popularite} !")
    
    def quelEstTonNom(self):
        return super().quelEstTonNom()
    
    def liberer(self, dame):
        if isinstance(dame, Dame) and not dame.est_libre():
            self.__popularite += 1
            dame.se_faire_liberer(self)
            self.parle(f"C'est toujours un plaisir d'aider une dame en détresse !")

    def tirer(self, brigand):
        if isinstance(brigand, Brigand):
            print(f"Le {self.__adjectif} {self.quelEstTonNom()} tire sur {brigand.quelEstTonNom()}. PAN !")
            self.parle(f"Prends ça, rascal !")