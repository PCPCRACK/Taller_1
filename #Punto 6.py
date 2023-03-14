letra = input("Ingrese una letra: ") #solicita un caracter
if letra.lower() in ['a', 'e', 'i', 'o', 'u']: #convierte el caracter en minuscula
    print("La letra ingresada es una vocal")
else:
    print("La letra ingresada es una consonante")
