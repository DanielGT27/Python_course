# Un metodo es una función 

class Celular:
    def __init__(self,marca,modelo,camara):
        self.marca  =marca
        self.modelo =modelo
        self.camara =camara
    
# Se define un metodo por medio de una función , en una función se tiene que poner la palabra self como parametro de la fuinció 
    def llamada(self):
#Para referenciar alguno de los atributos del objeto tenemos que hacer referencia con la palabra self
        print(f'Estas haciendo una llamada desde un {self.modelo}')
        
        
celular1=Celular("Samsung","S22","48MP")


print(celular1.llamada())