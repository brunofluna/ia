# Exercício 1
numero = int(input("Digite um número de 1 a 3: "))
if numero == 1:
    print("um")
elif numero == 2:
    print("dois")
elif numero == 3:
    print("três")
else:
    print("Número inválido!")

# Exercício 2
numero = float(input("Digite um número: "))
if numero > 10:
    print("O número é maior que 10")
else:
    print("O número não é maior que 10")

# Exercício 3
dia = int(input("Digite um número de 1 a 7 para o dia da semana: "))
dias = {
    1: "Domingo",
    2: "Segunda-feira",
    3: "Terça-feira",
    4: "Quarta-feira",
    5: "Quinta-feira",
    6: "Sexta-feira",
    7: "Sábado"
}
if 1 <= dia <= 7:
    print(dias[dia])
else:
    print("Dia inválido!")

# Exercício 4
cor = input("Digite uma cor (vermelho, verde, azul): ").lower()
if cor == "vermelho":
    print("A cor vermelha representa paixão e energia")
elif cor == "verde":
    print("A cor verde representa natureza e esperança")
elif cor == "azul":
    print("A cor azul representa tranquilidade e confiança")
else:
    print("Cor inválida!")

# Exercício 5
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Ambos os números são pares")
else:
    print("Pelo menos um dos números não é par") 