def Lectura(n1,n2):
    with open('Texto', encoding='utf-8') as f:
        for num_linea, linea in enumerate(f):  
            print(linea, end='')
            if n1>num_linea<n2:
                break
def Cambiador(p):
    print("Continuar [1], cambiar [2] o apagar [3].")
    r=input("Introducir respuesta:")
    if r=="1":
        print("Entendido")
    elif r=="2":
        p=37
    elif r=="3":
        p=42
    return p
def Corrector(mensaje):
    while True:
        try:
            número=float(input(mensaje))
            return número
            break
        except ValueError:
            print("Valor incorrecto.")
def Límite(mensaje,número):
    a=Corrector(mensaje)
    while True:
        if a<número:
            break
        elif a>=número:
            a=Corrector(mensaje)
    return a
def checkArgument(condition:bool,message=None):    
    if(not condition):
        raise Exception(message)