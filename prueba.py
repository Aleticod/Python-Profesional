# Python module to know if a number is prime
def is_prime(number: int) -> bool:
    # Return True if number is prime or False if the number is not prime
    if number == 2:
        return True
    elif number == 1 or number % 2 == 0 or number % 3 == 0:
        return False
    else:
        return True


def run():
    for i in range (1, 1000):
        if is_prime(i):
           print(i)

if __name__ == '__main__':
    run()

'''
def is_prime(num: int) -> bool:
    result = [i for i in range(1, num + 1) if num % == 0]
    return len(result) == 2
'''