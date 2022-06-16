itens = [
    {
        'cod':1,
        'produto':'REFRIGERANTE DE COLA',
        'preco': 7
    },
    {
        'cod':2,
        'produto':'BATATA FRITA',
        'preco': 10 
    },
    {
        'cod':3,
        'produto':'BARRA DE CEREAL',
        'preco': 3 
    },
     {
        'cod':4,
        'produto':'ÁGUA SEM GÁS',
        'preco': 3
    },
     {
        'cod':5,
        'produto':'ÁGUA COM GÁS',
        'preco': 3
    },
     {
        'cod':6,
        'produto':'ACHOCOLATADO',
        'preco': 8
    },
     {
        'cod':7,
        'produto':'BALA DE MENTA',
        'preco': 2 
    },
]

sair= False
item = ''

while sair == False:
    print("***************************MÁQUINA DE PRODUTOS***************************")
    for i in itens:
        print(f"Dados Produto: {i['produto']} - preco: {i['preco']} REAIS - cod: {i['cod']}")

    consulta = int(input("Digite o código do produto que você deseja comprar: "))
    for i in itens:
        if consulta == i['cod']:
            item = i
    if item == '':
        print('CODIGO INVÁLIDO')
    else:
        print(f"Obrigado por escolher: {item['produto']}! Este produto vai te custar: {item['preco']} REAIS")

        valor = int(input(f"Insira {item['preco']} reais para comprar: "))
        if valor == item['preco']:
            print(f"Pagamento Confirmado!, aqui está seu produto: {item['produto']}!")
        else:
            print(f"Insira apenas o valor de: {item['preco']} reais")

    consulta = input("Para continuar comprando digite c, para sair digite qualquer tecla! ")
    if consulta == 'c':
        sair = False
    else:
        sair = True
    print('')