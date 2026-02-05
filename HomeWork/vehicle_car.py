class Vehicle:
    def __init__(self, brand: str, speed: int):
        self.brand = brand
        self.speed = speed
    
    def info(self):
        return f"{self.brand}, скорость {self.speed} км/ч"
    
    def is_fast(self):
        return self.speed > 100


class Car(Vehicle):
    def __init__(self, brand: str, speed: int, fuel: float):
        super().__init__(brand, speed)
        self.fuel = fuel
    
    def drive(self, km: int):
        fuel_needed = km * 0.1
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
            return f"{self.info()}. Проехали {km} км, топлива: {self.fuel}"
        else:
            return "Недостаточно топлива"


car = Car("Тойота", 120, 10)
print(car.is_fast())    
print(car.drive(50))    
print(car.drive(100))   
