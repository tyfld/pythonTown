class Humain():
    def __init__(self, nom, boisson_pref="eau"):
        self.__nom = nom
        self.__boisson_pref = boisson_pref

    def parle(self, text):
        print(f"({self.__nom}) - {text}")

    def se_presenter(self):
        self.parle(f"Bonjour, je m'appelle {self.__nom}, et ma boisson préférée est le {self.__boisson_pref}.")

    def boire(self):
        self.parle(f"Ah ! Un bon verre de {self.__boisson_pref} ! GLOUPS !")

    def quelEstTonNom(self):
        return self.__nom
    
    def quelleEstTaBoissonPref(self):
        return self.__boisson_pref