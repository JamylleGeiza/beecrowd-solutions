N = int(input())
hora, minuto, segundo = 3600, 60, 1
print(f"{N // hora}:{(N % hora) // minuto}:{(N % hora) % minuto}")