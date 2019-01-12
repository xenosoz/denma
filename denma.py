#!/usr/bin/env python3
'''Example:
./denma.py -c "line.replace('before', 'after')" input.txt
./denma.py -c "line=line.replace('after', 'after')" input.txt
'''
__author__ = 'Taihyun Hwang <xenosoz.hwang@gmail.com>'

import argparse
import ast
import fileinput
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--command')
parser.add_argument('-i', '--inplace', action='store_true')
parser.add_argument('file', nargs='*')
args = parser.parse_args()


class Runner:
    def __init__(self, command):
        self.command = command
        self.node = ast.parse(self.command)

        expr = isinstance(self.node, ast.Expression)
        expr = expr or (len(self.node.body) == 1 and isinstance(self.node.body[0], ast.Expr))
        self.run = self._run_expr if expr else self._run_stmt

    def _run_expr(self, line):
        globals, locals = dict(), {'line': line}
        return eval(self.command, globals, locals)

    def _run_stmt(self, line):
        globals, locals = dict(), {'line': line}
        exec(self.command, globals, locals)
        return locals['line']

runner = Runner(args.command)


with fileinput.input(files=args.file, inplace=args.inplace) as file:
    for line in file:
        sys.stdout.write(runner.run(line))

