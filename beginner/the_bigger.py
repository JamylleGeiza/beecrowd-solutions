A, B, C = map(int, input().split())
maiorAB = (A + B + abs(A - B)) / 2
maiorABC = (maiorAB + C + abs(maiorAB - C)) / 2
print (f'{int(maiorABC)} eh o maior ')