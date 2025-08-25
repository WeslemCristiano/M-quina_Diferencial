# Máquina Diferencial de Babbage

Uma implementação em Python do algoritmo de diferenças finitas utilizado na histórica Máquina de Diferenças de Charles Babbage, um dos primeiros computadores mecânicos da história.

## 📖 Sobre o Projeto

A Máquina de Diferenças de Babbage foi projetada no século XIX para calcular tabelas matemáticas automaticamente. Este projeto simula o funcionamento dessa máquina, implementando o método das diferenças finitas para calcular polinômios usando apenas operações de adição.

## 🚀 Funcionalidades

- **Cálculo de Diferenças Sucessivas**: Gera tabelas de diferenças finitas
- **Interpolação Polinomial**: Utiliza o método de Newton para calcular valores intermediários
- **Predição de Valores**: Estende sequências polinomiais para encontrar próximos termos
- **Exemplo Prático**: Demonstra o funcionamento com um polinômio cúbico

## 🛠️ Como Usar

### Executar o programa:
```bash
python Máquina_Babbage.py
```

### Exemplo de saída:
```
x: [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
y: [9.0, 8.702, 8.808, 9.318, 10.232, 11.55]

Tabela de diferenças:
[9.0, 8.702, 8.808, 9.318, 10.232, 11.55]
[-0.298, 0.106, 0.51, 0.914, 1.318]
[0.404, 0.404, 0.404, 0.404]
[0.0, 0.0, 0.0]

Próximo valor da sequência: 13.272
Valor em x=0.9: 17.238
```

## 📚 Algoritmo

### Método das Diferenças Finitas

1. **Primeira Linha**: Valores originais do polinômio
2. **Linhas Sucessivas**: Diferenças entre elementos consecutivos
3. **Parada**: Quando a diferença se torna constante (para polinômios)

### Interpolação de Newton

O programa usa a fórmula de Newton para diferenças progressivas:

```
f(x₀ + nh) = f(x₀) + nΔf(x₀) + n(n-1)/2! Δ²f(x₀) + ...
```

## 🔧 Funções Principais

- `diferencas(valores)`: Calcula a tabela de diferenças finitas
- `proximo_valor(tabela)`: Prediz o próximo valor da sequência
- `gerar_valor(x_inicial, h, valores, x_desejado)`: Interpola valores usando Newton
- `fatorial(n)`: Calcula o fatorial de um número

## 📊 Exemplo de Uso

O código demonstra o cálculo com o polinômio:
```
P(x) = 2x³ - 3x² + 2x + 9
```

Para pontos x = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]

## 🎯 Aplicações

- Cálculo de tabelas logarítmicas e trigonométricas
- Interpolação numérica
- Predição de sequências polinomiais
- Educação sobre história da computação

## 🏛️ História

Charles Babbage (1791-1871) projetou a Máquina de Diferenças para automatizar cálculos matemáticos que anteriormente eram feitos manualmente. Embora nunca tenha sido completamente construída em sua época devido às limitações tecnológicas, o conceito foi revolucionário e é considerado um precursor dos computadores modernos.

## 📝 Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

## 👨‍💻 Autor

Desenvolvido por [Weslem Cristiano](https://github.com/WeslemCristiano)

---

*"A Máquina Analítica não tem pretensões de originar qualquer coisa. Ela pode fazer tudo o que sabemos como ordenar que ela execute."* - Ada Lovelace