def imc ():
    peso = float(input("Insira seu peso: ").replace(",", "."))
    altura = float(input("Insira sua altura: ").replace(",", "."))

    imc = peso/(altura**2)

    if imc < 18.5:
        print(f"Seu IMC é {imc:.2f} e você está Abaixo do Peso adequado.")

    elif imc >= 18.5 and imc <= 24.8:
        print(f"Seu IMC é {imc:.2f} e você está com o Peso normal.")

    elif imc >= 24.9 and imc <= 29.8:
        print(f"Seu IMC é {imc:.2f} e você está com Excesso de peso.")

    elif imc >= 29.9 and imc <= 34.8:
        print(f"Seu IMC é {imc:.2f} e você está com Obesidade Classe I")

    elif imc >= 34.9 and imc <= 39.8:
        print(f"Seu IMC é {imc:.2f} e você está com Obesidade Classe II")

    else:
        print(f"Seu IMC é {imc:.2f} e você está com Obesidade Classe III")

"""
selo de aprovação do titio:

aprovado
"""