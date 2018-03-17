'''
Created on Feb 13, 2018

@author: hridesh
'''
from antlr4 import *
from ArithLangLexer import ArithLangLexer
from ArithLangParser import ArithLangParser

class Reader:
    def read(self, pgm_file):
        pgm_stream = FileStream(pgm_file)
        lexer = ArithLangLexer(pgm_stream)
        stream = CommonTokenStream(lexer)
        parser = ArithLangParser(stream)
        pgm = parser.program()
        # Uncomment the following line to print the parse tree.
        # print(pgm.toStringTree(recog=parser))
        return pgm.ast
    
if __name__ == '__main__':
    Reader().read()