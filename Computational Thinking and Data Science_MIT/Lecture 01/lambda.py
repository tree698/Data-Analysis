
# (lambda 인자 : 표현식)
a = (lambda x, y: x+y)(10, 20)
print(a)

# map(함수, 리스트)
b = list(map(lambda x: x**2, range(5)))
print(b)

# reduce(함수, 순서형 자료)  (순서형 자료: 문자열 / 리스트 / 튜플)
from functools import reduce
c = reduce(lambda x, y: x+y, [0,1,2,3,4])
print(c)
d = reduce(lambda x, y: y+x, 'abcde')
print(d)
e = reduce(lambda x: x+1, [2])
print(e)

# filter(함수, 리스트)  결과가 참(True)인 값을 리스트로 반환
f = list(filter(lambda x: x < 5, range(10)))
print(f)
g = list(filter(lambda x: x % 2, range(10)))  # 홀수값 반환
print(g)
