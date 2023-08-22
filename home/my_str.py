# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)

from datetime import datetime
from getpass import getuser

class MyStr(str):
    """Simple extension of an inbuilt class str.
    Adds time of creation of str and username.
    """
    def __new__(cls, string):
        instance = super().__new__(cls, string)
        instance.name = getuser()
        instance.time = datetime.now()
        return instance
    

if __name__ == "__main__":
    s = MyStr("Hello, World!")
    print(s, s.name, s.time)
