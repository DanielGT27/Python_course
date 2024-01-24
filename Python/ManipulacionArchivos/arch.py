# Para mandar a llamar a un archivo es necesario teneer en cuenta la carpeta en la que se encuentra
# y el nombre del archivo junto a su formato.abs
# Todo esto dentro de la función open()

archivo_sin_leer = open("Python\\ManipulacionArchivos\\texto_delgt.txt", encoding="UTF-8")


# Con el método read se lee el contenido del archivo
# ! Importante tener en cuenta que ele archivo se puede leer una unica vez ¡

#archivo= archivo_sin_leer.read()

# Acceder a lineas individuales del archivo
# El método de la función open ; readlines() . Deevuelve un arreglo con todas las lineas que posee el archivo
#linea_1 = archivo_sin_leer.readlines()

# El método readline(), permite acceder a la primera linea
# El parametro de esté método es un número el cual simboliza la cantidad de caracteres que se quieren leer 


linea_1 = archivo_sin_leer.readline(3)


#Cerrar el archivo 

archivo_sin_leer.close()

print(linea_1)
