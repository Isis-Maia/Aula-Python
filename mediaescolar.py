def media ():
    print("Escolha um numero entre 2 e 4, que seja correspondente ao seu bimestre.")
    div = int(input("Digite o numero: "))

    if div == 2:
        B1 = float(input("Primeira nota: ").replace("," , "."))
        B2 = float(input("Segunda nota: ").replace("," , "."))
        Bt = (B1 + B2) 
        med = (B1+B2)/div
        print(f"No total você está com {B1+B2}.")
        if Bt == 20:
            print(f"Sua media é {med:.2f}")
            print(f"Não precisa de recuperação")
        elif Bt >= 12:
            print(f"Sua media é {med:.2f}")
            print(f"Você esta na media, você precisava de mais {20-Bt:.2f}.")
            print(f"Você precisa de {24-Bt:.2f} para completar 24.")
        else:
            print(f"Sua media é {med:.2f}")
            print(f"Você esta na recuperação, você precisa de {20-Bt:.2f} para passar no bimestre")
            print(f"Você precisa de {24-Bt:.2f} para completar 24.")
    elif div == 3:
        B1 = float(input("Primeira nota: ").replace("," , "."))
        B2 = float(input("Segunda nota: ").replace("," , "."))
        B3 = float(input("Terceira nota: ").replace("," , "."))
        Bt = (B1 + B2 + B3) 
        med = (B1+B2+B3)/div
        print(f"No total você está com {B1+B2+B3}.")
        if Bt == 30:
            print(f"Sua media é {med:.2f}")
            print(f"Não precisa de recuperação")
        elif Bt >= 18:
            print(f"Sua media é {med:.2f}")
            print(f"Você esta na media.")
            print(f"Você precisa de {24-Bt:.2f} para completar 24.")
        else:
            print(f"Sua media é {med:.2f}")
            print(f"Você esta na recuperação, você precisa de {30-Bt:.2f} para passar nos 2 bimestres")
            print(f"Você precisa de {24-Bt:.2f} para completar 24.")
    elif div == 4:
        B1 = float(input("Primeira nota: ").replace("," , "."))
        B2 = float(input("Segunda nota: ").replace("," , "."))
        B3 = float(input("Terceira nota: ").replace("," , "."))
        B4 = float(input("Quarta nota: ").replace("," , "."))
        Bt = (B1 + B2 + B3 +B4) 
        med = (B1+B2+B3+B4)/div
        print(f"No total você está com {B1+B2+B3+B4}.")
        if Bt == 40:
            print(f"Sua media é {med:.2f}")
            print(f"Não precisa de recuperação")
        elif Bt >= 24:
            print(f"Sua media é {med:.2f}")
            print(f"Você esta na media, você precisava de mais {40-Bt:.2f}.")
            print(f"Você precisa de {24-Bt:.2f} para completar 24.")
        else:
            print(f"Sua media é {med:.2f}")
            print(f"Você esta na recuperação, você precisa de {40-Bt:.2f} para passar no bimestre")
            print(f"Você precisa de {24-Bt:.2f} para completar 24.")
