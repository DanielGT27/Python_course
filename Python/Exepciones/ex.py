# Un evento se refiere a una aciion o suceso especifico que ocurre en un programa 
# y que puede ser manejado por codigo .Lo eventos son tipicamente generados
# en respuesta a la interacción del usuario

def suma ():
    
    # Se ejecuta un vule en el cual si la sentencia es True se seguirá ejecuntando
    
    while True:
    # Se asignan dos variables que son el número que va a ingresar  el usuario 
    
        a = input('Numero 1: ') 
        b = input('Numero 2: ') 
    # Intenta el siguiente codigo :
        try :
             resultado = int(a)+int(b)
             break
    # En caso de recibir una exepcion ejecuta este 
    # Exeptcion es un objehto el cual contiene a todas las exepciones , mediante a este es posible acceder a todas las exepciones
        except Exception as e: 
            print('Te pedio un número , alto gey que eres')
            print(f'El error es : {type(e).__name__}')
    #En caso de no recibir uan exepción ejecuta el else
        else:
            break
        finally:
            print('Se han verificado los errores')
    # El finally se ejecuta independientemente de de lo que se ejecute enteriormente 
       
    return resultado


print(suma())