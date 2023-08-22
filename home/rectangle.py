# Задание №5
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

# Задание №6
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

class Rectangle():
    """Simple rectangel class that can do math operations,
    and logical operations.
    """
    def __init__(self, lenght: float = None, height: float = None, perimeter: float = None) -> None:
        if lenght is None and height is None:
            self.perimeter = perimeter
        else:
            self.area = lenght * height
            self.perimeter = 2 * (lenght + height)
    
    def __add__(self, other):
        return Rectangle(perimeter=(self.perimeter + other.perimeter))
    
    def __sub__(self, other):
        if self.perimeter - other.perimeter > 0:
            return Rectangle(perimeter=(self.perimeter - other.perimeter))
    
    def __mul__(self, other):
        return Rectangle(perimeter=(self.perimeter * other.perimeter))
    
    def __truediv__(self, other):
        return Rectangle(perimeter=(self.perimeter / other.perimeter))
    
    def __str__(self) -> str:
        if self.perimeter is not None:
            return f"{self.perimeter}"
        return f"{self.area}"
    
    def __eq__(self, other) -> bool:
        return True if self.area == other.area else False
    
    def __ne__(self, other) -> bool:
        return True if self.area != other.area else False
    
    def __gt__(self, other) -> bool:
        return True if self.area > other.area else False
    
    def __ge__(self, other) -> bool:
        return True if self.area <= other.area else False
    
    def __lt__(self, other) -> bool:
        return True if self.area < other.area else False
    
    def __le__(self, other) -> bool:
        return True if self.area >= other.area else False
    
    
if __name__ == "__main__":
    ABCD = Rectangle(10, 10, None)
    DCBA = Rectangle(5, 5, None)
    DCAB = Rectangle(100, 100, None)
    
    print(ABCD + DCAB)
    print(ABCD - DCAB)
    print(ABCD * DCBA)
    print(DCAB / ABCD)
    
    print(f"{ABCD == DCAB = }")
    print(f"{ABCD > DCAB = }")
    print(f"{ABCD < DCAB = }")
    print(f"{ABCD != DCAB = }")
