# El encapsulamiento se trata en definir atributos privados y atributos super privados
#Para definir un atributo privado se utiliza el guion bajo _
# Para definit un atributo super privado se utiliza un doble guon bajo __


class Miclass:
    def __init__(self):
        self.__atributo_privado = "Valor"
        
    def __hablar(self):
        print("Hola")
 

objeto =Miclass()

print(objeto.__atributo_privado)