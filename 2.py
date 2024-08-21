diccionario1 = {'a': 1,'b': 2,'c': 3}
diccionario2 = {'a': 1,'b': 2,'c': 3,'d': 4}

def verificar_diccionarios(a, b):
    for clave, valor in a.items():
        if clave not in b or b[clave] != valor:
            return False
    return True

if verificar_diccionarios(diccionario1, diccionario2):
    print("Todos los elementos de diccionario1 están en diccionario2.")
else:
    print("No todos los elementos de diccionario1 están en diccionario2.")


