course = ("this is my laptop")
another = (course[:])
#print(course[0:5] + another)
first = "john"
last = "smith"
messsage = first +' ['+ last +'] is a coder'
msg = f'{first} [{last}] is a coder'
print(messsage)
print(msg)
print(len(course))
print(course.upper())
print(course.lower())
print(course.find('i')) #index of 'i' will return
print(course.replace('laptop','new laptop'))
print('is' in course)  #boolean value will return