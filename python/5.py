from input import slurp
import pdb
from collections import defaultdict

FULL_DATA = slurp(5)
ENCODED_RULES, ENCODED_PAGES = FULL_DATA.split('\n\n')

def standard_rule_dict():
    rule_dict = defaultdict(set)

    for rule in ENCODED_RULES.splitlines():
        before, after = rule.split('|')
        rule_dict[before].add(after)
    
    return rule_dict

input_pagelists = [pgl.split(',') for pgl in ENCODED_PAGES.splitlines()]


class Page:
    def __init__(self, number, after_list):
        self.number = number
        self.after_list = after_list

    def __lt__(self, other):
        return other.number in self.after_list

class PagelistCheck:

    def __init__(self, rule_dict):
        self.rule_dict = rule_dict

    def check_order(self, pagelist):
        for idx, pg in enumerate(pagelist):
            for value_after in pagelist[idx+1:]:
                if pg in self.rule_dict[value_after]:
                    return False

        return True

    @classmethod
    def middle_value(cls, pagelist):
        return int(pagelist[len(pagelist) // 2])

    def sums(self, all_pagelists):
        valid_sum = 0
        reordered_sum = 0
        for pagelist in all_pagelists:
            if self.check_order(pagelist):
                valid_sum += self.middle_value(pagelist)
            else:
                reordered_sum += self.middle_value(self.reorder(pagelist))
        return valid_sum, reordered_sum


    def reorder(self, pagelist):
        decorated = [Page(n, self.rule_dict[n]) for n in pagelist]
        decorated.sort()
        return [page.number for page in decorated]


checker = PagelistCheck(standard_rule_dict())
print(checker.sums(input_pagelists))

first_row = input_pagelists[0]
print(first_row)
checker = PagelistCheck(standard_rule_dict())
print(checker.check_order(first_row))
print(checker.reorder(first_row))


# test_rules = defaultdict(set, {'1': ['2', '3'], '3': ['2']})

# checker = PagelistCheck(test_rules)

# print(checker.reorder(['1', '2', '3']))



