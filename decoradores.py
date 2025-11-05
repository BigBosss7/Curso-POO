# Ejemplo básico de un decorador, comentar todo el codigo ctrl + /
def mi_decorador(funcion):
    def wrapper():
        print("Se ejecuta antes de la función")
        funcion()
        print("Se ejecuta después de la función")
    return wrapper

# Usando el decorador con @
@mi_decorador
def saludo():
    print("¡Hola mundo!")

# Llamando a la función decorada
saludo()

# Ejemplo de decorador con parámetros
def decorador_con_argumentos(arg1, arg2):
    def decorador_real(funcion):
        def wrapper():
            print(f"Argumentos del decorador: {arg1}, {arg2}")
            funcion()
        return wrapper
    return decorador_real

@decorador_con_argumentos("Hola", "Mundo")
def otra_funcion():
    print("Esta es otra función")

# Llamando a la segunda función decorada
otra_funcion()