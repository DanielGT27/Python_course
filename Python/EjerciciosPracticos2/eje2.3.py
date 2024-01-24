# Una funcion que meustre una serie fobonaci


def Fibonacci (num) :
    a,b = 0,1 
    fibonacci_lista = [0]
    
    for i in range(num):
        if a+b > num : return fibonacci_lista
        else :
            a,b = b,a+b
            fibonacci_lista.append(b)
        
    return fibonacci_lista



print(Fibonacci(20))



# Evalucación de varias funciones 

# Funcion integrada any()

condiciones = [1,2,2,3,4,3,4,3,5]

condicional = [i > 4 for i in condiciones]

if any(condicional) :
    
 while 2 in condiciones:
     condiciones.remove(2)
     
 print(condiciones)
else :
    print("A dormir GT27")
    
# Evaluar si existen numeros en un grupo de caracteres 


mi_lista = "HOLAAAAA****222234432"

buscar_numerso = [i.isdigit() for i in mi_lista]



if any(buscar_numerso) :
   print("Que bueno")
else:
   print( "Que malo")
   
   
#Funcion integrada all()

usuario ="ElShino"

if all(i.isalpha() for i in usuario):
    
    print(f'{usuario} , es un nombre válido')

else :
    print(f'Los sentimos "{usuario}" no es un nombre válido')
    


# Ejercicios :

primos_hasta = lambda num :list(filter(lambda x:all(x % i !=0 for i in range(2,int(x**0.5)+ 1) ) , range(2,num)))

print(primos_hasta(12))


