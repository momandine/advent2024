import re
from typing import List

from input import slurp

text = slurp(3)

do_chunks = text.split("do()")
do_these = [chunk.split("don't()")[0] for chunk in do_chunks]
minus_donts = "".join(do_these)

def evalute(mult_str: str) -> int:
    nums = re.findall("\d{1,3}", mult_str)
    assert len(nums) == 2
    return int(nums[0]) * int(nums[1])

def find_multiplications(string: str) -> List[str]:
    to_match = "mul\(\d{1,3},\d{1,3}\)"
    return re.findall(to_match, string)

print(sum([evalute(match) for match in find_multiplications(minus_donts)]))
