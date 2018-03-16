# Generated from ArithLang.g by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from AST import *

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("m\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\5\3#\n\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\63\n\4\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\6\5<\n\5\r\5\16\5=\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\6\6J\n\6\r\6\16\6K\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\6\7X\n\7\r\7\16\7Y\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\6\bf\n\b\r\b\16")
        buf.write("\bg\3\b\3\b\3\b\3\b\2\2\t\2\4\6\b\n\f\16\2\2\2p\2\20\3")
        buf.write("\2\2\2\4\"\3\2\2\2\6\62\3\2\2\2\b\64\3\2\2\2\nB\3\2\2")
        buf.write("\2\fP\3\2\2\2\16^\3\2\2\2\20\21\5\4\3\2\21\22\b\2\1\2")
        buf.write("\22\3\3\2\2\2\23\24\5\6\4\2\24\25\b\3\1\2\25#\3\2\2\2")
        buf.write("\26\27\5\b\5\2\27\30\b\3\1\2\30#\3\2\2\2\31\32\5\n\6\2")
        buf.write("\32\33\b\3\1\2\33#\3\2\2\2\34\35\5\f\7\2\35\36\b\3\1\2")
        buf.write("\36#\3\2\2\2\37 \5\16\b\2 !\b\3\1\2!#\3\2\2\2\"\23\3\2")
        buf.write("\2\2\"\26\3\2\2\2\"\31\3\2\2\2\"\34\3\2\2\2\"\37\3\2\2")
        buf.write("\2#\5\3\2\2\2$%\7\n\2\2%\63\b\4\1\2&\'\7\3\2\2\'(\7\n")
        buf.write("\2\2(\63\b\4\1\2)*\7\n\2\2*+\7\t\2\2+,\7\n\2\2,\63\b\4")
        buf.write("\1\2-.\7\3\2\2./\7\n\2\2/\60\7\t\2\2\60\61\7\n\2\2\61")
        buf.write("\63\b\4\1\2\62$\3\2\2\2\62&\3\2\2\2\62)\3\2\2\2\62-\3")
        buf.write("\2\2\2\63\7\3\2\2\2\64\65\7\4\2\2\65\66\7\5\2\2\66\67")
        buf.write("\5\4\3\2\67;\b\5\1\289\5\4\3\29:\b\5\1\2:<\3\2\2\2;8\3")
        buf.write("\2\2\2<=\3\2\2\2=;\3\2\2\2=>\3\2\2\2>?\3\2\2\2?@\7\6\2")
        buf.write("\2@A\b\5\1\2A\t\3\2\2\2BC\7\4\2\2CD\7\3\2\2DE\5\4\3\2")
        buf.write("EI\b\6\1\2FG\5\4\3\2GH\b\6\1\2HJ\3\2\2\2IF\3\2\2\2JK\3")
        buf.write("\2\2\2KI\3\2\2\2KL\3\2\2\2LM\3\2\2\2MN\7\6\2\2NO\b\6\1")
        buf.write("\2O\13\3\2\2\2PQ\7\4\2\2QR\7\7\2\2RS\5\4\3\2SW\b\7\1\2")
        buf.write("TU\5\4\3\2UV\b\7\1\2VX\3\2\2\2WT\3\2\2\2XY\3\2\2\2YW\3")
        buf.write("\2\2\2YZ\3\2\2\2Z[\3\2\2\2[\\\7\6\2\2\\]\b\7\1\2]\r\3")
        buf.write("\2\2\2^_\7\4\2\2_`\7\b\2\2`a\5\4\3\2ae\b\b\1\2bc\5\4\3")
        buf.write("\2cd\b\b\1\2df\3\2\2\2eb\3\2\2\2fg\3\2\2\2ge\3\2\2\2g")
        buf.write("h\3\2\2\2hi\3\2\2\2ij\7\6\2\2jk\b\b\1\2k\17\3\2\2\2\b")
        buf.write("\"\62=KYg")
        return buf.getvalue()


