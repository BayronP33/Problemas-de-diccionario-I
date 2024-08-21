def mezclar_diccionarios(a, b):
    diccionario_mezclado = a.copy()

    for clave, valor in b.items():
        if clave not in diccionario_mezclado:
            diccionario_mezclado[clave] = valor
    return diccionario_mezclado

diccionario1 = {'a': 1,'b': 2,'c': 3}
diccionario2 = {'b': 20,'c': 30,'d': 4}

resultado = mezclar_diccionarios(diccionario1, diccionario2)

print("Diccionario mezclado:")
print(resultado)


