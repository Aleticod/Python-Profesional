import time
def fibonacci_gen(n: int):
    a, b = 0, 1
    counter = 0
    while counter < n:
        counter += 1
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    fibonacci = fibonacci_gen(2)
    for element in fibonacci:
        print(element)
        time.sleep(1)