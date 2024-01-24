# Los decoradores toman una función como entrada, le agrega una funcionalidad extra 
# y devuevle como salida la nueva función 


# Se establece uns función con el nombre decorador, la cual tiene el parametro funcion
#Luego dentro de esta se crea otra función con el nombre de función modificada, 
#Esta ejecuta una linea de codigo , la función esperada en el parametro y otra linea de codigo luego de ejecutar esa nueva función

def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la función")
        funcion()
        print("Despues de llamar a la funcion")

# Es importante retornar la función modificada al luego de declararla 
    return funcion_modificada

# Se establce la función que servira como parametro del decorador

# def saludo():
#     print("Hola como estas")


# # Es necesario declarar la fiunción decoradora junto a su nueva función como variable
# saludo_modificado= decorador(saludo)

# #La variable se puede declarar como función 
# saludo_modificado()


#Manera optima de utilzar los decoradores: 

@decorador
def saludo():
    print("Hola buenas tardes")

saludo()


# Practica con el uso de decoradores

def decor(funcion):
    def funcion_modificada():
        
        hora_abrir= int(input("Dame la hora actual: "))
        if hora_abrir == 9 :
            funcion()
        else:
            print("No es hora de abrir")
    
    return funcion_modificada
        



@decor
def abrir():
    print("Es hora de abrir, pero necesito una contraseña")
    contraseña=int(input("Ingresa la contraseña: "))
    if contraseña==1234:
        print("La puerta está abierta")
    else:
        print("contraseña incorrecta")

abrir()