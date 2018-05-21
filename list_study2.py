#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

cars = ['bmw', 'audi', 'toyota', 'subaru']
for car in cars:
	print(car)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

squares = [value ** 2 for value in range(1,11)]
print(squares)

even_numbers = [number for number in range(2,21,2)]
print(even_numbers)

odd_numbers = [number for number in range(1,21,2)]
print(odd_numbers)

menus = ('coffee', 'tea', 'toast', 'juice', 'egg')
for menu in menus:
	print(menu)

# menus[0] = 'water'
