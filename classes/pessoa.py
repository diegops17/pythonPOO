class Pessoa:
    def __init__(self, nome, altura, cpf, dataNascimento, sexo, estudante):
        self.nome = nome
        self.altura = altura
        self.cpf = cpf
        self.dataNascimento = dataNascimento
        self.sexo = sexo
        self.estudante = estudante

    def validarGenero(self, sexo):
        self.sexo = sexo.upper()

        if self.sexo == 'M':
            print('Marmanjo')
        elif self.sexo == 'F':
            print('Princesa')
        else:
            print('Não se aplica')

p1 = Pessoa('João', 1.65, '12345678900','01/11/1980','M',True)
print(f'NOME: {p1.nome}\nCPF: {p1.cpf}\nDATA NASCIMENTO: {p1.dataNascimento}', end='')
print(f'\nSEXO: {p1.sexo}\nESTUDANTE: {p1.estudante}')
p1.validarGenero('f')