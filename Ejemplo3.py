h = []
i = 0 

n = int(input("Cuantos estudiantes?: "))
for i in range(n):
    alt = float(input("Dime la altura: "))
    h.append(alt)

suma = 0
for alt in h:
        suma += alt

media = suma/len(h)
print("La medida es ", media)

altos = 0
bajos = 0

for alt in h:
    if(alt > media):
        altos = altos + 1
    
    if (alt < media):
        bajos = bajos + 1

print("Altos: ", altos)
print("Bajos: ", bajos)





