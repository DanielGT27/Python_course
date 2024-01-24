# Creando diccionarios con dict()

diccionario = dict(nombre = 'Daniel', apellido ='Galindo ')


print(diccionario)

#Mostrando el diccionario
# Se puede incluir unicamente una tupla o un frozenset como llaves dentro de un diccionario
# Es recomendable utilziar una tupla puesto a que consume menos recursos

diccionario = {
    ("Hola", "Gente") : 'Dato1',
    'dinero' : 10000
}

print(diccionario)

print(diccionario[("Hola", "Gente")])


# Creando diccionario con el método fromkeys, este recibe dos paramentros iterables uno con las llaves y otras con los valores

dicionerio_formkeys = dict().fromkeys(['nombre','apellido'])

valor_nombre = dicionerio_formkeys['nombre'] = "Daniel"

print(dicionerio_formkeys)
print(valor_nombre)


# Llamar el valor de un conjunto