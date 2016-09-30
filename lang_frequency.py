import os.path
import sys
import argparse
import string
from collections import Counter


COUNT_WORD_TO_PRINT = 10


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'rt') as f:
        data = f.read()
    return data


def get_most_frequent_words(text):
    words = [word.strip(string.punctuation) for word in text.lower().split()]
    return Counter(words).most_common(COUNT_WORD_TO_PRINT)


def createParser():
    parser = argparse.ArgumentParser(description='Поиск %s часто встречающихся\
                                     слов в тексте.' % COUNT_WORD_TO_PRINT)
    parser.add_argument('-f', '--file', required=True, metavar='ФАЙЛ',
                        help='Путь до текстового файла.')
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()
    data = load_data(namespace.file)
    if not data:
        print('Файл не найден!')
        sys.exit()
    words_count = get_most_frequent_words(data)
    for num, word in enumerate(words_count[0:10], start=1):
        print('%s) \"%s\": %s' % (num, word[0], word[1]))
