# |-------------- Numeração automática --------------| #

proximo_numero = 1
class aluno:
    def __init__(self, nome, sobrenome, numero, nota):
        self.nome = nome
        self.numero=numero
        self.sobrenome= sobrenome
        self.nota=nota

# |-------------- Função exibir dados --------------| #

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Sobrenome: {self.sobrenome}")
        print(f"Numero de aluno: {self.numero}")
        print(f"Nota: {self.nota}")
        print("-" * 20)

estudantes = {}

# |-------------- Função de cadastra aluno --------------| #

def cadastrar_estudante():
    global proximo_numero 
    nome = input("Digite o nome: ").capitalize()
    sobrenome = input("Digite o sobrenome: ").capitalize()   
    numero_atribuido = proximo_numero
    estudante = aluno(nome, sobrenome, numero_atribuido, nota=0)
    estudantes[numero_atribuido] = estudante
    proximo_numero += 1 

    print(f"Estudante cadastrado com sucesso! Número atribuído: {numero_atribuido}\n")

# |-------------- Função de mudar nome no estudante --------------| #

def mudar_nome():
    while True:
        alvo = int(input("Digite o número do estudante para mudar o nome: "))
        encontrado = None
        for estudante in estudantes.values():
            if estudante.numero == alvo:
                encontrado = estudante
                break
    
        if encontrado:
            novo_nome = input(f"Insira o novo nome para {encontrado.nome}: ")
            encontrado.nome = novo_nome
            print("Nome alterado com sucesso!\n")
            break
        else:
            print("Estudante com esse número não encontrado, tente de novo.\n")

# |-------------- Função de mudar sobrenome --------------| #

def mudar_sobrenome():
    while True:
        alvo = int(input("Digite o número do estudante para mudar o sobrenome: "))
        encontrado = None
        for estudante in estudantes.values():
            if estudante.numero == alvo:
                encontrado = estudante
                break
        if encontrado:
            novo_sobrenome = input(f"Insira o novo sobrenome para {encontrado.nome} {encontrado.sobrenome}: ")
            encontrado.sobrenome = novo_sobrenome
            print("sobrenome alterado com sucesso!\n")
            break
        else:
            print("Estudante com esse número não encontrado, tente de novo.\n")

# |-------------- Função de adicionar nota --------------| #

def adicionar_nota():
   while True:
        alvo = int(input("Digite o número do estudante para adicionar a nota: "))
        encontrado = None
        for estudante in estudantes.values():
            if estudante.numero == alvo:
                encontrado = estudante
                break
        if encontrado:
            nota = float(input(f"Insira a nota para {encontrado.nome} (0-20): "))
            if 0 <= nota <= 20:
                encontrado.nota = nota
                print("Nota adicionada com sucesso!\n")
                break
            else:
                print("Nota inválida! Deve ser entre 0 e 20.\n")
        else:
            print("Estudante com esse número não encontrado.\n")

# |-------------- Função de mostrar estudantes  --------------| #

def exibir_estudantes():
    if not estudantes:
        print("Nenhum estudante cadastrado.\n")
        return
    print("\nLista de Estudantes:")
    for estudante in estudantes.values():
        estudante.exibir_dados()

# |-------------- Função de pesquisar estudantes --------------| #

def pesquisar_estudante():
    alvo = int(input("Digite o numero de estudante para buscar: "))
    encontrado = False
    for estudante in estudantes.values():
        if estudante.numero == alvo:
            print("\nEstudante encontrado:")
            estudante.exibir_dados()
            encontrado = True
            break
    if not encontrado:
        print("Estudante com esse número não encontrado.\n")

# |-------------- Função de remover estudantes --------------| #

def remover_estudante():
    alvo = int(input("Digite o numero para remover: "))
    
    if alvo in estudantes:
        del estudantes[alvo]
        print("Estudante removido com sucesso!\n")
    else:
        print("Estudante não encontrado.\n")

# |-------------- Interface Visual --------------| #

while True:
    print("1 - Cadastrar estudante")
    print("2 - Exibir estudantes")
    print("3 - Pesquisar estudante")
    print("4 - Remover estudante")
    print("5 - Adicionar nota")
    print("6 - Mudar nome")
    print("7 - Mudar sobrenome")
    print("8 - Sair")
    opcao = input("Escolha uma opção: ")

# |-------------- Menu --------------| #

    if opcao == "1":
        cadastrar_estudante()
    elif opcao == "2":
        exibir_estudantes()
    elif opcao == "3":
        pesquisar_estudante()
    elif opcao == "4":
        remover_estudante()
    elif opcao=="5":
        adicionar_nota()
    elif opcao=="6":
        mudar_nome()
    elif opcao=="7":
        mudar_sobrenome()
    elif opcao == "8":
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida!\n")