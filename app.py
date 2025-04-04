print('Olá mundo')
print('Vai corinthians')
caixa= 'yuri alberto'
print(caixa)

#nome= 'cezar'
idade= 25
altura= 1.81
estudante= True
#print(nome, idade, altura, estudante)

mensagem= '51 é pinga'
print(mensagem.upper())
print(mensagem.lower())
print(mensagem.strip())

#nome = input('Escreva seu nome: ')
#print(f'Olá {nome}, seja muito bem vindo ao codigo da transformação')
from datetime import datetime
nome= input('Escreva seu nome: ')
agora= datetime.now()
hora_atual= agora.strftime('%H:%M')
print(f'Olá {nome}, agora são {hora_atual}')