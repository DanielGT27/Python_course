# Las clases abstractas se refieren a una plantilla de la cual se pueden crear otras clases
# a diferencia de la herencia estas no pueden ser instanciadas


# ES NECCESARIO PARA LA CREACIÓN DE CLASES ABTRACTAS:
from abc import ABC, abstractclassmethod

#La clase abstracta debe heredar de ABC para ser considerada abstracta
class Persona(ABC):

#se introduce el decorador @abstractclassmethod para definir los atributos
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
        self.actividad=actividad

# de  igual forma se introduce este decorador al momento de realizar cualquier metodo en la clase abstracta

    @abstractclassmethod
    def  hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f'Hola me llamo {self.nombre}, y tengo {self.edad} años')
    
        

#Para utilizar la clase abstracta como plantilla , la nueva clase debe heredar la clase abstracta

class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)

#Tanto como la clase abtracta y la clase deben tener los mismos metodos o sino existe une excepción 

    def hacer_actividad(self):
        print(f'Estoy estudiando: {self.actividad}')
        


class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad)
        
    def hacer_actividad(self):
        print(f'Actualmente estoy trabajando en {self.actividad}')
        
        
estudiante1=Estudiante("Daniel",17,"masculino","programcion")
trabajador1=Trabajador("Lucas",23,"Nesquick","Construcción")

estudiante1.presentarse()
estudiante1.hacer_actividad()
trabajador1.presentarse()
trabajador1.hacer_actividad()
