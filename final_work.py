setArray    = [1, 2, 3, 5, 6, 8, 9, 10, 11, 12, 15, 16, 17]
searchNum   = 25

#print(int(len(setArray) / 2))

def searchInArray(array, number):
    length      = len(setArray)
    middleId    = length // 2
    result = 0
    resultText = ''
        
    if (array[middleId] > number):
        for i in range(0, middleId):
            if (array[i] == number):
                result = 1
                resultText = 'Искомое значение "' + str(number) + '" найдено в массиве под индексом ' + str(i)
        if (result):
            print(resultText)
        else:
            print('Искомого значения "' + str(number) + '" в массиве не найдено!')
    else:
        for i in range(middleId, length):
            if (array[i] == number):
                result = 1
                resultText = 'Искомое значение "' + str(number) + '" найдено в массиве под индексом ' + str(i)
        if (result):
            print(resultText)
        else:
            print('Искомого значения "' + str(number) + '" в массиве не найдено!')

searchInArray(setArray, searchNum)
