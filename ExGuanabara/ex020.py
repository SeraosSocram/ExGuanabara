from random import shuffle

# solução com random.shuffle - Embaralha a sequência internamente.

primeiro = input("Primeiro aluno: ")
segundo = input("Segundo aluno: ")
terceiro = input("Terceiro aluno: ")
quarto = input("Quarto aluno: ")
lista_alunos = [primeiro, segundo, terceiro, quarto]
shuffle(lista_alunos)
print(f"A ordem de apresentação será")
print(lista_alunos)
