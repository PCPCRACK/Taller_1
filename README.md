# Taller_1
#Punto 1: Quiz Python Beginner

[![Captura.png](https://i.postimg.cc/2jgSMnN1/Captura.png)](https://postimg.cc/14cSNntS)


#Punto 2: Un programa que lea tres números reales y determine cuál es el mayor
```python
print("Dime 3 numeros") #El programa pide 3 valores
A= float(input())
B= float(input())
C= float(input())
if A==B or B==C or A==C: #si algunos de los valores son iguales no se ejecutara
    print("dar valores diferentes")
elif A>B and A>C: #compara los cada uno de los valores con los demas para determinar cual es el mayor
    print(A)
elif B>A and B>C:
    print(B)
elif C>A and C>B:
    print(C)
print("es el mayor")
```

Diagrama de flujo

 [![a.png](https://i.postimg.cc/ZKvPRSXH/a.png)](https://postimg.cc/fJZS26zS)

#Punto 3


#Punto 4: Programa que lea dos números reales y determine si el primero es múltiplo del segundo.
```python
print("Dime 2 numeros") #El programa pide 2 valores
A= float(input())
B= float(input())
if A%B==0: #compra si la division por residuo sea cero
    print(A ," es multiplo de ", B) 
else:
    print (A ," NO es multiplo de ", B)
```


#Punto 5



#Punto 6: programa que solicite al usuario una letra y determine si es una vocal o una consonante
```python
letra = input("Ingrese una letra: ")
if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("La letra ingresada es una vocal")
else:
    print("La letra ingresada es una consonante")
```



#Punto 7 



#Punto 8: programa al que se le ingrese la frecuencia de una onda en hz y como salida arroje en que parte del espectro electromagnético se encuentra.


```python
frecuencia = float(input("Ingrese la frecuencia en Hz: "))
VL= 299792458
Longitud_onda = VL/frecuencia

if Longitud_onda < 10e-12:
    print("La frecuencia ingresada se encuentra en la banda de rayos gamma.")
elif Longitud_onda < 10e-9:
    print("La frecuencia ingresada se encuentra en la banda de rayos x.")
elif Longitud_onda < 220e-9:
    print("La frecuencia ingresada se encuentra en la banda de ultravioleta extremo.")
elif Longitud_onda < 380e-9:
    print("La frecuencia ingresada se encuentra en la banda de ultravioleta carcano.")
elif Longitud_onda < 780e-9:
    print("La frecuencia ingresada se encuentra en la banda de espectro visible.")
elif Longitud_onda < 2.5e-6:
    print("La frecuencia ingresada se encuentra en la banda de infrarojo cercano.")
elif Longitud_onda < 50e-6:
    print("La frecuencia ingresada se encuentra en la banda de infrarojo medio.")
elif Longitud_onda < 1e-3:
    print("La frecuencia ingresada se encuentra en la banda de infrarojo lejano.")
elif Longitud_onda < 10**-2:
    print("La frecuencia ingresada se encuentra en la banda de microondas.")
elif Longitud_onda < 1:
    print("La frecuencia ingresada se encuentra en la banda de ultra alta frecuencia de radio.")
elif Longitud_onda < 10:
    print("La frecuencia ingresada se encuentra en la banda de muy alta frecuencia de radio.")
elif Longitud_onda < 180:
    print("La frecuencia ingresada se encuentra en la banda de onda corta de radio.")
elif Longitud_onda < 650:
    print("La frecuencia ingresada se encuentra en la banda de onda media de radio.")
elif Longitud_onda < 10e3:
    print("La frecuencia ingresada se encuentra en la banda de onda larga de radio.")
else:
    print("La frecuencia ingresada se encuentra en la banda muy baja de radio.")

```





#Punto 9



#Punto 10: programa que dada una distancia calcule:
+El tiempo que le tomaría a la luz recorrer la distancia.
+El tiempo que le tomaría al sonido (en el aire) recorrer la distancia.
+El tiempo que le tomaría al vehiculo comercial más veloz recorrer la distancia.
+El tiempo que le tomaría a Bolt recorrer la distancia.


```python
print("inresa una distancia en METROS")
Dist=float(input())
VL= 299792458
VS=343
VC=341.106944
VB=12.42
Velocidad_luz = Dist/VL
Velocidad_sonido= Dist/VS
Velocidad_comercial= Dist/VC
Velocidad_bolt= Dist/VB

print("Velocidad de la luz:", Velocidad_luz, "segundos")
print("Velocidad del sonido", Velocidad_sonido,"segundos")
print("Velocidad del vehiculo mas rapido", Velocidad_comercial,"segundos")
print("Velocidad de Usain Bolt", Velocidad_bolt, "segundos")
```

