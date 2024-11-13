salari = 20000

if salari < 15000:
    iva = 0
elif salari < 30000:
    iva = 10
elif salari < 60000:
    iva = 21
else:
    iva = 21

Iva2 = salari * (iva / 100)

print("El IVA del", iva, "% de", salari, "€ és:", Iva2, "€")