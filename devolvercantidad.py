numero = int(input("ingrese el numero que deseas contar la cantidad: "))

def cont(numero,suma):
    if numero == 0:
        return suma + 1
    else:
        last = numero //10
        suma = suma + 1
        return cont(last,suma)
try:
    print(cont(numero,0))
except ValueError: 
    print("debes ingresar un numero no una letra ")
    numero = int(input("ingrese el numero que deseas contar la cantidad: "))
    print(cont(numero,0))