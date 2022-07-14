
from cgi import print_arguments
import urllib.request
from collections import Counter


def word_counter(func):
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        total_words = data.split()
        stop_words = ['y', 'Y', 'la', 'de', 'una', 'los', 'me',
                      'No', 'con', 'que', 'el', 'un', 'es',
                      'Que', 'muy', 'al', 'a', 'él', 'le', 'quiere',
                      'A', 'da', 'faltan', 'Mas', 'bien']
        words = [word for word in total_words if word not in stop_words]
        words_count = Counter(words)
        print('\n>>> TOP FIVE WORDS IN THIS SONG <<<\n')

        for w in words_count.most_common(5):
            print(f'{w[0]}: {w[1]}')
    return wrapper


@word_counter
def text_reader(url):
    data = urllib.request.urlopen(url).read().decode('utf_8')
    return data


def run():
    chilanga_banda = 'https://raw.githubusercontent.com/isabelyb/word_counter/main/chilanga_banda_lyrics.txt'
    p_to = 'https://raw.githubusercontent.com/isabelyb/word_counter/main/pto.txt'
    text_reader(chilanga_banda)
    text_reader(p_to)


if __name__ == '__main__':
    run()