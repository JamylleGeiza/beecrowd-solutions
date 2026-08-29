# O map pega uma ação (uma função) e aplicá-la em todos os itens de um grupo
# área do trapézio ((base maior + base menor) × altura) / 2
A, B, C = map(float, input().split())

areaTriangulo = (A * C) / 2
areaCirculo = 3.14159 * (C ** 2)
areaTrapezio = ((A + B) * C) / 2
areaQuadrado = B ** 2
areaRetangulo = A * B

print(f'''TRIANGULO: {areaTriangulo:.3f}
CIRCULO: {areaCirculo:.3f}
TRAPEZIO: {areaTrapezio:.3f}
QUADRADO: {areaQuadrado:.3f}
RETANGULO: {areaRetangulo:.3f}''')