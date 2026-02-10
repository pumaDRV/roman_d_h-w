class Developer:
    def __init__(self, level, promotions=0):
        self.level = level
        self.promotions = promotions
        
    def calculate_salary(self, hours_worked):
        if self.level == "Junior":
            hourly_rate = 10
        elif self.level == "Middle":
            hourly_rate = 15
        elif self.level == "Senior":
            hourly_rate = 20 + self.promotions
        else:
            raise ValueError("Некорректный уровень разработчика")
        
        return hourly_rate * hours_worked
    
    def promote(self):
        if self.level == "Senior":
            self.promotions += 1
            print(f"Senior получил повышение! Теперь ставка: {20 + self.promotions} тугриков/час")
        else:
            print(f"Повышение ставки доступно только для Senior")


junior_dev = Developer("Junior")
middle_dev = Developer("Middle")
senior_dev = Developer("Senior")

hours = 160

print("=== Расчет зарплаты за месяц (160 часов) ===")
print(f"Junior: {junior_dev.calculate_salary(hours)} тугриков")
print(f"Middle: {middle_dev.calculate_salary(hours)} тугриков")
print(f"Senior (без повышений): {senior_dev.calculate_salary(hours)} тугриков")

print("\n=== Senior получает повышения ===")
senior_dev.promote()
senior_dev.promote()

print(f"Senior (с 2 повышениями): {senior_dev.calculate_salary(hours)} тугриков")

print("\n=== Расчет за 80 часов ===")
print(f"Senior (с 2 повышениями) за 80 часов: {senior_dev.calculate_salary(80)} тугриков")

dev1 = Developer("Junior")
salary1 = dev1.calculate_salary(40)
print(f"\nJunior за 40 часов: {salary1} тугриков")

dev2 = Developer("Senior", 3)
salary2 = dev2.calculate_salary(120)
print(f"Senior с 3 повышениями за 120 часов: {salary2} тугриков")

dev3 = Developer("Middle")
salary3 = dev3.calculate_salary(200)
print(f"Middle за 200 часов: {salary3} тугриков")