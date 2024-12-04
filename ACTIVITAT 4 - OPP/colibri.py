# Crear una classe
class colibri:
    # Un constructor amb 5 paràmetres
    def __init__(self, specie, color, mida, aliment, zona):
        self.specie = specie
        self.color = color
        self.mida = mida
        self.aliment = aliment
        self.zona = zona

    # Getters i Setters
    def get_specie(self):
        return self.specie
    def set_specie(self, specie):
        self.specie = specie

    def get_color(self):
        return self.color
    def set_color(self, color):
        self.color = color

    def get_mida(self):
        return self.mida
    def set_mida(self, mida):
        self.mida = mida

    def get_aliment(self):
        return self.aliment
    def set_aliment(self, aliment):
        self.aliment = aliment
    
    def get_zona(self):
        return self.zona
    def set_zona(self, zona):
        self.zona = zona

        