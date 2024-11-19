def repetir ():
    while True:
        vz = int(input("Quantas vezes você quer repetir? "))
        pv = input("Qual a mensagem? ")

        if vz >0:
            break

    for _ in range(vz):
        print(f"{pv}")
