class Rectangle:
    def __init__(self, p1, p2):
        """Инициализация прямоугольника по двум противоположным углам"""
        x1, y1 = p1
        x2, y2 = p2
        

        self.left = min(x1, x2)   # Определяем границы прямоугольника
        self.right = max(x1, x2)
        self.top = max(y1, y2)    # ось Y вверх
        self.bottom = min(y1, y2)
    
    def get_pos(self):
        """Возвращает координаты верхнего левого угла"""
        return (round(self.left, 2), round(self.top, 2))
    
    def get_size(self):
        """Возвращает размеры прямоугольника (ширина, высота)"""
        width = self.right - self.left
        height = self.top - self.bottom
        return (round(width, 2), round(height, 2))
    
    def move(self, dx, dy):
        """Перемещает прямоугольник на dx, dy"""
        self.left += dx
        self.right += dx
        self.top += dy
        self.bottom += dy
    
    def resize(self, width, height):
        """Изменяет размеры (левый верхний угол остается на месте)"""
        self.right = self.left + width
        self.bottom = self.top - height
    
    def turn(self):
        """Поворачивает на 90° по часовой стрелке относительно центра"""
        center_x = (self.left + self.right) / 2    # Находим центр
        center_y = (self.top + self.bottom) / 2
        
        width = self.right - self.left
        height = self.top - self.bottom
        
    
        new_width = height    # Меняем местами ширину и высоту
        new_height = width
        
    
        self.left = center_x - new_width / 2    # Новые границы
        self.right = center_x + new_width / 2
        self.top = center_y + new_height / 2
        self.bottom = center_y - new_height / 2
    
    def scale(self, factor):
        """Масштабирует относительно центра"""
        center_x = (self.left + self.right) / 2    # Находим центр
        center_y = (self.top + self.bottom) / 2
        
        width = self.right - self.left    # Текущие размеры
        height = self.top - self.bottom
        
        new_width = width * factor    # Новые размеры
        new_height = height * factor
        
        self.left = center_x - new_width / 2    # Новые границы
        self.right = center_x + new_width / 2
        self.top = center_y + new_height / 2
        self.bottom = center_y - new_height / 2
    
    def perimeter(self):
        """Возвращает периметр прямоугольника"""
        width = self.right - self.left
        height = self.top - self.bottom
        return round(2 * (width + height), 2)
    
    def area(self):
        """Возвращает площадь прямоугольника"""
        width = self.right - self.left
        height = self.top - self.bottom
        return round(width * height, 2)


print("=== Тест задания 1 ===")
rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(f"Периметр: {rect.perimeter()}")
print(f"Площадь: {rect.area()}")
    
print("\n=== Тест задания 2 ===")
print(f"Позиция: {rect.get_pos()}")
print(f"Размер: {rect.get_size()}")
    
rect.move(1, 1)
print(f"После перемещения (1, 1): {rect.get_pos()}")
   
rect.resize(5, 5)
print(f"После изменения размера (5, 5): {rect.get_size()}")
    
print("\n=== Тест задания 3 ===")
rect2 = Rectangle((0, 0), (4, 2))
print(f"Начальная позиция: {rect2.get_pos()}")
print(f"Начальный размер: {rect2.get_size()}")
    
rect2.turn()
print(f"После поворота: {rect2.get_size()}")
print(f"Площадь после поворота: {rect2.area()}")
    
rect2.scale(2)
print(f"После масштабирования 2x: {rect2.get_size()}")
print(f"Площадь после масштабирования: {rect2.area()}")