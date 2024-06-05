prime = []
def numbers_in_prime_number(pass_in_something):
    prime_numbers = []
    count = 1
    for prime in pass_in_something:
        if prime % count == 0 and prime % prime == 0:
            prime_numbers.append(prime)
            count = count + 1
    return prime_numbers

for numbers in range(50):
    prime.append(numbers)
print(numbers_in_prime_number(prime))