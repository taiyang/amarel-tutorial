#! /usr/bin/env python3

"""
This script is for submitting replicated array jobs to Amarel.

Given the possible values of different parameters, the script automatically
generates the input files.
"""

from functools import reduce
from os.path import abspath
from os.path import dirname
from sys import argv

if __name__ == '__main__':

  if len(argv) == 1:
    input_path = abspath('input')
  else:
    input_path = abspath(argv[1])

  file = open(input_path, 'r')
  contents = file.readlines()
  pars = [row.rstrip('\n').split(' ') for row in contents]

  index_bounds = [len(x) for x in pars]
  index = [0 for x in pars]

  total_file_num = reduce( (lambda x, y: x * y), index_bounds)

  for counter in range(total_file_num):
    input_file = open('{}/input.{}'.format(dirname(input_path), counter),
              'w')

    for pid, idx in enumerate(index):
      input_file.write(pars[pid][idx])
      input_file.write('\n')


    input_file.close()

    index[0] += 1

    for i in range(len(pars)-1):
      if index[i] >= index_bounds[i]:
        index[i] = 0
        index[i+1] += 1
      else:
        break

  file.close()
