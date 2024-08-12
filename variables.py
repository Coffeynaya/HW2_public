"""
Объект для описания - кандидат на вакансию Директор по развитию региональной сети.
Переменные основных типов данных для описания этого объекта:
1. ФИО full_name (тип строка) - ввод,
2. возраст age (тип целое число) - ввод,
3. пол gender (тип строка) - ввод,
4. образование education (тип строка) - ввод,
5. место рождения place_birth (тип строка) - ввод,
6. в каких регионах жил более года regions_live (тип строка) - ввод,
7. стаж общий work_experience (число с плавающей точкой) - ввод,
8. годы опыта работы с региональными сетями regions_experience (тип целое число) - ввод,
9. с какими/в каких регионами есть опыт работы regions_work (тип строка) - ввод,
10. годы управленческого опыта management_experience (тип целое число) - ввод,
11. готовность к командировкам is_readiness_bus_trips (логический тип) - ввод.

В конце модуля с помощью функции type вывести тип для каждой из объявленных переменных


"""

full_name = input('Введите Ваше ФИО: ')
age = int(input('Введите год Вашего рождения:'))
gender = input('Введите Ваш пол: ')
education = input('Какое у Вас образование и по какой специальности? ')
place_birth = input('Где Вы родились (страна, населенный пункт): ')
regions_live = input('В каких регионах России Вы жили более 1 года? (субъект РФ, населенный пункт): ')
work_experience = float(input('Сколько лет Вы работаете? Укажите точный стаж'))
regions_experience = int(input('Сколько полных лет Вы работаете с регионами?'))
regions_work = input('В каких регионах России Вы работали более 1 года? (субъект РФ, населенный пункт): ')
management_experience = int(input('Сколько полных лет Вы работаете на управленческих должностях?'))
is_readiness_bus_trips = True
readiness_bus_trips = input('Готовы ли Вы к длительным командировкам в регионы? Готов/Не готов ')
if readiness_bus_trips == 'Да':
    readiness_bus_trips = is_readiness_bus_trips
    print('Готов к длительным командировкам')
else:
    print('Не готов к длительным командировкам')

print('\nСВОДНАЯ ИНФОРМАЦИЯ О КАНДИДАТЕ')
print('ФИО кандидата: ', full_name)
print('Год рождения: ', age)
print('Пол:', gender)
print('Образование: ', education)
print('Место рождения: ', place_birth)
print('Регионы проживания: ', regions_live)
print('Общий стаж, точных лет: ', work_experience)
print('Региональный стаж, полных лет: ', regions_experience)
print('Регионы работы: ', regions_work)
print('Управленческий стаж, полных лет: ', management_experience)
print('Готовность к командировкам: ', readiness_bus_trips)

print('\nРЕШЕНИЕ ЗАДАЧИ ОПРЕДЕЛИТЬ ТИП ПЕРЕМЕННЫХ')
print('ФИО кандидата: ', 'full_name', type(full_name))
print('Год рождения: ', 'age', type(age))
print('Пол:', 'gender', type(gender))
print('Образование: ', 'education', type(education))
print('Место рождения: ', 'place_birth', type(place_birth))
print('Регионы проживания: ', 'regions_live', type(regions_live))
print('Общий стаж, точных лет: ', 'work_experience', type(work_experience))
print('Региональный стаж, полных лет: ', 'regions_experience', type(regions_experience))
print('Регионы работы: ', 'regions_work', type(regions_work))
print('Управленческий стаж, полных лет: ', 'management_experience', type(management_experience))
print('Готовность к командировкам: ', 'is_readiness_bus_trips', type(is_readiness_bus_trips))