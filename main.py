class Aluno:
    def __init__(self, nome, matricula) -> None:
        self.nome = nome
        self.matricula = matricula

    def __eq__(self, outro_aluno) -> bool:
        return self.matricula == outro_aluno.matricula

mateus = Aluno('Mateus', '12345')
mateusPereira = Aluno('Mateus Pereira', '12345')

print("São iguais: ", mateus == mateusPereira)