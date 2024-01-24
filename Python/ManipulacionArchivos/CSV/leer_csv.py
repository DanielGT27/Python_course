# La maner ade leer archivos csv mediante python es con la libreria Csv
# No obtsnte se puede de una manera más eficiente con la libreria pandas
import csv

with open('Python\\ManipulacionArchivos\\CSV\\tabla.csv','r') as archivo:
   lector = csv.reader(archivo)
   for row in lector:
       print(row)