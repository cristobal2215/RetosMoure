#opcion 1
# def decimal_a_binario():
#     a = bin(int(input('ingresa el numero a convertir')))
#     return a
# print (decimal_a_binario())

#opcion 2:

def Decimal_A_Binario():
    decimal=int(input('ingresa el numero a convertir: '))
    resto=[]
    while decimal > 0:
        a= decimal % 2
        resultado = decimal // 2
        resto.append(a)
        decimal = resultado
    print (resto)
Decimal_A_Binario()