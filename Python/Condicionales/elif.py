# ELIF  If anidados 

ingreso_mensual = int(input())
gasto_mensual = 70000

if ingreso_mensual > 10000 :
   if ingreso_mensual - gasto_mensual <0:
       print("Estas en deficit")
   elif ingreso_mensual - gasto_mensual > 30000 :
       print("Tus gastos estás acordes a lo que ganas")
   else :
       print("Ten cuidado con lo que gastas pa")
       
elif ingreso_mensual > 1000 : # else if se declara elif
    print("Estás bien en latinoamerica")
else :
    print("Sos pobre")