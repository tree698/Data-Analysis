"""* : 곱셈, 제곱연산, 가변인자/키워드인자, unpacking에 활용"""

def asterisk_test1(a, *args):  # *args(가변 인자): 남은 값을 한번에 튜플로 받음
    print(a, args)             # 여러개 값을 한번에 받을 수 있음
    print(type(args))
asterisk_test1(1,2,3,4,5,6)
# 1 (2, 3, 4, 5, 6)
# <class 'tuple'>

def asterisk_test3(a, *args):
    print(a, args)
    print(a, args[0])
    print(type(args))
asterisk_test3(1, (2,3,4,5,6))
# 1 ((2, 3, 4, 5, 6),)          # 투플 type 안에 하나의 튜플이 존재 / 쉼표 확인
# 1 (2, 3, 4, 5, 6)             # args[0] 첫번째 원소
# <class 'tuple'>


def asterisk_test2(a, **kargs):
    print(a, kargs)
    print(type(kargs))
asterisk_test2(1, b=2, c=3, d=4, e=5)   # **args(키워드 인자): 남은 값을 한번에 dict로 받음
# 1 {'b': 2, 'c': 3, 'd': 4, 'e': 5}
# <class 'dict'>



"""asterrisk의 unpacking 기능"""

def asterisk_test4(a, args):    # args는 (2,3,4,5,6)을 튜플 형태로 받음
    print(a, *args)             # *args는 튜플을 각각 원소로 풀어버림
    #print(a, *args[0])         # 각각의 원소가 되므로 args[0]는 에러 발생
    print(type(args))
asterisk_test4(1, (2,3,4,5,6))
# 1 2 3 4 5 6
# <class 'tuple'>



a,b,c = ([1,2], [3,4], [5,6])   # unpacking 방법
print(a,b,c)
# [1, 2] [3, 4] [5, 6]
data = ([1,2], [3,4], [5,6])    # asterisk를 이용한 unpacking 방법
print(*data)
# [1, 2] [3, 4] [5, 6]




def asterisk_test5(a,b,c,d):
    print(a,b,c,d)
data1 = {"b":1, "c":2, "d":3}
asterisk_test5(10, **data1)    # **를 이용한 unpacking 방법
# 10 1 2 3


for i in zip(*([1,2],[3,4],[5,6])): # (1, 3, 5) (2, 4, 6)로 분해
    print(sum(i))
# 9
# 12

def asterisk_test6(a, b, c, d, e=0):
    print(a, b, c, d, e)
data2 = {"d":1, "c":2, "b":3, "e":56}
asterisk_test6(10, **data2)
# 10 3 2 1 56