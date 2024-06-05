word = []
def length_of_number(number):
    count = 0
    for word in number:
        count = count + 1
    return count

word = "semicolon"
print(length_of_number(word))