# Generated from ArithLang.g by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from AST import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("_\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\4\6\4!\n\4\r\4\16\4\"\3\5\3\5\7\5\'\n\5")
        buf.write("\f\5\16\5*\13\5\3\6\3\6\3\6\3\6\5\6\60\n\6\3\7\3\7\3\7")
        buf.write("\3\7\5\7\66\n\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\13\6")
        buf.write("\13A\n\13\r\13\16\13B\3\13\3\13\3\f\3\f\3\f\3\f\7\fK\n")
        buf.write("\f\f\f\16\fN\13\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\7\rY\n\r\f\r\16\r\\\13\r\3\r\3\r\3L\2\16\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\2\21\t\23\n\25\13\27\f\31\r\3\2\t\6\2")
        buf.write("&&C\\aac|\4\2\2\u0101\ud802\udc01\3\2\ud802\udc01\3\2")
        buf.write("\udc02\ue001\7\2&&\62;C\\aac|\5\2\13\f\16\17\"\"\4\2\f")
        buf.write("\f\17\17\2f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3\2\2")
        buf.write("\2\5\35\3\2\2\2\7 \3\2\2\2\t$\3\2\2\2\13/\3\2\2\2\r\65")
        buf.write("\3\2\2\2\17\67\3\2\2\2\219\3\2\2\2\23;\3\2\2\2\25@\3\2")
        buf.write("\2\2\27F\3\2\2\2\31T\3\2\2\2\33\34\7/\2\2\34\4\3\2\2\2")
        buf.write("\35\36\7\60\2\2\36\6\3\2\2\2\37!\5\17\b\2 \37\3\2\2\2")
        buf.write("!\"\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#\b\3\2\2\2$(\5\13\6")
        buf.write("\2%\'\5\r\7\2&%\3\2\2\2\'*\3\2\2\2(&\3\2\2\2()\3\2\2\2")
        buf.write(")\n\3\2\2\2*(\3\2\2\2+\60\t\2\2\2,\60\n\3\2\2-.\t\4\2")
        buf.write("\2.\60\t\5\2\2/+\3\2\2\2/,\3\2\2\2/-\3\2\2\2\60\f\3\2")
        buf.write("\2\2\61\66\t\6\2\2\62\66\n\3\2\2\63\64\t\4\2\2\64\66\t")
        buf.write("\5\2\2\65\61\3\2\2\2\65\62\3\2\2\2\65\63\3\2\2\2\66\16")
        buf.write("\3\2\2\2\678\4\62;\28\20\3\2\2\29:\7B\2\2:\22\3\2\2\2")
        buf.write(";<\7\60\2\2<=\7\60\2\2=>\7\60\2\2>\24\3\2\2\2?A\t\7\2")
        buf.write("\2@?\3\2\2\2AB\3\2\2\2B@\3\2\2\2BC\3\2\2\2CD\3\2\2\2D")
        buf.write("E\b\13\2\2E\26\3\2\2\2FG\7\61\2\2GH\7,\2\2HL\3\2\2\2I")
        buf.write("K\13\2\2\2JI\3\2\2\2KN\3\2\2\2LM\3\2\2\2LJ\3\2\2\2MO\3")
        buf.write("\2\2\2NL\3\2\2\2OP\7,\2\2PQ\7\61\2\2QR\3\2\2\2RS\b\f\2")
        buf.write("\2S\30\3\2\2\2TU\7\61\2\2UV\7\61\2\2VZ\3\2\2\2WY\n\b\2")
        buf.write("\2XW\3\2\2\2Y\\\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[]\3\2\2\2")
        buf.write("\\Z\3\2\2\2]^\b\r\2\2^\32\3\2\2\2\n\2\"(/\65BLZ\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class ArithLangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    Dot = 2
    Number = 3
    Identifier = 4
    Letter = 5
    LetterOrDigit = 6
    AT = 7
    ELLIPSIS = 8
    WS = 9
    Comment = 10
    Line_Comment = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'-'", "'.'", "'@'", "'...'" ]

    symbolicNames = [ "<INVALID>",
            "Dot", "Number", "Identifier", "Letter", "LetterOrDigit", "AT", 
            "ELLIPSIS", "WS", "Comment", "Line_Comment" ]

    ruleNames = [ "T__0", "Dot", "Number", "Identifier", "Letter", "LetterOrDigit", 
                  "DIGIT", "AT", "ELLIPSIS", "WS", "Comment", "Line_Comment" ]

    grammarFileName = "ArithLang.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


