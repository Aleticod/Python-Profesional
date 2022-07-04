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
           print(i)

if __name__ == '__main__':
    run()