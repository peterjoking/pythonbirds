class Pessoa:
    def __init__(self, *filhos, nombre=None, idade=42):
        self.idade = idade
        self.nombre = nombre
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Hola {id(self)}'

if __name__ == '__main__':
    Pedro = Pessoa(nombre="Carlitos")
    Lucas = Pessoa(nombre="Roberto", idade=55)
    Melisa = Pessoa(Pedro, nombre="Melisa")
    Melisa = Pessoa(Lucas, nombre="Melisa")
    print(Pessoa.cumprimentar(Pedro))
    print(id(Pedro))
    print(Pedro.cumprimentar())
    print(Melisa.nombre)
    print(Melisa.idade)
    for filho in Melisa.filhos:
        print(filho.nombre)

    print(Pedro.idade)
    print(Pedro.filhos)
    print(Pedro.nombre)
    Pedro.Apellido = 'Burlando'
    del Pedro.Apellido
    print(Pedro.__dict__)
    print(Lucas.__dict__)
    print(Melisa.__dict__)




