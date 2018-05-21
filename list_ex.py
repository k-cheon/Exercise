#
# list 생성하기: [] or list()
#
empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_bird = ['emu', 'ostrich', 'cassowary']
first_name = ['Graham', 'John', 'Terry', 'Terry', 'Michael']

another_empty_list = ()
print(another_empty_list)

#
# 다른 데이터 타입을 리스트로 변환하기: list()
#
print(list('cat'))

a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))

birthday = '1/6/1998'
print(birthday.split('/'))

splitme = 'a/b//c/d//e'
print(splitme.split('/'))
print(splitme.split('//'))

#
# [offset]으로 항목 얻기
#
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0])
print(marxes[1])
print(marxes[2])
print(marxes[-1])
print(marxes[-2])
print(marxes[-3])

#
# 리스트의 리스트
#
small_birds = ['humingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, carol_birds]
print(all_birds)
print(all_birds[0])
print(all_birds[1])
print(all_birds[2])
print(all_birds[1][0])

# [offset]으로 항목 바꾸기
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes)
marxes[2] = 'Wanda'
print(marxes)

# 슬라이스로 항목 추출하기
print(marxes[0:2])
print(marxes[::2])
print(marxes[::-2])
print(marxes[::-1])

# 리스트 끝에 항목 추가하기: append()
marxes.append('Zeppo')
print(marxes)

# 리스트 병합하기: extend() or +=
others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes)

marxes += others
print(marxes)
marxes.append(others)
print(marxes)

# offset과 insert()로 항목 추가하기
marxes = ['Groucho', 'Chico', 'Wanda', 'Zeppo']
print(marxes)
marxes.insert(3, 'Gummo')
print(marxes)
marxes.insert(-1, 'Karl')
print(marxes)
marxes.insert(10, 'CHEON')
print(marxes)

# offset으로 항목 삭제하기: del
del marxes[-1]
print(marxes)

# 값으로 항목 삭제하기: remove()
print("\nI'm going to remove() 'Gummo' ...")
marxes.remove('Gummo')
print(marxes)

# offset으로 항목을 얻은 후 삭제하기: pop()
print("\nI'm going to pop() ...")
print(marxes.pop())
print(marxes)

print("\nI'm going to pop(1) ...")
print(marxes.pop(1))
print(marxes)

# 값으로 항목 offset 찾기: index()
marxes = ['Groucho', 'Chico', 'Wanda', 'Zeppo']
print(marxes)
print("\nI'm going to index('Chico') ...")
marxes.index('Chico')
print(marxes.index('Chico'))