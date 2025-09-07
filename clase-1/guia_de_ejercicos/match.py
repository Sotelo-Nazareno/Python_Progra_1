#           Match           

"""
Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
    Si es invierno: solo se viaja a Bariloche.
    Si es verano: se viaja a Mar del plata y Cataratas.
    Si es otoño: se viaja a todos los lugares.
    Si es primavera: se viaja a todos los lugares menos Bariloche.
"""

estacion = input("Ingrese la estacion del anio: ")
lugar = input("Ingrese el destino: ")

viaja = "Se viaja"
no_viaja = "No se viaja"

match estacion:
    case "invierno":
        if lugar == "Bariloche":
            mensaje = viaja
        else:
            mensaje = no_viaja
    case "verano":
        if lugar == "Mar del Plata" or lugar == "Cataratas":
            mensaje = viaja
        else:
            mensaje = no_viaja
    case "primavera":
        if lugar == "Bariloche":
            mensaje = no_viaja
        else:
            mensaje = viaja
    case _:
        mensaje = viaja

print(mensaje)