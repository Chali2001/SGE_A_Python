num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]

print("Números parells:")
for parell in num:
    if parell % 2 == 0:
        print(parell)

print("Números imparells:")
for imparells in num:
    if imparells % 2 != 0:
        print(imparells)