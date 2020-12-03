# Generated from /home/sadi/Curso/Fase Atual/Introdução a Compiladores/Implementação de Compiladores/INE5622-Compiler/code/sadbeep/sadbeep/sadbeep.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2.")
        buf.write("\u0133\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \3 \3!\6!\u00cc\n!\r!\16!\u00cd\3\"\3\"\5\"\u00d2\n\"")
        buf.write("\3#\3#\7#\u00d6\n#\f#\16#\u00d9\13#\3$\3$\3$\3$\7$\u00df")
        buf.write("\n$\f$\16$\u00e2\13$\3$\3$\3$\3$\3$\3%\3%\3%\3%\7%\u00ed")
        buf.write("\n%\f%\16%\u00f0\13%\3%\3%\3&\3&\5&\u00f6\n&\3\'\6\'\u00f9")
        buf.write("\n\'\r\'\16\'\u00fa\3(\6(\u00fe\n(\r(\16(\u00ff\3(\3(")
        buf.write("\6(\u0104\n(\r(\16(\u0105\3)\3)\3)\3)\3)\3*\3*\3*\3*\3")
        buf.write("*\3*\3+\3+\5+\u0115\n+\3,\3,\7,\u0119\n,\f,\16,\u011c")
        buf.write("\13,\3,\3,\3,\7,\u0121\n,\f,\16,\u0124\13,\3,\5,\u0127")
        buf.write("\n,\3-\6-\u012a\n-\r-\16-\u012b\3-\3-\3.\3.\3/\3/\3\u00e0")
        buf.write("\2\60\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27")
        buf.write("\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\2C\2E\"G#I$")
        buf.write("K%M&O\'Q(S)U*W+Y,[-].\3\2\7\4\2C\\c|\4\2\f\f\17\17\3\2")
        buf.write("\62;\5\2\f\f\17\17))\5\2\13\f\17\17\"\"\2\u013e\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2E\3")
        buf.write("\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O")
        buf.write("\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2")
        buf.write("Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\3_\3\2\2\2\5a\3\2\2\2")
        buf.write("\7c\3\2\2\2\ti\3\2\2\2\13k\3\2\2\2\rm\3\2\2\2\17t\3\2")
        buf.write("\2\2\21v\3\2\2\2\23y\3\2\2\2\25|\3\2\2\2\27\177\3\2\2")
        buf.write("\2\31\u0084\3\2\2\2\33\u008a\3\2\2\2\35\u008e\3\2\2\2")
        buf.write("\37\u0095\3\2\2\2!\u0097\3\2\2\2#\u0099\3\2\2\2%\u009e")
        buf.write("\3\2\2\2\'\u00a3\3\2\2\2)\u00a5\3\2\2\2+\u00ac\3\2\2\2")
        buf.write("-\u00ae\3\2\2\2/\u00b0\3\2\2\2\61\u00b3\3\2\2\2\63\u00b6")
        buf.write("\3\2\2\2\65\u00b9\3\2\2\2\67\u00bc\3\2\2\29\u00be\3\2")
        buf.write("\2\2;\u00c0\3\2\2\2=\u00c2\3\2\2\2?\u00c4\3\2\2\2A\u00cb")
        buf.write("\3\2\2\2C\u00d1\3\2\2\2E\u00d3\3\2\2\2G\u00da\3\2\2\2")
        buf.write("I\u00e8\3\2\2\2K\u00f5\3\2\2\2M\u00f8\3\2\2\2O\u00fd\3")
        buf.write("\2\2\2Q\u0107\3\2\2\2S\u010c\3\2\2\2U\u0114\3\2\2\2W\u0126")
        buf.write("\3\2\2\2Y\u0129\3\2\2\2[\u012f\3\2\2\2]\u0131\3\2\2\2")
        buf.write("_`\7?\2\2`\4\3\2\2\2ab\7=\2\2b\6\3\2\2\2cd\7r\2\2de\7")
        buf.write("t\2\2ef\7k\2\2fg\7p\2\2gh\7v\2\2h\b\3\2\2\2ij\7*\2\2j")
        buf.write("\n\3\2\2\2kl\7+\2\2l\f\3\2\2\2mn\7t\2\2no\7g\2\2op\7v")
        buf.write("\2\2pq\7w\2\2qr\7t\2\2rs\7p\2\2s\16\3\2\2\2tu\7/\2\2u")
        buf.write("\20\3\2\2\2vw\7k\2\2wx\7h\2\2x\22\3\2\2\2yz\7(\2\2z{\7")
        buf.write("(\2\2{\24\3\2\2\2|}\7~\2\2}~\7~\2\2~\26\3\2\2\2\177\u0080")
        buf.write("\7g\2\2\u0080\u0081\7n\2\2\u0081\u0082\7u\2\2\u0082\u0083")
        buf.write("\7g\2\2\u0083\30\3\2\2\2\u0084\u0085\7y\2\2\u0085\u0086")
        buf.write("\7j\2\2\u0086\u0087\7k\2\2\u0087\u0088\7n\2\2\u0088\u0089")
        buf.write("\7g\2\2\u0089\32\3\2\2\2\u008a\u008b\7h\2\2\u008b\u008c")
        buf.write("\7q\2\2\u008c\u008d\7t\2\2\u008d\34\3\2\2\2\u008e\u008f")
        buf.write("\7u\2\2\u008f\u0090\7y\2\2\u0090\u0091\7k\2\2\u0091\u0092")
        buf.write("\7v\2\2\u0092\u0093\7e\2\2\u0093\u0094\7j\2\2\u0094\36")
        buf.write("\3\2\2\2\u0095\u0096\7}\2\2\u0096 \3\2\2\2\u0097\u0098")
        buf.write("\7\177\2\2\u0098\"\3\2\2\2\u0099\u009a\7h\2\2\u009a\u009b")
        buf.write("\7w\2\2\u009b\u009c\7p\2\2\u009c\u009d\7e\2\2\u009d$\3")
        buf.write("\2\2\2\u009e\u009f\7e\2\2\u009f\u00a0\7c\2\2\u00a0\u00a1")
        buf.write("\7u\2\2\u00a1\u00a2\7g\2\2\u00a2&\3\2\2\2\u00a3\u00a4")
        buf.write("\7<\2\2\u00a4(\3\2\2\2\u00a5\u00a6\7d\2\2\u00a6\u00a7")
        buf.write("\7t\2\2\u00a7\u00a8\7g\2\2\u00a8\u00a9\7c\2\2\u00a9\u00aa")
        buf.write("\7m\2\2\u00aa\u00ab\7=\2\2\u00ab*\3\2\2\2\u00ac\u00ad")
        buf.write("\7@\2\2\u00ad,\3\2\2\2\u00ae\u00af\7>\2\2\u00af.\3\2\2")
        buf.write("\2\u00b0\u00b1\7@\2\2\u00b1\u00b2\7?\2\2\u00b2\60\3\2")
        buf.write("\2\2\u00b3\u00b4\7>\2\2\u00b4\u00b5\7?\2\2\u00b5\62\3")
        buf.write("\2\2\2\u00b6\u00b7\7?\2\2\u00b7\u00b8\7?\2\2\u00b8\64")
        buf.write("\3\2\2\2\u00b9\u00ba\7#\2\2\u00ba\u00bb\7?\2\2\u00bb\66")
        buf.write("\3\2\2\2\u00bc\u00bd\7-\2\2\u00bd8\3\2\2\2\u00be\u00bf")
        buf.write("\7,\2\2\u00bf:\3\2\2\2\u00c0\u00c1\7\61\2\2\u00c1<\3\2")
        buf.write("\2\2\u00c2\u00c3\7\'\2\2\u00c3>\3\2\2\2\u00c4\u00c5\7")
        buf.write("k\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7\7r\2\2\u00c7\u00c8")
        buf.write("\7w\2\2\u00c8\u00c9\7v\2\2\u00c9@\3\2\2\2\u00ca\u00cc")
        buf.write("\t\2\2\2\u00cb\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd")
        buf.write("\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ceB\3\2\2\2\u00cf")
        buf.write("\u00d2\5A!\2\u00d0\u00d2\5K&\2\u00d1\u00cf\3\2\2\2\u00d1")
        buf.write("\u00d0\3\2\2\2\u00d2D\3\2\2\2\u00d3\u00d7\5A!\2\u00d4")
        buf.write("\u00d6\5C\"\2\u00d5\u00d4\3\2\2\2\u00d6\u00d9\3\2\2\2")
        buf.write("\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8F\3\2\2")
        buf.write("\2\u00d9\u00d7\3\2\2\2\u00da\u00db\7\61\2\2\u00db\u00dc")
        buf.write("\7,\2\2\u00dc\u00e0\3\2\2\2\u00dd\u00df\13\2\2\2\u00de")
        buf.write("\u00dd\3\2\2\2\u00df\u00e2\3\2\2\2\u00e0\u00e1\3\2\2\2")
        buf.write("\u00e0\u00de\3\2\2\2\u00e1\u00e3\3\2\2\2\u00e2\u00e0\3")
        buf.write("\2\2\2\u00e3\u00e4\7,\2\2\u00e4\u00e5\7\61\2\2\u00e5\u00e6")
        buf.write("\3\2\2\2\u00e6\u00e7\b$\2\2\u00e7H\3\2\2\2\u00e8\u00e9")
        buf.write("\7\61\2\2\u00e9\u00ea\7\61\2\2\u00ea\u00ee\3\2\2\2\u00eb")
        buf.write("\u00ed\n\3\2\2\u00ec\u00eb\3\2\2\2\u00ed\u00f0\3\2\2\2")
        buf.write("\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f1\3")
        buf.write("\2\2\2\u00f0\u00ee\3\2\2\2\u00f1\u00f2\b%\2\2\u00f2J\3")
        buf.write("\2\2\2\u00f3\u00f6\5M\'\2\u00f4\u00f6\5O(\2\u00f5\u00f3")
        buf.write("\3\2\2\2\u00f5\u00f4\3\2\2\2\u00f6L\3\2\2\2\u00f7\u00f9")
        buf.write("\t\4\2\2\u00f8\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa")
        buf.write("\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fbN\3\2\2\2\u00fc")
        buf.write("\u00fe\t\4\2\2\u00fd\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2")
        buf.write("\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0101\3")
        buf.write("\2\2\2\u0101\u0103\7\60\2\2\u0102\u0104\t\4\2\2\u0103")
        buf.write("\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0103\3\2\2\2")
        buf.write("\u0105\u0106\3\2\2\2\u0106P\3\2\2\2\u0107\u0108\7V\2\2")
        buf.write("\u0108\u0109\7t\2\2\u0109\u010a\7w\2\2\u010a\u010b\7g")
        buf.write("\2\2\u010bR\3\2\2\2\u010c\u010d\7H\2\2\u010d\u010e\7c")
        buf.write("\2\2\u010e\u010f\7n\2\2\u010f\u0110\7u\2\2\u0110\u0111")
        buf.write("\7g\2\2\u0111T\3\2\2\2\u0112\u0115\5Q)\2\u0113\u0115\5")
        buf.write("S*\2\u0114\u0112\3\2\2\2\u0114\u0113\3\2\2\2\u0115V\3")
        buf.write("\2\2\2\u0116\u011a\7)\2\2\u0117\u0119\n\5\2\2\u0118\u0117")
        buf.write("\3\2\2\2\u0119\u011c\3\2\2\2\u011a\u0118\3\2\2\2\u011a")
        buf.write("\u011b\3\2\2\2\u011b\u011d\3\2\2\2\u011c\u011a\3\2\2\2")
        buf.write("\u011d\u0127\7)\2\2\u011e\u0122\7$\2\2\u011f\u0121\n\5")
        buf.write("\2\2\u0120\u011f\3\2\2\2\u0121\u0124\3\2\2\2\u0122\u0120")
        buf.write("\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0125\3\2\2\2\u0124")
        buf.write("\u0122\3\2\2\2\u0125\u0127\7$\2\2\u0126\u0116\3\2\2\2")
        buf.write("\u0126\u011e\3\2\2\2\u0127X\3\2\2\2\u0128\u012a\t\6\2")
        buf.write("\2\u0129\u0128\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u0129")
        buf.write("\3\2\2\2\u012b\u012c\3\2\2\2\u012c\u012d\3\2\2\2\u012d")
        buf.write("\u012e\b-\2\2\u012eZ\3\2\2\2\u012f\u0130\7\60\2\2\u0130")
        buf.write("\\\3\2\2\2\u0131\u0132\7.\2\2\u0132^\3\2\2\2\21\2\u00cd")
        buf.write("\u00d1\u00d7\u00e0\u00ee\u00f5\u00fa\u00ff\u0105\u0114")
        buf.write("\u011a\u0122\u0126\u012b\3\b\2\2")
        return buf.getvalue()


class sadbeepLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    ID = 32
    COMMENT = 33
    LINE_COMMENT = 34
    NUMBER = 35
    INT = 36
    FLOAT = 37
    TRUE = 38
    FALSE = 39
    BOOL = 40
    STRING = 41
    WS = 42
    DOT = 43
    COMMA = 44

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "';'", "'print'", "'('", "')'", "'return'", "'-'", "'if'", 
            "'&&'", "'||'", "'else'", "'while'", "'for'", "'switch'", "'{'", 
            "'}'", "'func'", "'case'", "':'", "'break;'", "'>'", "'<'", 
            "'>='", "'<='", "'=='", "'!='", "'+'", "'*'", "'/'", "'%'", 
            "'input'", "'True'", "'False'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>",
            "ID", "COMMENT", "LINE_COMMENT", "NUMBER", "INT", "FLOAT", "TRUE", 
            "FALSE", "BOOL", "STRING", "WS", "DOT", "COMMA" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "ID_START", 
                  "ID_BODY", "ID", "COMMENT", "LINE_COMMENT", "NUMBER", 
                  "INT", "FLOAT", "TRUE", "FALSE", "BOOL", "STRING", "WS", 
                  "DOT", "COMMA" ]

    grammarFileName = "sadbeep.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


