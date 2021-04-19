"""lambda, reduce는 직관성이 떨어져 python3에서는 사용 권장하지 않음. 그러나 여전히 사용 중"""

def f(x,y):
    return x + y
print('#1:', f(1,4))

f2 = (lambda x,y:x+y)(1,4)
f3 = lambda x,y: x+y
print("#2:", f2)
print("#3:", f3(1,4))

"""map: Sequence 자료형의 각 요소에 동일한 function을 적용하여 Sequence 자료형으로 반환"""
ex = [1,2,3,4,5]
f4 = lambda x: x ** 2
print("#4:", list(map(f4, ex)))

f5 = list(map(lambda x: x ** 2, ex))
print("#5:", f5)

f6 = list(map(lambda x: x ** 2 if x > 2 else x, ex))  # if else 사용 가능 / else 반드시 추가
print("#6:", f6)
print("#6-1:", [x ** 2 for x in ex if x > 2])         # map을 굳이 쓰지 않아도 되는 이유 / 어떻게 else 추가?


print("#7:", map(f4, ex))         # 반환값 없음 --> python3 이후는 list를 붙여야 함
for i in map(f4, ex):             # list를 붙이지 않으면 for문으로 출력 가능
    print('#8:', i)

result1 = map(f4, ex)
print('#9:', next(result1))
print('#9:', next(result1))
print('#9:', next(result1))

result2 = list(map(f3, ex, ex))    # 두 개 이상의 list에도 적용 가능
print('#10:', result2)


"""reduce: Sequence 자료형의 각 요소에 동일한 function을 적용한 값을 통합하여 반환"""

from functools import reduce

print("#11:", reduce(lambda x,y: x+y, [1,2,3,4,5]))
print('#12:', reduce(lambda x,y: y+x, 'abcd'))

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n+1))

result3 = factorial(5)
print('#13:', result3)