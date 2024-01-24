# Crear una función que nos permita obtener todos los numeros primos anteriores al numero que le ingresemos



# Funcion que nos permite determinar si jun numero es primo o no 


def numeros_primos (num) :
  
   for i in range(2,num-1):
     if num%i == 0 : return False
     return True
   
def primos_hasta (num) :
  primos = []
  for i in range(2,num+1) :
   resultado = numeros_primos(i)
   if resultado == True : 
     primos.append(i)
     
  return primos   


resultado = primos_hasta(17)

print(resultado)