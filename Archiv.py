# # Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# # Входные и выходные данные хранятся в отдельных текстовых файлах.
# # aaaaabbbcccc -> 5a3b4c
# # 5a3b4c -> aaaaabbbcccc
string1 = 'aaaaabbbcccc'
string2 = '5a3b4c'
inputStr=''
data = open('file44.txt','w')
data.writelines(string1+string2)
data.close()
data = open('file44.txt','r')
inputStr += data.readline()
print(f'Исходная строка {inputStr}')


counter = 1
zipStr = ''
for i in range (1,len(inputStr)):
    if inputStr[i-1].isdigit():
        num = int(inputStr[i-1])
        for z in range(num):
            zipStr += inputStr[i]
        inputStr = inputStr.replace(inputStr[i], ' ')        
           
            
    else:
        if inputStr[i] != inputStr[i-1]:
                zipStr += str(counter) + inputStr[i-1]
                counter = 1 
        if inputStr[i] == inputStr[i-1]:
            counter+=1
            if i == len(inputStr) - 1:
                zipStr += str(counter) + inputStr[i-1] 
   


zipStr = zipStr.replace('1 ','')
data2 = open('file45.txt','w')
data2.writelines(zipStr)
data2.close()

print(f'Форматированная строка {zipStr}')    

