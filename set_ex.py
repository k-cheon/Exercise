# create

empty_set = set()
print(empty_set)

even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers)
print(odd_numbers)

# 데이터 타입 변환하기: set()
print(set('letters'))

lists = ['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon']
lists_to_set = set(lists)
print(lists)
print(lists_to_set)

tuples = ('Ummagumma', 'Echoes', 'Atom Heart Mother')
tuples_to_set = set(tuples)
print(tuples)
print(tuples_to_set)

dictionaries = {'apple': 'red', 'orange': 'orange', 'cherry': 'red'}
dictionaries_to_set = set(dictionaries)
print(dictionaries)
print(dictionaries_to_set)

# in

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}

for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

print()
for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)

print()
# combination, set intersection operator
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)

print()
for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)

bruss = drinks['black russian']
wruss = drinks['white russian']
print()
print(drinks)
print(bruss)
print(wruss)

a = {1, 2}
b = {2, 3}
print(a & b)
print(a.intersection(b))
print(bruss & wruss)

# unions
print()
print(a | b)
print(a.union(b))
print(bruss | wruss)

# differenct
print()
print(a - b)
print(a.difference(b))
print(bruss)
print(wruss)
print(bruss - wruss)
print(wruss - bruss)

# ^ symmetric_difference(), exclusive
print()
print(a ^ b)
print(a.symmetric_difference(b))
print(bruss ^ wruss)

# <=, issubset()
print()
print(a)
print(b)
print(bruss)
print(wruss)
print(a <=b)
print(a.issubset(b))
print(bruss <= wruss)

# 첫 번째 셋이 두번째 셋의 proper subset(진부분집합)이 될려면,
# 두 번쨰 셋에는 첫 번째 셋의 모든 멤버를 포함한 그 이상의 멤버가 있어야 한다.
print()
print(b)
print(b)
print(a < b)
print(a < a)
print(bruss < wruss)

# 슈퍼셋은 서브셋의 반대
# >= or issuperset()
print()
print(a >= b)
print(a.issuperset(b))
print(wruss >= bruss)

# 모든 셋은 자신의 수퍼셋이다.
print(a >= a)
print(a.issuperset(a))

# proper superset >
print()
print(a > b)
print(a > a)
print(wruss > bruss)

# 복습
# list: []
# tuple: '
# dictionary: {}

marx_list = ['Groucho', 'Chico', 'Harpo']
marx_tuple = 'Groucho', 'Chico', 'Harpo' # ('Groucho', 'Chico', 'Harpo')
marx_dict = {'Groucho': 'banjo', 'Chico': 'piano', 'Harpo': 'harp'}

print()
print(marx_list[2])
print(marx_tuple[2])
print(marx_dict['Harpo'])

#
marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['Chapman', 'Clesse', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']

tuples_of_lists = marxes, pythons, stooges
print()
print(marxes)
print(pythons)
print(stooges)
print(tuples_of_lists)

list_of_lists = [marxes, pythons, stooges]
print()
print(marxes)
print(pythons)
print(stooges)
print(list_of_lists)

dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooges}
print()
print(marxes)
print(pythons)
print(stooges)
print(dict_of_lists)

houses = {
    (44.79, -93.14, 285): 'My House',
    (38.89, -77.03, 130): 'The White House'
}
print()
print(houses)