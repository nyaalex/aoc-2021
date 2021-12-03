#!/bin/env python3
import argparse
import os


def main():
    template = '''from advent import AdventDay


class Day{day}(AdventDay):

    def __init__(self):
        super().__init__({year}, {day})

    def part_1(self):
        pass
        
    def part_2(self):
        pass


if __name__ == '__main__':
    d{day} = Day{day}()
    d{day}.main()
'''
    parser = argparse.ArgumentParser(description='Generate template code for a new day')
    parser.add_argument('day', type=int)
    parser.add_argument('year')

    args = parser.parse_args()

    code = template.format_map(dict(day=args.day, year=args.year))
    filename = os.path.join(os.getcwd(), 'day%02d.py' % args.day)

    if os.path.exists(filename):
        print('This file already exists')
    else:
        with open(filename, 'x') as file:
            file.write(code)
            print('Created template code in %s'%filename)


if __name__ == '__main__':
    main()
