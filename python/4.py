from input import slurp
from typing import List

orientations = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, 1), (1, 0), (1, -1)]
next_letter_offsets = [("M", 1), ("A", 2), ("S", 3)]

def check_direction(vert: int, horiz: int, i: int, j: int, grid: List[str]) -> bool:
    for char, mutliplier in next_letter_offsets:
        x = vert * mutliplier + i
        y = horiz * mutliplier + j

        # Overflow vertically 
        if x >= len(grid) or x < 0:
          return False

        # Overflow horzontally
        if y >= len(grid[0]) or y < 0:
            return False

        if grid[x][y] != char:
             return False
    return True


# M S
# .A
# S M

# find Xes
# look all directions for Xes from there

def search_for_xmas(i: int, j: int, grid: List[str]):
    return sum(check_direction(vert, horiz, i, j, grid) for vert, horiz in orientations)

diagonals = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
valid_mas = ["MMSS", "SSMM", "SMSM", "MSMS"]

def search_for_cross_mas(i: int, j: int, grid: List[str]):
    collector = ""
    for vert, horiz in diagonals:
        x = i + vert
        y = j + horiz

        if x < 0 or x >= len(grid):
            return 0 

        if y < 0 or y >= len(grid[0]):
            return 0
        collector += grid[x][y]
        
    chars = "".join(collector)
    print(chars)
    if chars in valid_mas:
        return 1

    return 0

def count_xmas(grid: List[str], critical_char="X", count_from_location=search_for_xmas) -> int:
    total = 0
    for i in range(len(grid)):
        # Could use find instead
        for j in range(len(grid[i])):
            if grid[i][j] == critical_char:
                total += count_from_location(i, j, grid)
    return total

# print(count_xmas(["XMAS"]))
# print(count_xmas(["SAMX"]))
# print(count_xmas(["SMAX"]))
# print(count_xmas(["X", "M", "A", "S"]))
# print(count_xmas(["S", "A", "M", "X"]))
# print(count_xmas(["SAMX", "..M.", ".A..", "S..."]))

#print(count_xmas(slurp(4).splitlines()))

test_matrix = [
    "M.S",
    ".A.",
    "M.S"
]


print(count_xmas(slurp(4).splitlines(), "A", search_for_cross_mas))



