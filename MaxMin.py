def mcd(a, b):
  if b == 0:
    print(a)
  else:
    mcd(b, a%b)

def mcm(a, b):
  print(a*b // mcd(a, b))

a= int(input("Ingresa el primer número: "))
b= int(input("Ingresa el segundo número: "))

mcd(a, b)
mcm(a, b)