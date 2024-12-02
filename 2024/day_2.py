import collections
import itertools
import re
import copy

import pandas as pd
import numpy as np

from utils import InputFile


def part_1():
    file = InputFile("2")

    print(file)
    print(len(file))
    print(file.to_num()[:10])

    cnt = 0
    for line in file.to_num():
        if line == sorted(line) or line == list(reversed(sorted(line))):
            print(line)
            cur = line[0]
            lc = 0
            for num in line[1:]:
                if 1 <= abs(cur - num) <= 3:
                    lc += 1
                cur = num

            if lc == len(line) - 1:
                cnt += 1

    print(cnt)


def part_2():
    file = InputFile("2")

    print(file)
    print(len(file))
    print(file.to_num()[:10])
    cnt = 0
    for line in file.to_num():
        if test(line):
            cnt += 1
        else:
            for i in range(len(line)):
                new_line = copy.copy(line)
                del new_line[i]
                if test(new_line):
                    print(new_line)
                    cnt += 1
                    break

    print(cnt)


def test(line):
    if line == sorted(line) or line == list(reversed(sorted(line))):
        cur = line[0]
        lc = 0
        for num in line[1:]:
            if 1 <= abs(cur - num) <= 3:
                lc += 1
            cur = num

        return lc == len(line) - 1
    return False

if __name__ == "__main__":
    # part_1()
    part_2()
