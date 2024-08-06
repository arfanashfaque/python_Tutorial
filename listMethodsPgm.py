numbers = [2,1,5,5,3,4,3,1,4]
print(numbers)
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
uniques.sort()
print(uniques)