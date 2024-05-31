
def even_numbers_in_numbers(pass_in_something):
    even_numbers = []
    for numbers in pass_in_something:
        if numbers % 2 == 0:
            even_numbers.append(numbers)
    return even_numbers

numbers = [1,2,3,4,5,6,7,8,9]
print(even_numbers_in_numbers(numbers))