'''
Задача:
Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

'''

def all_variants(text):
    len_txt = len(text)


    for start in range(len_txt):


        for end in range(start + 1, len_txt + 1):


            yield text[start:end]

a = all_variants("abc")
for i in a:
    print(i)