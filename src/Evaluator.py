'''
Created on Feb 13, 2018

@author: hridesh
'''

from AST import Visitor
from Value import NumVal

class Evaluator(Visitor):
    def eval(self, program):
        return self.visitProgram(program)

    def visitProgram(self, program):
        print(program.e())
        return program.e().accept(self)

    def visitNumExp(self, numexp):
        return NumVal(numexp.v())