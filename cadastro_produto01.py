# Projeto de E-commerce ↓

estoque = {}  #Armazenar dados do meu sistema
quantidade_a_cadastrar = int(input("Digite a quantidade de produtos a serem cadastrados: "))

for i in range(quantidade_a_cadastrar):
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

print(estoque)

# print ( codigo, "\n", categoria, "\n", nome, "\n", descricao, "\n", preco)

# print("\n \n------------------------------------")
# print("-------INFORMAÇÕES DO PRODUTO-------")
# print("------------------------------------")
# print(f"Código: {codigo}")
# print(f"Categoria: {categoria}")
# print(f"Nome: {nome}")
# print(f"Descrição: {descricao}")
# print(f"Preço: {preco}")


# EXIBINDO SOMENTE AS CHAVES DO DICIONARIO COM METODO .keys() ↓

# estoque = {'Livros': [
#             {'codigo': 12, 'produto': 'Harry Potter', 'info': 'lalala', 'preco': 45.89}], 
#            'Eletronicos': [
#             {'codigo': 23, 'produto': 'Smartphone', 'info': 'lalala', 'preco': 999.1}]}
# print(estoque.keys())
# fim


# EXIBINDO SOMENTE OS VALORES/INFORMAÇÕES DENTRO DE CADA CATEGORIA DO DICIONARIO COM METODO .values() ↓

# estoque = {'Livros': [
#             {'codigo': 12, 'produto': 'Harry Potter', 'info': 'lalala', 'preco': 45.89}], 
#            'Eletronicos': [
#             {'codigo': 23, 'produto': 'Smartphone', 'info': 'lalala', 'preco': 999.1}]}
# print(estoque.values())
# fim

# EXIBINDO CADA CATEGORIA E OS PRODUTOS DENTRO DELA ↓

estoque = {'Livros': [{'codigo': 12, 'produto': 'Harry Potter', 'info': 'lalala', 'preco': 45.89}], 
           'Eletronicos': [
            {'codigo': 23, 'produto': 'Smartphone', 'info': 'lalala', 'preco': 999.1}]}

# print("\n \n------------------------------------")
# print("-------INFORMAÇÕES DO PRODUTO-------")
# print("------------------------------------")

# for categoria in estoque:
#     for produto in estoque[categoria]:
#         print(f"PRODUTO: {produto['produto']}")
#         print(f"Código: {produto['codigo']}")
#         print(f"Categoria: {categoria}")
#         print(f"Nome: {produto['produto']}")
#         print(f"Descrição: {produto['info']}")
#         print(f"Preço: {produto['preco']}")
#         print("")
# fim
