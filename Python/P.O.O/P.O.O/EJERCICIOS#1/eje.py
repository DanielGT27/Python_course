# Crear una clase estudiante , que tenga los atributos nombre, edad y grado , además
# de un métopdo llamada estudiar 


class estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre =nombre
        self.edad =edad
        self.grado=grado
        
    def estudiar(self):
        print(f'El estudiante {self.nombre} está estudiando')
        

nombre= input("Dame el nombre del estudiante: ")
edad = int(input("Dame la edad del estudiante: "))
grado = input("Dame el grado del estudiante: ")


estudiante1=estudiante(nombre,edad,grado)



print(f"""
      DATOS DEL ESTUDIANTE:\n\n 
      Nombre:{estudiante1.nombre}\n
      edad:{estudiante1.edad}\n
      grado:{estudiante1.grado}\n
      
      """)


while True:
 estudiar = input()
 if(estudiar.lower() == "estudiar"):
    estudiante1.estudiar()