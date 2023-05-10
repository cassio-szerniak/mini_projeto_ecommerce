# Projeto de E-commerce

estoque = {}  #Armazenar dados do meu sistema

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

# print ( codigo, "\n", categoria, "\n", nome, "\n", descricao, "\n", preco)

print("\n \n------------------------------------")
print("-------INFORMAÇÕES DO PRODUTO-------")
print("------------------------------------")
print(f"Código: {codigo}")
print(f"Categoria: {categoria}")
print(f"Nome: {nome}")
print(f"Descrição: {descricao}")
print(f"Preço: {preco}")
