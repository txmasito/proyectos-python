print('-- COMPRANDO TU NUEVO SMARTPHONE --')

tipo_de_cell = (input('Android o IOS:\n'
                           'A - Android\n'
                           'B - IOS '))

if tipo_de_cell == 'A':
    pregunta = (input('Tienes dinero: SI o NO\n'))

    if pregunta == 'SI':
        print('Pues te recomendamos el Google Pixel 5 XL')
    if pregunta == 'NO':
        print('Pues te compras un Xiaomi pa "kalidat-prezio"')

if tipo_de_cell == 'B':
    pregunta = (input('Tienes dinero: SI o NO\n'))

    if pregunta == 'SI':
        print('Pues te recomendamos el Iphone 12 Pro Max (256GB)')
    if pregunta == 'NO':
        print('Pues te compras un Iphone 7 de segunda mano crack')

else:
    print('Las opciones disponibles solo son A y B')