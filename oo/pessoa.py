class Pessoa:
    olhos = 2
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
    Lucas.olhos = 1
    print(Pedro.__dict__)
    print(Lucas.__dict__)
    print(Melisa.__dict__)
    #del Lucas.olhos
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(Lucas.olhos)
    print(Pedro.olhos)
    print(id(Pessoa.olhos), id(Lucas.olhos), id(Pedro.olhos), id(Melisa.olhos))



