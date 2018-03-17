'''
Reads a program file and produces an abstract syntax tree (AST)
for the program created in that file.

@author: Hridesh Rajan
Copyright (c) 2018, All rights reserved.
See LICENSE file in the root directory for licensing information.
'''
from antlr4 import CommonTokenStream
from antlr4 import FileStream
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