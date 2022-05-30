from random import choice

#solução random.choice - Retorna um elemento aleatório da sequência não vazia

primeiro = input("Primeiro aluno: ")
segundo = input("Segundo aluno: ")
terceiro = input("Terceiro aluno: ")
quarto = input("Quarto aluno: ")
lista_alunos = [primeiro, segundo, terceiro, quarto]
print(lista_alunos)
print(f"O aluno escolhido foi {choice(lista_alunos)}")
