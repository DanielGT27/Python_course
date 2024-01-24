# Si el modulo a importar se encuentra en una carpoeta dentro de la misma ruta
# import funciones.modulo_saludar as m_saludar

import sys

print(sys.builtin_module_names)
print(sys.path)

# Agregar un modulo que se encuentre en una carpeta que pertenezca a otra ruta 

sys.path.append("c:\\Users\\trans\\OneDrive\\Escritorio\\MamadasParaLaMontanaDeAzucar\\Python\\Modulos(Funciones_buenas)")


import modulo_saludar  

print(modulo_saludar.saludar("Daniel"))

print(__name__)