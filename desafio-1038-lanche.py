codigo, quantidade = map(int, input().split())
especificacao = ['cachorro-quente','x-salada','x-bacon','torrada simples','refrigerante']
pedido = especificacao[codigo - 1]
precos = [4.00, 4.50, 5.00, 2.00, 1.50]
valor = precos[codigo - 1] * quantidade
print(f'Total: R$ {valor:.2f}')

  