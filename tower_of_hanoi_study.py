

# modeling a stack (which represents the towers)

from typing import TypeVar, Generic, List
T = TypeVar('T')

class Stack(Generic[T]):

    def __init__(self) -> None:
        self._container: List[T] = []       # list as a base for storage

    # LIFO (last-in-first-out)

    def push(self, item: T) -> None:        # insert a new item on the stack
        self._container.append(item)

    def pop(self) -> T:                     # remove and return the last item that was inserted
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)

# filling up the stacks (the towers)

num_discs: int = 3
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()
for i in range(1, num_discs + 1):
    tower_a.push(i)

# moving one disc from one tower to another

def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(begin, temp, end, n -1)

# checking if discs were moved

if __name__ == '__main__':
    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)




