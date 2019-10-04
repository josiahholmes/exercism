from typing import List


def greater_than_equal_to_row(idx: int, row: List[int]) -> bool:
    num = row[idx]
    row.pop(idx)
    return all(num >= n for n in row)


def less_than_equal_to_column(idx: int, column: List[int]) -> bool:
    num = column[idx]
    column.pop(idx)
    return all(num <= n for n in column)


def saddle_points(matrix: List[List]) -> List[dict]:
    point = {}
    columns = []
    saddle_points = []

    for idx in range(len(matrix)):
        columns.append([row[idx] for row in matrix])

    

matrix = [[4, 5, 4], [3, 5, 5], [1, 5, 4]]
# column = [[4, 3, 1], [5, 5, 5], [4, 5, 4]]
'''
4 5 4
3 5 5
1 5 4
'''
saddle_points(matrix)
