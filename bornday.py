'''
Написать программу или модернизировать предыдущую используя условные операторы:
- Спросить у пользователя год рождения А.С. Пушкина
- Если пользователь ввел верный год, спросить у него день рождения
- Если день рождения введен верно, вывести 'Верно'
- Если день рождения введен неверно, вывести 'Неверный день рождения'
- Если неверно введен год, то сразу вывести 'Неверный год рождения', а день рождения не спрашивать
'''

year_birth = int('1799')
day_birth = '6 июня'
question_year = int(input('В каком году родился А.С. Пушкин? '))
if question_year != year_birth:
    print('Неверный год рождения')
else:
    question_day = str(input('А теперь назови дату рождения: число и месяц '))
    if question_day != day_birth:
        print('Нверный день рождения')
    else:
        print('Верно')