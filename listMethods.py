numbers = [5,2,8,9,2,4]
numbers.append(20) # so it will append a number 20 to the list
print(numbers)
numbers.insert(0,10)  # the number 10 will be added to the 1st position of the list
print(numbers)
numbers.remove(9)
print(numbers)
# numbers.clear() # clears the list
# print(numbers)
numbers.pop() # removes the last number in the list, ie 20
print(numbers)
print(numbers.index(8)) # it is 3
print(50 in numbers) # the output will be boolean, 50 is not in the list
print(numbers.count(2)) # the output is 2. since there are two 2's in the list
numbers.sort() # sort all the number in the list in ascending order
print(numbers)
numbers.reverse() # in descending method
print(numbers)

numbers2= numbers.copy()
numbers.append(9)
print(numbers2) # numbers will be copied in number2