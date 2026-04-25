from random import randint

cur_chance = 1
score = 0
record = 0
accfile = open('plr\\NOTDELETETHIS.txt')
nick = ''

c2 = int(input('Для игры надо либо войти(1) либо зарегистрироваться(2)'))
if c2 == 1:
    nick = input('Введи ник: ')
    record = int(open(r'plr\\' + nick + '.txt', 'r').read())
    print('Вы вошли в аккаунт. Хорошей игры!')
else:
    nick = input('Введи ник: ')
    accfile = open(r'plr\\' + nick + '.txt', 'w')
    print('Аккаунт создан!')

while True:
    c = int(input('Привет! Играть(1) или узнать рекорд(2)?'))
    if c == 1:
        while True:
            c1 = int(input('Идти дальше(1) или остановиться(2)?'))
            if c1 == 1:
                if randint(0, 100) > cur_chance:
                    score += 1
                    if cur_chance < 50:
                        cur_chance += 1
                    print('Ты выиграл с шансом', 100 - cur_chance, 'и идёшь дальше!')
                else:
                    print('Ты проиграл с результатом', str(score) + '. Шанс проиграть был', cur_chance)
                    score = 0
                    cur_chance = 0
                    break
            if c1 == 2:
                print('Ты вышел с результатом', score)
                if record < score:
                    record = score
                    accfile.write(str(record))
                score = 0
                break
    if c == 2:
        print('Текущий рекорд:', record)