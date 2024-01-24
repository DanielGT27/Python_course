#Funciones que tienen un nombre especial reservado

class Persona():
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
#Esta función nos permite mediante el metodo dunden __str__ es que al momento de imprimir la clase se ejecute lo de la función
    def __str__(self):
        return f'Persona(nombre={self.nombre},edad={self.edad})'

# Forma de sumar clases: (sobrecarga de operadores)
    
    def __add__(self,otro):
     nuevo_valor= self.edad + otro.edad
     return Persona(self.nombre+otro.nombre,nuevo_valor)
    

daniel=Persona("Daniel",17)
pedro=Persona("Pedro",35)


nueva_persona= daniel+pedro

print(nueva_persona)