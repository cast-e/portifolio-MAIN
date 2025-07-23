#solução 1
#alunos = 10 ["aluno1", "aluno2", "aluno3", "aluno5"]
#professor = 0
#for anotacao in alunos:
#    professor += 1
#print(f'Total de alunos:{professor}')
#solução 2
#filas = [
#    ["aluno1", "aluno2", "aluno3"],
#    ["aluno4", "aluno5"], 
#    ["aluno6", "aluno7", "aluno8", "aluno9"]  
#]
#contagem  = 0
#for alunas in filas:
#    contagem += len(alunas)
#print(f'O total de alunas é: {contagem}')

#solução 3
#carteiras = int(input('Qual o número total de carteiras?'))
#carteiras_vazias = int(input('informe o número de carteiras vazias?'))
#alunos_presentes = carteiras - carteiras_vazias
#print(f'O número de alunos presentes na solução 3 é: {alunos_presentes}')
#solução4:
n=21
total = 0
for presente in range(0,n,2):
    if presente + 1 < n:
        total +=2 #adiciona 2 alunos na soma
    else:
        total += 1 #adiciona o ultimo na soma
print(f' Total de alunos na solução 4 é {total}')