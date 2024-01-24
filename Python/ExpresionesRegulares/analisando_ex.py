import re

text = 'TheTheThe quick brown fox jumps over the lazy dog'

# * encuentra Todos los patrones con esa coincidencia

x = re.findall(r'^The.*dog$', text)

print(x)


#2------------


text_ = 'La fecha es 23/06/2021 y el telefono es +1-555-555-5555'


# Patron a encontrar

pattern = r'\d{2}/\d{2}/\d{2,4}'

# TRexto con el cual se va a remplazar el patron

remplazo = 'Fecha oculta'

#Remplazar todas las apariciones del patron en la cadena de texto

new_text = re.sub(pattern,remplazo,text_)

#Imprimir el resultado 

print(new_text)



#3-----------------


text__ ='Remplazando todas las vocales por asterisco'

pattern_ = r'[aeiou]'

remplazo= '#'

nuevo = re.sub(pattern_,remplazo,text__)

print(nuevo)



#4-----------

email = 'xdaniel032@gmail.com2'

patron = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.[a-z]{2,}\w'

ver = re.findall(patron,email)

print(ver)

if re.findall(patron,email):
   print("Si funciona el email")
else:
     print('No es un correo válido')



#5------------


form = 'Hola Master mji numero es : +54 11 3456-2345'

pattern__ = r'\+\d{2}\s\d{2}\s\d{4}-\d{4}'


nuevo_form = re.sub(pattern__,'(Numero desconocido)',form)

print(nuevo_form)