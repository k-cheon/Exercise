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

# 존재 여부 확인하기: in
print('Groucho' in marxes)
print('Bob' in marxes)

# 값 세기: count()
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes)
print("I'm going to count('Harpo') ...")
print(marxes.count('Harpo'))
print("I'm going to count('Bob') ...")
print(marxes.count('Bob'))

# 문자열로 변환하기: join()
print("\nI'm going to join(marxes) ...")
joined_string = ', '.join(marxes)
print("\n" + joined_string)

friends = ['Groucho', 'Chico', 'Harpo']
separator = ' * '
joined = separator.join(friends)
print("\nNow friends is:")
print(friends)
print("\nI'm going to join friends with ' * '")
print(joined)
print("Again split() it")
separated = joined.split(separator)
print(separated)
print(separated == friends)

# 정렬: sort()
# sort()는 리스트 자체를 내부적으로 정렬한다.
# sorted()는 리스트의 정렬된 복사본을 반환한다.

print("\nsort() and sorted()")
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(marxes)

sorted_marxes = sorted(marxes)
print("sorted marxes")
print(sorted_marxes)
print("original marxes")
print(marxes)

print("\nI'm going to sort(marxes) ...")
marxes.sort()
print(marxes)

print("\nI'm going to sort() numbers")
numbers = [2, 1, 4.0, 3]
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

# 항목 개수 얻기: len()
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(len(marxes))

# 할당: =, 복사: copy()
# 하나의 리스트를 변수 두 곳에 할당했을 경우, 한 리스트를 변경하면 다른 리스트도 변경된다.
# 복사를 한 경우에는 적용되지 않는다.

print("\n---- '=', copy()")
a = [1, 2, 3]
print(a)
print("a를 b에 할당하고 b룰 출력")
b = a
print(b)
print("a[0] 값을 변경한 후 a와 b를 출력")
a[0] = 'surprise'
print(a)
print(b)
print("b[0]값을 변경하고 a와 b를 출력")
b[0] = 'I hate surprise'
print(a)
print(b)

# 할당이 아니라 복사한 경우
print("\n복사한 경우에는 하나의 값을 변경해도 영향을 받지 않는다.")
a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]

a[0] = 'Integer lists are boring'
print(a)
print(b)
print(c)
print(d)