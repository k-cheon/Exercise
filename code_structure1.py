#
alphbet = 'abcdefg' + \
        'hijklmn' + \
        'opqrstu' + \
        'vwxyz'

print(alphbet)

x = 1 + 2 + \
    3

print(x)

#
disaster = True
if disaster:
    print("Woe!")
else:
    print("Whee!")

furry = True
small = True
if furry:
    if small:
        print("It's a cat")
    else:
        print("It's a bear!")
else:
    if small:
        print("It's a skink!")
    else:
        print("It's a human, Or a hairless bear.")

color = "puce"
if color == "read":
    print("It's a tomato")
elif color == "green":
    print("It is a green pepper")
elif color == "bee purple":
    print("I don't know what it is, but only bees can see it")
else:
    print("I've never heard of the color", color)

x = 7
print(x == 5)
print(x == 7)
print(5 < x)
print(x < 10)
print(5 < x and x < 10)
print((5 < x) and (x < 10))
print(5 < x or x < 10)
print(5 < x and x > 10)
print(5 < x and not x > 10)
print(5 < x < 10)
print(5 < x < 10 < 999)

some_list = []
if some_list:
    print("There's something in here")
else:
    print("Hey, it's empty")

count = 1
while count <=5:
    print(count)
    count += 1

'''
while True:
    stuff = input("String to capitalioze [type q to quit!]: ")
    if stuff == 'q':
        break
    print(stuff.capitalize())

while True:
    value = input("Integer, please [q to quit]: ")
    if value == 'q':
        break
    number = int(value)
    if number % 2 == 0:
        continue
    print(number, "squared is", number*number)
'''

numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else:
    print('No even number found')

