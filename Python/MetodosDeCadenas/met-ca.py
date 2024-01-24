# Metodos: funciones especificas  que tienen los objetos en phyton

cadena1 = "hola soy ELGT27"
cadena2 = "bienvenido maquina"
numero = 14

dir(cadena1) # dir nos permite conocer todos los metodos del objeto selecionado

print(dir(cadena1))

resultado = dir(cadena1)

# Upper : Convierte todo a mayusculas
# se estructura un métodod de la siguiente forma  : objeto.metodo()
print(cadena1.upper())

#Lower : Convierte todo en minuscula

print(cadena1.lower())

#Capitalize : Convierte la primera letra en mayuscula

print(cadena1.capitalize())
print(cadena2.capitalize())


# Find : encontrar una cadena dentro de otra

print("hola" in cadena1)
print(cadena1.find("hola"))

# La diferencia entre el metdod .find y el operador in . 
# Es que el metodo devuelve la posición en la que se encuentra la cadena.
# Si no encuentra la cadena devuelve -1.


 # Index : encontrar una cadena dentro de otra
 # La diferencia con el método Find es que si no encuentra la caden devuelve un error 
 # Se manejara luego para la exepciones
 

print(cadena1.index("ola"))

# Isnumeric consulta si la cadena consiste en sólo valores numericos 


cadena1 = "12345679g"

print(cadena1.isnumeric())



# Isalfa consulta si en la cadena solo hay letras 

cadena2= "HolaSoyElgt"

print(cadena2.isalpha())

# Count : nos dice cuantas veces encontro una cadena dentro de otra

print(cadena2.count("aSoy"))

#len : contamos la contidad de caracteres que tiene una cadena LEN ES UNA FUNCIÓN  NO ES UN MÉTODO

print(len(cadena1))


#startwith : nos dice si una cadena empieza con otra cadena  

print(cadena2.startswith("Ho"))



# endswith : nos dice si la cadena termina con otra cadena que le asignemos.

print(cadena1.endswith("9g"))

# replace : nos permite cambiar un a cadena dentro de otra 


cadena3 = "Hola.Gente.Increible.Gods"

print(cadena1.replace("123", "was"))
print(cadena1)

correccion = cadena3.replace(".", " ")

print(cadena3)
print(correccion)

correcion_2 = correccion.capitalize()

print(correcion_2)
print(correcion_2.upper())


# Split : permite separar una cadena con otra cadena que le pasemos, convierte al nuevo valor en una lista


print(cadena3.split("."))
