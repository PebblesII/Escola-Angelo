def calcular(x, y, op):
    if op == 1:
        print(x + y)
    elif op == 2:
        print(x - y)
    elif op == 3:
        print(x * y)
    elif op == 4:
        print(x / y)
    elif op == 5:
        print(x % y)
    elif op == 6:
        print(x ** y)

x = int(input("N1 ="))
y = int(input("N2 ="))
print("--OPERACÕES--")
print("1 = +")
print("2 = -")
print("3 = *")
print("4 = /")
print("5 = %")
print("6 = **")

op = int(input("Escolha uma operação = "))
calcular(x, y, op)