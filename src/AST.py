'''
This class hierarchy represents expressions in the abstract syntax tree
manipulated by this interpreter.
 
@author hridesh
'''
from abc import ABC, abstractmethod

class AST(ABC):

    class ASTNode(ABC):
        @abstractmethod
        def accept(self, visitor):
            pass
    
    class Program(ASTNode):
        exp = None
        def __init__(self, e):
            self.exp = e
        def e(self):
            return self.exp
        def accept(self, visitor):
            return visitor.visit(self)

    class Exp(ASTNode):
        @abstractmethod
        def accept(self, visitor):
            pass  
          
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

    class AddExp(CompoundArithExp):
        def __init__(self, args):
            self.rest = args
        def accept(self, visitor):
            return visitor.visit(self)        

    class SubExp(CompoundArithExp):
        def __init__(self, args):
            self.rest = args
        def accept(self, visitor):
            return visitor.visit(self)        

    class MultExp(CompoundArithExp):
        def __init__(self, args):
            self.rest = args
        def accept(self, visitor):
            return visitor.visit(self)        

    class DivExp(CompoundArithExp):
        def __init__(self, args):
            self.rest = args
        def accept(self, visitor):
            return visitor.visit(self)        

class Visitor(ABC):
    def visit(self, astnode):
        if type(astnode) is AST.Program:
            return self.visitProgram(astnode)
        elif type(astnode) is AST.NumExp:
            return self.visitNumExp(astnode)
        elif type(astnode) is AST.AddExp:
            return self.visitAddExp(astnode)
        elif type(astnode) is AST.SubExp:
            return self.visitSubExp(astnode)
        elif type(astnode) is AST.MultExp:
            return self.visitMultExp(astnode)
        elif type(astnode) is AST.DivExp:
            return self.visitDivExp(astnode)
        else: 
            print("visit: check if one or more AST Nodes are unimplemented. Current node's type is:" + str(type(astnode)))
            return -1
    @abstractmethod
    def visitProgram(self, program):
        pass
    @abstractmethod
    def visitNumExp(self, numexp):
        pass
    @abstractmethod
    def visitAddExp(self, addexp):
        pass
    @abstractmethod
    def visitSubExp(self, addexp):
        pass
    @abstractmethod
    def visitMultExp(self, addexp):
        pass
    @abstractmethod
    def visitDivExp(self, addexp):
        pass
