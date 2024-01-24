# Atributos de instacia se crean a la par del objeto 

class Celular:
 #Metodo contructor: Apenas instanciamos una clase se ejecuta este metodo
 #self: palabra resercada para hacer referencia a si mismo en este caso al objeto
 #Definimos los atributos que queremos para el objeto, para luego darle los valores especificos
    def __init__(self,marca,modelo,camara):
        self.marca=marca
        self.modelo=modelo
        self.camara=camara 
        

# Definimos los valores de los atributos del celular1
celular1=Celular("Apple","iPhon 15","48MP")
celular2=Celular("Samsung","S22","24MP")

print(celular1.marca)
print(celular2.marca)
        