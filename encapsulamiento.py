class MiClase:
    def __init__(self):
        self._atributo_privado = "Valor Privado"

    def _hablar(self):
        print("Este es un método protegido.")

objeto = MiClase()
print(objeto._atributo_privado)  # Aunque es posible acceder, no es recomendable

print(objeto._hablar())  # Aunque es posible acceder, no es recomendable


class Persona:
    def __init__(self, nombre, edad):   
        self.__nombre = nombre
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre
    
chanchito = Persona("Juan", 25)

nombre = chanchito.get_nombre()
print(nombre)  # Output: Juan