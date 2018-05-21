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