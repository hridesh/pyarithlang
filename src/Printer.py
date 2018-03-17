'''
Created on Feb 13, 2018

@author: hridesh
'''
from AST import Visitor
from AST import AST

class Printer:

    def prnt(self,obj):
        if type(obj) is AST.Program:
            print(Printer.Formatter().visit(obj))
        else: 
            print(obj)

    class Formatter(Visitor):

        def visitProgram(self, program):
            return program.e().accept(self)

        def visitNumExp(self, numexp):
            return str(numexp.val)
 
        def visitAddExp(self, addexp):
            result = "(+ "
            for operand in addexp.all():
                result += operand.accept(self) + " "
            return result + ")"

        def visitSubExp(self, subexp):
            result = "(- "
            for operand in subexp.all():
                result += operand.accept(self) + " "
            return result + ")"

        def visitMultExp(self, multexp):
            result = "(* "
            for operand in multexp.all():
                result += operand.accept(self) + " "
            return result + ")"

        def visitDivExp(self, divexp):
            result = "(/ "
            for operand in divexp.all():
                result += operand.accept(self) + " "
            return result + ")"
