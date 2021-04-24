def empilha(lista, origem, destino):

    y = lista[origem]
    lista.remove(lista[origem])
    lista.remove(lista[destino])
    lista.insert(destino, y)

    return lista
    