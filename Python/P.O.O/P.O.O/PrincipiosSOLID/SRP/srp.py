class Auto():
    def __init__(self,tanque):
        self.posicion = 0
        self.tanque=tanque
    
    def mover(self,distancia):
        if self.tanque.obetener_combustible()>=distancia/2:
            self.posicion+=distancia
            self.tanque.usar_combustible(distancia/2)
        else:
            print("No hay suficiente combustible")
   
   

class TanqueCombustible:
    def __init__(self,combustible):
        self.combustible = 100
        
    def obetener_combustible(self):
        return self.combustible
    
    def agregar_combustible(self,cantidad):
        self.combustible += cantidad
    
    def usar_combustible(self,cantidad):
        self.combustible -=cantidad
        
        
        
tanque=TanqueCombustible()
autito=Auto(tanque)

print(autito.mover(100))