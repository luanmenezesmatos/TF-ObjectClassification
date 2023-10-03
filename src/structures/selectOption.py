# Função para fazer a pergunta e mostrar as opções; inserir os parâmetros para no arquivo main.py utilizar o match case e retornar o valor da opção escolhida

class selectOption:
    def __init__(self, question, options):
        self.question = question
        self.options = options

    def show(self):
        print(self.question)
        for i in range(len(self.options)):
            print(f"{i+1} - {self.options[i]}")
        print()

    def choose(self):
        self.show()
        return int(input("Escolha uma opção: "))