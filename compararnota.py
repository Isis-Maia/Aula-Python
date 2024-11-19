def comparação ():

    n1 = input("Nome: ").capitalize()
    v1 = float(input("Nota: "))
    n2 = input("Nome: ").capitalize()
    v2 = float(input("Nota: "))
    n3 = input("Nome: ").capitalize()
    v3 = float(input("Nota: "))

    if v1 > v2 and v1 > v3:
        if v2 > v3:
            print(f"{n1} está em primeiro com a nota {v1}")
            print(f"{n2} está em segundo lugar com a nota {v2}")
            print(f"{n3} está em terceiro lugar com a nota {v3}")
        else:
            print(f"{n1} está em primeiro com a nota {v1}")
            print(f"{n3} está em segundo lugar com a nota {v3}")
            print(f"{n2} está em terceiro lugar com a nota{v2}")
    elif v2 > v1 and v2 > v3:
        if v1 > v3:
            print(f"{n2} está em primeiro com a nota {v2}")
            print(f"{n1} está em segundo lugar com a nota {v1}")
            print(f"{n3} está em terceiro lugar com a nota {v3}")
        else:
            print(f"{n2} está em primeiro com a nota {v2}")
            print(f"{n3} está em segundo lugar com a nota {v3}")
            print(f"{n1} está em terceiro lugar com a nota {v1}")
    #empates
    elif v1 == v2 and v1 > v3:
        print(f"{n1} e {n2} empataram em primeiro lugar com a nota {v1}")
        print(f"{n3} está em segundo lugar com a nota {v3}")
    elif v1 == v3 and v1 > v2:
        print(f"{n1} e {n3} empataram em primeiro lugar com a nota {v1}")
        print(f"{n2} está em segundo lugar com a nota {v2}")
    elif v2 == v3 and v2 > v1:
        print(f"{n2} e {n3} empataram em primeiro lugar com a nota {v2}")
        print(f"{n1} está em segundo lugar com a nota {v1}")

    elif v1 == v2 and v1 < v3:
        print(f"{n3} está em primeiro lugar com a nota {v3}")
        print(f"{n1} e {n2} empataram em segundo lugar com a nota {v1}")
    elif v1 == v3 and v1 < v2:
        print(f"{n2} está em primeiro lugar com a nota {v2}")
        print(f"{n1} e {n3} empataram em segundo lugar com a nota {v1}")
    elif v2 == v3 and v2 < v1:
        print(f"{n1} está em primeiro lugar com a nota {v1}")
        print(f"{n3} e {n2} empataram em segundo lugar com a nota {v3}")
    #todos iguais
    elif v1 == v2 and v1 == v3:
        print(f"Todos tem a mesma nota, não tem ranking")
    else:
        if v1 > v2:
            print(f"{n3} está em primeiro com a nota {v3}")
            print(f"{n1} está em segundo lugar com a nota {v1}")
            print(f"{n2} está em terceiro lugar com a nota {v2}")
        else:
            print(f"{n3} está em primeiro com a nota {v3}")
            print(f"{n2} está em segundo lugar com a nota {v2}")
            print(f"{n1} está em terceiro lugar com a nota {v1}")

