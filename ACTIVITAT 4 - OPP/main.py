# Importem les classes Cotxe i Colibri des dels arxius corresponents
from cotxe import cotxe
from colibri import colibri

# 3 Instàncies de Cotxe
cotxe1 = cotxe("Toyota", "Corolla", 2020, "Blau", "Hibrid")
cotxe2 = cotxe("Ford", "Focus", 2021, "Vermell", "Diesel")
cotxe3 = cotxe("BMW", "X5", 2022, "Negre", "Gasolina")

# 3 Instàncies de Colibri
colibri1 = colibri("Colibrí Verdos", "Verde", "Petit", "Nèctar", "Amèrica")
colibri2 = colibri("Colibrí Rubí", "Vermell", "Mitjà", "Flor", "Amèrica")
colibri3 = colibri("Colibrí Nevat", "Blanc", "Gran", "Fruit", "Àsiatic")

# Mostrem 3 getters de Cotxe
print("cotxe 1: Marca =", cotxe1.get_marca())
print("cotxe 1: Model =", cotxe1.get_model())
print("cotxe 1: Any =", cotxe1.get_any())

# Mostrem 4 getters de Colibri
print("colibrí Verdos: Specie =", colibri1.get_specie())
print("colibrí Verdos: Color =", colibri1.get_color())
print("colibrí Verdos: mida =", colibri1.get_mida())
print("colibrí Verdos: Zona =", colibri1.get_zona())

# Modificar 2 atributs de Cotxe a través dels setters
cotxe1.set_color("Verd")
cotxe1.set_combustible("Electric")

# Mostrar els 2 atributs modificats a través dels getters
print("Cotxe 1 modificat: Color =", cotxe1.get_color())
print("Cotxe 1 modificat: Combustible =", cotxe1.get_combustible())

# Modificar 2 atributs de Colibrí a través dels setters
colibri1.set_color("lila")
colibri1.set_mida("Molt petit")

# Mostrar els 2 atributs modificats a través dels get
print("Colibri 1 modificat: Color =", colibri1.get_color())
print("Colibri 1 modificat: Mida =", colibri1.get_mida())