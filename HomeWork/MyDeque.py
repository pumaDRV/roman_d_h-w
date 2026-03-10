class MyDeque:
    def __init__(self, items=None):
        if items is None:
            self._items = []
        else:
            self._items = list(items)

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return f"Deque({self._items})"

    def __repr__(self):
        return str(self)

    def append(self, x):
        # Добавляем элемент в правый конец.
        self._items.append(x)

    def appendleft(self, x):
        # Добавляем элемент в левый конец.
        self._items.insert(0, x)

    def pop(self):
        # Удаляем элемент из правого конца.
        if len(self._items) == 0:
            raise IndexError("pop from an empty deque")

        return self._items.pop()

    def popleft(self):
        # Удаляем элемент из левого конца.
        if len(self._items) == 0:
            raise IndexError("popleft from an empty deque")

        return self._items.pop(0)


if __name__ == "__main__":
    print("Проверка MyDeque")
    print("-" * 40)

    queue = MyDeque([1, 2, 3])
    print("Начальная очередь:", queue)
    print("Длина очереди:", len(queue))
    print()

    queue.append(4)
    print("После append(4):", queue)

    queue.appendleft(0)
    print("После appendleft(0):", queue)
    print()

    right_value = queue.pop()
    print("pop() вернул:", right_value)
    print("Очередь после pop():", queue)

    left_value = queue.popleft()
    print("popleft() вернул:", left_value)
    print("Очередь после popleft():", queue)