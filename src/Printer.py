'''
This class implements a printer for AST nodes in 
this programming language that makes use of the 
formatter. The formatter extends the AST visitor
and provides implementation for each case of visit.

@author: Hridesh Rajan
Copyright (c) 2018, All rights reserved.
See LICENSE file in the root directory for licensing information.
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
            return result.rstrip() + ")"

        def visitSubExp(self, subexp):
            result = "(- "
            for operand in subexp.all():
                result += operand.accept(self) + " "
            return result.rstrip() + ")"

        def visitMultExp(self, multexp):
            result = "(* "
            for operand in multexp.all():
                result += operand.accept(self) + " "
            return result.rstrip() + ")"

        def visitDivExp(self, divexp):
            result = "(/ "
            for operand in divexp.all():
                result += operand.accept(self) + " "
            return result.rstrip() + ")"
