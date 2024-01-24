#Ejercicio Herencia

class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    
    def edad_grado(self):
        return f'Mi nombre es {self.nombre}, y tengo {self.edad} años'
        

class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado=grado
    
    def grade(self):
     return self.grado

estudiante1=Estudiante("Daniel","16","11c")
        
print(estudiante1.edad_grado())
print(estudiante1.grade())