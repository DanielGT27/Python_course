# Ejercicio herencia multiple y MRO

class Animal:
    def comer(self):
        print("Soy un animal que come")

class Mamifero(Animal):
    def amamantar(self):
        print("Soy un animal que amamanta")

class Ave(Animal):
    def volar(self):
        print("Soy un animal qeu vuela")
        

class Muricelago(Mamifero,Ave):
     def animal(self):
         print(f'{super().comer()},{super().amamantar()},{super().volar()}')


murcielago=Muricelago()

murcielago.animal()