class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad   

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.nacionalidad}."


class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self):
        print(f"Mi habilidad artística es {self.habilidad}.")

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, empresa, salario):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.empresa = empresa
        self.salario = salario

    def mostrar_info_empleo(self):
        return f"Trabajo como {self.puesto} y mi salario es {self.salario}."
    
    def presentarse(self):
        print(f"Hola, soy: {self.nombre},{self.mostrar_habilidad()} y trbajo en {self.empresa}.")
        
     

roberto = EmpleadoArtista("Roberto", 30, "Mexicano", "guitarra", "Amazon", 50000)

roberto.presentarse()

herencia= issubclass(EmpleadoArtista, Artista)
instancia= isinstance(roberto, Persona)

print(herencia)