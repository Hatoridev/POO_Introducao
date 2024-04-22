#include <iostream>
#include <string>

using namespace std;

// Na Programação Orientada a Objetos (POO), a herança é um princípio que permite criar novas classes baseadas em classes existentes, conhecidas como superclasses.
// Com a herança, uma classe pode herdar atributos e métodos de outra classe, promovendo a reutilização de código e organizando a estrutura do programa de forma hierárquica.
// Abaixo, usaremos C++ para demonstrar o conceito de herança na POO.

// Definindo a classe pai ou superclasse
class Veiculo {
public:
    Veiculo(string marca, string modelo) : marca(marca), modelo(modelo) {}

    void imprimir_info() {
        cout << "Marca: " << marca << ", Modelo: " << modelo << endl;
    }

protected:
    string marca;
    string modelo;
};

// Definindo uma subclasse que herda da classe Veiculo
class Carro : public Veiculo {
public:
    Carro(string marca, string modelo, string cor) : Veiculo(marca, modelo), cor(cor) {}

    void imprimir_info() {
        Veiculo::imprimir_info();
        cout << "Cor: " << cor << endl;
    }

private:
    string cor;
};

// Função principal
int main() {
    // Criando um objeto da subclasse Carro
    Carro meu_carro("Toyota", "Corolla", "Preto");

    // Imprimindo informações sobre o carro
    meu_carro.imprimir_info();

    return 0;
}

