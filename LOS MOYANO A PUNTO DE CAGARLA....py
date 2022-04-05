import random

print('LOS MOYANO A PUNTO DE CAGARLA...\n')
print('Los hermanos Moyano y 4 amigos más Mark, Wicho y Camila\n'
      'se sumergen en un mundo virtual que simula a la perfección el Call of Duty Mobile,\n'
      'y resulta que caen en un Buscar y Destruir en el mapa de RAID. Su respanw\n'
      'toca del lado de jungla.\n')
print('Mark con QQ-9\n'
      'Wicho con AK117\n'
      'Camila con Bizon\n'
      'Diego con Locus\n'
      'Rodrigo con QXRn\n')
print('Comienza el juego y hacen la táctica estandar los Moyano se van a defender\n'
      'la bomba de B (al frente de lavandería), Mark y Camila se van a defender la bomba de A (en cancha)\n'
      'y Wicho se va solo al cubrir medio (en cocina).')
print('El primero en morir fue Wicho quien lo alcanzó un esnipazo desde piscina cuando trataba\n'
      'de ver desde la ventana de dinero si veía un enemigo, solo quedan 4 jugadores vs 5.')
print('Wicho le dice el callout a Mark.')

opcion1 = input('¿Mark rushea SI o NO? ')

if opcion1 == 'SI':
    print('Mark rushea, el sniper lo escucha venir y la rata saca duales y mata a Mark.\n'
          'Aparecen los 5 enemigos uno detras del otro y Camila los mata a todos con full auto con la Bizon y ganan.')
else:
    print('Mark no rushea, aguanta posi el sniper se confia avanza y Mark lo mata.\n')
    print('Los Moyano le dan el call a Mark de que los demás enemigos quieren ir full B\n\n')

    opcion2 = input('¿Mark se va junto con Camila a B o se queda para seguir avanzando por piscina? SI o NO ')

    if opcion2 == 'SI':
        print('Se van hacia B y se unen a los Moyano para defender.\n')
        print('Mark llendo hacia B detras de Camila sale un enemigo por cocina mata a Camila y Mark lo mata.\n'
              'Ahora el juego está 3vs3 el enemigo ve que tienen la bomba de B bien protegida y decide retroceder\n'
              'e ir a por la bomba de A.\n\n'
              'Los Moyano y Mark van hacia A por detras de cocina y Diego ve el arma de Camila en el piso\n\n')

        opcion3 = input('¿La toma SI o NO?')

        if opcion3 == 'SI':
            print('Llegan a la bomba de A Rodrigo mata a un enemigo en piscina, otro enemigo\n'
                  'mata a Mark, Rodrigo mata a ese enemigo y el ultimo enemigo mata a Rodrigo\n'
                  'deside rushear a Diego este le falla varias balas del sniper, pero toma el arma\n'
                  'secundaria (que era de Camila) y lo mata y ganan.')
        else:
            print('Llegan todos a la bomba de A Rodrigo y Mark matan a dos enemigos y el ultimo\n'
                  'los termina matando a ellos va le rushea a Diego este le falla balas del sniper\n'
                  'tiene que recargar pero el enemigo lo mat y pierden.')
    else:
        print('Decide avanzar por piscina donde de la nada sale un enemigo en dormitorio\n'
              'y mata a Mark haciendo que Camila escapara por dobles yendo por cocina hasta llegar a lavanderia\n'
              'con los Moyano.\n')
        print('Los Moyano junto con Camila defienden B, Camila mata uno en pilares, Rodrigo mata otro\n'
              'en estatua y Diego luego de tanto disparar con el Locus a ver si colaba el wallban se queda\n'
              'con 5 balas en el cargador. Aún quedan dos enemigos.\n\n'
              'Uno de ellos está en arte y Rodrigo decide lanzarle una granada, pero primero necesita saber\n'
              'cuanto dinero le dejó su padre antes de irse a trabajar y le pregunta a Diego ¿Diego cuanto dinero\n'
              'dejó el viejo?\n\n'
              'Diego no sabia exactamente cuanto dinero dejó y calcula la cantidad que dejó la semana\n'
              'pasada unos 200 pesos por una cantidad random.\n')

        opcion4 = 200

        opcion5 = int(input('¿Cual es la cantidad?'))

        if opcion5 == opcion4 * '{}'.format(random.randint):
            print('Le dice la cantidad correcta a Rodrigo tira bien la granada mata al enemigo\n'
                  'y Camila ve el otro enemigo por rampa lo mata y ganan.')
        else:
            print('No le dice la cantidad correcta a Rodrigo duda de la cantidad que le dice Diego\n'
                  'se ponen a discutir sobre eso, matan a Rodrigo desde arte,\n'
                  'el otro enemigo les da la vuelta mata a Camila y le rushea\n'
                  'a Diego en lavandería lo mata y pierden.')