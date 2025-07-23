print("ENUNCIADO: Biblioteca Digital da Escola")

print("A equipe de tecnologia da escola está organizando uma biblioteca digital. Foram levantados os seguintes dados:")

print(" Os alunos que baixaram livros de matemática:")

matematica = {"João", "Maria", "Lucas", "Ana"}
print(matematica)

print(" Os alunos que baixaram livros de programação:")

programacao = {"Lucas", "Ana", "Felipe", "Carla"}
print(programacao)

print("Com base nesses dados, crie um programa em Python que responda:")

print("   1. Quais alunos baixaram livros de ambas as disciplinas?")

print( matematica & programacao )

print("   2. Quais alunos baixaram apenas livros de Matemática?")

print( matematica - programacao )

print("   3. Quais alunos baixaram pelo menos um dos dois tipos de livros?")

print( matematica | programacao )

print("   4. Há algum aluno que baixou todos os livros de Matemática e também todos os de Programação? (Ou seja, um subconjunto completo)")

if matematica.issubset(programacao):
    print("Verdadeiro!")
else:
    print("Falso!")
