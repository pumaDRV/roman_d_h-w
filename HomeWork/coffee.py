class Coffee:
    size_list = ["S", "M", "L"] 
    
    def __init__(self, size):
        if size not in self.size_list:
            raise ValueError(f"Size must be one of {self.size_list}")
        self.size = size

    def prepare(self):
        return f"Готовим кофе размера {self.size}"

    def price(self):
        if self.size == "S":
            return 100
        elif self.size == "M":
            return 150
        else:  
            return 200


class Latte(Coffee):
    def prepare(self):
        return super().prepare() + " с молоком"


class Espresso(Coffee):
    def price(self):
        return super().price() + 50


if __name__ == "__main__":
    print(f"Допустимые размеры: {Coffee.size_list}")
    
    c = Coffee("M")
    print(c.prepare())  
    print(c.price())    

    l = Latte("L")
    print(l.prepare())  
    print(l.price())    

    e = Espresso("S")
    print(e.prepare())  
    print(e.price())    
