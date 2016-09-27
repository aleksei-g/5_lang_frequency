import os.path
import re


def load_data(filepath):
    with open(filepath, 'rt') as f:
        data = f.read()
    return data


def get_most_frequent_words(text):
    words = text.lower().split()
    words_count = [{'word': word, 'count': words.count(word)}
                   for word in set(words) if not re.match('^\W$', word)]
    words_count.sort(key=lambda d: d['count'], reverse=True)
    for num, word in enumerate(words_count[0:10], start=1):
        print('%s) \"%s\": %s' % (num, word['word'], word['count']))


if __name__ == '__main__':
    while True:
        filepath = input('Enter file path: ')
        if os.path.exists(filepath):
            break
        else:
            print('File not found!')
    data = load_data(filepath)
    get_most_frequent_words(data)
