def calcular_potencia(b, e):

    r = 1

    if b == 0 and e != 0:
        return 0

    if b != 0 and e == 0:
        return 1

    if b == 0 and e == 0:
        return print("Indeterminado")

    if b != 0 and e > 0:

        for i in range(e):
            r = r * b
        return r


print(calcular_potencia(3, 3))