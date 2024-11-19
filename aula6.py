nome = str(input("Qual seu nome? "))
idade = int(input("Qual sua idade? "))

if idade > 17:
    print(f"Você foi aprovado.")

elif idade == 17:
    print(f"Está na media, volte daqui a um ano")

else:
    print(f"Você reprovou.")