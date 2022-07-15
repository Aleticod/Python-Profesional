import time

# Clase que representa a los objetos del tipo iterador
class FiboIter():
    # Metodo constructor
    def __init__(self, max = None):
        self.max = max


    # Metodo inicializador (Elemento que necesitamos para que el iterador funcione)
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self


    # Metodo iterador de siguiente
    def __next__(self):
        if (not self.max or self.counter < self.max) and self.counter == 0:
            self.counter += 1
            return self.n1
        elif (not self.max or self.counter < self.max) and self.counter == 1:
            self.counter += 1
            return self.n2
        elif (not self.max or self.counter < self.max):
            self.aux = self.n1 + self.n2
            #self.n1 = self.n2
            #self.n2 = self.aux
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux
        else:
            raise StopIteration


if __name__ == '__main__':
    fibonacci = FiboIter()  # Se ejecuta __iter__()
    fibonacci.__iter__()
    print(fibonacci.__next__())
    print(fibonacci.__next__())
    print(fibonacci.__next__())
    print(fibonacci.__next__())
    print(fibonacci.__next__())
    print(fibonacci.__next__())
    print(fibonacci.__next__())
    print(fibonacci.__next__())
    print(fibonacci.__next__())
    print(fibonacci.__next__())
    print(fibonacci.__next__())
    print(fibonacci.__next__())


    # for element in fibonacci:  # Se ejecuta el __next()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    #     print(element)
    #     time.sleep(0.05)