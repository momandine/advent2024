from input import slurp

text = slurp(1)
rows = text.splitlines()

col1 = []
col2 = []

for r in rows:
  left, right = r.split('   ')
  col1.append(int(left))
  col2.append(int(right))

col1.sort()
col2.sort()

print(sum([abs(col1[i] - col2[i]) for i in range(len(col1))]))
print(sum([x * col2.count(x) for x in col1]))
   