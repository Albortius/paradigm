firstData   = [2, 5, 8, 3, 6]
secondData  = [5, 3, 9, 4, 2]

def corelationPirsonFunc(xArr, yArr):
    xSum    = 0
    ySum    = 0
    xx      = 0
    yy      = 0
    xy      = 0
    size    = len(xArr)
    
    for i in range(len(xArr)):
        xSum    += xArr[i]
        ySum    += yArr[i]
        xx      += xArr[i] ** 2
        yy      += yArr[i] ** 2
        xy      += xArr[i] * yArr[i]
    return (size * xy - xSum * ySum) / ((size * xx - xSum ** 2) * (size *yy - ySum ** 2)) ** 0.5

print(corelationPirsonFunc(firstData, secondData))
