# Напишите программу, которая принимает текст и выводит два слова:
# наиболее часто встречающееся и самое длинное.

import collections

text = 'longest freq freq freq sf la ny freq nothing'


def words_finder(source: str) -> tuple:
    splited = collections.Counter(source.split(' '))

    most_frequency, _ = splited.most_common()[0]
    longest: str = max(splited, key=len)

    return most_frequency, longest


assert words_finder(text) == ('freq', 'longest')
