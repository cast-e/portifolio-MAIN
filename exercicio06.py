A = {10, 20, 30}

num = int(input('Digite um número: '))

if num in A:
    print(f'O número {num} pertence ao conjunto A!')
else:
    print(f'O número {num} não pertence ao conjunto A!')

A = {1, 2, 3, 4}
B = {4, 5, 6, 7}

print(f'União: { A | B }')
print(f'Interseção: { A & B }')
print(f'A está contido em B? { A.issubset(B) }')
print(f'B está contido em A? { B.issubset(A) }')
