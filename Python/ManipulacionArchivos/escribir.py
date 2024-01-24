# Utilizadno el with Open para acceder al archivo txt 
# luego 'w' define que se va a hacer con el archivo , por ejemplo en este caso es escritura (sobreescribir)
# Luego la palabra reservada as permite llamar al archivo de cierta manera 

with open('Python\\ManipulacionArchivos\\texto_2.txt','w',encoding='UTF-8') as archivo :
    #Sobreescribiedo el archivo mediante una lista 
      lista = ["Hola", "Buenas\n"]
      archivo.writelines(lista)
    # Al volver a declarar el metodo write , el contenido que se escriba se agregará al contenico anterior
      archivo.write('BRUUH')
      
    
      
      