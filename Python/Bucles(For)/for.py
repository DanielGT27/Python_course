# un bucle se trabaja con elementos iterables
# Un elemento iterable es ele que consta de un iterador

# Elementos iterables , las listas , cadenas de texto , tupla , dict , conjunto

# Bucle for in , nos permite iterar


animales = ["perro", "gato", "larartija", "pajaro","iguana","loro"]

for animal in animales :
    
    print(f'Ahora el valor de animal es : {animal}')
   


# Recorriendo la lista numeros y multiplicando cada uno de sus elementos por 2
numeros = [23,45,12,5,6,78]

for i in numeros :
    print(i*2)
    
# función range para generar una lista de numeros range(min , max)

# Iterar dos listas al mismo tiempo
# Es importante que ambas listas tegan la misma cantidad de elementos
# Se utilza la función zip() de la siguiente forma

for i,a in zip(animales, numeros):
    print(f'recorriendo lista 1 : {i}')
    print(f'recorriendo lista 2:{a}')
    
# Iterando con la función range ()

for num in range(1,20):
    
    resultado = num * 2
    print(resultado)
    
    if resultado == 10:
        break


# forma correcta de recotrer una lista por us indice
# La función enumerate convuerte a cada elemento en una tupla con dos datos , (el indice, el elemento)

for num in enumerate(numeros) : 
    
    valor = num[1]
    indice = num[0]
    print(indice)
    
# desempaquetar 

for i,num in enumerate(numeros) :
    print(f'el indice {i} tiene el valor de {num}')


# usando el else en un for
#for else
# El el se ejecuta una sola vez y es al final de cada bucle 

for num in numeros :
    print(num)
else :
    print( "El bucle terminó")



# Todo lo anterior funciona para tuplas, listas y conjuntos


# Iterar diccionarios :

diccionario = {
    'nombre' : 'Daniel',
    'apellido' : 'Galindo',
    'subs' : 1
    
}

# Para recorrer ambos llave y valor se utilza el método items()

for key in diccionario.items():
    
    llave = key[0]
    valor = key[1]
    
    print(f'La llave es {llave}, su valor es {valor}')


# Más iteraciones 

frutas = ["manzana", "pera", "tomate", "fresa", "naranja", "Guanabana"]


# continue nos permite que si el iterador se encuentra con cierto valor , que se lo salte y continue con el ciclo

for i in frutas :
    if i == "fresa" :
        continue
    print(f'me voy a comer {i}')
    

# Evitar que el bucle siga ejecutandose  utilizando break:
# Cuando se utiliza break , todo lo que vaya despues de eso no se ejecuta incluido un else

for i in frutas :
    
    print(i)
    if i == "fresa":
        break
    
# Recorrer una cadena de texto :
# Se recorre caracter por caracter

cadena = "Hola Elgt27"

for i in cadena :
    print(i)
    
# bucles for en una sola linea de codigo para duplicar una lista de numeros
#  sin una sola linea de codigo :

bitcoin = [3,4,5,7,9]

numeros_duplicados= list()

for i in bitcoin :
    numeros_duplicados.append(i*2)
    
print(numeros_duplicados)
    
# Optimizado una sola linea de codigo

numeros_duplicados = [x*2 for x in bitcoin]

   
   
    