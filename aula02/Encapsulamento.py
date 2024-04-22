# Na Programação Orientada a Objetos (POO), o encapsulamento é um princípio que permite ocultar os detalhes internos de um objeto e expor apenas as operações relevantes através de métodos públicos.
# Isso ajuda a proteger os dados dentro de um objeto, prevenindo acesso não autorizado e garantindo que a manipulação dos dados seja feita de maneira controlada.
# Abaixo, utilizamos Python para demonstrar o conceito de encapsulamento na POO.

# Definindo a classe Carro
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__ligado = False  # Atributo privado encapsulado

    # Método público para ligar o carro
    def ligar(self):
        self.__ligado = True

    # Método público para desligar o carro
    def desligar(self):
        self.__ligado = False

    # Método público para verificar se o carro está ligado
    def esta_ligado(self):
        return self.__ligado

# Criando um objeto da classe Carro
meu_carro = Carro("Toyota", "Corolla")

# Tentativa de acessar o atributo privado diretamente (isso resultará em um erro)
# print(meu_carro.__ligado)

# Utilizando os métodos públicos para ligar e desligar o carro
meu_carro.ligar()
print("O carro está ligado?", meu_carro.esta_ligado())  # Saída: O carro está ligado? True

meu_carro.desligar()
print("O carro está ligado?", meu_carro.esta_ligado())  # Saída: O carro está ligado? False

