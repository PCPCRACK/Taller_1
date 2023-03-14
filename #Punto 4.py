print("Dime 2 numeros") 
A= float(input()) #El programa pide 2 numeros reales
B= float(input())
if A%B==0: #compara si la division por residuo sea cero
    print(A ," es multiplo de ", B) 
else:
    print (A ," NO es multiplo de ", B)
