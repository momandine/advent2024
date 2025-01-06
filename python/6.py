from input import slurp
from copy import deepcopy

map = [[cell for cell in row] for row in slurp(6).splitlines()]


# Starting, will go upwards only
# Every time we 

GUARD_CHAR = '^'
BLOCKAGE = '#'
ROTATION_CYCLE = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIRECTIONS = len(ROTATION_CYCLE)

def determine_starting_position(map):
    for row, values in enumerate(map):
        if GUARD_CHAR in values:
            return (row, values.index(GUARD_CHAR))
    raise ValueError("Guard Not Found")


class Guard:
    OFF_MAP = 0
    CYCLE = 1

    def __init__(self, map):
        self.map = map
        self.row, self.col = determine_starting_position(map)
        self.rotation_index = 0
        self.visited = set([self.position_tuple])

    @property
    def position_tuple(self):
        return (self.row, self.col, self.rotation_index)

    def turn(self):
        self.rotation_index = (self.rotation_index + 1) % DIRECTIONS
    
    def move(self):
        row_offset, col_offset = ROTATION_CYCLE[self.rotation_index % DIRECTIONS]
        next_row = self.row + row_offset
        next_col = self.col + col_offset

        # Guard is off the map
        if next_row < 0 or next_col < 0:
            return self.OFF_MAP
        if next_row >= len(self.map) or next_col >= len(self.map[0]):
            return self.OFF_MAP
        
        if self.map[next_row][next_col] == BLOCKAGE:
            self.turn()
        else:
            self.row = next_row
            self.col = next_col

        if self.position_tuple in self.visited:
            return self.CYCLE

        self.visited.add(self.position_tuple)
    
    def explore(self):
        value = None
        while value is None:
            value = self.move()
        
        return value
    
guard = Guard(map)

cycling_block_counts = 0
              
for row, values in enumerate(map):
    for col, cell in enumerate(values):
        if cell == GUARD_CHAR:
            continue

        map_copy = deepcopy(map)
        map_copy[row][col] = BLOCKAGE

        guard = Guard(map_copy)
        value = guard.explore()
        print(row, col, value)
        cycling_block_counts += value
        

#print(len(guard.visited))
print(cycling_block_counts)