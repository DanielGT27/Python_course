
diccionario = {
    'nombre' : "Daniel",
    'apellido' : "Galindo",
    'subs' : 1
}


#Keys : devuelve las llaves del diccionario , es util para iterar

claves = diccionario.keys()

print(claves)

# Get : devuelve el valor de una llave que pongamos , no devuele un esatdo de exepción

buscar_get = diccionario.get('apellido')

print(buscar_get)

# La diferencia entre obtener un valor con el metodo y sin el metodo es que sin el metodo genera una excepción

print(diccionario['nombre'])

# Clear : elimina todo el contenido del diccionario

# elimina_elementos = diccionario.clear()
print(diccionario)

# Pop : elimina un elemento del diccionario por el nombre de la llave

eliminar_un_elemento = diccionario.pop('apellido')

print(diccionario)

# Items devuelve los elementos del diccionario de manera iterable

diccionario_iterable = diccionario.items()

print(diccionario_iterable)


