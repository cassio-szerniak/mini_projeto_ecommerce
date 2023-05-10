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


estoque = {}  #Armazenar dados do meu sistema
#estoque = {'Livros': [{'codigo': 12, 'produto': 'Harry Potter', 'info': 'lalala', 'preco': 45.89}], 'Eletronicos': [{'codigo': 23, 'produto': 'Smartphone', 'info': 'lalala', 'preco': 999.1}]}

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

