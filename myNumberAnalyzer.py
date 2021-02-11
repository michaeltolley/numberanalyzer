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


numbers = [1,2,3,4,5,31,25,43,13,25]
moreNumbers = [123,2133,123,12,3344,12,1239,489]

average = getAverage(numbers)
sum = getSum(numbers)

moreAverage = getAverage(moreNumbers)

print ("sum equals " + str(sum) )

print ("average equals " + str(average)) 

print ("moreAverage equals " + str(moreAverage)) 