# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)

from datetime import datetime

class MyStr(str):
    """Simple extension of an inbuilt class str.
    Adds time of creation of str and username.
    """
    def __init__(self, word: str) -> None:
        super().__init__()
        self.word = word
        self.time = datetime.now()
        
    def get_user_name(self, username: str) -> None:
        self.name = username
    
    def __str__(self) -> str:
        if self.name is None:
            return f"Error!\nYou must enter a username."
        return f"Username: {self.name}\nTime: {self.time}\n{self.word}"


if __name__ == "__main__":
    s = MyStr("hello")
    s.get_user_name("null")
    print(s)
