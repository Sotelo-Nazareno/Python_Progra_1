from utn_fra.datasets import (
    lista_poke_ids, lista_poke_nombres,
    lista_poke_tipos, lista_poke_poderes,
    lista_poke_condiciones
)

import app

app.pokedex(lista_poke_ids, lista_poke_nombres, lista_poke_tipos, lista_poke_poderes, lista_poke_condiciones)