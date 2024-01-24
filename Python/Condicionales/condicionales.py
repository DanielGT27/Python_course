
if 5 < 4 :
    print("El número es válido")
else :
    print("El número no es válido ")
    

edad = int(input())

if edad >= 18 :
    print("Puedes pasar")
else : 
    print("raja de aca")


# Verificando contraseña 

contraseña_almacenada = "ItanElDelBarrio"

contraseña_ingresada = input()

if contraseña_ingresada == contraseña_almacenada :
    print("INICIANDO SESIÓN...")
else :
    print("CONTRASEÑA INCORRECTA")
    

# Else if

ingreso_mensual = int(input())
gasto_mensual = 70000

if ingreso_mensual > 10000 :
   if ingreso_mensual - gasto_mensual <0:
       print("Estas en deficit")
   elif ingreso_mensual - gasto_mensual > 3000 :
       print("Tus gastos estás acordes a lo que ganas")
   else :
       print("Ten cuidado con lo que gastas pa")
       
elif ingreso_mensual > 1000 : # else if se declara elif
    print("Estás bien en latinoamerica")
else :
    print("Sos pobre")