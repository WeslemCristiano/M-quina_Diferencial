# Máquina Diferencial de Babbage

def diferencas(valores):
    tabela = [valores]
    while len(tabela[-1]) > 1:
        linha = []
        for i in range(len(tabela[-1]) - 1):
            linha.append(tabela[-1][i+1] - tabela[-1][i])
        tabela.append(linha)
    return tabela

def proximo_valor(tabela):
    soma = 0
    for linha in tabela:
        soma += linha[-1]
    return soma

def gerar_valor(x_inicial, h, valores, x_desejado):
    tabela = diferencas(valores)
    n = int(round((x_desejado - x_inicial) / h))
    resultado = valores[0]
    for k in range(1, len(valores)):
        termo = 1
        for j in range(k):
            termo *= (n - j)
        resultado += termo * tabela[k][0] / fatorial(k)
    return resultado

def fatorial(n):
    r = 1
    for i in range(2, n+1):
        r *= i
    return r

coef = [2, -3, 2, 9]
x = [i*0.1 for i in range(6)]
y = [sum(coef[j]*(xi**(len(coef)-1-j)) for j in range(len(coef))) for xi in x]

tabela = diferencas(y)

print("x:", [round(v, 2) for v in x])
print("y:", [round(v, 3) for v in y])
print("\nTabela de diferenças:")
for linha in tabela:
    print([round(v, 3) for v in linha])

print("\nPróximo valor da sequência:", round(proximo_valor(tabela), 3))
print("Valor em x=0.9:", round(gerar_valor(x[0], 0.1, y, 0.9), 3))

