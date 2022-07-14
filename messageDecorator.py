from tokenize import maybe


def with_custom_message(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'{message}')
            func(*args, **kwargs)
        return wrapper
    return decorator


@with_custom_message('This is a message')
def multiply(a: int, b: int):
    c = a * b
    print(f'The result of {a} * {b} is {c}')

def run():
    multiply(4, 6)

if __name__ == '__main__':
    run()