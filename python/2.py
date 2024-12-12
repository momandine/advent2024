from input import slurp

reports = [[int(x) for x in row.split(' ')] for row in slurp(2).splitlines()]

def is_monotonic(levels: str) -> bool:
    sorted_levels = sorted(levels)
    return sorted_levels == levels or sorted_levels == levels[::-1]

def check_gaps(levels: str) -> bool:
    return all(4 > abs(levels[i] - levels[i + 1]) > 0 for i in range(len(levels) - 1))

# Original
print(sum([is_monotonic(report) and check_gaps(report) for report in reports]))


def check_with_eliminates(rep: str) -> bool:
    if is_monotonic(rep) and check_gaps(rep):
        return True
    for i in range(len(rep)):
            without = rep[:i] + rep[i+1:]
            if is_monotonic(without) and check_gaps(without):
                return True
    return False

print(sum([check_with_eliminates(rep) for rep in reports]))

