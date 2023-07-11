import os
os.system("cls")

#precios  
#platinium $120.000 (del 1 al 20)
#gold $80.000 (del 21 al 50)
#silver $50.000 (del 51 al 100)

#esta lista almacena todas las ubicaciones disponible y ocupadas
ubicaciones = [
                [1,2,3,4,5,6,7,8,9,10],
                [11,12,13,"x","x","x",17,18,19,20],
                [21,22,23,24,25,26,27,28,29,30],
                [31,32,"x",34,35,36,37,38,39,40],
                [41,42,43,44,"x",46,47,48,49,50],
                [51,52,53,54,55,56,57,58,59,60],
                [61,62,63,64,65,66,67,68,69,70],
                [71,72,73,74,75,76,77,78,79,80],
                [81,82,83,84,85,86,87,88,89,90],
                [91,92,93,94,95,96,97,98,99,100],
            ]
#SE GUARDARA rut- nombre(opcional) - numero de asiento
asistentes = []

while True:
    print("\n")
    print("Compra De Entradas Para El Conciento VIP De Michael Jam")
    print("1.-Compra De Entradas")
    print("2.-Ver Ubicaciones Disponibles")
    print("3.-Ver Listado De Asistentes")
    print("4.-Ganancias Totales De La Venta De Entradas")
    print("5.-Salir")

    try:
        op=int(input("Ingrese un opcion entre 1 y 5: "))
    except:
        print("\n")
        print("Error, Ingrese Solo Numeros entre 1 y 5...")
        op = 0

    if op == 1:
        print("Selecciono La Compra De Entradas")
        #La cantidad a comprar debe ser entre 1 y 3 - 
        cant_ubi = int(input("Ingrese La Cantidad De Entradas A Comprar[Solo permitido entre 1 y 3]: "))
        if cant_ubi == 0 or cant_ubi >= 4:
            print("Error, Debe Ser Un Valor Entre 1 y 3")
        else: 
            print(ubicaciones)
            print("""
                   Precios De Las Entradas  
                   Platinium  $120.000 (Del Asiento 1 al 20)
                   Gold       $80.000  (Del Asiento 21 al 50)
                   Silver     $50.000  (Del Asiento 51 al 100)
                  """)    
        asientos = int(input("Ingrese Los Asientos Que Desea Comprar[Aquellos con una X NO Estan Disponibles]: "))
        
    if op == 2:
        print("Selecciono Ver Ubicaciones Disponibles")
    if op == 3:
        print("Selecciono Ver Listado De Asistentes")
    if op == 4:
        print("Selecciono Ganancias Totales De La Venta De entradas")
    if op == 5:
        print("Salir Del Menu")
        print("Gracias Por Preferirnos, Hasta Pronto...")
        break
input("Presione Cualquier Boton Para Continuar")