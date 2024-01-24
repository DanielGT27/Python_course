import pandas as pd


df = pd.read_csv('Python\\TrabajandoConArchivos\\tabla.csv')

#Cambiar el tipo de dato de la columna a una cadena de texto

df['Edad']= df['Edad'].astype(str)

#mostrar el tipo de dato de la columna edad

print(type(df['Edad'][0]))


#Remplazando los datos de la columna nombre

df['Nombre'].replace("Juan","Shinooo", inplace=True)

#Mostrando los cambios

print(df['Nombre'])

#Eliminar filas con datos faltantes con el método dropna , en el caso en el que se quieran eliminar columnas con datos faltastes 
# Se hace con el parametro axis=1


print(df)

df=df.dropna()

print(df)

#Eliminar filas repetidas , con el método drop_duplicates

df= df.drop_duplicates()

print(df)

#Creae un nuevo dataframe con las modificaciones

df.to_csv('Python\\TrabajandoConArchivos\\tabla_limpia.csv')