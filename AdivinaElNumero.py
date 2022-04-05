import random

numero_ganador = random.randint(1, 10)
numero_elejido = int(input('Elija un numero: '))

if numero_ganador == numero_elejido:
    print('Haz ganado')

if numero_elejido > 10:
    print('Uy te haz pasado un poco')

print('No, el numero ganador era: {}'.format(numero_ganador))