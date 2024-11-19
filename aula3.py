nome = input("Qual seu nome? ")

nome = nome.title().split()
nome = " ".join(nome)


print(nome)

#.lower = baixo, letras minusculas
#.upper = alto, letra maiuscula
#.capitalize = fica em maiusculo o primeiro caractere, o resto é deixado em minusculo
#.title =  fica em maiusculo o primeiro caractere de cada palavra
#.strip = remove espaços em branco; 
    # lstrip = remove espaços em branco da esquerda;
    # rstrip = remove os espaços em branco da direita;
#split =  quebra a string em uma lista, considerando os espaços separadores.
