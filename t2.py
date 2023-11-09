rus_grade = int(input('Введите количество баллов по русскому языку: '))
math_grade = int(input('Введите количество баллов по математике: '))
inform_grade = int(input('ведите количество баллов по информатике: '))
if rus_grade+math_grade+inform_grade >= 270:
    print('Поздравляю, ты поступил на бюджет!')
else:
    print('К сожалению, ты не прошёл на бюджет.')