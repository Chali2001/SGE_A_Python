num = 200
salida = True
while num and salida:
    if 100 <= num <= 400:
        print("El número està entre 100 i 400.")
        salida = False
    else:
        print("El número no està entre 100 i 400")
        salida = False