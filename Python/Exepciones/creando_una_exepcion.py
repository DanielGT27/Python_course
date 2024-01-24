
class MiExepcion (Exception): 
    def __init__ (self,err):
        print(f'Impresionaste cometiste el siguiente error {err}')
        
        
# Lanzando una exepción 
#raise MiExepcion('Jjajaj sos re gey ')

#Manejando la exepción :

try :
    raise MiExepcion('Jjajajaja sos re gey')

except:
    print('Bueno cometiste el error nada que hacer')