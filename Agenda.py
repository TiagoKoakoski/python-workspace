# Tiago Koakoski Bianco de Souza - 03/03/2022

def imprimeMenu():
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("1.	Cadastrar Pessoa na Agenda \n2.	Alterar dados da Pessoa\n3.	Listar Agenda\n4.	Procurar pessoa na Agenda\n5.	Excluir Pessoa da Agenda\n6.	Sair do sistema")

def cadastrarPessoa():
    pessoa = {
        'nome' : "",
        'telefone' : "",
        'cidade' : "",
        'estado' : "",
        'status' : ""
    }
    pessoa['nome'] = str(input("Digite o nome: "))
    pessoa['telefone'] = str(input("Digite o telefone: "))
    pessoa['cidade'] = str(input("Digite a cidade: "))
    pessoa['estado'] = str(input("Digite o estado: "))
    pessoa['status'] = str(input("Digite o (P-> Pessoal) ou (C-> Comercial): "))
    agenda.append(pessoa)

def buscarPessoa(nome):
    posicao = -1
    for i in range(len(agenda)):
        if nome == agenda[i]['nome']:
            posicao = i
    if posicao == -1:
        print("Pessoa com o nome ", nome, " não encontrada")
    return posicao
    

def alteraPessoa(posicao):
    print("Nome cadastrado: ", agenda[posicao]['nome'])
    agenda[posicao]['nome'] = str(input("Novo nome: "))
    print("Telefone cadastrado: ", agenda[posicao]['telefone'])
    agenda[posicao]['telefone'] = str(input("Novo telefone: "))
    print("Cidade cadastrada: ", agenda[posicao]['cidade'])
    agenda[posicao]['cidade'] = str(input("Nova cidade: "))
    print("Estado cadastrado: ", agenda[posicao]['estado'])
    agenda[posicao]['estado'] = str(input("Novo estado: "))
    print("Status cadastrado: ", agenda[posicao]['status'])
    agenda[posicao]['status'] = str(input("Novo status(P-> Pessoal) ou (C-> Comercial):  "))


def listarAgenda():
    if len(agenda) == 0:
        print("Agenda sem cadastros")
    else:
        for i in range(len(agenda)):
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
            print("Contato ", i+1, " Status: ", agenda[i]['status'], " - ", agenda[i]['nome'], "  - Tel: ", agenda[i]['telefone'], " - Cidade/Estado: ", agenda[i]['cidade'], "/", agenda[i]['estado'] )

def mostrarPessoa(posicao):
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("Contato ", posicao+1)
    print("Nome: ", agenda[posicao]['nome'])
    print("Telefone: ", agenda[posicao]['telefone'])
    print("Cidade: ", agenda[posicao]['cidade'])
    print("Estado: ", agenda[posicao]['estado'])
    print("Status: ", agenda[posicao]['status'])

menu = 0
agenda = []
while not menu == 6:
    imprimeMenu()
    menu = int(input("Digite a opção desejada: "))

    if menu > 6 or menu < 1:
        print("Erro: opção inválida!")
    else:
        if menu == 1:
            cadastrarPessoa()

        if menu == 2:
            pessoa = str(input("Quem deseja alterar? "))
            posicao = buscarPessoa(pessoa)
            if not posicao == -1:
                alteraPessoa(posicao)

        if menu == 3:
            listarAgenda()

        if menu == 4:
            pessoa = str(input("Quem deseja buscar? "))
            posicao = buscarPessoa(pessoa)
            mostrarPessoa(posicao)

        if menu == 5:
            pessoa = str(input("Quem deseja deletar? "))
            posicao = buscarPessoa(pessoa)
            if not posicao == -1:
                agenda.pop(posicao)
                print("Cadastro excluído")