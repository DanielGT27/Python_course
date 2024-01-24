
class Persona:
 def __init__(self,nombre,fuerza,velocidad):
     self.nombre=nombre
     self.fuerza=fuerza
     self.velocidad=velocidad
    
 def __str__(self):
    return f'Persona(nombre={self.nombre},fuerza={self.fuerza},velocidad={self.velocidad})'
 
 def __add__(self,otro):
     nuevo_nombre= self.nombre + "-"+ otro.nombre
     nueva_habilidad=((self.fuerza + otro.fuerza)/2)**2
     nueva_velocidad=((self.velocidad+otro.velocidad)/2)**2
     
     return Persona(nuevo_nombre,nueva_habilidad,nueva_velocidad)
 
 


numero_personajes= int(input("Cuantos personajes deseas crear: "))
personajes=list()
objetos=list()


for i in range(numero_personajes):
    
    nombre=input("Dame el nombre de tu personaje: ")
    fuerza=int(input("Dame su nivel de fuerza: "))
    velocidad=int(input("Dame su nivel de velocidad: "))
    
    i=Persona(nombre,fuerza,velocidad)
   
    personajes.append(str(i))
    objetos.append(i)
    



def fusion():
    num_busquedas=int(input("Cuantos personajes deseas fusionar:"))
    per_buscados=list()
    per_econtr=list()
    
    for i in range(num_busquedas):
        nombre_buscado=input("Igresa el nombre del personaje que  deseas fusionar: ")
        per_buscados.append(nombre_buscado)

    for nombre_buscado in per_buscados:
        for obj in objetos:
            if obj.nombre ==nombre_buscado:
                per_econtr.append(obj)
                break
            
    resultado_suma=per_econtr[0]
    
    
    for obj in per_econtr[1:]:
        
        resultado_suma=resultado_suma+obj
        
    return resultado_suma
    
print(f'Estos son los personajes disponibles hasta el momento:{personajes}')

fusionar_personajes=input("Desea fusionar a sus personajes ?: ")

if fusionar_personajes =="si":
    print(fusion())




