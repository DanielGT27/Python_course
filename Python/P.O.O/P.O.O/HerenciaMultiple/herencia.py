class Persona:
    def __init__(self,nombre,edad):
        self.nombre =nombre
        self.edad =edad
        
        
class Artista:
    def __init__(self,habilidad):
     self.habilidad = habilidad
     
    def mostrar_habilidad(self):
        print(f'Mi habilidad es {self.habilidad}')
     

class Estudiante(Persona):
    def __init__(self,nombre,edad,notas,universidad):
        super().__init__(nombre,edad)
        self.notas=notas
        self.universidad =universidad
        
# Herencia multiple:
# La manera de utilizar herencia multiple es primero incluir las clases padre como parametros de la nueva clase
#Luego menidante el metodo contrutor __init__ se ingresan todos los atributos incluyendo los que se quieran agregar de los padres
# Luego se utiliza el metodo contructor super() o el nombre de la clase padre en conjunto con el metodo __init__ y se incluye los atributos correspodientes

class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,edad,habilidad,salario,empresa):
        Persona.__init__(self,nombre,edad)
        Artista.__init__(self,habilidad)
        self.salario =salario
        self.empresa =empresa
        
    def mostrar_habilidad(self):
        print("no tengo jaja")
    
    def presentarse(self):
        return f'{super().mostrar_habilidad()}'
        



empleado1=EmpleadoArtista("SI","si","si","si","si")

print(empleado1.presentarse())

#Manaera de saber si una clase es una subclase de otra o de otras, mediante la función issubclass()
#Como primer parametro de la función se establece el nombre de la clase a evaluar, mientras que el segundo parametro es la clase
# de la que se cree que hereda sus atributos


herencia = issubclass(EmpleadoArtista,Artista)

print(herencia)


#Manera de saber si un objeto es una instancia de una clase,mediante la función isinstance()
#Como primer parametro de la función se establece el nombre del objeto a evaluar, mientras que el segundo parametro es la clase
# de la que se cree que proviene


instancia =isinstance(empleado1,EmpleadoArtista)
print(instancia)