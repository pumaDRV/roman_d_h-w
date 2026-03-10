class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __len__(self):
        squared_x = self.x  
        squared_y = self.y  
        length_value = (squared_x + squared_y) ** 0.5
        rounded_length = round(length_value)
        return rounded_length

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        # Складываем два вектора покоординатно.
        if isinstance(other, Vector2D):
            new_x = self.x + other.x
            new_y = self.y + other.y
            result_vector = Vector2D(new_x, new_y)
            return result_vector

        raise TypeError

    def __eq__(self, other):
        # Векторы равны, если совпадают обе координаты.
        if isinstance(other, Vector2D):
            x_is_equal = self.x == other.x
            y_is_equal = self.y == other.y
            return x_is_equal and y_is_equal

        raise TypeError


if __name__ == "__main__":
    print("Проверка Vector2D")
    print("-" * 40)

    first = Vector2D(3, 4)
    second = Vector2D(1, 2)
    third = Vector2D(3, 4)

    print("1) Красивый вывод")
    print("   first:", first)
    print("   second:", second)
    print()

    print("2) len (длина вектора, округленная до целого)")
    print("   len(Vector2D(3, 4)):", len(first))
    print("   len(Vector2D(1, 2)):", len(second))
    print()

    print("3) Сложение векторов")
    sum_vector = first + second
    print("   first + second =", sum_vector)
    print("   Координаты суммы:", sum_vector.x, sum_vector.y)
    print()

    print("4) Сравнение векторов")
    print("   first == second:", first == second)
    print("   first == third:", first == third)