import random

tontos = ["Miki", "Franca", "Pablito", "Germy"]

while True:
    print("Opcion 1 - Añadir nombres")
    print("Opcion 2 - Quitar nombres")
    print("Opcion 3 - Saber quien es elmas")
    print("Opcion 4 - Salir del programa")
    print("Elija su optionen")

    opcion = input() #stdin

    opcion = int(opcion) #convertir resultado a numero entero (integer)

    if opcion == 1:
        nombre = input("Añadi el nombre: ") #hace print y despues el stdin
        nombre = nombre.capitalize() #poner la primer letra en mayuscula
        tontos.append(nombre) #agrega un object al final de la lista
        print(tontos)

    elif opcion == 2:
        nombre = input("Quita a un nombre: ")
        nombre = nombre.capitalize()
        tontos.remove(nombre) #elimina un object de la lista 
        print(tontos) 

    elif opcion == 3 :
        elmas = random.choice(tontos) #usamos el metodo choice() del modulo random, para que devuelva un resultado al azar dentro de la lista
        print(f"{elmas} es el mas tonto") #la "f" da formato y permite poner variables como parte de un texto
        break


    

        

    

