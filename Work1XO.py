# Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

#Инициализация карты
import random
desc = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  

#Вывод карты на экран
def printMaps(desc):
    
    print(desc[0], end = ' ')
    print(desc[1], end = ' ')
    print(desc[2])

    print(desc[3], end = ' ') 
    print(desc[4], end = ' ') 
    print(desc[5])

    print(desc[6], end = ' ')
    print(desc[7], end = ' ')
    print(desc[8])

victoryCheckPosition = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8],
[0,4,8], [2,4,6]]

def victoryCheck():
    victory = ''
    for position in victoryCheckPosition:
        if desc[position[0]] == 'X' and desc[position[1]] == 'X' and desc[position[2]] == 'X':
            victory = 'Победил игрок X'
            
        if desc[position[0]]== 'O' and desc[position[1]]== 'O' and desc[position[2]] == 'O':
            victory = 'Победил бот'
       
    return victory 

printMaps(desc) 

#Ход игрока
def playersMove (desc):
    strokeNumber = 1
    game = victoryCheck()
    
    while(strokeNumber <= 5):
        #Первый игрок
        positionX = int(input('Игрок X введите номер квадрата, для того чтобы совершить ход: '))
        while(desc[positionX - 1] == 'X'or desc[positionX - 1] == 'O'):
            positionX = int(input('Клетка занята, игрок X введите повторно номер квадрата, для того чтобы совершить ход: '))
        desc[positionX - 1] = 'X'
        printMaps(desc)
        victory = victoryCheck()
        if(victory != ''):
            print(victory)
            break
        #Второй игрок
        if(strokeNumber != 5):
            print('Ход бота')
            if(desc[0]=='X' and desc[1] =='X' and desc[2] != "O"):
                desc[2] = 'O'
                printMaps(desc)
                strokeNumber += 1
                continue
            if(desc[8]=='X' and desc[4] == 'X'and desc[0] != 'O'):
                desc[0] = 'O'
                printMaps(desc)
                strokeNumber += 1
                continue
                
            if(desc[3]=='X' and desc[4] == 'X'and desc[5] != 'O'):
                desc[5] = 'O'
                printMaps(desc)
                strokeNumber += 1
                continue
            if(desc[1]=='X' and desc[4] == 'X'and desc[7] != 'O'):
                desc[7] = 'O'
                printMaps(desc)
                strokeNumber += 1
                continue
            if(desc[2]=='X' and desc[4] == 'X'and desc[6] != 'O'):
                desc[6] = 'O'
                printMaps(desc)
                strokeNumber += 1
                continue
            if(desc[6]=='X' and desc[4] == 'X'and desc[2] != 'O'):
                desc[2] = 'O'
                printMaps(desc)
                strokeNumber += 1
                continue
            if(desc[2]=='X' and desc[5] == 'X'and desc[8] != 'O'):
                desc[8] = 'O'
                printMaps(desc)
                strokeNumber += 1
                continue
               
            if(desc[6] == 'X' and desc[7] == 'X' and desc[8] != 'O'):
                desc[8] = 'O'
                printMaps(desc)
                strokeNumber += 1
                continue
            if(desc[7]=='X' and desc[4] == 'X'and desc[1] != 'O'):
                desc[1] = 'O'
                printMaps(desc)
                strokeNumber += 1
                continue
            if(desc[8]=='X' and desc[7] == 'X'and desc[6] != 'O'):
                desc[6] = 'O'
                printMaps(desc)
                strokeNumber += 1
                continue
            else:
                positionO = random.randint(1,9)
                while(desc[positionO - 1] == 'X'or desc[positionO - 1] == 'O'):
                    positionO = random.randint(1,9)
                desc[positionO - 1] = 'O'
                printMaps(desc)
                victory = victoryCheck()
                if(victory != ''):
                    print(victory)
                    break
        if(strokeNumber == 5):
            print('Ничья')    
        strokeNumber += 1


playersMove(desc)