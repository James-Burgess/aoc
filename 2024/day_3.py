import collections
import itertools
import re

import pandas as pd
import numpy as np

from utils import InputFile


def part_1():
    file = InputFile("3")

    print(file)
    print(len(file))

    text = ''.join(file.lines)
    x = re.findall("mul\(\d{1,3},\d{1,3}\)", text)
    cnt = 0
    for i in x:
        c = re.findall("\d+", i)
        cnt += int(c[0]) * int(c[1])

    print(cnt)


def part_2():
    file = InputFile("3")

    print(file)
    print(len(file))

    text = ''.join(file.lines)

    st = text.split("don't()")
    vb = st[0]
    for i in st[1:]:
        j = i.split("do()")
        if len(j) > 1:
            vb += ''.join(j[1:])

    print(vb)

    x = re.findall("mul\(\d{1,3},\d{1,3}\)", vb)
    cnt = 0
    for i in x:
        c = re.findall("\d+", i)
        cnt += int(c[0]) * int(c[1])

    print(cnt)


if __name__ == "__main__":
    part_1()
    part_2()
