age = int(input("Enter a valid age: "))

if age < 0:
    print('Not a valid age')
elif (0 < age) < 18:
    print('You are too young')
elif age == 18:
    print('You have just entered adulthood')
elif (19 < age) < 21:
    print('You are a bachelor')
else:
    print('You are in the economical group')
