class Persona:
    def __init__(self,nombre,edad):
        self.__nombre=nombre
        self.edad=edad
#El decorador property define si lo de abajo es un getter o un setter, de est forma se puede utilizar como propiedad

#Ya habiendo utilizado el decorador es posible cambiar el nombre de la función al mismo del atributo original

    @property
    def nombre(self):
        return self.__nombre

# Uso del decorador property pero para setters: 
#Se pone el nombre del getter y se utiliza el metodo setter
    @nombre.setter
    
    def nombre(self,new_name):
        self.__nombre =new_name
        
#Existe un tercer decorador el cual es deletre que permite eliminar valores

    @nombre.deleter
    def nombre(self):
     del self.__nombre
    

persona1=Persona("Daniel",17)

nombre=persona1.nombre

print(nombre)

persona1.nombre="JUAN"

nombre=persona1.nombre

print(nombre)

del persona1.nombre

nombre=persona1.nombre

print(nombre)