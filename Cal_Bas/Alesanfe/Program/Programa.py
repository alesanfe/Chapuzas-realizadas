from Alesanfe.Program.Tool import Mates
from Alesanfe.Program.Tool import Easy
import math
from datetime import datetime
respuesta=30
print("Cal_Bas ha iniciado. {}\n".format(datetime.now()))
while respuesta<40: 
    Easy.Lectura(0,14)  
    programa=str(input("Introduzca lo que quiere hacer:"))
    print()
    respuesta=30
    if programa=="1":       
        x=0
        while respuesta<35:
            print("Programa de cálculo.")
            print("x=ANS ")
            print("ANS=",x)
            operacion=input("Introduce la operación a realizar (suma [+],resta [-],multiplica [*],divide [x/a] o [a/x]) y eleva [a**x] o[x**a]: ").lower()
            if operacion=="+":
                a=Easy.Corrector("Introduzaca el número:")      
                x=x+a
                print("x+a={}".format(a))
            elif operacion=="-":
                a=Easy.Corrector("Introduzaca el número:")
                x=a-x
                print("x=a-x={}".format(a))
            elif operacion=="*":
                a=Easy.Corrector("Introduzaca el número:")
                x=x*a
                print("x=x*a={}".fprmat(a))
            elif operacion=="x/a":
                a=Easy.Corrector("Introduzaca el número:")
                while True:
                    try:      
                        x=x/a
                        break
                    except ZeroDivisionError:
                        print("No se puede dividir entre 0.")
                print("x=x/a={}".format(a))
            elif operacion=="a/x":
                a=Easy.Corrector("Introduzaca el número:")
                while True:
                    try:
                        x=a/x
                        break
                    except ZeroDivisionError:
                        print("No se puede dividir entre 0.")
                    print("x=a/x={}".format(a))
            elif operacion=="a**x":
                a=Easy.Corrector("Introduzaca el número:")
                x=a**x
                print("x=a**x={}".format(a))
            elif operacion=="x**a":
                a=Easy.Corrector("Introduzaca el número:")
                x=x**a
                print("x=x**a={}".format(a))
            else:
                print ("Operación no contemplada")
            print("¿Consevar x?")
            r1=input("SI o NO:").upper()
            if r1=="SI":
                print("Entendido.")
            elif r1=="NO":
                print("Eliminando información.")
                x=Easy.Corrector("Introduzca el valor de  x:")
            respuesta=Easy.Cambiador(respuesta)
        print()
    elif programa=="2":
        while respuesta<35:
            print("Programa para calcular número de bits de un número.")
            A=Easy.Corrector("Introduzaca el número:")  
            x=int(math. log2(A)+1)
            print("Resultado:",x)
            respuesta=Easy.Cambiador(respuesta)
        print()
    elif programa=="3":
        while respuesta<35:
            print("Programa para calcular números de Fermat.")
            print("¿Todos los resultados?")
            r0=input("SI o NO:").upper()
            A=Easy.Límite("Introduzca un número menor que 18:", 18)
            B=0
            while B<A:
                B+=1
                if r0=="SI":
                    print(B,"Resultado:",Mates.Fermat(B)) 
            if r0=="NO":
                print("Resultado:",Mates.Fermat(B))
            respuesta=Easy.Cambiador(respuesta)
        print()
    elif programa=="4":    
        while respuesta<35:
            print("Programa para calcular números de Mersenne.")
            print("¿Todos los resultados?")
            r0=input("SI o NO:").upper()
            A=Easy.Corrector("Introduzaca un número:")
            B=0
            while B<=A:
                B+=1
                if r0=="SI":
                    print(B,"Resultado:",Mates.Marsenne(B)) 
            if r0=="NO":
                print("Resultado:",Mates.Marsenne(B))
            respuesta=Easy.Cambiador(respuesta)
        print()
    elif programa=="5":        
        while respuesta<35:
            print("Programa para calcular números de Fibonacci.")
            print("¿Todos los resultados?")
            r0=input("SI o NO:").upper()
            A=Easy.Corrector("Introduzaca un número:")
            B=0
            while B<=A:
                B+=1
                if r0=="SI":
                    print(B,"Resultado:",Mates.Fibonacci(B)) 
            if r0=="NO":
                print("Resultado:",Mates.Fibonacci(B))
            respuesta=Easy.Cambiador(respuesta) 
        print()
    elif programa=="6":      
        while respuesta<35:
            print("Progrma para calcular medias.")
            Mates.Medias()
            respuesta=Easy.Cambiador(respuesta)
    elif programa=="7":      
        while respuesta<35:
            print("Programa de cálculo de raíz cuadrada.")
            Mates.Raíces_Cuadradas()
            respuesta=Easy.Cambiador(respuesta)
        print()
    elif programa=="8":      
        while respuesta<35:
            print("Programa para comparar números.")
            Mates.Comparador()
            respuesta=Easy.Cambiador(respuesta)
        print()
    elif programa=="9":      
        while respuesta<35:
            print("Programa para calcular máximo común divisor y mínimo común múltiplo.")
            Mates.mcd_mcm()
            respuesta=Easy.Cambiador(respuesta)
        print()
    elif programa=="10":        
        while respuesta<35:
            print("Programa de adivinar un número.")
            Mates.Adivina()
            respuesta=Easy.Cambiador(respuesta)
        print()
    elif programa=="11":      
        while respuesta<35:
            print("Programa para sulcionar ecuaciones de grado 1.")
            Mates.sol_ecuacion_primer_grado()
            respuesta=Easy.Cambiador(respuesta)
        print()
    elif programa=="12":
        while respuesta<35:
            print("Programa para solucionar ecuaciones de grado 2.")
            Mates.sol_ecuacion_segundo_grado()
            respuesta=Easy.Cambiador(respuesta)
        print()
    else:
        print("Por favor, introduzca una de las opciones.\n")
print("Cal_Bas ha finalizado.")
