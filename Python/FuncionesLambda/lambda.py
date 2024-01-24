# Lambda es una manera de crear una función anonima
# es decir no tiene nombre

#Creando una función lambda para multiplicar por 2
# Son utiles cuando se quiere hacer algo sencillo
# Se retornan automaticamente

operacion = lambda x : x*2

# Usando filter como una función común


operacion_=operacion(2)

print(operacion_)


lista = [1,2,3,4,5,6,77,8,8]

# creando una función que diga si es par o no

def numeros_pares(numeros) :
    if (numeros%2 ==0) :
     return True 
 

numeros_= filter(numeros_pares, lista)

print(list(numeros_))

# Ahora utilizandpo lambda

numeros_p = filter(lambda numero : numero%2 == 0 , numero)

print(numeros_p([3,45,6,7,8,9]))