# Python module to know if a number is prime
def is_prime(number: int) -> bool:
    # Return True if number is prime or False if the number is not prime
    limit = (number / 2)
    i = 2
    condition = True
    if number == 1:
        condition = False
    else:
        while i <= limit:
            if(number % i == 0):
                condition = False
                break
            i += 1
    return condition


def run():
    for i in range (1, 1000):
        if is_prime(i):
            print('Numero prime: ' + str(i))

if __name__ == '__main__':
    run()

'''
def is_prime(num: int) -> bool:
    result = [i for i in range(1, num + 1) if num % == 0]
    return len(result) == 2
'''
