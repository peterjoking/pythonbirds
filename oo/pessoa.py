class Pessoa:
    def __init__(self, nombre=None, idade=42):
        self.idade = idade
        self.nombre = nombre
    def cumprimentar(self):
        return f'Hola {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Carlitos')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nombre)
    p.nombre = 'Pedro'
    print(p.nombre)


