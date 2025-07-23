def bool_to_str_pt(a):
    if a:
        return "Verdadeiro"
    else:
        return "Falso"

#1.
print("1. ---\n")

A = {110, 20, 32, 45, 50}
print(f'A: {A}')

B = {101, 22, 33, 45, 50}
print(f'B: {B}')

print(f'- A é subconjunto de B? {bool_to_str_pt(A.issubset(B))}')
print(f'- B é subconjunto de A? {bool_to_str_pt(B.issubset(A))}')

# --------------------------//----------------------------

#2.
print("\n2. ---\n")

C = {11, 43, 55, 67}
print(f'C: {C}')

D = {12, 43, 45, 8, 11, 67}
print(f'D: {D}')

print(f'- C união com D: {C | D}')
print(f'- C intersecção com D: {C & D}')

# --------------------------//----------------------------

#3.
print("\n3. ---\n")

E = {"maça", "banana", "laranja"}
print(f'E: {E}')

F = {"banana", "uva", "kiwi"}
print(f'F: {F}')

print(f'- E diferença com F: {E - F}')
print(f'- F diferença com E: {F - E}')

# --------------------------//----------------------------

#4.
print("\n4. ---\n")

Python = {"Alice", "Bob", "Charlie", "David", "Eve", "Frank"}
print(f'Oficina de Python: {Python}')

Java = {"Alice", "George", "Hannah", "Ivy", "Jack"}
print(f'Oficina de Java: {Java}')

Javascript = {"Charlie", "David", "Eve", "Jack", "Liam"}
print(f'Oficina de Javascript: {Javascript}')

print(f'- a) Quais são os participantes que estão APENAS na oficina de Python: {Python - (Java | Javascript)}')
print(f'- b) Quais são os participantes que estão em todas as oficinas: {Python & Java & Javascript}')
print(f'- c) Quais são os participantes que estão em pelo menos uma das oficinas: {Python | Java | Javascript}')
print(f'- d) Quais são os participantes que estão APENAS na oficina de Javascript: {Javascript - (Python | Java)}')
print(f'- e) Quais são os participantes que estão APENAS na oficina de Javas ou Python mas NÃO em ambas: {(Python | Java) - (Python & Java)}')

