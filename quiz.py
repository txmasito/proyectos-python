titulo = 'Bienvenido al test de queso'
print('\n' + titulo + '\n' + '-' * len(titulo) + '\n')


puntuacion = 0

opcion = input('Pregunta 1: Que haces cuando vez una tabla de quesos?\n'
               'A - Salgo corriendo\n'
               'B - Pruebo uno de los quesos o incluso varios\n'
               'C - No puedo evitar devorarla\n')

if opcion == 'A':
    puntuacion += 0
elif opcion == 'B':
    puntuacion += 5
elif opcion == 'C':
    puntuacion += 10

else:
    print('Las opciones posibles son A, B y C')
    exit()

opcion = input('Pregunta 2: Como te gusta la hamburguesa\n'
               'A - Sin queso\n'
               'B - Con queso\n'
               'C - Pan y queso\n')

if opcion == 'A':
    puntuacion += 0
elif opcion == 'B':
    puntuacion += 5
elif opcion == 'C':
    puntuacion += 10
else:
    print('Las opciones posibles son A, B y C')
    exit()

opcion = input('Pregunta 3: Eres intolerante a la lactosa?\n'
               'A - Si\n'
               'B - A veces\n'
               'C - No\n')

if opcion == 'A':
    puntuacion += 0
elif opcion == 'B':
    puntuacion += 5
elif opcion == 'C':
    puntuacion += 10
else:
    print('Las opciones posibles son A, B y C')
    exit()

if puntuacion >= 25:
    print('Resultado: Felicidades, eres fanatico de los quesos')
elif puntuacion >= 15:
    print('Resultaod: Felicidades, eres una persona que le gusta el queso')
else:
    print('Resultado: Felicidades, no te gusta el queso')

print(puntuacion)