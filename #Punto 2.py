print("Dime 3 numeros") 
A= float(input()) #El programa pide 3 numeros reales
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
