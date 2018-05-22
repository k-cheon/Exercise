# Create dictionary

empty_dict = {}
print(empty_dict)

bierce = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses"
}

print(bierce)

# Convert to dictionary
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(lol)
print(dict(lol))
# lol 자체가 변경되는 것은 아니다.
print(lol)

lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
print(lot)
print(dict(lot))
tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
print(tol)
print(dict(tol))

print("")
los = ['ab', 'cd', 'ef']
print(los)
print(dict(los))
tos = ('ab', 'cd', 'ef')
print(tos)
print(dict(tos))

# 항목 추가/변경 하기: [key]
pythons = {
    'Champman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}
print()
print(pythons)
pythons['Gilliam'] = 'Gerry'
print(pythons)
pythons['Gilliam'] = 'Terry'
print(pythons)

# dictionary 결합하기: update()
others = {'Marx': 'Groucho', 'Howard': 'Moe'}
pythons.update(others)
print(pythons)

first = {'a': 1, 'b': 2}
second = {'b': 'platypus'}
print(first)
print(second)
print("Now first.update(second)")
first.update(second)
print(first)

# key와 del로 항목 삭제하기
del pythons['Marx']
print(pythons)
del pythons['Howard']
print(pythons)

# in
print('Champman' in pythons)
print('HHH' in pythons)

# clear()
print()
pythons.clear()
print(pythons)
pythons.update(others)
print(pythons)
pythons = {}
print(pythons)
