from random import random

toid = 'id_for_plr.txt'

c1 = int(input('Для игры создать аккаунт(1) или войти(2)'))
if c1 == 1:
    nick = str(input('Напиши ник:'))
    while nick in open(toid).read():
        nick = str(input('Ник уже занят! Напиши новый:'))

c2 = int(input('Привет! Играть(1) или узнать рекорд(2)?'))