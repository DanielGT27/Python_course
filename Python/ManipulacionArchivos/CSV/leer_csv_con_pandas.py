import pandas as pd 

# Leer archivo con pandas
# Cabe aclarar que un archivo csv , se trata de un dataframe ya que se trata de una estructura de datos bidimensional en forma de tablas
# Un data frame consta de dos valores ; filas y columnas 


df= pd.read_csv('Python\\ManipulacionArchivos\\CSV\\tabla.csv', names=['name','age','Studies','DI'])
df2= pd.read_csv('Python\\ManipulacionArchivos\\CSV\\tabla.csv', names=['name','age','Studies','DI'])

print(df)

# Acceder a una columna especifica 

nombres =df['name']

print(df)

print(nombres)

# Slicing : Tecnica de python que permite realizar ciertas operciones cuendo se trabaja con ciertos elementos 


cadena = '0123456789'

print(cadena[2:6])


# Ordenando DataFrame por la edad 

df_ordenado_edad =df.sort_values("age")

print(df_ordenado_edad)


#Ordenando de manera descendente 

df_ordenado_edad_des = df.sort_values('age', ascending=False)

print(df_ordenado_edad_des)


# Concatenando 2 DataFrames 

df_concatenado = pd.concat([df,df2])


print(df_concatenado)


#accediendo a las primeras filas con head(), el parametro de este método es la fila que queremos que muestre de manera ascendente 

primer_fila = df.head(3)

print(primer_fila)


# accediendo a las últimas filas con tails() , se muestran las filas de abajo hacia arriba

ultima_fila = df.tail(1)

print(ultima_fila)


#Accediendo a la cantidad de filas y columnas con shape, devuelve primeroi la cantidad de filas y luego la cantidad de columnas

filas_totales,columnas_totales= df.shape

#Accediendo a la cantidad de filas



print(filas_totales, columnas_totales)

#Describe nos permite obtener datos estadisticos del dataFrame

df_info=df.describe()

print(df_info)


# Accediendo a un elemento especifico del df con loc

elemento_especifico = df.loc[2,'age']


print(elemento_especifico)

#Accediendo a un elemnto especifico del df con iloc

elemento_especifico_iloc = df.iloc[1,2]


print(elemento_especifico_iloc)


#Accediendo a todas las filas de una columna  

edad = df.iloc[:,1]

# Accediendo a todas las columnas de una fila

columna = df.iloc[2,:]

print(edad)
print(columna)

#Accediendo a las edades mayores a 13

edad_mayor = df.loc[df['age']>13, :]

print(edad_mayor)