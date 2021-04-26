"""sort()는 리스트 자체를 정렬해서 반환"""
"""sorted()는 리스트 자체는 그냥 두고 정렬된 새로운 리스트를 반환 """
"""sorted(리스트, key=(딕셔너리)정렬기준, reverse=False(오름차순)"""

a = [2, 4, 1, 9, 100, 29, 40, 10]

b = sorted(a)
c = sorted(a, reverse=True)
# 아무것도 출력되지 않음
#d = a.sort()

e = [2, 4, 1, 9, 100, 29, 40, 10]
e.sort()


print("a:", a)
print("b:", b)
print("c:", c)
#print("d:", d)
print("a:", a)
print("e:", e)
