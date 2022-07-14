def border_decorator(func):
    def wrapper(*args, **kwargs):
        print(' ' + '_' * (3 + len(*args)))
        print('/' + '_' * (2 + len(*args)) + '/|')
        print('|' + ' ' * (2 + len(*args)) + '||')
        print(f'| {func(*args, **kwargs)} ||')
        print('|' + '_' * (2 + len(*args)) + '|/')
    return wrapper


@border_decorator
def printer(texto: str):
    return texto


def text_input():
    text = input('Harvey says: ')
    return text


def run():
    printer(text_input())


if __name__ == '__main__':
    run()
