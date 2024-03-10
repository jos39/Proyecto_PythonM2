# Iniciamos un bucle para que el programa se ejecute hasta que el usuario ponga un dato correcto
while True:
    opcion = input('¿Qué programa deseas ejecutar? (1, 2 o 3): \
                   \n1 Longitud de una palabra \
                   \n2 Encuentra un cuadrante  \
                   \n3 Salir del programa  \n')
    

    ########################### Programa 1 ##############################################
    if opcion == '1':
        # Iniciamos un bucle para que el programa se ejecute hasta que el usuario ponga los datos
        while True:
            palabra = input('Introduce una palabra entre 4 y 8 letras: ')
            if not palabra:                                             # Vericamos que no este vacio el campo
                print('Por favor, introduce una palabra.')
                continue                                                # Si esta correcto continua el programa

            if not palabra.isalpha():                                   # Verifica si la palabra contiene solo letras
                print('Por favor, introduce solo letras.')
            else:
                longitud_palabra = len(palabra)                         # Variable para guarda cual es longitud de la palabra
                if 4 <= longitud_palabra <= 8:                          # Si contiene la palabra entre 4 y 8 entra a esta condicion
                    print('La palabra es correcta.')
                elif longitud_palabra < 4:                              # Si contiene la palabra menos de 4 entra a esta condicion
                    print('Faltan letras. La palabra', palabra, 'solo tiene', longitud_palabra, 'letras.')
                else:                                                   # si no se cumple las condiciones entra aqui
                    print('Sobran letras. La palabra', palabra, 'tiene', longitud_palabra, 'letras.')
                break  # Salir del bucle interno si no se quiere ejecutar de nuevo


    ########################### Programa 2 ##############################################
    elif opcion == '2':
        # Creamos una funcion para que pida x, y para no tener que repetir el codigo
        def solicitar_coordenada(coordenada):
            while True:
                x = input(coordenada)
                if not x.lstrip('-').isdigit():                         # ELiminamos si introduce negativo para verificar que introduzca un digito
                    print('Por favor, introduce un número.')
                    continue

                x = int(x)                                              # Casteamos el numero a entero

                if x == 0:                                              # Verificamos si intruduce cero
                    print('Introduce un número diferente de 0.')
                else:
                    break                                               # Rompemos el bucle
            return x                                                    # Devuelve el valor de la coordenada
        
        # Llamamos a la función para obtener los valores de x, y
        x = solicitar_coordenada('Introduce X: ')
        y = solicitar_coordenada('Introduce Y: ')

        # Hacemos la validaciones correspodientes para determinar el cuadrante
        if x > 0 and y > 0:
            print('El punto se encuentra en el cuadrante I')
        elif x < 0 and y > 0:
            print('El punto se encuentra en el cuadrante II')
        elif x < 0 and y < 0:
            print('El punto se encuentra en el cuadrante III')
        else:
            print('El punto se encuentra en el cuadrante IV')


    # Sale del programa 
    elif opcion == '3':
        break


    # Si no introduce una opcion correcta
    else:
        print('Opción no válida. Por favor, ingresa "1", "2" o "3".')


    respuesta = input('¿Desea volver a ejecutar otro programa? (s/n): ')# Por si el usuario quiere volver a intertarlo
    if respuesta.lower() != 's':                                        # Transforma a minusculas
        break