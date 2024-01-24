#Polimorfismo ,es escencia es el mismo mesnsaje pero cambia dependiendo del objeto con el que estemos tratando 

#Ambas clases  tienen el metodo sonido, no obstante este cambia dependiedo si es un gato o un perro
class Gato:
    def sonido(self):
        print("miau")


class Perro:
    def sonido(self):
        print("guau")
        
def haciendo_sonido(animal):
   print(animal.sonido())
    

perro =Perro()

haciendo_sonido(perro)