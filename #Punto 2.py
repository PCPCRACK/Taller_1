print("Dime 3 numeros")
A= float(input())
B= float(input())
C= float(input())
if A==B or B==C or A==C:
    print("dar valores diferentes")
elif A>B and A>C:
    print(A)
elif B>A and B>C:
    print(B)
elif C>A and C>B:
    print(C)
print("es el mayor")
