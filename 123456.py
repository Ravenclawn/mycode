#!/usr/bin/python3
# -*- coding:utf-8 -*-

import codecs
import sys

if len(sys.argv) > 1:
    FILE=sys.argv[1]
else:
    FILE="hp.txt"

fp = codecs.open(FILE, 'r', 'ASCII')
texts = fp.read()
fp.close()
print(texts)