import operator
import functools
from Alesanfe.Program.Tool import Easy
import math
import random
def Fermat(número):
    C=2**2**número+1
    return C
def Marsenne (número):
    C=2**número-1
    return C
def Fibonacci(número):
    x=1/math.sqrt(5)
    y1=(1+math.sqrt(5));y2=(1-math.sqrt(5))
    z1=(y1/2)**número;z2=(y2/2)**número
    w1=x*z1;w2=x*z2
    F1=w1;F2=w2
    C=F1-F2
    return C
def mcm(a,b):
    x=a*b/mcd(a, b)
    return x
def mcd(a,b):
    if b == 0:
        return a
    else:
        return mcd(b, a%b)
def mcd_mcm():
    A=Easy.Corrector("Introduzca primer número: ");B=Easy.Corrector("Introduzca segundo número: ")
    print("El máximo común divisor es:",mcd(A,B))
    print("El mínimo común múltiplo es:",mcm(A,B))

def genera_numero(minimo,maximo):
    aleatorio=random.randint(minimo,maximo)
    return aleatorio
def lee_numero(minimo,maximo):
    mensaje="Introduzca un número del"+" "+str(minimo)+" "+"al"+" "+str(maximo)+":"
    n=int(input(mensaje))
    return n
def comprueba_numero(aleatorio,n):
    if n==aleatorio:
        print("Has acertado.")
        acertado=True
    elif aleatorio>n:
        print("Elija un número mayor.")
        acertado=False
    else:
        print("Elija un número menor.")
        acertado=False
    return acertado
def Medias():
    y=0
    z=0
    while True:
        print("¿Quiere añadir un número? ")    
        r=input("SI o NO:").upper()
        if r=="SI":
            x=Easy.Corrector("Introduzca el número: ")
            z+=x  
            y+=1 #lo mismo que y+=x/x, pero da menos errores ya que no puede darse 0/0 (es una indeterminaci�n).
        elif r=="NO":
            break 
        else:
            print("Por favor, responda SI o NO.")
    n=z/y
    print("Número de valores introducidos:",y)
    print("Total:",z)
    print("Último valor introducido:",x)
    print("Media:",n)
def Comparador():
    A=Easy.Corrector("Introduzca número A: ");B=Easy.Corrector("Introduzca número B: ")
    if A==B:
        print("Son iguales.")
    if A<B:
        print("A es menor que B.")
    if A>B:
        print("A es mayor que B")
  
def sol_ecuacion_primer_grado():
    print("Ax+B=0")
    A=Easy.Corrector("Introduzca número A: ");B=Easy.Corrector("Introduzca número B ")
    Easy.checkArgument(A!=0, "A debe ser distinto de 0.")
    print("La solución es:",-A/B)
def sol_ecuacion_segundo_grado():
    print("Ax^2+Bx+C=0")  
    A=Easy.Corrector("Introduzca número A: ");B=Easy.Corrector("Introduzca número B: ");C=Easy.Corrector("Introduzca número C: ")
    Easy.checkArgument(A!=0, "A debe ser distinto de 0.")
    D =B**2-4*A*C
    E=math.sqrt(abs(B**2-4*A*C))
    if D>0:
        print("Las soluciones son {} y {}.".format((-B+E)/(2*A),(-B-E)/(2*A)))
    elif D<0:
        print("Las soluciones son {} y {}.".format(complex(-B,E)/2*A,complex(-B,-E)))
def Adivina():
    mínimo=Easy.Corrector("Introduzca el mínimo: ")
    máximo=Easy.Corrector("introduzca el máximo: ")
    aleatorio=genera_numero(mínimo, máximo)
    acertado=False
    while acertado==False:
        n=lee_numero(mínimo, máximo)
        acertado=comprueba_numero(aleatorio, n)
def Primos():
    print("p=6k±1")
    k=Easy.Corrector("Introduzca un número: ")
    Easy.checkArgument(k>3, "No se admite ese valor.")
    i=input("¿Valor positivo o negativo? ").upper()
    if i=="POSITIVO":
        p=6*k+1
        print("El primo buscado es {}".format(p))
    elif i=="NEGATIVO":
        p=6*k-1
        print("El primo buscado es {}".format(p))
def Demostración_Primos():
    A=Easy.Corrector("Introduzca el número: ")
    Easy.checkArgument(A>4,"Imposible de calcular.")
    B=int(math.sqrt(A))
    for i in range(2,B):
        z=A%i
        if z==0:
            print("No es primo.")
            break
    if z!=0:
        print("Es primo.")
def Criba_Erastótenes():
    n = int(input("¿Hasta qué número? "))
    lista = list(range(2, n+1))
    i = 0
    while(lista[i]*lista[i] <= n):
        for num in lista:
            if num <= lista[i]:
                continue
            elif num % lista[i] == 0:
                lista.remove(num)
            else:
                pass
        i += 1 
    print(lista)
def Método_Herón():
    raíz=Easy.Corrector("Número a calcular raíz: ")
    iteraciones= Easy.Corrector("Número de iteraciones: ")
    Easy.checkArgument(iteraciones<15,"Imposible de calcular.")   
    Valores=[]
    Valores.append(1)
    iteraciones_realizadas=0
    while True:
        if iteraciones_realizadas<iteraciones:
            Valores[0]=0.5*(Valores[0]+raíz/Valores[0])
            iteraciones_realizadas+=1
        elif iteraciones_realizadas==iteraciones:
            print("La raíz es:", Valores[0])
            break
def Número_Euclides():
    iteraciones=Easy.Corrector("Número de iteraciones:") 
    Valores=[]
    Valores.append(2)
    iteraciones_realizadas=0
    while True:
        if iteraciones_realizadas<iteraciones:
            Valores.append(functools.reduce(operator.mul, Valores, 1)+1)  
            iteraciones_realizadas+=1
        elif iteraciones_realizadas==iteraciones:
            print("Los números de Euclides pedidos son: ",Valores)
            break
def Raiz_Cuadrada(x):
    if x < 0:
        return '%s i' % math.sqrt(-x)
    elif x>0:
        return math.sqrt(x)

        
        
