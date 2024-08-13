'''
Используя любые средства написать программу викторина:
Выбрать минимум 5 известных людей и узнать их год рождения.
Программа должна по очереди спрашивать у пользователя год рождения знаменитости.
После того как пользователь ввел все ответы, программа считает и выводит на экран:
- количество правильных ответов
- количество ошибок
- процент правильных ответов (можно посчитать как ПРАВИЛЬНЫЕ ОТВЕТЫ*100/ВСЕГО ВОПРОСОВ)
- процент неправильных ответов
После вывода информации программа спрашивает пользователя хочет ли он начать игру сначала,
если да - то повторяем все сначала,
если ответ нет - выходим из программы
- В программе с помощью комментариев написать подсказки - правильные ответы для каждой знаменитости

Пять самых известных советских шахматистов
Александр Алехин 1892
Михаил Ботвинник 1911
Тигран Петросян 1929
Анатолий Карпов 1951
Гарри Каспаров 1963

'''

alehin_birth = int(1892)
botvinnik_birth = int(1911)
petrosyan_birth = int(1929)
karpov_birth = int(1951)
kasparov_birth = int(1963)

correct_answers = int(0)
wrong_answers = int(0)
sum_answers = int(0)

while sum_answers == int(0):
    print('Я перечислю пятерых известных совестких шахматистов. Назови год рождения каждого из них.')
    qwestion1 = int(input('Александр Алехин ')) #1892
    qwestion2 = int(input('Михаил Ботвинник ')) #1911
    qwestion3 = int(input('Тигран Петросян ')) #1929
    qwestion4 = int(input('Анатолий Карпов ')) #1951
    qwestion5 = int(input('Гарри Каспаров ')) #1963
    if qwestion1 == alehin_birth:
        correct_answers += 1
    else:
        wrong_answers += 1
    if qwestion2 == botvinnik_birth:
        correct_answers += 1
    else:
        wrong_answers += 1
    if qwestion3 == petrosyan_birth:
        correct_answers += 1
    else:
        wrong_answers += 1
    if qwestion4 == karpov_birth:
        correct_answers += 1
    else:
        wrong_answers += 1
    if qwestion5 == kasparov_birth:
        correct_answers += 1
    else:
        wrong_answers += 1
    print('Правильных ответов: ', correct_answers)
    print('Ошибок: ', wrong_answers)
    sum_answers = correct_answers + wrong_answers
    correct_answers_share = int(correct_answers * 100 / sum_answers)
    wrong_answers_share = int(wrong_answers * 100 / sum_answers)
    print('Процент правильных ответов: ', correct_answers_share, '%')
    print('Процент неправильных ответов: ', wrong_answers_share, '%')
    povtor = input('Хочешь сыграть еще раз?')
    if povtor == 'Да':
        sum_answers = int(0)
    elif povtor == 'да':
        sum_answers = int(0)
    elif povtor == 'yes':
        sum_answers = int(0)
    elif povtor == 'Yes':
        sum_answers = int(0)
    elif povtor == 'Ok':
        sum_answers = int(0)
    elif povtor == 'ok':
        sum_answers = int(0)
    else:
        print('Спасибо за игру!')





















