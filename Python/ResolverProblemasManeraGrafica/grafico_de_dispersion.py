import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr 


# Se lee el DataFrame mediante pandas

df = pd.read_csv('Python\\ResolverProblemasManeraGrafica\\TiempoDinero.csv')

# Se hace un grafic de dispersión para analizar la correlación entre las variables con el método de sns , scatterplot


sns.scatterplot(x='Tiempo',y='Dinero', data=df)

# Se calcula el coeficiente de determinacion mediante la función importanda pearsonr de la libreria scipy.stats 

pearson = pearsonr(df['Tiempo'],df['Dinero'])

# Se imprime el coeficinte de correlación

print(pearson)

# Se imprimen otros datos estadisticos acerca del csv

print(df.describe())

#Se muestra la grafica de dsipersion

plt.show()