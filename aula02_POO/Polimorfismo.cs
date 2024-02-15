using System;

// Na Programação Orientada a Objetos (POO), o polimorfismo permite que objetos de diferentes classes sejam tratados de maneira uniforme.
// Isso significa que um objeto pode se comportar de várias maneiras, dependendo do contexto em que é usado.
// No contexto da herança, o polimorfismo permite que um objeto de uma classe derivada seja tratado como um objeto da classe base.
// Abaixo, usaremos C# para demonstrar o conceito de herança e polimorfismo na POO.

// Definindo a classe base Animal
class Animal
{
    public virtual void FazerSom()
    {
        Console.WriteLine("Animal fazendo som...");
    }
}

// Definindo a subclasse Cachorro que herda de Animal
class Cachorro : Animal
{
    public override void FazerSom()
    {
        Console.WriteLine("Cachorro: Au au!");
    }
}

// Definindo a subclasse Gato que herda de Animal
class Gato : Animal
{
    public override void FazerSom()
    {
        Console.WriteLine("Gato: Miau!");
    }
}

class Program
{
    // Função para fazer um animal fazer som, independentemente do tipo
    static void FazerSom(Animal animal)
    {
        animal.FazerSom();
    }

    // Função principal
    static void Main(string[] args)
    {
        // Criando objetos das classes Cachorro e Gato
        Cachorro meuCachorro = new Cachorro();
        Gato meuGato = new Gato();

        // Chamando a função FazerSom para diferentes tipos de animais
        FazerSom(meuCachorro); // Polimorfismo: tratando um objeto Cachorro como um objeto Animal
        FazerSom(meuGato);     // Polimorfismo: tratando um objeto Gato como um objeto Animal
    }
}

