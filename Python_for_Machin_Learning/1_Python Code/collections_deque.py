"""Collections
- List, Tuple, Dict에 대한 Python Built-in 확장 자료 구조
- from collections import deque
- from collections import Counter
- from collections import OrderedDict
- from collections import defaultdict
- fromm collection import namedtuple"""


from collections import deque

deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(deque_list)


deque_list.appendleft(10)
print(deque_list)


deque_list.rotate(2)
print(deque_list)
deque_list.rotate(2)
print(deque_list)


print(deque_list)
print(deque(reversed(deque_list)))


deque_list.extend([5,6,7])
print(deque_list)
deque_list.extendleft([5,6,7])
print(deque_list)