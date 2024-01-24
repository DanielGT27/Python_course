# Datos compuestos son los cuales tiene más de un sólo dato ya sea simple o compuesto 

# LISTA : Un conjunto de datos expresados con []

lista =["DanielGT27", True, 16 ]

print(lista)

# Acceder a un dato especifico de la lista
# Lista es un tipo de matriz

lista[0] = "hola"
print(lista[0])

print(lista)



numero = "123456"
Descomponer = list(numero)

print(Descomponer)

#TUPLAS : Similares a las listas pero se expresa por medio de ()

# La diferencia entre una lista y una tupla es que una tupla no se puede modificar ninguno de los valores de la lista

tupla = ("DanielGT27", True, 16 )

# tupla[1]= False (Esto no es válido)

# CONJUNTO (SET) No tiene un orden fijo que pueden cambiar  

conjunto = {"DanielGT27", True, 16 , "DanielGT27"}

# En un conjunto no se puede acceder a un elemnto por medio de un indice
# En un conjunto no pueden haber datos duplicados

print(conjunto)

numeros = "123234343123345322312233478923397"

Descomponer = set(numeros)

print(Descomponer)

# La manera de accedera los items de un conjunto en  mediante un bucle


#DICCIONARIO (dict) (La esgtructura es key : value y se separa por comas)

diccionario ={
'nombre' : "Daniel Galindo",
'edad' : 16 ,
'Feliz' : False 

    
}


print(diccionario)
print(diccionario['nombre'])




