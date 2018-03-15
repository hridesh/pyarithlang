'''
This class hierarchy represents expressions in the abstract syntax tree
manipulated by this interpreter.
 
@author hridesh
'''

class AST:

    class ASTNode:
        def accept(self, visitor):
            return -1
    
    class Program(ASTNode):
        exp = None
        def __init__(self, e):
            self.exp = e
        def e(self):
            return self.exp
        def accept(self, visitor):
            return visitor.visit(self)

    class Exp(ASTNode):
        def accept(self, visitor):
            return -1  
          
    class NumExp(Exp):
        val = 0.0
        def __init__(self, val):
            self.val = val
        def v(self):
            return self.val
        def accept(self, visitor):
            return visitor.visit(self)
    
    class CompoundArithExp(Exp):
        rest = None
        def __init__(self, args):
            self.rest = args
        def all(self):
            return self.rest

class Visitor:
    def visit(self, astnode):
        if type(astnode) is AST.Program:
            self.visitProgram(astnode)
        if type(astnode) is AST.NumExp:
            self.visitNumExp(astnode)
        return -1;
    def visitProgram(self, program):
        return -1;
    def visitNumExp(self, numexp):
        return -1;
    