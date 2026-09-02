N1, N2, N3, N4 = map(float, input().split())
MEDIA = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10
print(f'Media: {MEDIA:.1f}')
if MEDIA >= 7.0:
    print('Aluno aprovado.')
elif MEDIA <= 6.9 and MEDIA >= 5.0:
    print('Aluno em exame.')
    N5 = float(input())
    print(f'Nota do exame: {N5:.1f}')
    MEDIA = (MEDIA + N5) / 2
    if MEDIA >= 5.0:
        print('Aluno aprovado.')
        print(f'Media final: {MEDIA:.1f}')
    else:
        print('Aluno reprovado.')
        print(f'Media final: {MEDIA:.1f}')
else:
    print('Aluno reprovado.')