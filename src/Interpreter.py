'''
Created on Feb 13, 2018

@author: hridesh
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
    
    
    
#    print "Type a program to evaluate and press the enter key," + \
#        " e.g. ((lambda (av bv cv) (let ((a av) (b bv) (c cv) (d 279) (e 277)) (+ (* a b) (/ c (- d e))))) 3 100 84) \n" + \
#        "Type (quit) to exit."
