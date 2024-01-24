# desempaqutado : creacr variables nuevas tomando datos de una tupla o otros

tupla = ('Daniel', 'Galindo ')
lista = ['Hola', 'Manzana',10000]

# El desempaquetado s´polo funciona si la cnatidad de variables es igual a la cantidad de datos de la tupla

# Desempaquetado de tupla

nombre, apellido = tupla

print(nombre)
print(apellido)

# Desempaquetado lista

saludo, comida,dinero = lista

print(dinero)


# Creacion de tuplas (empaquetado )


datos_tupla = tuple(["Dato1","Dato2"])

print(datos_tupla)

# Creando una tupla sin parentesis.
# Se puede crear un atupla de esta manera unicamente separando los datos por una coma

datos_tupla = "Dato1", "Dato2"

print(datos_tupla)

# De igual forma se puede crear una tupla con un único dato de esat forma :

datos_tupla = "Dato1",

print(datos_tupla)


# LAS TUPLAS SE UTILZAN UNICAMENTE EN DATOS DE SOLO LECTURA


# SET (Conjuntos)
# No se pueden poner listas y diccionarios dentro de un conjunto puesto a que estos son modificables 

conjunto_set = set(["Dato 1", "Dato 2"])

# metiendo un conjunto en otro conjunto 

# La manera de meter un conjunto de otro es mediante la función frozenset() , que hace inmutable el conjunto por ende ashable

conjunto1 = frozenset(["Dato1","Dato2"])
conjunto2 = {conjunto1, "Dato3"}


print(conjunto2)


# Teoria de conjuntos 

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

# Metodos de los conjuntos :
# issubset : permite saber si un conjunto es subconjunto de otro , recibe como parametro el conjunto que creemos que es el superconjunto

resultado = conjunto2.issubset(conjunto1)
print(resultado)

# La funcionalidad del metodd .issubset se puede remplazar con el operador logico <=

resultado = conjunto2 <= conjunto1

print(resultado)


# issuperset : nos perite verificar si un conjunto es el superconjunto de otro

resultado = conjunto1.issuperset(conjunto2)

print(resultado)

# Mediante los operadores lógicos se utilza >= para evaluar si un conjunto es el superconjunto de otro

resultado = conjunto1 > conjunto2

print(resultado)

# Verificar si hay algún numero en común
# isdisjoint : evaua si los dos conjuntos son diferentes , es decir , que no tengan ningún elemento en común

resultado1 = conjunto1.isdisjoint(conjunto2) # Arroja false porque tienen elementos en común

print(resultado1)

