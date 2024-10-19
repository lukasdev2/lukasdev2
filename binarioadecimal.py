binary = int(input("ingrese el numero binario que desea convertir  a decimal: "))

def binaryconvert(binary,peso):

    save = binary
    if binary == 0:
        return 0
    else:
        ultimo = binary //10
        converted = binary % 10 *2 ** peso
        
        return converted + binaryconvert(ultimo,peso + 1)
        
print(binaryconvert(binary,0))