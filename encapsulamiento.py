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

    def get_nombre(self): #funcion que accede al atributo privado de la clase
        return self.__nombre
    
    def set_nombre(self, new_nombre): #funcion que modifica el atributo privado de la clase
        self.__nombre = new_nombre
    
chanchito = Persona("Juan", 25)

nombre = chanchito.get_nombre()
print(nombre)  # Output: Juan

chanchito.set_nombre("Pedro")
nombre_actualizado = chanchito.get_nombre()
print(nombre_actualizado)  # Output: Pedro