import json

# aplicando os conceitos de POO para gerenciar alunos
class Aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula

    def to_dict(self):
        
        return {
            "nome": self.nome,
            "idade": self.idade,
            "matricula": self.matricula,
        }


class SistemaAlunos:
    def __init__(self, arquivo='alunos.json'):
        self.arquivo = arquivo
        self.alunos = self.carregar_alunos()

    def carregar_alunos(self):
        
        try:
            with open(self.arquivo, 'r') as f:
                return [Aluno(**dados) for dados in json.load(f)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def salvar_alunos(self):
        
        with open(self.arquivo, 'w') as f:
            json.dump([aluno.to_dict() for aluno in self.alunos], f, indent=4)

    def adicionar_aluno(self, nome, idade, matricula):
        
        self.alunos.append(Aluno(nome, idade, matricula))
        self.salvar_alunos()

    def remover_aluno(self, matricula):
        
        self.alunos = [aluno for aluno in self.alunos if aluno.matricula != matricula]
        self.salvar_alunos()

    def listar_alunos(self):
        return [aluno.to_dict() for aluno in self.alunos]


def menu():
    sistema = SistemaAlunos()

    while True:
        print("\nSistema de Gerenciamento de Alunos")
        print("1. Coordenador (Adicionar/Remover Alunos)")
        print("2. Público Geral (Visualizar Alunos)")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            senha = input("Digite a senha do coordenador: ")
            if senha == "coordenador123":  # Senha fixa
                while True:
                    print("\n-- Modo Coordenador --")
                    print("1. Adicionar Aluno")
                    print("2. Remover Aluno")
                    print("3. Voltar")

                    opcao = input("Escolha uma opção: ")
                    if opcao == '1':
                        nome = input("Nome do aluno: ")
                        idade = int(input("Idade do aluno: "))
                        matricula = input("Número de matrícula: ")
                        sistema.adicionar_aluno(nome, idade, matricula)
                        print("Aluno adicionado com sucesso!")
                    elif opcao == '2':
                        matricula = input("Digite a matrícula do aluno a ser removido: ")
                        sistema.remover_aluno(matricula)
                        print("Aluno removido com sucesso!")
                    elif opcao == '3':
                        break
                    else:
                        print("Opção inválida!")
            else:
                print("Senha incorreta!")

        elif escolha == '2':
            print("\n-- Lista de Alunos --")
            for aluno in sistema.listar_alunos():
                print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Matrícula: {aluno['matricula']}")

        elif escolha == '3':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")



menu()
