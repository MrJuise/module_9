'''
Задача:
Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

'''

def all_variants(text):
    for length in range(1, len(text) + 1):
        for start in range(len(text)):
            if start + length <= len(text):
                yield text[start:start + length]
a = all_variants("abc")
for i in a:
    print(i)

