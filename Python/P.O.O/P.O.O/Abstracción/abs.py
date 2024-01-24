#La abtracción hace referencia a darle al ususario acceso a las funcionalidades sin que tenga que comprender la complejidad
# detrás de cada uno de los procesos


class Auto():
    def __init__(self):
     self._estado ="apagado"
    
    def encender(self):
        self._estado = "encendido"
        print("El auto está encendido")
    
    def conducir(self):
        if self._estado =="apagado":
            self.encender()
        print("conducioendo el auto")
        
miauto=Auto()
miauto.conducir()