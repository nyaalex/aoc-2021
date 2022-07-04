import math

import requests
import os
from pyfiglet import Figlet
import re


class AdventDay:

    def __init__(self, year, day):
        # URLs
        self.year = year
        self.day = day
        self.base_url = 'https://adventofcode.com/%s/day/%s' % (year, day)

        self.session = requests.Session()

        # Read secret cookie
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(self.dir_path, 'SECRET_COOKIE'), 'r') as cookie_file:
            secret_cookie = cookie_file.read().strip()

        # Set our cookie
        c = self.session.cookies
        c.set('session', secret_cookie, domain='adventofcode.com')

        # Now get the input as text
        self.day_input = ''
        self.get_input()

        # Define some useful constants
        self.v_neighbours = [
            (0, -1),
            (1, 0),
            (0, 1),
            (-1, 0),
        ]

        # Moore neighbourhood
        self.m_neighbours = [(i // 3 - 1, i % 3 - 1) for i in range(9) if i != 4]

    def get_input(self):
        # check if its been downloaded to the cache
        cache_pathname = os.path.join(self.dir_path, '.cache', '%s-%02d-input.txt' % (self.year, self.day))
        if os.path.exists(cache_pathname):
            with open(cache_pathname) as cache_file:
                self.day_input = cache_file.read()

        else:
            r = self.session.get(self.base_url + '/input')
            self.day_input = r.text

            with open(cache_pathname, 'x') as cache_file:
                cache_file.write(self.day_input)

    def submit(self, submission, level):
        data = {
            'level': level,
            'answer': submission
        }

        r = self.session.post(self.base_url + '/answer', data=data)
        if 'That\'s not the right answer' in r.text:
            print(' * Sowwy u got it wrong >w<, don\'t lose hope though, you got this!!')

        elif 'You gave an answer too recently' in r.text:
            print(' * You gave an answer too recently')

        elif 'That\'s the right answer' in r.text:
            print(' * You got it right!!! one more star for you UwU')
        else:
            print(' * Already Submitted')

    def main(self):
        f = Figlet(justify='center')
        print(f.renderText('%s - DAY %s' % (self.year, self.day)))
        for i in '12':
            print(f' * Now solving part {i}!!')
            if i == '1':
                solution = self.part_1()
            else:
                solution = self.part_2()

            if solution is None:
                print(f' * No solution for part {i}')
                continue

            print(f' * We got a returned  value of {solution}, would you like to submit this answer? (y/n)')
            should_submit = input(':')

            if should_submit == 'y' or should_submit == 'y':
                print(f' * Now submitting part {i} to aoc')
                self.submit(solution, i)

        print(' * All finished!! I hope you have a lovely day!')

    def part_1(self):
        pass

    def part_2(self):
        pass

    # Helper functions:
    def read_lines(self, line_type=str):
        # Basic read lines function
        if line_type == bin:
            line_type = lambda x: int(x, 2)

        return [line_type(i) for i in self.day_input.split('\n') if i]

    def parse_ints(self, one_per_line=False):
        # Get a list of ints per line for every line in the input
        if one_per_line:
            all_ints = re.findall("-?\\d+", self.day_input)
            return list(map(int, all_ints))
        else:
            lines = []
            for line in self.day_input.split('\n'):
                all_ints = re.findall("-?\\d+", line)
                if all_ints:
                    lines.append(list(map(int, all_ints)))

            return lines

    def split_types(self, delim=' ', types=(str, str)):
        # Split each line and convert to the specified types
        out_list = []

        for line in self.day_input.split('\n'):
            line = line.split(delim)
            if len(line) != len(types):
                continue

            fields = []
            for t, v in zip(types, line):
                fields.append(t(v))

            out_list.append(tuple(fields))

        return out_list

    def int_grid(self):
        # Read input as a 2d grid of single digit integers
        return [[int(i) for i in line] for line in self.read_lines()]

    @staticmethod
    def distance(a, b, manhattan=True):
        if manhattan:
            return sum([abs(a_i - b_i) for a_i, b_i in zip(a, b)])
        else:
            return math.sqrt(sum([(a_i - b_i)**2 for a_i, b_i in zip(a, b)]))

    @staticmethod
    def get_neighbours(coord, size, von_neumann=False, wrap=False):

        x, y = coord
        max_x, max_y = size

        if von_neumann:
            n_hood = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        else:
            n_hood = [(i % 3 - 1, i//3 - 1) for i in range(9) if i != 4]

        for dx, dy in n_hood:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx > max_x or ny < 0 or ny > max_y:
                if wrap:
                    nx %= max_x
                    ny %= max_y
                else:
                    continue

            yield nx, ny

