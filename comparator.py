'''
temp greater than 30 - hot day
otherwise less than 10 - cold day
otherwise neither hot nor cold
'''

#temp = 35
temp = input("enter the temp: ")
if int(temp) > 30:   # >,<,==,!=
    print("Hot day")
elif int(temp) < 10:
    print("Cold day")
else:
    print("neither hot nor cold")
