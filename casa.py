#informar o nome do personagem
#verificar qual a casa do personagem de harry potter

n = input("Digite um personagem: ").title()

'''
if n == "Harry Potter" or n == "Hermione Granger" or n== "Rony Weasley":
    print(f"{n} é da casa Gryffinoria")
elif n == "Luna Lovegood":
    print(f"{n} é da casa Corvinal")
elif n == "Draco Malfoy":
    print(f"{n} é da casa Sonserina")
elif n == "Cedric Diggory":
    print(f"{n} é da casa Lufs-Lufa")
elif n == "Remo Lupin" or n == "Sirius Black":
    print(f"AUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")
else:
    print(f"{n} não pertence a nenhuma casa")
'''

match n:
    case "Harry Potter" | "Hermione Granger" | "Rony Weasley":
        print("Grifinoria")
    case "Draco Malfoy":
        print("Sonserina")
    case "Luna Lovegood":
        print("Corvinal")
    case "Cedric Diggory":
        print("Lufa-Lufa")
    case "Remo Lupin" | "Sirius Black":
        print("AAAUUUUUUUUUUUU")
    case "Tom Riddle" | "Lord Voldemort":
        print("Não fale de você-sabe-quem.")
    case _:
        print("Personagem não encontrado.")