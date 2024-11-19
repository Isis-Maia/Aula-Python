def repetir ():
    ve = int(input("Quantas vezes deseja repetir? "))
    fr = input("Digite a mensagem: ")

    while ve != 0:
        print(f"{fr}")
        ve -= 1