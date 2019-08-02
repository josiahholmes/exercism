from typing import List


def slices(series: str, length: int) -> List[str]:
    if 0 < length <= len(series):
        return [series[n:n+length] for n in range(len(series)-length+1)]
    raise ValueError(f'Error in retrieving splices.')
