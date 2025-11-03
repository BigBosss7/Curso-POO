class Animal:
    def sonido (self):
        pass

class Gato:
    def sonido(Animal):
        return "Miau"
    
class Perro:
    def sonido(Animal):
        return "Guau"

def hacer_sonido(animal):
    print(animal.sonido())
   
gato = Gato()
perro = Perro()

hacer_sonido(gato)  # Output: Miau
hacer_sonido(perro)  # Output: Guau