x = float(input("Digite o primeiro numero: "))
y = float(input("Digite o segundo numero: "))

resultado = x**y
resultado = f"{resultado:_.2f}"
resultado = resultado.replace("." , ",").replace("_", ".")
print(f"{x} elevado ao {y} é igual a {resultado}")

#round arredonda o numero
# ", 2" deixa apenas duas casa decimais
# formatar é colocar um formato a algo
