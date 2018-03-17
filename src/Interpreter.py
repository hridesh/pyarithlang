'''
This module implements the Read-Eval-Print-Loop of the interpreter with
the help of Reader, Evaluator, and Printer modules. 

@author: Hridesh Rajan
Copyright (c) 2018. All rights reserved.
See LICENSE file in the root directory for licensing information.
'''
import sys

from Reader import Reader
from Evaluator import Evaluator
from Printer import Printer

def main(argv):

    rd = Reader() 
    ev = Evaluator()
    pr = Printer()
    program = rd.read(argv[1])
    pr.prnt(program)
    value = ev.eval(program)
    pr.prnt(value)


if __name__ == '__main__':
    main(sys.argv)
    