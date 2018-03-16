# Generated from ArithLang.g by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from AST import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("k\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\6\7-\n\7\r\7\16\7.\3\b\3\b\7\b\63\n\b")
        buf.write("\f\b\16\b\66\13\b\3\t\3\t\3\t\3\t\5\t<\n\t\3\n\3\n\3\n")
        buf.write("\3\n\5\nB\n\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\16\6")
        buf.write("\16M\n\16\r\16\16\16N\3\16\3\16\3\17\3\17\3\17\3\17\7")
        buf.write("\17W\n\17\f\17\16\17Z\13\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\20\3\20\3\20\3\20\7\20e\n\20\f\20\16\20h\13\20\3\20\3")
        buf.write("\20\3X\2\21\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\2\27\f\31\r\33\16\35\17\37\20\3\2\t\6\2&&C\\aac|\4\2")
        buf.write("\2\u0101\ud802\udc01\3\2\ud802\udc01\3\2\udc02\ue001\7")
        buf.write("\2&&\62;C\\aac|\5\2\13\f\16\17\"\"\4\2\f\f\17\17\2r\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\3!\3\2\2\2\5#\3\2\2\2\7%\3\2\2\2\t\'\3")
        buf.write("\2\2\2\13)\3\2\2\2\r,\3\2\2\2\17\60\3\2\2\2\21;\3\2\2")
        buf.write("\2\23A\3\2\2\2\25C\3\2\2\2\27E\3\2\2\2\31G\3\2\2\2\33")
        buf.write("L\3\2\2\2\35R\3\2\2\2\37`\3\2\2\2!\"\7/\2\2\"\4\3\2\2")
        buf.write("\2#$\7*\2\2$\6\3\2\2\2%&\7-\2\2&\b\3\2\2\2\'(\7+\2\2(")
        buf.write("\n\3\2\2\2)*\7\60\2\2*\f\3\2\2\2+-\5\25\13\2,+\3\2\2\2")
        buf.write("-.\3\2\2\2.,\3\2\2\2./\3\2\2\2/\16\3\2\2\2\60\64\5\21")
        buf.write("\t\2\61\63\5\23\n\2\62\61\3\2\2\2\63\66\3\2\2\2\64\62")
        buf.write("\3\2\2\2\64\65\3\2\2\2\65\20\3\2\2\2\66\64\3\2\2\2\67")
        buf.write("<\t\2\2\28<\n\3\2\29:\t\4\2\2:<\t\5\2\2;\67\3\2\2\2;8")
        buf.write("\3\2\2\2;9\3\2\2\2<\22\3\2\2\2=B\t\6\2\2>B\n\3\2\2?@\t")
        buf.write("\4\2\2@B\t\5\2\2A=\3\2\2\2A>\3\2\2\2A?\3\2\2\2B\24\3\2")
        buf.write("\2\2CD\4\62;\2D\26\3\2\2\2EF\7B\2\2F\30\3\2\2\2GH\7\60")
        buf.write("\2\2HI\7\60\2\2IJ\7\60\2\2J\32\3\2\2\2KM\t\7\2\2LK\3\2")
        buf.write("\2\2MN\3\2\2\2NL\3\2\2\2NO\3\2\2\2OP\3\2\2\2PQ\b\16\2")
        buf.write("\2Q\34\3\2\2\2RS\7\61\2\2ST\7,\2\2TX\3\2\2\2UW\13\2\2")
        buf.write("\2VU\3\2\2\2WZ\3\2\2\2XY\3\2\2\2XV\3\2\2\2Y[\3\2\2\2Z")
        buf.write("X\3\2\2\2[\\\7,\2\2\\]\7\61\2\2]^\3\2\2\2^_\b\17\2\2_")
        buf.write("\36\3\2\2\2`a\7\61\2\2ab\7\61\2\2bf\3\2\2\2ce\n\b\2\2")
        buf.write("dc\3\2\2\2eh\3\2\2\2fd\3\2\2\2fg\3\2\2\2gi\3\2\2\2hf\3")
        buf.write("\2\2\2ij\b\20\2\2j \3\2\2\2\n\2.\64;ANXf\3\b\2\2")
        return buf.getvalue()


class ArithLangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    Dot = 5
    Number = 6
    Identifier = 7
    Letter = 8
    LetterOrDigit = 9
    AT = 10
    ELLIPSIS = 11
    WS = 12
    Comment = 13
    Line_Comment = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'-'", "'('", "'+'", "')'", "'.'", "'@'", "'...'" ]

    symbolicNames = [ "<INVALID>",
            "Dot", "Number", "Identifier", "Letter", "LetterOrDigit", "AT", 
            "ELLIPSIS", "WS", "Comment", "Line_Comment" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "Dot", "Number", "Identifier", 
                  "Letter", "LetterOrDigit", "DIGIT", "AT", "ELLIPSIS", 
                  "WS", "Comment", "Line_Comment" ]

    grammarFileName = "ArithLang.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


