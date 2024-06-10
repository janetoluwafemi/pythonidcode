def average_numbers(numbers):
    counter = 0
    average_numbers = 0
    for count in numbers:
        counter = counter+1
        sum = 0
    for num in numbers:
        sum = sum + num
        average_numbers = sum / counter
    return average_numbers


number = [1,2,3,4,5]
print(average_numbers(number))

def odd_numbers(numbers):
    sum = 0
    for num in numbers:
        if (num%2==1):
            odd = num
            sum += odd
            return sum

number = [1,2,3,4,5]
print(odd_numbers(number))

def even_numbers(numbers):
    sum = 0
    for num in numbers:
        if (num%2==0):
            even = num
            sum += even
            return even

number = [1,2,3,4,5]
print(even_numbers(number))


def length_of_numbers(numbers):
    counter = 0
    for count in numbers:
        counter = counter+1
    return counter

number = [1,2,3,4,5]
print(length_of_numbers(number))



def largest_of_numbers(numbers):
    largest = 0
    for num in numbers:
        if(num > largest):
            largest = num
    return largest

number = [1,2,3,4,5]
print(largest_of_numbers(number))


def smallest_of_numbers(numbers):
    counter = 0
    smallest = 0
    for num in numbers:
        if(num < smallest):
            smallest = num
    return smallest

number = [1,2,3,4,5]
print(smallest_of_numbers(number))


def length_of_strings(word):
    counter = 0
    for count in word:
        counter = counter+1
    return counter

words = ["semicolon"]
print(length_of_numbers(words))