"""Librerias o modulos de Pyton."""
#son llamadas con la palabra import 
import pandas   
#se les puede asignar un alias o apodo 
import math as m
#Se puede importar atributos o funciones sin impotar toda la libreria con la from  .... import....
from openpyxl import Workbook
#definimos dos funciones para calcular la media y la desviacion 
def media( X):
  media=sum(X)/len(X)
  return media

def desviacion(X):
  D=(X-media(X))**2
  v=sum(D)/(len(D)-1)
  S=m.sqrt(v)
  return S
#despues de llamada la libreria se llama la funcion libreria/alias.funcion()
df = pandas.read_csv('2019.csv',';')#Cargamos los datos del P10 en un dataframe   
encabezados= list(df.keys()) #obtenemos los encabezados de la tabla en una lista
print(encabezados)
Medias=[]
D=[]
# con el ciclo for se calcula la media y la deviacion de cada columna asociada al encabezado
for i in range(1,13):
  p=media(df[encabezados[i]])
  s=desviacion(df[encabezados[i]])
  Medias.append(format(p,".2f"))
  D.append(format(s,".2f"))

print(Medias)
print(D)
#Abrimos un libro de trabajo
wb = Workbook()
ws = wb.active
ws.title='Media y Desviacion'
#Añadimos por filas
H=encabezados[1:13]
ws.append(H)
ws.append(Medias)
ws.append(D)
#Guardamos en un excel
wb.save("estadisticos8.xlsx")