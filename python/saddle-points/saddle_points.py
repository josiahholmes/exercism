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
    columns = []
    saddle_points = []

    if matrix:
        for idx in range(len(matrix)):
            columns.append([row[idx] for row in matrix])

        for row in matrix:
            for i in range(len(row)):
                if greater_than_equal_to_row(i, row.copy()) and less_than_equal_to_column(i, columns[i].copy()):
                    saddle_points.append(
                        {"row": matrix.index(row) + 1, "column": i + 1})
                else:
                    saddle_points = [{}]
        if {} not in saddle_points:
            saddle_points = list(
                {sp['row']: sp for sp in saddle_points}.values())
    else:
        saddle_points = [{}]
    return saddle_points
