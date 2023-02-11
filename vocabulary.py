from tkinter import *
import re
import pandas
from random import randint
from openpyxl import load_workbook

# root = Tk()
#
#
# def btn_click():
#     print('Тренировка началась')
#
#
# root['bg'] = '#fafafa'
# root.title('Словарь')
# root.wm_attributes('-alpha', 1)
# root.geometry('300x250')
#
# frame = Frame(root, bg='green')
# frame.place(relwidth=1, relheight=1)
#
# title = Label(frame, text='Упражнение', bg='blue', font=30)
# title.pack()
#
# button = Button(frame, text='Начать тренировку', bg='yellow', command=btn_click)
# button.pack()
#
# root.mainloop()


def delete_sym(word):
    word = re.sub("'", "", word)
    word = re.sub('"', "", word)
    return word


def choose_words(vocab):
    words = vocab[0]
    translates = vocab[1]
    values = vocab[2]
    values_sorted = sorted(values, reverse=True)
    div = len(values) // 4
    values_max = set(values_sorted[: div + 1])
    values_mean = set(values_sorted[(div + 1): (3 * div + 1)])
    values_min = set(values_sorted[(3 * div + 1):])
    return values_max, values_mean, values_min


def write_word(words, translates, value, choice, spec_list):
    i = 0
    right_answers = 0
    wrong_answers = 0
    print('Укажите количество слов для повторения:')
    l = int(input())
    used_words = list()
    while i != l:
        n = randint(0, len(words))
        if choice in [1, 2]:
            while words[n] in used_words or value[n] not in spec_list:
                n = randint(0, len(words))
        else:
            while words[n] in used_words:
                n = randint(0, len(words))
        used_words.append(words[n])
        translate = delete_sym(str(translates[n]))
        print('Переведите:' + ' ' + translate[1:-1])
        answer = input().lower().strip()
        cell = 'C' + str(n + 2)
        if answer == words[n].lower():
            print('правильно!')
            if sheet[cell].value + 6 > 100:
                sheet[cell].value = 100
                print('показатель слова:', 100, '\n')
            else:
                sheet[cell].value += 6
                print('показатель слова:', value[n] + 6, '\n')
            right_answers += 1
        else:
            print('неверно! Верный ответ: ' + words[n])
            if sheet[cell].value - 2 < 0:
                sheet[cell].value = 0
                print('показатель слова:', 0, '\n')
            else:
                sheet[cell].value -= 2
                print('показатель слова:', value[n] - 2, '\n')
            wrong_answers += 1
        i += 1

# def get_four_words()

data = pandas.read_excel('./words.xlsx')
words = list(data['word'])
translates = list(data['translate'])
value = list(data['value'])
translates = [w.split(';') for w in translates]

vocab = [words, translates, value]
values_max, values_mean, values_min = choose_words(vocab)

wb = load_workbook('./words.xlsx')
sheet = wb['list1']

print('Какие слова будем повторять?')
print('1 - плохо выученные')
print('2 - хорошо выученные')
print('3 - любые', '\n')
choice = int(input())
if choice not in [1, 2, 3]:
    print('Вы не выбрали тип тренировки!')

i = 0
right_answers = 0
wrong_answers = 0

if choice == 1:
    print('Укажите количество слов для повторения:')
    l = int(input())
    used_words = list()
    while i != l:
        n = randint(0, len(words))
        while words[n] in used_words or value[n] not in values_min:
            n = randint(0, len(words))
        used_words.append(words[n])
        translate = delete_sym(str(translates[n]))
        print('Переведите:' + ' ' + translate[1:-1])
        answer = input().lower().strip()
        cell = 'C' + str(n + 2)
        if answer == words[n].lower():
            print('правильно!')
            if sheet[cell].value + 6 > 100:
                sheet[cell].value = 100
                print('показатель слова:', 100, '\n')
            else:
                sheet[cell].value += 6
                print('показатель слова:', value[n] + 6, '\n')
            right_answers += 1
        else:
            print('неверно! Верный ответ: ' + words[n])
            if sheet[cell].value - 2 < 0:
                sheet[cell].value = 0
                print('показатель слова:', 0, '\n')
            else:
                sheet[cell].value -= 2
                print('показатель слова:', value[n] - 2, '\n')
            wrong_answers += 1
        i += 1


elif choice == 2:
    print('Укажите количество слов для повторения:')
    l = int(input())
    used_words = list()
    while i != l:
        n = randint(0, len(words))
        while words[n] in used_words or value[n] not in values_max:
            n = randint(0, len(words))
        used_words.append(words[n])
        translate = delete_sym(str(translates[n]))
        print('Переведите:' + ' ' + translate[1:-1])
        answer = input().lower().strip()
        cell = 'C' + str(n + 2)
        if answer == words[n].lower():
            print('правильно!')
            if sheet[cell].value + 6 > 100:
                sheet[cell].value = 100
                print('показатель слова:', 100, '\n')
            else:
                sheet[cell].value += 6
                print('показатель слова:', value[n] + 6, '\n')
            right_answers += 1
        else:
            print('неверно! Верный ответ: ' + words[n])
            if sheet[cell].value - 2 < 0:
                sheet[cell].value = 0
                print('показатель слова:', 0, '\n')
            else:
                sheet[cell].value -= 2
                print('показатель слова:', value[n] - 2, '\n')
            wrong_answers += 1
        i += 1


elif choice == 3:
    print('Укажите количество слов для повторения:')
    l = int(input())
    used_words = list()
    while i != l:
        n = randint(0, len(words))
        while words[n] in used_words:
            n = randint(0, len(words))
        used_words.append(words[n])
        translate = delete_sym(str(translates[n]))
        print('Переведите:' + ' ' + translate[1:-1])
        answer = input().lower().strip()
        cell = 'C' + str(n + 2)
        if answer == words[n].lower():
            print('правильно!')
            if sheet[cell].value + 6 > 100:
                sheet[cell].value = 100
                print('показатель слова:', 100, '\n')
            else:
                sheet[cell].value += 6
                print('показатель слова:', value[n] + 6, '\n')
            right_answers += 1
        else:
            print('неверно! Верный ответ: ' + words[n])
            if sheet[cell].value - 2 < 0:
                sheet[cell].value = 0
                print('показатель слова:', 0, '\n')
            else:
                sheet[cell].value -= 2
                print('показатель слова:', value[n] - 2, '\n')
            wrong_answers += 1
        i += 1

else:
    print('До свидания!', '\n')


wb.save('words.xlsx')

print('Тренировка окончена. Ваш результат:')
print('Правильных ответов: ', right_answers)
print('Неверных ответов: ', wrong_answers)

