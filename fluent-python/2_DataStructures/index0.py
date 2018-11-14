#!/use/bin/env python
# -*- coding, utf-8 -*-

import os
import re
import sys

WORD_RE = re.compile('\w+')
zen_txt = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'zen.txt')

index = {}

with open(zen_txt, encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            occurences = index.get(word, [])
            occurences.append(location)
            index[word] = occurences

for word in sorted(index, key=str.upper):
    print(word, index[word])
