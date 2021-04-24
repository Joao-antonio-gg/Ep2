def empilha(lista2, origem, destino):

    y = lista2[origem]
    lista2.remove(lista2[origem])
    lista2.remove(lista2[destino])
    lista2.insert(destino, y)

    return lista2
    