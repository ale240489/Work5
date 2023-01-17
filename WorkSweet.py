#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая 
# ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать 
# не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
#a) Добавьте игру против бота
#b) Подумайте как наделить бота 'интеллектом'
import random

numberOfCandies = int(input('Укажите стартовое количество конфет: '))
print(numberOfCandies)

def game (numberOfCandies):
    while(numberOfCandies > 0):
        if(numberOfCandies <= 28):
            print('Игрок 1 забрал последнее, ты выиграл!!!')
            break
        candiesPlayer1 = int(input('Игрок 1, сколько ты хочешь забрать конфет? Но не больше 28!!!  '))
        if(candiesPlayer1 > 28):
            print('Больше 28 нельзя, засчитываю 28!!!')
            candiesPlayer1 = 28
        numberOfCandies-=candiesPlayer1
        print(f'Осталось {numberOfCandies}')
       
        if(numberOfCandies < 28):
            print('Бот забирает остаток и одерживает победу!!!')
            break
        if(numberOfCandies > 56):
            candiesPlayer2 = random.randint(1,28)
            
        if(numberOfCandies < 56 and numberOfCandies > 29):
            candiesPlayer2 = numberOfCandies - 29    
        print(f'Бот забрал {candiesPlayer2} конфет')    
        numberOfCandies-=candiesPlayer2
        print(f'Осталось {numberOfCandies}')
          
        
       

game(numberOfCandies)
