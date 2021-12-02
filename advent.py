import requests
import os
from pyfiglet import Figlet
import re


class AdventDay:
    _YEAR = 2021

    def __init__(self, day):
        # URLs
        self.day = day
        self.base_url = 'https://adventofcode.com/%s/day/%s' % (self._YEAR, day)

        self.session = requests.Session()

        # Read secret cookie
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path, 'SECRET_COOKIE'), 'r') as cookie_file:
            secret_cookie = cookie_file.read().strip()

        # Set our cookie
        c = self.session.cookies
        c.set('session', secret_cookie, domain='adventofcode.com')

        # Now get the input as text
        r = self.session.get(self.base_url + '/input')
        self.day_input = r.text

    def submit(self, submission, level):
        return 'Yep'
        pass

    def main(self):
        f = Figlet(justify='center')
        print(f.renderText('DAY: %s' % self.day))
        for i in '12':
            print(f' * Now solving part {i}!!')
            if i == '1':
                solution = self.part_1()
            else:
                solution = self.part_2()

            print(f' * We got a returned  value of {solution}, would you like to submit this answer? (y/n)')
            should_submit = input(':')

            if should_submit == 'y' or should_submit == 'y':
                print(f' * Now submitting part {i} to aoc')
                result = self.submit(solution, 1)
        print(' * All finished!! I hope you have a lovely day!')

    def part_1(self):
        return 'UNDEFINED'

    def part_2(self):
        return 'UNDEFINED'

    # Helper functions:
    def parse_ints(self, one_per_line=False):
        # Get a list of ints per line for every line in the input
        if one_per_line:
            all_ints = re.findall("\\d+", self.day_input)
            return list(map(int, all_ints))
        else:
            lines = []
            for line in self.day_input.split('\n'):
                all_ints = re.findall("\\d+", line)
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
