# Setters y Getters son dos metodos que se utilizan para acceder y modificar atributos y metodos muy privados


class Persona:
    def __init__(self,nombre,edad):
# Se establecen los atributos privados con la notación del guion bajo
        self.__nombre=nombre
        self.__edad=edad

# Se realiza una función con el prefijo get_ y el nombre del atributo para acceder al atributo privado

    def get_nombre(self):
        return  self.__nombre

# Se utilizan los setters para definir el atribut privado, como se ve a continuación:
    
    def set_edad(self,new_age):
        self.__edad =  new_age

#Luego de modificar el atributo privado es necesario utilizar una función getter para mostrarlo

    def get_edad(self):
        return self.__edad
    
#Accediendo de manera convencional al atributo
persona1=Persona("Daniel",17)

#print(persona1.__nombre)

#Accediendo mediante el uso de getters

nombre=persona1.get_nombre()

print(nombre)

#Modificando el valor del atributo super privado con el uso de Setters

edad_nueva=persona1.set_edad(24)

#Mostrando el nuevo valor de atributo mediante getters:

edad=persona1.get_edad()

print(edad)




        
