def even_numbers(numbers):
    sum = 0
    for num in numbers:
        if (num%2==0):
            even = num
            sum += even
            return even

number = [1,2,3,4,5]
print(even_numbers(number))