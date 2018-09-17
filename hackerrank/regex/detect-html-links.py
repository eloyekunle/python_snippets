"""
https://www.hackerrank.com/challenges/detect-html-links/problem
"""

import re

p = re.compile('<a href="(.*?)".*?>\s?([\w ,./]*?)\s?(?=</)')

for _ in range(int(input())):
    m = p.findall(input())
    for l,t in m:
        print('{},{}'.format(l,t))