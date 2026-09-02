#O comando .split() corta o texto toda vez que encontra um espaço.
produto1 = input().split()
produto2 = input().split()

codigo1, qtde1, valor1 = int(produto1[0]), int(produto1[1]), float(produto1[2])
codigo2, qtde2, valor2 = int(produto2[0]), int(produto2[1]), float(produto2[2])

pagar = (qtde1 * valor1) + (qtde2 * valor2)
print(f'VALOR A PAGAR: R$ {pagar:.2f}')