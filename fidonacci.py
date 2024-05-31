firstNumber = 0
secondNumber = 1
sum = 0
print(firstNumber,end=" ")
for number in range(1,11):
    sum = secondNumber
    firstNumber = secondNumber + firstNumber
    secondNumber = firstNumber
    print(sum, end=" ")
    firstNumber = sum





