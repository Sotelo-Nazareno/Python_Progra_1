import app
import funciones
from utn_fra.datasets import (
        lista_autos_marcas,
        lista_autos_modelos,
        lista_autos_cantidades,
        lista_autos_precios
    )

app.mostrar_menu(lista_autos_marcas, lista_autos_modelos, lista_autos_cantidades, lista_autos_precios)