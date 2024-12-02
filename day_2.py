import collections
import itertools
import re

import pandas as pd
import numpy as np

from utils import InputFile


def part_1():
    file = InputFile("d2.txt")

    print(file)
    print(len(file))
    print(file.to_num()[:10])


def part_2():
    ...


if __name__ == "__main__":
    part_1()
    part_2()
