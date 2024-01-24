# Modulos 
# Cualquier archivo .py 

# Se puede llamar un modulo desde otro módulo con el fin de utilizar las funciones 
# , Las variables y demás apartados del modulo llamado


# Tipos de modulo:

#Python module , modulos incorporados por python

# Third-part module , modulos hechos por terceros

# Own module , modulo creado por nosostros 

 
#import modulo_saludar as m_saludar
# Manera de importar unicamente una función del modulo

# Se importo las funciones de un modulo y se les cambió el nombre
# De la misma manera utilizado el simbolo * ,es posible importar todas las funciones

from modulo_saludar import saludar as saludaso, shino as chino

# Importar desde otra carpeta 

import EnrutamientoModulos.enmod

# La funciones dentro del modulo que se importó se convierten en un método
# saludo = modulo_saludar("Daniel")

saludo= saludaso("DanielGT27")

conversacion = chino()

print(saludo)
print(conversacion)

# Operador as
# Asigna primero el valor y luego la variable en la que se va a almacenar 



