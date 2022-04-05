dolar_euro = 0.91
libra_euro = 1.18

opcion = input('Elija que conversion quiere:\n'
               'A - (LE) Para lia a euro\n'
               'B - (DE) Para dolar a euro')

if opcion == 'A':
    cantidad_en_libras = float(input('Introduzca la cantidad de libras: '))
    print('La cantidad de libras a euros es: {}'.format(cantidad_en_libras * libra_euro))
    print('La cantidad en libras es: {}'.format(cantidad_en_libras * libra_euro))

if opcion == 'B':
    cantidad_en_dolar = float(input('Introduzca la cantidad de dolares: '))
    print('La cantidad de libras a euros es: {}'.format(cantidad_en_dolar * dolar_euro))
    print('La cantidad en libras es: {}'.format(cantidad_en_dolar * dolar_euro))


else:
    print('La conversion no esxiste.')




