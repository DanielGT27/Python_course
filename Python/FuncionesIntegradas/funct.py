# Función es un fragmento de codigo que puede ser reutilizado en cualquier momento
# Las funciones build-in , son las que python tiene integradas


numeros = [12,34,56,78,109]

# encontrando el mayor número de una lista con la función max()
# Aplica en todods los iterables

numero_mas_alto = max(numeros)

print(numero_mas_alto)

# Encontrando el menor numero de una lista 

numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

# Redondeando a 6 decimales
# Con la función integrada round , es posible escoger la cantidad de decimales a las que queremso redondear.
# La  función round recibe dos parametros el numero y la cantidad de cigfras decimales

numero_redondeado  = round(12.345, 2)

print(numero_redondeado)

# Funcion bool ()
# Retorna falso => si está vacio, 0 , False , None \ True => True , cadena , datos no vacios


resultado_bool = bool([])

print(resultado_bool     )

resultado_bool = bool(["Holaa", 12]) 

print(resultado_bool)

# Reorna true si todods los valores son verdaderos con la función all
# recibe un iterable

resultado_all = all(["Holaa",23])

print(resultado_all)

# Suma todods los valores de un iterable

suma_total = [1,2,3,4,5,6]

print(sum(suma_total))