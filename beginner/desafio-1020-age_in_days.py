idade = int(input())
ano, mes, dia = 365, 30, 1
print(f"{idade // ano} ano(s)")
print(f"{(idade % ano) // mes} mes(es)")
print(f"{(idade % ano) % mes} dia(s)")