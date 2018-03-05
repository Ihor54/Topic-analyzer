import re
import string
import nltk
from pymorphy2 import MorphAnalyzer

nltk.download('stopwords')
from nltk.corpus import stopwords


def splitText(text):
    """
    Splits text using regular expressions
    :param text: Input Text
    :return: list of words
    """
    # собираем символы которые будем отбрасывать
    punctuation = string.punctuation + '\u2014\u2013\u2012\u2010\u2212' + '«»‹›‘’“”„`'
    word_tokenize = re.compile(r"([^\w_\u2019\u2010\u002F-]|[+])")
    words = []
    for token in word_tokenize.split(text):
        # если слово не попадает в те которые мы исключаем
        if token and not token.isspace() and not token in punctuation:
            # добавляем слово в список
            words.append(token.lower())
    # возвращаем список слов
    return words


def normalForm(wordList):
    """
    Normalises words
    :param wordList: list of words
    :return: normalized list of words
    """
    normalized = []
    morph = MorphAnalyzer()
    for word in wordList:
        wordToNormal = morph.parse(word)[0].normal_form
        normalized.append(wordToNormal)
    return normalized


def removeStopWords(wordList):
    """
    Removes stopwords
    :param wordList: normalized list of words
    :return: normalized list of words without stopwords
    """
    withoutStopWords = []
    stop_words = stopwords.words('russian')
    for word in wordList:
        if word not in stop_words:
            withoutStopWords.append(word)
    return withoutStopWords


def analyseFrequency(wordList):
    """
    Calculates word frequency and returns 3 most popular words
    :param wordList: list of words
    :return: normalised list of words
    """
    frequency = {}
    for word in wordList:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    analysed = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    result = analysed[0:3]
    return '{}'.format([' '.join([i[0] for i in result])])


if __name__ == '__main__':
    text = 'Иногда могут помочь какие-то особенности задачи. Например,' \
           ' если нужно просклонять слово, и известно, что на входе ожидается' \
           ' слово в именительном падеже, то лучше брать вариант разбора в именительном падеже, а не первый.' \
           ' В общем же случае для выбора точного разбора необходимо каким-то ' \
           'образом учитывать не только само слово, но и другие слова в предложении.'
    words = splitText(text)
    print(words)
    normalized = normalForm(words)
    print(normalized)
    noStop = removeStopWords(normalized)
    print(noStop)
    analysed = analyseFrequency(noStop)
    print(analysed)