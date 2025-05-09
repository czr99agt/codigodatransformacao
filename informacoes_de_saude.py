#inserindo o nome do usuario
print("Bem-vindo ao sistema de avaliação de saúde!")
nome = input("Insira seu nome: ")
print(f'Olá, {nome}! vamos começar')
#lista onde vão ficar os dados 
info = []
#Estrutura de repetição
while True:
    nome = input("Digite seu nome: ")
    idade = int(input('Digite sua idade: '))
    peso = float(input('Digite seu peso: '))
    altura = float(input('Digite sua altura: '))

    paciente = {
        "nome": nome,
        "idade": idade,
        "peso": peso,
        "altura": altura
  }
    
    info.append(paciente)

    continuar = input('Deseja cadastrar mais algum paciente? (s/n): ').lower()
    if continuar != "s":
        break

imc = peso / (altura ** 2)

if idade < 18:
    categoria_idade = "jovem"
elif idade < 60:
    categoria_idade = "adulto"
else
    cat

    