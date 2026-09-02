A, B, C = map(float, input().split())
delta = (B**2) - 4 * A * C
if A != 0 and delta >= 0:
    x = delta ** 0.5
    R1 = ((- B) + x) / (2 * A)  
    R2 = ((- B) - x) /(2 * A)   
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")
else:
    print("Impossivel calcular")