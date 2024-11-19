def main():
    print("--- Calculadora de Quadrados: ---")
    n = float(input("Qual o numero?"))
    quadrado = calculadora_quadrado(n)
    cubo = calculadora_cubo(n)
    print(f"{n} ao quadrado é {quadrado:.2f} e ao cubo é {cubo:.2f}")


def calculadora_quadrado(n):
    return n ** 2 


def calculadora_cubo(n):
    return n ** 3 


main()

