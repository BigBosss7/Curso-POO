class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    def hacer_llamada(self):
        print(f"Llamando... desde {self.modelo}")


    def tomar_foto(self):
        print(f"Tomando foto... en un {self.modelo} cámara")

Celular1 = Celular("Apple", "iPhone 13", "12MP")
Celular2 = Celular("Samsung", "Galaxy S21", "64MP")

print(Celular1.marca)
print(Celular2.modelo)
Celular2.hacer_llamada()
Celular1.tomar_foto()

    