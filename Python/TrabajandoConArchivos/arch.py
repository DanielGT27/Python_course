#2 listas , unas con nombres y otras con apellidos


nombres = ['Daniel','Jose','Ricardo','Chimbo','Siu']

apellidos = ['Torres','Negro','Perex','Molinos','Venezuela']

# Registrar la informacion de ambas listas en un txt de manera optima 

with open('Python\\TrabajandoConArchivos\\nombre_y_apellidos.txt','w') as archivo:
    archivo.writelines('Los datos son :\n')
    [archivo.writelines(f'nombre: {n}\n Apellido :{a}\n------------') for n,a in zip(nombres,apellidos)]