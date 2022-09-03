from statistics import median
import statistics
puntuacion = [1,10,8,2,19,14,30,6,4,1,26,28,9,40]
puntos = puntuacion
i = 1
print("Datos del array")
for i in range (len(puntuacion)):
    print(puntos[i])
media = statistics.mean(puntuacion)
print("La media es: ", media)
