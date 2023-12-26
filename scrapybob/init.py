from scrapybob import fundos

print('''
Seja bem vindo ao analisador de fundos imobiliarios !!! 

Para encerrar o programa digite EXIT a qualquer momento.

Vamos começar.

''')

fundo = input('Digite o nome do fundo imobiliario que deseja analisar: ')
while True:
    fundo = fundo.lower()
    try:
        fundos.getPoints(fundo)
    except:
        print('\n')
        print('Fundo nao encontrado')

    print('\n')
    fundo = input('Bora pro proximo fundo: ')
    if(fundo == 'EXIT' or fundo == 'exit'):
        break