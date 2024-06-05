numbers_in_a_list = []
def finding_odd_numbers(pass_in_something):
    odd_numbers = []
    for numbers_in_a_list in pass_in_something:
        if numbers_in_a_list % 2 == 1:
            odd_numbers.append(numbers_in_a_list)
    return odd_numbers


for numbers in range(0,50):
    numbers_in_a_list.append(numbers)
print(finding_odd_numbers(numbers_in_a_list))