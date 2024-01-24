import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

#  Leyendo el dataframe con pandas

df = pd.read_csv('Python\\ResolverProblemasManeraGrafica\\Ingresos.csv')

# Realizando la grafica de barras


#Mostrar la totalidad de los ingresos

totalidad_ingresos = ['Total de ingresos',df['Ingresos'].sum()]

nuevo_dataframe = pd.DataFrame([totalidad_ingresos], columns=df.columns)

print(nuevo_dataframe)

df_actualizado=pd.concat([df,nuevo_dataframe],ignore_index=True)

sns.barplot(x='Fuentes',y='Ingresos', data=df_actualizado)

print(totalidad_ingresos)
#Mostrando la grafica de barras 

plt.show()
