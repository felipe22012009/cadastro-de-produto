def formatar_nome(nome):
    return nome.strip().title()

def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite p preço do produto: "))
    categoria = input("Digite a categoria do produto: ")
    return (formatar_nome(nome), preco, categoria)

def salvar_produto(produto):
    with open("produtos.txt", "a", encoding="utf-8") as arquivo:
        linha = f"{produto[0]};{produto[1]};{produto[2]}\n"
        arquivo.write(linha)

def listar_produtos():
    try:
        with open("produtos,txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome, preco, categoria = linha.strip().strip(";")
                print(f"Produto: {nome} | Preço: r${preco} | Categoria: {categoria}")
    except FileNotFoundError:
        print("Nenhum produto cadastrado ainda.") 

while True:
    print("\n1 - cadastror produto")
    print("2 - listar produtros")
    print("0 -  Sair")
    opcao = input("Escolha: ")
    
    if opcao == "1":
        produto = cadastro_produto()