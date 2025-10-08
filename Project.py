# Listas
doadores = []
doacoes = []
voluntarios = []

def exibir_menu():
    print("""
===== TURMA DO BEM =====
1. Cadastrar doador
2. Registrar doação
3. Cadastrar voluntário
4. Relatório
5. Sair
""")

def cadastrar_doador():
    nome = str(input("Nome do doador: "))
    email = input("Email do doador: ")
    contato = int(input("Contato do doador: "))
    doadores.append({"nome": nome, "email": email, "contato": contato})
    print(f"\n Doador {nome} cadastrado com sucesso!\n")

def registrar_doacao():
    nome = input("Nome do doador: ")
    valor = input("Valor da doação: R$ ")
    doacoes.append({"nome": nome, "valor": valor})
    print(f"\n Doação de R${valor} registrada para {nome}.\n")

def cadastrar_voluntario():
    nome = input("Nome do voluntário: ")
    area = input("Área de atuação (ex: dentista, psicólogo, apoio): ")
    voluntarios.append({"nome": nome, "area": area})
    print(f"\n Voluntário {nome} cadastrado na área de {area}.\n")

def listar_cadastros():
    print("===== LISTA DE CADASTROS =====")
    print("Doadores:")
    for d in doadores:
        print(f"- {d['nome']} ({d['email']})")
    print("Doações:")
    for d in doacoes:
        print(f"- {d['nome']} → R$ {d['valor']}")
    print("Voluntários:")
    for v in voluntarios:
        print(f"- {v['nome']} ({v['area']})")
    print()

# Menu
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_doador()
    elif opcao == "2":
        registrar_doacao()
    elif opcao == "3":
        cadastrar_voluntario()
    elif opcao == "4":
        listar_cadastros()
    elif opcao == "5":
        print("Obrigado por fazer parte dessa causa!")
        break
    else:
        print("Opção inválida! Escolha um número de 1 a 5.")
