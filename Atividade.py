import compararnota
import mediaescolar
import imc
import repetição
import aceita

print("---Vamos iniciar---")
nome = input("Insira seu nome para iniciar: ").capitalize()
print(f"Olá {nome}, seja bem vindo.")

aceita.termos()

escolha = input(f"aperte 1 para prosseguir ou 2 para abrir a tabela. ")
opção = 0

if escolha == "1":
     opção = input("Qual a função? ").upper()
#calculadora
     if opção == "M":
          M = input("Insira o calculo: ")
          M = eval (M)
          print(f"O resultado foi {M:.2f}")
     elif opção == "I":
          imc.imc()
     elif opção == "ME":
          mediaescolar.media()
     elif opção == "CN":
          compararnota.comparação()
     elif opção == "R":
          repetição.repetir()
elif escolha == "2":
     print("---Funções---")
     print("Calculo: M")
     print("IMC: I")
     print("Media Escolar: ME")
     print("Comparar Nota: CN")
     print("Listar Livros: LL")
     print("Jogo da Forca: JF")
     print("Repetição: R")
     opção = input("Qual a função? ").upper()
     if opção == "M":
          M = input("Insira o calculo: ")
          M = eval (M)
          print(f"O resultado foi {M:.2f}")
     elif opção == "I":
          imc.imc()
     elif opção == "ME":
          mediaescolar.media()
     elif opção == "CN":
          compararnota.comparação()
     elif opção == "R":
          repetição.repetir()
else:
     print("Comando errado.")
