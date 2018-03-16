# Generated from ArithLang.g by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from AST import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("s\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\6")
        buf.write("\t\65\n\t\r\t\16\t\66\3\n\3\n\7\n;\n\n\f\n\16\n>\13\n")
        buf.write("\3\13\3\13\3\13\3\13\5\13D\n\13\3\f\3\f\3\f\3\f\5\fJ\n")
        buf.write("\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\17\3\20\6\20U\n")
        buf.write("\20\r\20\16\20V\3\20\3\20\3\21\3\21\3\21\3\21\7\21_\n")
        buf.write("\21\f\21\16\21b\13\21\3\21\3\21\3\21\3\21\3\21\3\22\3")
        buf.write("\22\3\22\3\22\7\22m\n\22\f\22\16\22p\13\22\3\22\3\22\3")
        buf.write("`\2\23\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\2\33\16\35\17\37\20!\21#\22\3\2\t\6\2&&C\\aac|\4")
        buf.write("\2\2\u0101\ud802\udc01\3\2\ud802\udc01\3\2\udc02\ue001")
        buf.write("\7\2&&\62;C\\aac|\5\2\13\f\16\17\"\"\4\2\f\f\17\17\2z")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\3%\3\2\2\2\5\'")
        buf.write("\3\2\2\2\7)\3\2\2\2\t+\3\2\2\2\13-\3\2\2\2\r/\3\2\2\2")
        buf.write("\17\61\3\2\2\2\21\64\3\2\2\2\238\3\2\2\2\25C\3\2\2\2\27")
        buf.write("I\3\2\2\2\31K\3\2\2\2\33M\3\2\2\2\35O\3\2\2\2\37T\3\2")
        buf.write("\2\2!Z\3\2\2\2#h\3\2\2\2%&\7/\2\2&\4\3\2\2\2\'(\7*\2\2")
        buf.write("(\6\3\2\2\2)*\7-\2\2*\b\3\2\2\2+,\7+\2\2,\n\3\2\2\2-.")
        buf.write("\7,\2\2.\f\3\2\2\2/\60\7\61\2\2\60\16\3\2\2\2\61\62\7")
        buf.write("\60\2\2\62\20\3\2\2\2\63\65\5\31\r\2\64\63\3\2\2\2\65")
        buf.write("\66\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\67\22\3\2\2\2")
        buf.write("8<\5\25\13\29;\5\27\f\2:9\3\2\2\2;>\3\2\2\2<:\3\2\2\2")
        buf.write("<=\3\2\2\2=\24\3\2\2\2><\3\2\2\2?D\t\2\2\2@D\n\3\2\2A")
        buf.write("B\t\4\2\2BD\t\5\2\2C?\3\2\2\2C@\3\2\2\2CA\3\2\2\2D\26")
        buf.write("\3\2\2\2EJ\t\6\2\2FJ\n\3\2\2GH\t\4\2\2HJ\t\5\2\2IE\3\2")
        buf.write("\2\2IF\3\2\2\2IG\3\2\2\2J\30\3\2\2\2KL\4\62;\2L\32\3\2")
        buf.write("\2\2MN\7B\2\2N\34\3\2\2\2OP\7\60\2\2PQ\7\60\2\2QR\7\60")
        buf.write("\2\2R\36\3\2\2\2SU\t\7\2\2TS\3\2\2\2UV\3\2\2\2VT\3\2\2")
        buf.write("\2VW\3\2\2\2WX\3\2\2\2XY\b\20\2\2Y \3\2\2\2Z[\7\61\2\2")
        buf.write("[\\\7,\2\2\\`\3\2\2\2]_\13\2\2\2^]\3\2\2\2_b\3\2\2\2`")
        buf.write("a\3\2\2\2`^\3\2\2\2ac\3\2\2\2b`\3\2\2\2cd\7,\2\2de\7\61")
        buf.write("\2\2ef\3\2\2\2fg\b\21\2\2g\"\3\2\2\2hi\7\61\2\2ij\7\61")
        buf.write("\2\2jn\3\2\2\2km\n\b\2\2lk\3\2\2\2mp\3\2\2\2nl\3\2\2\2")
        buf.write("no\3\2\2\2oq\3\2\2\2pn\3\2\2\2qr\b\22\2\2r$\3\2\2\2\n")
        buf.write("\2\66<CIV`n\3\b\2\2")
        return buf.getvalue()


class ArithLangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    Dot = 7
    Number = 8
    Identifier = 9
    Letter = 10
    LetterOrDigit = 11
    AT = 12
    ELLIPSIS = 13
    WS = 14
    Comment = 15
    Line_Comment = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'-'", "'('", "'+'", "')'", "'*'", "'/'", "'.'", "'@'", "'...'" ]

    symbolicNames = [ "<INVALID>",
            "Dot", "Number", "Identifier", "Letter", "LetterOrDigit", "AT", 
            "ELLIPSIS", "WS", "Comment", "Line_Comment" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "Dot", 
                  "Number", "Identifier", "Letter", "LetterOrDigit", "DIGIT", 
                  "AT", "ELLIPSIS", "WS", "Comment", "Line_Comment" ]

    grammarFileName = "ArithLang.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


