import random


def roll(numberOfDice, sidesOfDice):
    totalPointsPerRoll = 0
    for i in range (numberOfDice):
        value = random.randint(1,sidesOfDice)
        totalPointsPerRoll +=  value        
    return totalPointsPerRoll

#test1     
print(roll(1,6))


def test(numberOfDice, sidesOfDice, rolls):
    totalPoints = []
    for i in range (rolls):
        totalPoints.append(roll(numberOfDice, sidesOfDice))
    return totalPoints

#test2 
print(test(1,6,10))


def get_stats(listOfPoints):    
    value1 ={}
    value2 ={}
    value3 = 0
    sumPoints = 0
    dicestats = {'count':value1, 'sequence':value2, 'average':value3}
    newList =list(set(listOfPoints)) 
    for i in range (len(newList)):
        size = 0
        
        for j in range (len(listOfPoints)):
            
            if listOfPoints[j] == newList[i] :
                size += 1
                value1[newList[i]] = size
            continue
        streakList = set()
        length = 1
        for a, b in enumerate(listOfPoints):
            if a > 0:
                if b == listOfPoints[a-1] == newList[i]:
                    length += 1
                else:
                    streakList.update([length])
                    length = 1
        streakList.update([length])
        value2[newList[i]] = max(streakList)
    for x in range(len(listOfPoints)):
        sumPoints += listOfPoints[x]

    dicestats["average"]=(int(sumPoints /(len(listOfPoints))))
    
    return dicestats

#test3
print(get_stats(test(1,6,1000)))


    
    
    
                   
                   
        
    
    
    
