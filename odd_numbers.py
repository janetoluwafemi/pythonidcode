
def odd_numbers(numbers):
    sum = 0
    for num in numbers:
        if (num%2==1):
            odd = num
            sum += odd
            return sum

number = [1,2,3,4,5]
print(odd_numbers(number))