class ArithLangParser ( Parser ):

    grammarFileName = "ArithLang.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'", "'('", "'+'", "')'", "'*'", "'/'", 
                     "'.'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'@'", "'...'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "Dot", "Number", 
                      "Identifier", "Letter", "LetterOrDigit", "AT", "ELLIPSIS", 
                      "WS", "Comment", "Line_Comment" ]

    RULE_program = 0
    RULE_exp = 1
    RULE_numexp = 2
    RULE_addexp = 3
    RULE_subexp = 4
    RULE_multexp = 5
    RULE_divexp = 6

    ruleNames =  [ "program", "exp", "numexp", "addexp", "subexp", "multexp", 
                   "divexp" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    Dot=7
    Number=8
    Identifier=9
    Letter=10
    LetterOrDigit=11
    AT=12
    ELLIPSIS=13
    WS=14
    Comment=15
    Line_Comment=16

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
            self.state = 14
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
            self.s = None # SubexpContext
            self.m = None # MultexpContext
            self.d = None # DivexpContext

        def numexp(self):
            return self.getTypedRuleContext(ArithLangParser.NumexpContext,0)


        def addexp(self):
            return self.getTypedRuleContext(ArithLangParser.AddexpContext,0)


        def subexp(self):
            return self.getTypedRuleContext(ArithLangParser.SubexpContext,0)


        def multexp(self):
            return self.getTypedRuleContext(ArithLangParser.MultexpContext,0)


        def divexp(self):
            return self.getTypedRuleContext(ArithLangParser.DivexpContext,0)


        def getRuleIndex(self):
            return ArithLangParser.RULE_exp




    def exp(self):

        localctx = ArithLangParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_exp)
        try:
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                localctx.n = self.numexp()
                localctx.ast =  localctx.n.ast 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                localctx.a = self.addexp()
                localctx.ast =  localctx.a.ast 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 23
                localctx.s = self.subexp()
                localctx.ast =  localctx.s.ast 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                localctx.m = self.multexp()
                localctx.ast =  localctx.m.ast 
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 29
                localctx.d = self.divexp()
                localctx.ast =  localctx.d.ast 
                pass


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
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                localctx.n0 = self.match(ArithLangParser.Number)
                localctx.ast =  AST.NumExp(int((None if localctx.n0 is None else localctx.n0.text))) 
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.match(ArithLangParser.T__0)
                self.state = 37
                localctx.n0 = self.match(ArithLangParser.Number)
                localctx.ast =  AST.NumExp(-int((None if localctx.n0 is None else localctx.n0.text))) 
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                localctx.n0 = self.match(ArithLangParser.Number)
                self.state = 40
                self.match(ArithLangParser.Dot)
                self.state = 41
                localctx.n1 = self.match(ArithLangParser.Number)
                localctx.ast =  AST.NumExp(float((None if localctx.n0 is None else localctx.n0.text)+"."+(None if localctx.n1 is None else localctx.n1.text))) 
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 43
                self.match(ArithLangParser.T__0)
                self.state = 44
                localctx.n0 = self.match(ArithLangParser.Number)
                self.state = 45
                self.match(ArithLangParser.Dot)
                self.state = 46
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
            self.state = 50
            self.match(ArithLangParser.T__1)
            self.state = 51
            self.match(ArithLangParser.T__2)
            self.state = 52
            localctx.e = self.exp()
            localctx.list.append(localctx.e.ast) 
            self.state = 57 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 54
                localctx.e = self.exp()
                localctx.list.append(localctx.e.ast) 
                self.state = 59 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ArithLangParser.T__0) | (1 << ArithLangParser.T__1) | (1 << ArithLangParser.Number))) != 0)):
                    break

            self.state = 61
            self.match(ArithLangParser.T__3)
            localctx.ast = AST.AddExp(localctx.list)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubexpContext(ParserRuleContext):

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
            return ArithLangParser.RULE_subexp




    def subexp(self):

        localctx = ArithLangParser.SubexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_subexp)
        localctx.list = [] 
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(ArithLangParser.T__1)
            self.state = 65
            self.match(ArithLangParser.T__0)
            self.state = 66
            localctx.e = self.exp()
            localctx.list.append(localctx.e.ast) 
            self.state = 71 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 68
                localctx.e = self.exp()
                localctx.list.append(localctx.e.ast) 
                self.state = 73 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ArithLangParser.T__0) | (1 << ArithLangParser.T__1) | (1 << ArithLangParser.Number))) != 0)):
                    break

            self.state = 75
            self.match(ArithLangParser.T__3)
            localctx.ast = AST.SubExp(localctx.list) 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MultexpContext(ParserRuleContext):

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
            return ArithLangParser.RULE_multexp




    def multexp(self):

        localctx = ArithLangParser.MultexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_multexp)
        localctx.list = [] 
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(ArithLangParser.T__1)
            self.state = 79
            self.match(ArithLangParser.T__4)
            self.state = 80
            localctx.e = self.exp()
            localctx.list.append(localctx.e.ast) 
            self.state = 85 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 82
                localctx.e = self.exp()
                localctx.list.append(localctx.e.ast) 
                self.state = 87 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ArithLangParser.T__0) | (1 << ArithLangParser.T__1) | (1 << ArithLangParser.Number))) != 0)):
                    break

            self.state = 89
            self.match(ArithLangParser.T__3)
            localctx.ast = AST.MultExp(localctx.list) 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DivexpContext(ParserRuleContext):

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
            return ArithLangParser.RULE_divexp




    def divexp(self):

        localctx = ArithLangParser.DivexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_divexp)
        localctx.list = [] 
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(ArithLangParser.T__1)
            self.state = 93
            self.match(ArithLangParser.T__5)
            self.state = 94
            localctx.e = self.exp()
            localctx.list.append(localctx.e.ast) 
            self.state = 99 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 96
                localctx.e = self.exp()
                localctx.list.append(localctx.e.ast) 
                self.state = 101 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ArithLangParser.T__0) | (1 << ArithLangParser.T__1) | (1 << ArithLangParser.Number))) != 0)):
                    break

            self.state = 103
            self.match(ArithLangParser.T__3)
            localctx.ast = AST.DivExp(localctx.list) 
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





