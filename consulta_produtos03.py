# Projeto de E-commerce ↓
# Criando MENU de interação

# funções são criadas pelo metodo def ↓

def cadastrar_produto(estoque):
    codigo = int(input("Digite o codigo do produto: "))
    categoria = (input("Digite o categoria do produto: "))
    nome = (input("Digite o nome do produto: "))
    descricao = (input("Digite o descrição do produto: "))
    preco = float((input("Digite o preço do produto: ")))

    # Aqui "produto" será uma estrutura conhecida como "dicionário" no python
    produto = {"codigo": codigo, "produto": nome, "info": descricao, "preco": preco}

    # Aqui uma condição para verificar se a categoria já existe dento do dicionário
    if categoria not in estoque:
        estoque[categoria] = [] # cria a categoria dentro de estoque
        estoque[categoria].append(produto)  # o metodo append vai adicionar os novos valores dentro de estoque
    else: # senão, caso a categoria já exista, apenas obtem os valores
        estoque[categoria].append(produto)
    return estoque

# criando função para exibir dados na tela ↓

def mostrar_produto(estoque):
    print("\n \n------------------------------------")
    print("-------INFORMAÇÕES DO PRODUTO-------")
    print("------------------------------------")

    for categoria in estoque:
        for produto in estoque[categoria]:
            print(f"PRODUTO: {produto['produto']}")
            print(f"Código: {produto['codigo']}")
            print(f"Categoria: {categoria}")
            print(f"Nome: {produto['produto']}")
            print(f"Descrição: {produto['info']}")
            print(f"Preço: {produto['preco']}")
            print("")


#estoque = {}  #Armazenar dados do meu sistema
#estoque = {'Livros': [{'codigo': 12, 'produto': 'Harry Potter', 'info': 'lalala', 'preco': 45.89}], 'Eletronicos': [{'codigo': 23, 'produto': 'Smartphone', 'info': 'lalala', 'preco': 999.1}]}

# Dados brutos para não precisar digitar:
estoque = { "Eletronicos": [{
                               'codigo': 2578,
                               'produto': "Televisão Smart 70'",
                               'info': 'Televisão smart de 70 polegadas, para você assistir a filmes e séries com mais emoção!',
                               'preco': 4799.99 },
                               
                            {
                               'codigo': 2749,
                               'produto': 'Iphone 14 Pro Max 256G',
                               'info': 'Iphone 14 Pro Max 256GB de armazenamento interno, acompanha carregador e capinha.',
                               'preco': 9499.99},
                            
                            {
                               'codigo': 1478,
                               'produto': 'Smartphone Samsung Glaxy S23 Ultra',
                               'info': 'Smartphone Samsung Glaxy S23 Ultra 512GB de armazenamento interno, 16GB de memória RAM.',
                               'preco': 6799.99},

                            {
                               'codigo': 3658,
                               'produto': 'Notebook Dell Inspration',
                               'info': 'Notebook Dell Inspration: 32GB de RAM, 1TB SSD, 4GB Placa de Vídeo dedicada, processador intel core i9.',
                               'preco': 6799.99},
                            ],
            
             "Livros": [{
                            'codigo': 6987,
                            'produto': 'Livro O Senhor dos Anéis (Volume único)',
                            'info': 'Livro da obra literária "O Senhor dos Anéis", de J.R.R.Tolkien. Aproveite esta oferta!',
                            'preco': 129.90}
                        ]
            }

# estrutura para não fechar o menu enquanto o usuario não escolher a opção 3 - SAIR ↓ 
while True:

    opcao = int(input("O que você deseja fazer? \n\n 1- CADASTRO \n 2- MOSTRAR PRODUTOS \n 3- SAIR DO SISTEMA \n"))

    if opcao == 1:
        cadastrar_produto(estoque)
    elif opcao == 2:
        mostrar_produto(estoque)
    elif opcao == 3:
        print("Programa encerrado")
        break
    else:
        print("Opção inválida")

