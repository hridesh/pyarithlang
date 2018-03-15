# Generated from ArithLang.g by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from AST import *

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("\37\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\5\4\35\n\4\3\4\2\2\5\2\4\6\2\2\2\36\2\b\3\2\2\2\4\13")
        buf.write("\3\2\2\2\6\34\3\2\2\2\b\t\5\4\3\2\t\n\b\2\1\2\n\3\3\2")
        buf.write("\2\2\13\f\5\6\4\2\f\r\b\3\1\2\r\5\3\2\2\2\16\17\7\5\2")
        buf.write("\2\17\35\b\4\1\2\20\21\7\3\2\2\21\22\7\5\2\2\22\35\b\4")
        buf.write("\1\2\23\24\7\5\2\2\24\25\7\4\2\2\25\26\7\5\2\2\26\35\b")
        buf.write("\4\1\2\27\30\7\3\2\2\30\31\7\5\2\2\31\32\7\4\2\2\32\33")
        buf.write("\7\5\2\2\33\35\b\4\1\2\34\16\3\2\2\2\34\20\3\2\2\2\34")
        buf.write("\23\3\2\2\2\34\27\3\2\2\2\35\7\3\2\2\2\3\34")
        return buf.getvalue()


class ArithLangParser ( Parser ):

    grammarFileName = "ArithLang.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'", "'.'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'@'", "'...'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "Dot", "Number", "Identifier", 
                      "Letter", "LetterOrDigit", "AT", "ELLIPSIS", "WS", 
                      "Comment", "Line_Comment" ]

    RULE_program = 0
    RULE_exp = 1
    RULE_numexp = 2

    ruleNames =  [ "program", "exp", "numexp" ]

    EOF = Token.EOF
    T__0=1
    Dot=2
    Number=3
    Identifier=4
    Letter=5
    LetterOrDigit=6
    AT=7
    ELLIPSIS=8
    WS=9
    Comment=10
    Line_Comment=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.e = None # ExpContext

        def exp(self):
            return self.getTypedRuleContext(ArithLangParser.ExpContext,0)


        def getRuleIndex(self):
            return ArithLangParser.RULE_program




    def program(self):

        localctx = ArithLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            localctx.e = self.exp()
            localctx.ast =  AST.Program(localctx.e.ast) 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.n = None # NumexpContext

        def numexp(self):
            return self.getTypedRuleContext(ArithLangParser.NumexpContext,0)


        def getRuleIndex(self):
            return ArithLangParser.RULE_exp




    def exp(self):

        localctx = ArithLangParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            localctx.n = self.numexp()
            localctx.ast =  localctx.n.ast 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumexpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.n0 = None # Token
            self.n1 = None # Token

        def Number(self, i:int=None):
            if i is None:
                return self.getTokens(ArithLangParser.Number)
            else:
                return self.getToken(ArithLangParser.Number, i)

        def Dot(self):
            return self.getToken(ArithLangParser.Dot, 0)

        def getRuleIndex(self):
            return ArithLangParser.RULE_numexp




    def numexp(self):

        localctx = ArithLangParser.NumexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_numexp)
        try:
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                localctx.n0 = self.match(ArithLangParser.Number)
                localctx.ast =  AST.NumExp(int((None if localctx.n0 is None else localctx.n0.text))) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(ArithLangParser.T__0)
                self.state = 15
                localctx.n0 = self.match(ArithLangParser.Number)
                localctx.ast =  AST.NumExp(-int((None if localctx.n0 is None else localctx.n0.text))) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 17
                localctx.n0 = self.match(ArithLangParser.Number)
                self.state = 18
                self.match(ArithLangParser.Dot)
                self.state = 19
                localctx.n1 = self.match(ArithLangParser.Number)
                localctx.ast =  AST.NumExp(float((None if localctx.n0 is None else localctx.n0.text)+"."+(None if localctx.n1 is None else localctx.n1.text))) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 21
                self.match(ArithLangParser.T__0)
                self.state = 22
                localctx.n0 = self.match(ArithLangParser.Number)
                self.state = 23
                self.match(ArithLangParser.Dot)
                self.state = 24
                localctx.n1 = self.match(ArithLangParser.Number)
                localctx.ast =  AST.NumExp(float("-" + (None if localctx.n0 is None else localctx.n0.text)+"."+(None if localctx.n1 is None else localctx.n1.text))) 
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





