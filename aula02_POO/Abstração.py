# Abstração na Programação Orientada a Objetos (POO) é o processo de identificar os aspectos essenciais de um objeto e ignorar os detalhes irrelevantes.

# Isso permite modelar objetos de forma simplificada, focando apenas nos detalhes que são relevantes para o problema em questão.

# No exemplo abaixo, estamos usando a linguagem Python para demonstrar a abstração na POO.

# Definindo a classe abstrata Animal
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Método abstrato que será implementado nas subclasses
    def emitir_som(self):
        pass

# Definindo uma subclasse concreta Cachorro que herda de Animal
class Cachorro(Animal):
    # Implementação do método emitir_som específico para Cachorro
    def emitir_som(self):
        return "Au au!"

# Definindo uma subclasse concreta Gato que herda de Animal
class Gato(Animal):
    # Implementação do método emitir_som específico para Gato
    def emitir_som(self):
        return "Miau!"

# Criando objetos
rex = Cachorro("Rex", 3)
garfield = Gato("Garfield", 5)

# Usando a abstração para chamar o método emitir_som sem se preocupar com a implementação específica de cada animal
print(rex.emitir_som())  # Saída: Au au!
print(garfield.emitir_som())  # Saída: Miau!

