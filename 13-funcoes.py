def exibirMensagem(nome, idade):
    print(f"Olá, {nome} com {idade} anos!")


def somar(a, b):
    return a + b


def calcularAreaCirculo(raio):
    area = 3.1415 * raio**2
    return area


nome = input("Digite o seu nome!")
idade = input("Digite o seu idade!")
exibirMensagem(idade, nome)


valorA = int(input("Digite o primeiro número: "))
valorB = int(input("Digite o segundo número: "))
resultado = somar(valorA, valorB)
print(f"O resultado da soma = {resultado}")

print("a Área do círculo!!")
raio = float(input("Digite o valor do raio: "))
area = calcularAreaCirculo(raio)
print(f"A área do círculo : : {area:.2f}")