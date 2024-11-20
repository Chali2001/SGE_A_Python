num = [1, 4, 5, 67, 34, 55, 78, 90, 2, 44, 65, 33, 35, 50]

sumaParell = 0
sumaImparell = 0

for numero in num:
    if numero % 2 == 0:
        sumaParell += numero
    else:
        sumaImparell += numero

print("La suma dels Parells es: ", sumaParell)
print("La suma dels Imparells es: ", sumaImparell)