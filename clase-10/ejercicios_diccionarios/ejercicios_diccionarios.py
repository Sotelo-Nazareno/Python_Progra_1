# Ejercicios diccionarios
# 1. Creación y Acceso Básico
# Ejercicio: Crea un diccionario llamado informacion_personal con las claves: 
# "nombre", "edad", "ciudad", y "ocupación". Asigna valores apropiados. Luego, imprime el valor de la clave "edad".


informacion_personal = dict ([
    ('nombre', 'Lebron'),
    ('edad', 40),
    ('ciudad', 'Los Angeles'),
    ('ocupacion', 'Basketbolista')
])

#print(informacion_personal['edad'])
print(informacion_personal.get('edad'))


# 2. Agregar y Modificar Elementos
# Ejercicio: Usando el diccionario informacion_personal del ejercicio anterior, agrega una nueva clave llamada "email" con un correo ficticio. 
# Después, cambia el valor de la clave "ciudad" a "Córdoba". Imprime el diccionario completo.

informacion_personal['email'] = 'lebronjames@gmail.com'
informacion_personal['ciudad'] = 'Cordoba'
print(informacion_personal)


# 3. Eliminar Elementos (usando del)
# Ejercicio: Crea un diccionario llamado frutas con al menos tres frutas y sus precios. Luego, usa la palabra clave del para eliminar una de las frutas y su precio. 
# Imprime el diccionario antes y después de la eliminación.

frutas = {
    'manzana': 100,
    'banana': 120,
    'frutilla': 150
}

print(frutas)

del frutas['banana']
print(frutas)


# 4. Iterar sobre Claves y Valores
# Ejercicio: Itera sobre el siguiente diccionario capitales e imprime cada par clave-valor en el formato: "La capital de [País] es [Capital]".
# capitales = { "Japón": "Tokio","Francia": "París", "Canadá": "Ottawa" }

capitales = { "Japón": "Tokio","Francia": "París", "Canadá": "Ottawa" }

def mostrar_valores(diccionario:dict)->None:
    """
    Imprime por consola cada valor de las keys del dicccionario

    Args:
        diccionario (dict): El diccionario que ingrese el usario

    Returns:
        None: No devuelve nada
    """

    for elemento_actual in (diccionario.keys()):
        pais = elemento_actual
        capital = diccionario.get(pais)
        print(f"La capital de {pais} es {capital}")

mostrar_valores(capitales)


# 5. Obtener Claves, Valores y Pares (keys(), values(), items())
# Ejercicio: Dado el diccionario colores, imprime por separado una lista de todas las claves, una lista de todos los valores y, por último, la representación de todos
#  los pares clave-valor.
# colores = { "rojo": "#FF0000", "verde": "#00FF00", "azul": "#0000FF" }

colores = { "rojo": "#FF0000", "verde": "#00FF00", "azul": "#0000FF" }

print(list(colores.keys()))

print(list(colores.values()))

print(list(colores.items()))



# 6. Uso de get() para Evitar Errores
# Ejercicio: Intenta acceder a una clave que no existe en el diccionario configuración de dos maneras: configuración = {"tema": "oscuro", "fuente": "Arial"}
# Directamente con corchetes ([]). (Esto debería causar un error si no lo manejas).
# Usando el método .get(), proporcionando un valor predeterminado (default) de "No configurado".

configuración = {"tema": "oscuro", "fuente": "Arial"}

#print(configuración['estilo'])
print(configuración.get('estilo', 'No se encuntra en el diccionario'))


# 7. Contar Frecuencias con un Diccionario
# Ejercicio: Dada la siguiente lista de palabras, usa un diccionario para contar y almacenar la frecuencia de cada palabra (cuántas veces aparece).
# palabras = ["gato", "perro", "gato", "pez", "perro", "gato"]

palabras = ["gato", "perro", "gato", "pez", "perro", "gato"]

def contar_elementos(lista:list)->None:
    """
    Cuneta la cantidad de elementos de una lista

    Args:
        lista (list): La lista que ingrese el usuario

    Returns:
        None: No devuelve nada
    """

    diccionario_aux = dict()

    for elemento in lista:
        if elemento not in diccionario_aux.keys():
            diccionario_aux[elemento] =  1
        else:
            diccionario_aux[elemento] = diccionario_aux.get(elemento) + 1
    print(diccionario_aux)

contar_elementos(palabras)



# 8. Diccionario Anidado (Nested Dictionary)
# Ejercicio: Crea un diccionario llamado estudiantes donde cada clave sea un nombre y su valor sea otro diccionario 
# con las claves "matematicas" e "programación 1" con las notas de ese estudiante. Imprime la nota de matemáticas de "Pepe" (Debe ser una de las claves de tu diccionario).

estudiantes = {
    'Naza' : {
        'matematicas' : 9,
        'programacion 1' : 10
    },
    'Nacho' : {
        'matematicas' : 8,
        'programacion 1' : 9
    },
    'Enzo' : {
        'matematicas' : 2,
        'programacion 1' : 5.5
    }
}


print(estudiantes['Naza']['matematicas'])
print(estudiantes.get('Enzo').get('matematicas'))


# 9. Actualizar Diccionarios con update()
# Ejercicio: Tienes un diccionario base usuario_perfil y un diccionario de nuevas configuraciones nuevas_preferencias.
# Usa el método .update() para fusionar las nuevas preferencias en el perfil del usuario.
# usuario_perfil = {"nombre": "Leo", "tema": "claro", "notificaciones": True} nuevas_preferencias = {"tema": "oscuro", "sonido": False}

usuario_perfil = {"nombre": "Leo", "tema": "claro", "notificaciones": True}
nuevas_preferencias = {"tema": "oscuro", "sonido": False}

usuario_perfil.update(nuevas_preferencias)

print(usuario_perfil)


# 10. pop() para Extraer y Eliminar
# Ejercicio: Usa el método .pop() para obtener y eliminar la clave "puerto" del diccionario servidor. 
# Imprime el valor extraído y luego el diccionario restante.
# servidor = { "ip": "192.168.1.1", "puerto": 8080, "estado": "activo" }
servidor = { "ip": "192.168.1.1", "puerto": 8080, "estado": "activo" }

puerto = servidor.pop('puerto')

print(puerto)
print(servidor)