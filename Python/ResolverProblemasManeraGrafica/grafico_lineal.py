import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 


nuevo_registro = ['08-30',13]


    
df = pd.read_csv('Python\\ResolverProblemasManeraGrafica\\Registro.csv')
    
    

# Se realiza un nuevo datframe utilizando el método de la libreria pandas DataFrame , esdte tiene dos parametros:
# El primero se trata de una lista que contiene el contenido de las filas , mientras que el segundo contiene el nombre y la cantidad de columnas

nuevo_dataframe = pd.DataFrame([nuevo_registro],columns=df.columns) 

print(nuevo_dataframe)

# Se concatena el dataframe nuevo con el anterior , mediante el metodo concat de la libreria , este tiene dos parametros
# El primero tiene uns lista con los datframes que se va a concatenar , el segundo especifica si se quieren ignorar los inidices.abs

df_actualizado =pd.concat([df, nuevo_dataframe],ignore_index=True)

print(df_actualizado)

punto_maximo_asesinatos = df_actualizado['Asesinatos'].idxmax()

print(punto_maximo_asesinatos)

punto_max_x,punto_max_y = df_actualizado.iloc[punto_maximo_asesinatos,0],df_actualizado['Asesinatos'].max()

print([punto_max_x,punto_max_y])


sns.lineplot(x='Fecha',y='Asesinatos',data=df_actualizado)

plt.plot(punto_max_x,punto_max_y,'o')

plt.show()
