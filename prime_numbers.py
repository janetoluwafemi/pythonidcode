def numbers_in_prime_number(pass_in_something):
    prime = []
    for numbers in pass_in_something:
        for count in range(2,10):
            if numbers % count == 0:
                prime.append(numbers)
    return prime

numbers = [1,2,3,4,5,6,7,8,9]
print(numbers_in_prime_number(numbers))