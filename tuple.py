#
# TUPLE
# 1. tuple은 더 적은 공간을 차지한다.
# 2. 실수로 tuple의 항목이 손상될 염려가 없다.
# 3. tuple은 딕셔너리 키로 사용할 수 있다.
# 4. named tuple은 객체의 단순한 대안이 될 수 있다.
# 5. 함수의 인자들은 tuple로 전달된다.
#

empty_tuple = ()
print(empty_tuple)

one_marx = 'Groucho',
print(one_marx)

marx_tuple = 'Groucho', 'Chico', 'Harpo'
print(marx_tuple)
marx_tuple = ('Groucho', 'Chico', 'Harpo')
print(marx_tuple)

# tuple unpacking
a, b, c = marx_tuple
print("a = " + a)
print("b = " + b)
print("c = " + c)

password = 'swordfish'
icecream = 'tuttifrutti'

print("password: " + password, "icecream: " + icecream)
password, icecream = icecream, password
print("password: " + password, "icecream: " + icecream)

marx_list = ['Groucho', 'Chico', 'Harpo']
print(marx_list)

# marx_list 자체가 tuple로 변경되는 것은 아니다.
print(tuple(marx_list))
print(marx_list)