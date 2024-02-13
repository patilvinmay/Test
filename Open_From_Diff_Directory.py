import os
import sys


def print_abcdefg_hi(name):
    print_abcdefg(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    sys.path.insert(1, 'C:\\Users\\admin\\Desktop')

from Hello import print_abcdefg_hi

print_abcdefg_hi('Vinu')
