
#Clase padre:

class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre =nombre
        self.edad =edad
        self.nacionalidad=nacionalidad
        
# Como hacer que un objeto herede los atributos de una clase padre
#Ingresamos como atributo el nombre de la clase padre

class Empleado(Persona):
#incluimos dentro del metodo contructor los atributos que queremos que herede de la clase padre
    def __init__(self,nombre,edad,nacionalidad,trabajo,salario,carrera):
#utilizamos super para declarar y nombrar las propiedades heredadas
     super().__init__(nombre,edad,nacionalidad)
     self.trabajo =trabajo
     self.salario =salario
     self.carrera =carrera


roberto = Empleado("Roberto","16","Frances","Tenis","2","IngIndustrial")

print(roberto.carrera)