# a ) Pedirle al usuario que diga cualquier texto real y 

# - Calcular cuanto tardaría en decir esa frase
# - Cuantas palabras dijo

#------ Variables-------
texto_ususario = input("Dime cualquier cosa , maestro : ")
lista_texto_ususario = texto_ususario.split(" ")
cantidad_de_palabras = len(lista_texto_ususario)

# ------- Cuanto tardaria en decir una frase -------

tiempo_habla =  cantidad_de_palabras / 2

if tiempo_habla > 60 :
    print("Che amigo tampoco te pedi la biblia")
else :
    print(f' El tiempo que tardarias en decir lo que escribiste sería de : {tiempo_habla} segundos')

#------- Cantidad de palabras ----------

print(f'El número de palabras que dijiste fueron : {cantidad_de_palabras}')


# ------ HABLA DEL DALTO -----


tiempo_habla_dalto =  tiempo_habla - ((tiempo_habla * 30) / 100 ) 

print(f'El tiempo que tardaría dalto en decir lo que tu escribiste sería de : {tiempo_habla_dalto} segundos')



