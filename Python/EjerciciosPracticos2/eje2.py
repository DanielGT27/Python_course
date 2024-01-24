
# Falto el profe y los pibes van a hacer la clase

# pedir el nombre y la edad de los compañeros



def obtener_compañeros(cantidad) :
     compañeros = []

     for i in range(cantidad) :
         nombre = input(f'Hola compañero , me puedes decir tu nombre : ')
         edad = int(input(f'Hola amigo, tambien me podrias decir tu edad: '))
         compañero =(nombre, edad)
         compañeros.append(compañero)
         
     compañeros.sort(key=lambda x : x[1])
     asistente = compañeros[0][0]
     maestro = compañeros[-1][0]
     return asistente , maestro
 

asistente, profesor = obtener_compañeros(4)

print(f'El alumno que es el maestro es {asistente} y su asistente es {profesor}')




def alumnos (lista) :
    ordenar = max(lista)
    return ordenar


print(alumnos([1,34,56,78]))