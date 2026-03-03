class SmartString(str):
    def new(cls, value: str = ""):
        if not isinstance(value, str):
            raise TypeError("SmartString value must be str")
        return super().new(cls, value)

    def len(self) -> int:
        return len(set(self))

    def str(self) -> str:
        original_length = str.len(self)
        unique_symbols = len(self)
        return f"{super().str()} (длина: {original_length}, уникальных: {unique_symbols})"

    def add(self, other):
        if isinstance(other, (str, SmartString)):
            if isinstance(other, SmartString):
                other_value = str.str(other)
            else:
                other_value = other

            combined_value = super().add(other_value)
            return SmartString(combined_value)
        return NotImplemented

    def radd(self, other):
        if isinstance(other, (str, SmartString)):
            if isinstance(other, SmartString):
                other_value = str.str(other)
            else:
                other_value = other

            combined_value = other_value + super().str()
            return SmartString(combined_value)
        return NotImplemented


if name == "main":
    print("Проверка SmartString")
    print("-" * 40)

    sample = SmartString("abca")
    print("1) len() и str()")
    print("   len(SmartString('abca')):", len(sample))
    print("   str(SmartString('abca')):", str(sample))
    print()

    left_sum = sample + "de"
    print("2) Сложение SmartString + str")
    print("   Результат:", left_sum)
    print("   Исходная строка результата:", str.str(left_sum))
    print("   Тип результата:", type(left_sum).name)
    print()

    right_sum = "de" + SmartString("abc")
    print("3) Сложение str + SmartString")
    print("   Результат:", right_sum)
    print("   Исходная строка результата:", str.str(right_sum))
    print("   Тип результата:", type(right_sum).name)
    print()

    smart_sum = SmartString("ab") + SmartString("cc")
    print("4) Сложение SmartString + SmartString")
    print("   Результат:", smart_sum)
    print("   Исходная строка результата:", str.str(smart_sum))
    print("   len(результата):", len(smart_sum))
    print("   Тип результата:", type(smart_sum).name)
    print()

    print("5) Проверка ошибки при неверном типе")
    try:
        SmartString(123)
        print("   Ошибка: TypeError не возник")
    except TypeError:
        print("   Ожидаемо: при SmartString(123) возникает TypeError")