def my_gen():
    """Un Ejemplo de generador"""

    print("Hello world")
    n = 0
    yield n

    print("Hello heaven")
    n = 1
    yield n

    print("Hello hell")
    n = 2
    yield n


a = my_gen()

print(next(a))
print(next(a))
print(next(a))
