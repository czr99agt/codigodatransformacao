print("Bem-vindo ao sistema de cadastro de alunos!")
nome_usuario = input("Digite seu nome: ")
print(f"Olá, {nome_usuario}! Vamos começar.\n")

# Módulo 4: Estruturas de dados
alunos = []

# Módulo 3: Estrutura de repetição
while True:
    nome = input("Nome do aluno: ")
    idade = int(input("Idade: "))
    nota = float(input("Nota (0 a 10): "))

    aluno = {
        "nome": nome,
        "idade": idade,
        "nota": nota
    }

    alunos.append(aluno)

    continuar = input("Deseja cadastrar outro aluno? (s/n): ").lower()
    if  continuar!= 's':
        break
