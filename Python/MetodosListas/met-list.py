 
 
 # List : en una función que nos permite crear una lista , util para crear listas vacias
 
lista = list(["Hola",2 ,"Buenas", "SHINO",True])

# Len : Nos permitre conocer la cantidad de elementos que hay en una lista

lista_len = len(lista)

print(lista_len)

# Append : nos permite agregar elementos 

agregar_elemento_append = lista.append("CHINO")

print(lista)

print(len(lista))

#Insert : permite agregar un elemento a la lista per especificandole la posición en la qu equeremso poner dicho elemento

agregar_elemento_insert = lista.insert(3, "Tardes")

print(lista)


# Extend : permite agregar varios elementos a la lista , la manera de agregarlos es por medio de otra lista

agregar_elemento_extend = lista.extend(["CHESS", "GOD", 23 , True])

print(lista)
print(len(lista))

#Pop : eliminando un elemento de la lista por su indice, s epuede eliminar el ultimo con -1

elminar_pop = lista.pop(-2)

print(lista)
print(len(lista))

# Remove : se remueve un elemento de la lista por su valor

eliminar_remove = lista.remove("SHINO")
print(lista)
print(len(lista))

# Clear : elimina todos los elementos de la lista

# eliminar_clear = lista.clear()

print(lista)

# Sort : ordena los elementos de manera ascendente con su propiedad reverse= true , se invierte este orden

lista_2 = [21,True,67,False,2]

ordenar_acendente=lista_2.sort()

print(lista_2)

ordenar_decendete=lista_2.sort(reverse=True)

print(lista_2)


# Reverse : invierte los elementos de la lista

lista_3 =[21,True,67,False,2]

invertir_el = lista_3.reverse()

print(lista_3)

# En el caso de las tuplas solo se puede contar los elementos con el metodo count y buscar un elemento en la lista

tupla = tuple([1,"Hola", 34])

print(dir(tuple([1,"Hola", 34])))

buscar_index = tupla.index(34)

print( buscar_index)

contar_count = tupla.count(34)

print(contar_count)


# En el caso de un conjunto set , lo unico que se puede hacer es remover (remove) , quitar (pop), copiar (copy) 


print(dir(set(["Hola",3 , 24])))

conjunto = set(["Hola",3 , 24])

