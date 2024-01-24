

 # Creando una función simple:
 # Esta se declara usando def , el nombre de la función dos puntos y el código que va a ejecutar
 
def saludar () :
    print("Hola Lucas mi dios como estás")


# Esta es la manera de ejecuar una función

saludar()

# Creando una función con un parametro
# Un parametro es una variable que existe dentro d euna función
# Esta función crea un saludo , teniendo en cuenta el nombr ey el sexo de la persona

def saludo (nombre,sexo) :
    sexo = sexo.lower()
    
    if(sexo =='mujer') :
       adjetivo = "Diosa"
    elif (sexo =='hombre'):
       adjetivo = "Maestro"
    else :
        adjetivo = "A bueno"

    print(f'Hola {nombre} mi {adjetivo} eres increible')
    
    
saludo('DanielGt27','hombre')


# Creando una función que nos retorne valores

def calculo(num) :
    
    chars = list("Hoalhdihdiwdi")
    numero_entero = str(num)
    num = int(numero_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f'{chars[c1]}{chars[c2]}{chars[c3]}{num}'
    # return se utilza para que el valor que le pasemos se almacene como un valor que le podemos dar a una variable
    # return nos puede retornar multiples valores 
    return contraseña, num
    
    
pasword, indice = calculo(345) 

print(f'Tu nueva contraseña es : {pasword}')
print(f'El npumero utilizado para crear tu contraseña fue : {indice}')


# Función args

# Forma no optima de recorrer valores mediante un bucle 

def suma(lista):
    numeros_sumados = 0
    for i in lista :
        numeros_sumados = numeros_sumados + i
    
    return numeros_sumados

resultado = suma([2,3,4,5])
print(resultado)

# Manera optima de  utilizando el parametro args
# El parametro args se escribe con *
# Y su funcionalidad es que convierte todos los parametros que le demos en una unica lista iterable

# El parametro se tiene que utilizar al final 


def suma_(nombre,*numeros) :
     suma_numeros = f' {nombre} , la suma de tus números es : {sum(numeros)}'
     return suma_numeros

resultado1 = suma_(1,2,3,4,5,5)
print(resultado1)

# Keyword arguments : 

def frase(nombre, apellido , adjetivo ) :
    
        return f'Hola {nombre} {apellido} , tu eres muy {adjetivo}'
    

# Una forma de cambiar el orden el el cual ingresamos los parametros es declarandolas como si fueran una variable

print(frase(apellido='Galindo ', adjetivo='Increible', nombre='Daniel'))

# de igaul forma se pueden declarar los parametros de manera forzada desde el inicio 
# De todas formas posteriormente pueden ser cambiados al redefinir dicho parametro