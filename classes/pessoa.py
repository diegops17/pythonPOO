from datetime import date
class Pessoa:
    def __init__(self, nome = '', altura = '', cpf = '', dataNascimento = '', sexo = '', estudante = ''):
        self.nome = nome
        self.altura = altura
        self.cpf = cpf
        self.dataNascimento = dataNascimento
        self.sexo = sexo
        self.estudante = estudante
        self.idade = 0

    def validarGenero(self, sexo):
        self.sexo = sexo.upper()

        if self.sexo == 'M':
            print('Marmanjo')
        elif self.sexo == 'F':
            print('Princesa')
        else:
            print('Não se aplica')

    def __str__(self):
        return f'{self.nome} é estudante? {self.estudante}'

    def verificarIdade(self, dataNascimento):
        anoNascimento = int(self.dataNascimento[6:10])
        self.idade = date.today().year - anoNascimento
        return self.idade
        
    def verificarMaiorIdade(self, idade):
        if self.idade >= 18:
            m = 'Maior de idade'
        else:
            m = 'Menor de idade'
        return m
#p1 = Pessoa('João', 1.65, '12345678900','01/11/1980','M',True)
#print(f'NOME: {p1.nome}\nCPF: {p1.cpf}\nDATA NASCIMENTO: {p1.dataNascimento}', end='')
#print(f'\nSEXO: {p1.sexo}\nESTUDANTE: {p1.estudante}')
#p1.validarGenero('f')

#p2 = Pessoa('João', 1.65, '12345678900','01/11/2018','M',True)
#idade = p2.verificarIdade('01/11/1988')
#idade = p2.verificarIdade(p2.dataNascimento)
#print(f'{p2.nome} tem {idade} anos, {p2.verificarMaiorIdade(idade)}')

#p3 = Pessoa('Creuza', 1.65, '12345678900','01/11/1980','M',True)
#print(p3)

class Estudante(Pessoa):
    def __init__(self, nome, altura, cpf, dataNascimento, sexo, estudante, matricula):
        super().__init__(nome, altura, cpf, dataNascimento, sexo, estudante)
        self.matricula = matricula
    
       
e = Estudante('Junior', 1.75, '12345678900','01/11/1999','M', False, '00000')
print(e.validarGenero('M'))
print(f"{e.verificarIdade('04/03/2000')} anos")
print(e)
