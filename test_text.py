from text import cleaners
from text import text_to_sequence, sequence_to_text


if __name__ == '__main__':
    # print(cleaners.flowtron_cleaners('it 10 Hello :) - you! вау'))

    sample1 = text_to_sequence('Вітаю! Мене звати Лада.')
    print(sample1)

    text1 = sequence_to_text(sample1)
    print(text1)
