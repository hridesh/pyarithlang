# Generated from ArithLang.g by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from AST import *

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("\64\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\5\3\24\n\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4$\n\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\6\5-\n\5\r\5\16\5.\3\5\3\5\3\5\3\5\2")
        buf.write("\2\6\2\4\6\b\2\2\2\64\2\n\3\2\2\2\4\23\3\2\2\2\6#\3\2")
        buf.write("\2\2\b%\3\2\2\2\n\13\5\4\3\2\13\f\b\2\1\2\f\3\3\2\2\2")
        buf.write("\r\16\5\6\4\2\16\17\b\3\1\2\17\24\3\2\2\2\20\21\5\b\5")
        buf.write("\2\21\22\b\3\1\2\22\24\3\2\2\2\23\r\3\2\2\2\23\20\3\2")
        buf.write("\2\2\24\5\3\2\2\2\25\26\7\b\2\2\26$\b\4\1\2\27\30\7\3")
        buf.write("\2\2\30\31\7\b\2\2\31$\b\4\1\2\32\33\7\b\2\2\33\34\7\7")
        buf.write("\2\2\34\35\7\b\2\2\35$\b\4\1\2\36\37\7\3\2\2\37 \7\b\2")
        buf.write("\2 !\7\7\2\2!\"\7\b\2\2\"$\b\4\1\2#\25\3\2\2\2#\27\3\2")
        buf.write("\2\2#\32\3\2\2\2#\36\3\2\2\2$\7\3\2\2\2%&\7\4\2\2&\'\7")
        buf.write("\5\2\2\'(\5\4\3\2(,\b\5\1\2)*\5\4\3\2*+\b\5\1\2+-\3\2")
        buf.write("\2\2,)\3\2\2\2-.\3\2\2\2.,\3\2\2\2./\3\2\2\2/\60\3\2\2")
        buf.write("\2\60\61\7\6\2\2\61\62\b\5\1\2\62\t\3\2\2\2\5\23#.")
        return buf.getvalue()


class ArithLangParser ( Parser ):

    grammarFileName = "ArithLang.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'", "'('", "'+'", "')'", "'.'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'@'", "'...'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "Dot", "Number", "Identifier", "Letter", 
                      "LetterOrDigit", "AT", "ELLIPSIS", "WS", "Comment", 
                      "Line_Comment" ]

    RULE_program = 0
    RULE_exp = 1
    RULE_numexp = 2
    RULE_addexp = 3

    ruleNames =  [ "program", "exp", "numexp", "addexp" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    Dot=5
    Number=6
    Identifier=7
    Letter=8
    LetterOrDigit=9
    AT=10
    ELLIPSIS=11
    WS=12
    Comment=13
    Line_Comment=14

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
            self.state = 8
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
            self.a = None # AddexpContext

        def numexp(self):
            return self.getTypedRuleContext(ArithLangParser.NumexpContext,0)


        def addexp(self):
            return self.getTypedRuleContext(ArithLangParser.AddexpContext,0)


        def getRuleIndex(self):
            return ArithLangParser.RULE_exp




    def exp(self):

        localctx = ArithLangParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_exp)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ArithLangParser.T__0, ArithLangParser.Number]:
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                localctx.n = self.numexp()
                localctx.ast =  localctx.n.ast 
                pass
            elif token in [ArithLangParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                localctx.a = self.addexp()
                localctx.ast =  localctx.a.ast 
                pass
            else:
                raise NoViableAltException(self)

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
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                localctx.n0 = self.match(ArithLangParser.Number)
                localctx.ast =  AST.NumExp(int((None if localctx.n0 is None else localctx.n0.text))) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.match(ArithLangParser.T__0)
                self.state = 22
                localctx.n0 = self.match(ArithLangParser.Number)
                localctx.ast =  AST.NumExp(-int((None if localctx.n0 is None else localctx.n0.text))) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 24
                localctx.n0 = self.match(ArithLangParser.Number)
                self.state = 25
                self.match(ArithLangParser.Dot)
                self.state = 26
                localctx.n1 = self.match(ArithLangParser.Number)
                localctx.ast =  AST.NumExp(float((None if localctx.n0 is None else localctx.n0.text)+"."+(None if localctx.n1 is None else localctx.n1.text))) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.match(ArithLangParser.T__0)
                self.state = 29
                localctx.n0 = self.match(ArithLangParser.Number)
                self.state = 30
                self.match(ArithLangParser.Dot)
                self.state = 31
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

    class AddexpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.ast = None
            self.list = None
            self.e = None # ExpContext

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ArithLangParser.ExpContext)
            else:
                return self.getTypedRuleContext(ArithLangParser.ExpContext,i)


        def getRuleIndex(self):
            return ArithLangParser.RULE_addexp




    def addexp(self):

        localctx = ArithLangParser.AddexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_addexp)
        localctx.list = [] 
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(ArithLangParser.T__1)
            self.state = 36
            self.match(ArithLangParser.T__2)
            self.state = 37
            localctx.e = self.exp()
            localctx.list = localctx.list + [localctx.e.ast] 
            self.state = 42 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 39
                localctx.e = self.exp()
                localctx.list = localctx.list + [localctx.e.ast] 
                self.state = 44 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ArithLangParser.T__0) | (1 << ArithLangParser.T__1) | (1 << ArithLangParser.Number))) != 0)):
                    break

            self.state = 46
            self.match(ArithLangParser.T__3)
            localctx.ast =  AST.AddExp(localctx.list) 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





