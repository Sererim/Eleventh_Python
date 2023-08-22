# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать, 
# ○ сравнения, 
# ○ сложения, 
# ○ *умножения матриц
from copy import deepcopy


class Matrix:
    """Class for basic work with matrixes
    Can print them.
    Compare them.
    Add two matrixes together.
    Multiply two matrixes together."""
    
    def __init__(self, nums:list[list[int]]) -> None:
        if Matrix.right_matrix(nums):
            self.nums = nums
        else:
            print("Error!\nWrong matrix type entered.")
    
    def __str__(self) -> str:
        for i, row in enumerate(self.nums):
            print(f"{i}: [", end=" ")
            for elem in row:
                print(f"{elem }", end=" ")
            print("]")
        return ""
    
    def comparable(self, other) -> bool:
        """Checks if matrixes can be compared or added together."""
        if len(self.nums) == len(other.nums):
            if (len(self.nums[0]) == len(other.nums[0])):
                return True
        return False
            
    def __add__(self, other) -> object:
        """Matrix addition, matrixes must have the same dimension."""
        if Matrix.comparable(self, other):
            result = deepcopy(self.nums)
            for row in range(len(self.nums)):
                for column in range(len(self.nums)):
                    result[row][column] = self.nums[row][column] + other.nums[row][column]
            return Matrix(result)
    
    def __mul__(self, other) -> object:
        """Matrix multiplication using nested list."""
        if len(self.nums[0]) != len(other.nums):
            raise ValueError("Error!\nWrong matrix dimensions")
        
        result = [[sum(a * b for a, b in zip(s_row, o_col))
                        for o_col in zip(*other.nums)]
                                    for s_row in self.nums]
        
        return Matrix(result)
            
    
    def __eq__(self, other) -> bool:
        if Matrix.comparable(self, other):
            for row in range(len(self.nums)):
                for column in range(len(self.nums)):
                    if self.nums[row][column] != other.nums[row][column]:
                        return False
            return True
    
    def __ne__(self, other) -> bool:
        if Matrix.comparable(self, other):
            for row in range(len(self.nums)):
                for column in range(len(self.nums)):
                    if self.nums[row][column] == other.nums[row][column]:
                        return False
            return True
    
    def __gt__(self, other) -> bool:
        if Matrix.comparable(self, other):
            for row in range(len(self.nums)):
                for column in range(len(self.nums)):
                    if self.nums[row][column] > other.nums[row][column]:
                        return False
            return True
    
    def __ge__(self, other) -> bool:
        if Matrix.comparable(self, other):
            for row in range(len(self.nums)):
                for column in range(len(self.nums)):
                    if self.nums[row][column] <= other.nums[row][column]:
                        return False
            return True
    
    def __lt__(self, other) -> bool:
        if Matrix.comparable(self, other):
            for row in range(len(self.nums)):
                for column in range(len(self.nums)):
                    if self.nums[row][column] < other.nums[row][column]:
                        return False
            return True
    
    def __le__(self, other) -> bool:
        if Matrix.comparable(self, other):
            for row in range(len(self.nums)):
                for column in range(len(self.nums)):
                    if self.nums[row][column] >= other.nums[row][column]:
                        return False
            return True
    
    @staticmethod
    def right_matrix(nums) -> bool:
        """Mehtod cheks if matrix is entered correctly.
        For exmaple
        matrix A:
        [1 1 1]
        [2 2  ]
        [3 3 3]
        is incorrectly entered matrix so method will return False."""
        l: list[int] = []
        for i in nums:
            l.append(len(i))
        if len(set(l)) != 1:
            return False
        return True 

if __name__ == "__main__":
    m1 = Matrix([[1, 1, 1],[1, 1, 1],[2, 2, 2]])
    print(m1)
    m2 = Matrix([[0, 0, 0],[1, 1, 1],[2, 2, 2]])
    print(m2)
    print(f"{m1 + m2}")
    print(m1 == m2)
    m3 = Matrix([[1, 1, 1, 1],
                 [2, 2, 2, 2],
                 [3, 3, 3, 3]])
    print(m1 * m3)
