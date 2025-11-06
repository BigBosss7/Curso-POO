class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad
        
    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'
    
    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad})'
    
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre,nuevo_valor)
    
chanchito = Persona("Canchito",21)
julio = Persona("Julio",47)

nueva_persona = chanchito + julio
print(nueva_persona.nombre)