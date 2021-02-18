def getSum(numbers):

    sum = 0

    for number in numbers:
        print(number)
        sum = sum + number

    return sum

def getAverage(numbers):
    sum = getSum(numbers)
    average = sum / len(numbers)
    return average


def getLowest(numbers):
    lowest = numbers[0]
    for number in numbers:
        if(number < lowest):
            lowest = number
    return lowest
     

numbers = [1,2,3,4,5,31,25,43,13,25]
moreNumbers = [7565,3436,565,34,3,43,5665,3,33,23,2]

average = getAverage(numbers)
sum = getSum(numbers)
lowest = getLowest(moreNumbers)

moreAverage = getAverage(moreNumbers)

print ("sum equals " + str(sum) )

print ("average equals " + str(average)) 

print ("moreAverage equals " + str(moreAverage))

print ("the lowest equals " + str(lowest))