from typing import List


class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = [[int(num) for num in nums.split(' ')]
                       for nums in matrix_string.splitlines()]

    def row(self, index: int) -> List[int]:
        return self.matrix[index-1].copy()

    def column(self, index: int) -> List[int]:
        return [row[index-1] for row in self.matrix]
