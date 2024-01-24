
#Se va a imprimir el "Hola" , unicamente cuando el archivo logró ser abierto correctamente

#Abriendo el archvo con width open
with open("Python\\ManipulacionArchivos\\texto_delgt.txt") as archivos:
    #Leyendo el  contendio del archivo 
    contenido = archivos.read()
    # Imprimiendo el archivo
    print(contenido)

# No es necesario cerrarlo al utilizar with open