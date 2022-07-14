
def decorador(func):
    def envoltura():
        print("Esto se añade a mi funcion original")
        func()
    return envoltura


@decorador
def saludo():
    print("hola")


def run():
    saludo()

if __name__ == '__main__':
    run()