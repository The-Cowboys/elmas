import csv

def leer_archivo(nombre):
    archivo = open(nombre,"r")
    contenido = csv.reader(archivo)
    valor = list(contenido)
    return valor
