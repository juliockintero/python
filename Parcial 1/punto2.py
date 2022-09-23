def convertir():

    print("Seleccione una opción:"
          "\n1 DEC A BIN "
          "\n2 DEC A OCT "
          "\n3 DEC A QUINT "
          "\n4 SALIR")
    op = input()
    if op == "1":
        print("Por favor ingrese la base")
        decimal = int(input())
        binario = ''
        while decimal // 2 != 0:
            binario = str(decimal % 2) + binario
            decimal = decimal // 2
        return str(decimal) + binario

    elif op == "2":
        print("Por favor ingrese la base")
        n = int(input())
        octal = ""
        while n > 0:
            res = n % 8
            octal = str(res) + octal
            n = int(n / 8)
        return octal
    elif op == "3":
        print("Por favor ingrese la base")
        n = int(input())
        quintal = ""
        while n > 0:
            res = n % 5
            quintal = str(res) + quintal
            n = int(n / 5)
        return quintal

    if op == "4":
        print("fin")

print(convertir())