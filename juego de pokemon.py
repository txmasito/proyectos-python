from random import randint
import os


VIDA_TOTAL_PICKACHU = 80
VIDA_TOTAL_SQUIRTEL = 90

BARRA_VIDA = 10

vida_pikachu = VIDA_TOTAL_PICKACHU
vida_Squirtel = VIDA_TOTAL_SQUIRTEL

while vida_pikachu > 0 and vida_Squirtel > 0:
    print('Turno de Picachu')
    ataque_pikachu = randint(1, 2)
    if ataque_pikachu == 1:
        print('Pikachu atacha con Bola Voltio')
        vida_Squirtel -= 10

    else:
        print('Pikachu  ataca con Onda Trueno')
        vida_Squirtel -= 11

    if vida_pikachu <= 0:
        vida_pikachu = 0
    if vida_Squirtel <= 0:
        vida_Squirtel = 0

    barra_vida_pikachu = int(vida_pikachu * BARRA_VIDA / VIDA_TOTAL_PICKACHU)
    print('Pikachu [{}{}] {}/{}'.format('#' * barra_vida_pikachu, ' ' * (BARRA_VIDA - barra_vida_pikachu),
                                        vida_pikachu,
                                        VIDA_TOTAL_PICKACHU))

    barra_vida_squirtel = int(vida_Squirtel * BARRA_VIDA / VIDA_TOTAL_SQUIRTEL)
    print('Squirtel [{}{}] {}/{}'.format('#' * barra_vida_squirtel, ' ' * (BARRA_VIDA - barra_vida_squirtel),
                                         vida_Squirtel,
                                         VIDA_TOTAL_SQUIRTEL))

    input('Enter para continuar...\n\n')
    os.system('cls')

    print('Turno de Squirtel')

    ataque_squirtel = None
    while ataque_squirtel != 'A' and ataque_squirtel != 'B' and ataque_squirtel != 'C':
        ataque_squirtel = input('Que ataque desea realizar?\n'
                            'A - Placaje\n'
                            'B - Pistola de agua\n'
                            'C - Burbuja\n'
                            'D - Nada')

    if ataque_squirtel == 'A':
        print('\nSquirtel ataca con Placaje')
        vida_pikachu -= 10
    elif ataque_squirtel == 'B':
        print('\nSquirtel ataca con Pistola de agua')
        vida_pikachu -= 12
    elif ataque_squirtel == 'C':
        print('\n'
              'Squirtel ataca con Burbuja')
        vida_pikachu -= 9
    elif ataque_squirtel == 'D':
        print('Squirtel no ataca...')

    if vida_pikachu <= 0:
        vida_pikachu = 0
    if vida_Squirtel <= 0:
        vida_Squirtel = 0


    barra_vida_pikachu = int(vida_pikachu * BARRA_VIDA / VIDA_TOTAL_PICKACHU)
    print('Pikachu [{}{}] {}/{}'.format('#' * barra_vida_pikachu, ' ' * (BARRA_VIDA - barra_vida_pikachu),
                                        vida_pikachu,
                                        VIDA_TOTAL_PICKACHU))

    barra_vida_squirtel = int(vida_Squirtel * BARRA_VIDA / VIDA_TOTAL_SQUIRTEL)
    print('Squirtel [{}{}] {}/{}'.format('#' * barra_vida_squirtel, ' ' * (BARRA_VIDA - barra_vida_squirtel),
                                         vida_Squirtel,
                                         VIDA_TOTAL_SQUIRTEL))

    input('Enter para continuar...\n\n')
    os.system('cls')

if vida_pikachu > vida_Squirtel:
    print('Pikachu gana')
else:
    print('Squirtel gana')

