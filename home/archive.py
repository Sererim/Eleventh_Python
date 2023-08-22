# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

class Archive:
    """Archive class that gets int and str. Keeps it.
    If new example of class is made it saves old data."""
    
    _list_of_nums: list[int] = []
    _list_of_strings: list[str] = []
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._list_of_nums = []
            cls._instance._list_of_strings = []
        else:
            cls._list_of_nums.append(cls._instance.num)
            cls._list_of_strings.append(cls._instance.string)
        return cls._instance
    
    def __init__(self, num: int, string: str) -> None:
        self.num = num
        self.string = string
        
        Archive._list_of_nums.append(self.num)
        Archive._list_of_strings.append(self.string)
        
    
    def __str__(self) -> str:
        """Information for user."""
        return f"{self.num} : {self.string}"
    
    def __repr__(self) -> str:
        """Information for programmist."""
        return f"{self.get_data()}\n"
    
    def get_data(self):
        return f"{Archive._list_of_nums}\n{Archive._list_of_strings}"
    

    
if __name__ == "__main__":
    a = Archive(20, "Hello")
    b = Archive(30, "World!")
    print(a)
    print(b)
    print(a.get_data())
    print(repr(a))
