class EvenNumbers:
    """ Clase que implementa un iterador
    de todos los numeros pares, o los numeros pares hasta un maximo"""

    def __init__(self, max = 100):
        self.max = max

    
    def __iter__(self):
        self.num = 0
        return self


    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            print(result)
            return result
        else:
            raise StopIteration