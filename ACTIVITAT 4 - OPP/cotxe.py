# Crear una classe
class cotxe:
    # Un constructor amb 5 paràmetres
    def __init__(self, marca, model, any, color, combustible):
        self.marca = marca
        self.model = model
        self.any = any
        self.color = color
        self.combustible = combustible

    # Getters i Setters
    def get_marca(self):
        return self.marca
    def set_marca(self, marca):
        self.marca = marca

    def get_model(self):
        return self.model
    def set_model(self, model):
        self.model = model

    def get_any(self):
        return self.any
    def set_any(self, any):
        self.any = any

    def get_color(self):
        return self.color
    def set_color(self, color):
        self.color = color
    
    def get_combustible(self):
        return self.combustible
    def set_combustible(self, combustible):
        self.combustible = combustible

        