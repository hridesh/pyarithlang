'''
This class implements the semantics of this small programming language.
It does so by providing the semantics of each expression (and declaration)
in the language. The semantics of each expression is given by defining how 
the expression is evaluated to a value.

@author: Hridesh Rajan
Copyright (c) 2018, All rights reserved.
See LICENSE file in the root directory for licensing information.
'''

from AST import Visitor
from Value import NumVal

class Evaluator(Visitor):
    def eval(self, program):
        return self.visitProgram(program)

    def visitProgram(self, program):
        return program.e().accept(self)

    def visitNumExp(self, numexp):
        return NumVal(numexp.val)
    
    def visitAddExp(self, addexp):
        operands = addexp.all()
        result = 0.0
        for operand in operands:
            opval = operand.accept(self)
            if type(opval) is NumVal:
                result += opval.val;
            else:
                topval = type(opval)
                raise ValueError("Expected NumVal found:" + str(topval))    
        return NumVal(result)
    
    def visitSubExp(self, subexp):
        operands = subexp.all()
        fstoperand = operands.pop(0)
        fstopval = fstoperand.accept(self)
        if type(fstopval) is NumVal:
            result = fstopval.val;
            for operand in operands:
                opval = operand.accept(self)
                if type(opval) is NumVal:
                    result -= opval.val;
                else:
                    topval = type(opval)
                    raise ValueError("Expected NumVal found:" + str(topval))    
            return NumVal(result)
        else:
            fstopval = type(fstopval)
            raise ValueError("Expected NumVal found:" + str(fstopval))    
    
    def visitMultExp(self, mulexp):
        operands = mulexp.all()
        result = 1.0
        for operand in operands:
            opval = operand.accept(self)
            if type(opval) is NumVal:
                result *= opval.val;
            else:
                topval = type(opval)
                raise ValueError("Expected NumVal found:" + str(topval))    
        return NumVal(result)
    
    def visitDivExp(self, divexp):
        operands = divexp.all()
        fstoperand = operands.pop(0)
        fstopval = fstoperand.accept(self)
        if type(fstopval) is NumVal:
            result = fstopval.val;
            for operand in operands:
                opval = operand.accept(self)
                if type(opval) is NumVal:
                    result /= opval.val;
                else:
                    topval = type(opval)
                    raise ValueError("Expected NumVal found:" + str(topval))    
            return NumVal(result)
        else:
            fstopval = type(fstopval)
            raise ValueError("Expected NumVal found:" + str(fstopval))    
    
    def checkNumVal(self, val):
        if type(val) is NumVal:
            return val
        else:
            tyval = type(val)
            raise ValueError("Expected NumVal found:" + str(tyval))    
