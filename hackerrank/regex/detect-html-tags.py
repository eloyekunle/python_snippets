import re

matches = set()

p = re.compile('<\s*(\w+)')

# p = re.compile('<\\b(\w+)')

# p = re.compile('<\s*([a-zA-Z0-9]+)')

# p = re.compile('<\s*([a-zA-Z0-9]+)\s?(?=[>\w(/>)])')

# p = re.compile('(?<=<)\s?([a-zA-Z]+)\s?(?=[>\w])')

for _ in range(int(input())):
    m = p.findall(input())
    matches.update(m)

print(';'.join(sorted(matches)))