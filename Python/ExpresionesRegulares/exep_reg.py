import re

texto = '''Hola maestro, esta es la cadena 1. 22 como estamos
Esta es la segunda fila de texto 234
y esta es la final 234 en definitiva mi capitan'''


# Con la funcion search del modulo re , es posible encontrar una conicidencia 
# en el texto qeu estamos evaluando 

resultado = re.search('Hola',texto)

print(resultado)

#Con la función findall , es posible encontrar todas las coincidencias del texto ques
#estamos evaluiando 
todos_resultados = re.findall('esta',texto,flags=re.IGNORECASE)

print(todos_resultados)

#Expresiones regulares 

#\d -->Busca digitos numericos del 0-9

numeros = re.findall(r'\d',texto)

print(numeros)

#\D --> Busca TODO menos digitos numericos 


todo_menos_numeros = re.findall(r'\D',texto)

print(todo_menos_numeros)


#\w --> Busca caracteres alfanumericos [0,9  a-z  A-Z   __]

alfanumerico = re.findall(r'\w',texto)

print(alfanumerico)

#\W --> Busca TODO menos los caracteres alfanumerico 

todo_menos_alfanumerico = re.findall(r'\W',texto)

#\s --> Busca todos los espacion es blanco --> espacios,tabs,saltos de linea 

espacios = re.findall(r'\s',texto)

print(espacios)

# . --> Busca todo exepcto saltos en linea

todo_menos_saltos_linea = re.findall(r'\.',texto)

#\n --> Busca saltos en linea 

saltos_linea = re.findall(r'\n', texto)

print(saltos_linea)

# \ -->cancela caracteres especiales, cancelar la funcion del punto y buscar puntos 


puntos = re.findall('\.',texto)

print(puntos)

#Armandi una cadena que busque un número,seguido un puntoy un espacio


cadena =re.findall(r'\d\.\s', texto)

print(cadena)

#^ -> Busca el comienzo de una linea
# Con el parametro flags se ingresan otras formas en las que se interpreta 

comienzo_linea = re.findall(r'^Esta',texto,flags=re.M)


print(comienzo_linea)

# $ --> Busca el final de una milea

final_linea = re.findall(r'capitan$',texto, )

print(final_linea)

#Grupos ,
# {n}--> Busca n cantidad de veces el patron de la izquierda


secuencia_numeros = re.findall(r'\d{3}',texto)

print(secuencia_numeros)

#Rangos -->
# {n,m} --> Buscar el dato minimo ncantidad de veces y máximo m cantidad de veces 

rango_numeros = re.findall(r'\d{2,3}',texto)

print(rango_numeros)

# | --> Busca una cosa o la otra