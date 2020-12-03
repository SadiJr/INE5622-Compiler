# Generated from /home/sadi/Curso/Fase Atual/Introdução a Compiladores/Implementação de Compiladores/INE5622-Compiler/code/sadbeep/sadbeep/sadbeep.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3.")
        buf.write("\u00f7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\7\2$\n\2\f\2\16")
        buf.write("\2\'\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\5\3C\n\3\3\3\3\3\3\3\3\3\3\3\7\3J\n\3\f\3\16\3")
        buf.write("M\13\3\3\3\3\3\7\3Q\n\3\f\3\16\3T\13\3\3\3\3\3\3\3\5\3")
        buf.write("Y\n\3\3\3\3\3\3\3\3\3\7\3_\n\3\f\3\16\3b\13\3\3\3\3\3")
        buf.write("\7\3f\n\3\f\3\16\3i\13\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3r\n\3\3\3\3\3\6\3v\n\3\r\3\16\3w\3\3\3\3\5\3|\n\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\7\3\u0084\n\3\f\3\16\3\u0087\13")
        buf.write("\3\3\4\3\4\5\4\u008b\n\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\5\7\u0095\n\7\3\7\3\7\3\7\3\b\3\b\3\b\7\b\u009d\n\b")
        buf.write("\f\b\16\b\u00a0\13\b\3\t\3\t\3\t\3\t\3\t\5\t\u00a7\n\t")
        buf.write("\3\n\3\n\7\n\u00ab\n\n\f\n\16\n\u00ae\13\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\5\13\u00b5\n\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\7\f\u00bd\n\f\f\f\16\f\u00c0\13\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\7\16\u00d1")
        buf.write("\n\16\f\16\16\16\u00d4\13\16\3\17\3\17\3\17\7\17\u00d9")
        buf.write("\n\17\f\17\16\17\u00dc\13\17\3\20\3\20\3\20\7\20\u00e1")
        buf.write("\n\20\f\20\16\20\u00e4\13\20\3\21\3\21\5\21\u00e8\n\21")
        buf.write("\3\21\3\21\3\21\3\21\5\21\u00ee\n\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\5\21\u00f5\n\21\3\21\2\3\4\22\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \2\6\3\2&\'\3\2\27\34\4\2\t\t")
        buf.write("\35\35\3\2\36 \2\u0111\2%\3\2\2\2\4{\3\2\2\2\6\u008a\3")
        buf.write("\2\2\2\b\u008c\3\2\2\2\n\u008e\3\2\2\2\f\u0090\3\2\2\2")
        buf.write("\16\u0099\3\2\2\2\20\u00a1\3\2\2\2\22\u00a8\3\2\2\2\24")
        buf.write("\u00b1\3\2\2\2\26\u00b9\3\2\2\2\30\u00c1\3\2\2\2\32\u00cd")
        buf.write("\3\2\2\2\34\u00d5\3\2\2\2\36\u00dd\3\2\2\2 \u00f4\3\2")
        buf.write("\2\2\"$\5\4\3\2#\"\3\2\2\2$\'\3\2\2\2%#\3\2\2\2%&\3\2")
        buf.write("\2\2&(\3\2\2\2\'%\3\2\2\2()\7\2\2\3)\3\3\2\2\2*+\b\3\1")
        buf.write("\2+,\5\n\6\2,-\7\3\2\2-.\5\4\3\2./\7\4\2\2/|\3\2\2\2\60")
        buf.write("\61\7\5\2\2\61\62\5\4\3\2\62\63\7\4\2\2\63|\3\2\2\2\64")
        buf.write("|\5\b\5\2\65|\5\f\7\2\66\67\7\6\2\2\678\5\4\3\289\7\7")
        buf.write("\2\29|\3\2\2\2:|\7+\2\2;<\7\b\2\2<=\5\4\3\2=>\7\4\2\2")
        buf.write(">|\3\2\2\2?|\7\"\2\2@|\5\24\13\2AC\7\t\2\2BA\3\2\2\2B")
        buf.write("C\3\2\2\2CD\3\2\2\2D|\5\32\16\2EF\7\n\2\2FK\5\4\3\2GH")
        buf.write("\7\13\2\2HJ\5\4\3\2IG\3\2\2\2JM\3\2\2\2KI\3\2\2\2KL\3")
        buf.write("\2\2\2L|\3\2\2\2MK\3\2\2\2NO\7\f\2\2OQ\5\4\3\2PN\3\2\2")
        buf.write("\2QT\3\2\2\2RP\3\2\2\2RS\3\2\2\2SU\3\2\2\2TR\3\2\2\2U")
        buf.write("X\5\22\n\2VW\7\r\2\2WY\5\22\n\2XV\3\2\2\2XY\3\2\2\2Y|")
        buf.write("\3\2\2\2Z[\7\16\2\2[`\5\4\3\2\\]\7\13\2\2]_\5\4\3\2^\\")
        buf.write("\3\2\2\2_b\3\2\2\2`^\3\2\2\2`a\3\2\2\2a|\3\2\2\2b`\3\2")
        buf.write("\2\2cd\7\f\2\2df\5\4\3\2ec\3\2\2\2fi\3\2\2\2ge\3\2\2\2")
        buf.write("gh\3\2\2\2hj\3\2\2\2ig\3\2\2\2j|\5\22\n\2kl\7\17\2\2l")
        buf.write("m\5\30\r\2mn\5\22\n\2n|\3\2\2\2oq\7\20\2\2pr\5\4\3\2q")
        buf.write("p\3\2\2\2qr\3\2\2\2rs\3\2\2\2su\7\21\2\2tv\5\20\t\2ut")
        buf.write("\3\2\2\2vw\3\2\2\2wu\3\2\2\2wx\3\2\2\2xy\3\2\2\2yz\7\22")
        buf.write("\2\2z|\3\2\2\2{*\3\2\2\2{\60\3\2\2\2{\64\3\2\2\2{\65\3")
        buf.write("\2\2\2{\66\3\2\2\2{:\3\2\2\2{;\3\2\2\2{?\3\2\2\2{@\3\2")
        buf.write("\2\2{B\3\2\2\2{E\3\2\2\2{R\3\2\2\2{Z\3\2\2\2{g\3\2\2\2")
        buf.write("{k\3\2\2\2{o\3\2\2\2|\u0085\3\2\2\2}~\f\20\2\2~\u0084")
        buf.write("\5\4\3\21\177\u0080\f\n\2\2\u0080\u0081\5\6\4\2\u0081")
        buf.write("\u0082\7\4\2\2\u0082\u0084\3\2\2\2\u0083}\3\2\2\2\u0083")
        buf.write("\177\3\2\2\2\u0084\u0087\3\2\2\2\u0085\u0083\3\2\2\2\u0085")
        buf.write("\u0086\3\2\2\2\u0086\5\3\2\2\2\u0087\u0085\3\2\2\2\u0088")
        buf.write("\u008b\5\36\20\2\u0089\u008b\5\34\17\2\u008a\u0088\3\2")
        buf.write("\2\2\u008a\u0089\3\2\2\2\u008b\7\3\2\2\2\u008c\u008d\t")
        buf.write("\2\2\2\u008d\t\3\2\2\2\u008e\u008f\7\"\2\2\u008f\13\3")
        buf.write("\2\2\2\u0090\u0091\7\23\2\2\u0091\u0092\7\"\2\2\u0092")
        buf.write("\u0094\7\6\2\2\u0093\u0095\5\16\b\2\u0094\u0093\3\2\2")
        buf.write("\2\u0094\u0095\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097")
        buf.write("\7\7\2\2\u0097\u0098\5\22\n\2\u0098\r\3\2\2\2\u0099\u009e")
        buf.write("\7\"\2\2\u009a\u009b\7.\2\2\u009b\u009d\7\"\2\2\u009c")
        buf.write("\u009a\3\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c\3\2\2\2")
        buf.write("\u009e\u009f\3\2\2\2\u009f\17\3\2\2\2\u00a0\u009e\3\2")
        buf.write("\2\2\u00a1\u00a2\7\24\2\2\u00a2\u00a3\5\4\3\2\u00a3\u00a4")
        buf.write("\7\25\2\2\u00a4\u00a6\5\4\3\2\u00a5\u00a7\7\26\2\2\u00a6")
        buf.write("\u00a5\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\21\3\2\2\2\u00a8")
        buf.write("\u00ac\7\21\2\2\u00a9\u00ab\5\4\3\2\u00aa\u00a9\3\2\2")
        buf.write("\2\u00ab\u00ae\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad")
        buf.write("\3\2\2\2\u00ad\u00af\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af")
        buf.write("\u00b0\7\22\2\2\u00b0\23\3\2\2\2\u00b1\u00b2\7\"\2\2\u00b2")
        buf.write("\u00b4\7\6\2\2\u00b3\u00b5\5\26\f\2\u00b4\u00b3\3\2\2")
        buf.write("\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b7")
        buf.write("\7\7\2\2\u00b7\u00b8\7\4\2\2\u00b8\25\3\2\2\2\u00b9\u00be")
        buf.write("\5\4\3\2\u00ba\u00bb\7.\2\2\u00bb\u00bd\5\4\3\2\u00bc")
        buf.write("\u00ba\3\2\2\2\u00bd\u00c0\3\2\2\2\u00be\u00bc\3\2\2\2")
        buf.write("\u00be\u00bf\3\2\2\2\u00bf\27\3\2\2\2\u00c0\u00be\3\2")
        buf.write("\2\2\u00c1\u00c2\7\6\2\2\u00c2\u00c3\5\n\6\2\u00c3\u00c4")
        buf.write("\7\3\2\2\u00c4\u00c5\5\4\3\2\u00c5\u00c6\7\4\2\2\u00c6")
        buf.write("\u00c7\5\4\3\2\u00c7\u00c8\7\4\2\2\u00c8\u00c9\5\n\6\2")
        buf.write("\u00c9\u00ca\7\3\2\2\u00ca\u00cb\5\4\3\2\u00cb\u00cc\7")
        buf.write("\7\2\2\u00cc\31\3\2\2\2\u00cd\u00d2\5\34\17\2\u00ce\u00cf")
        buf.write("\t\3\2\2\u00cf\u00d1\5\32\16\2\u00d0\u00ce\3\2\2\2\u00d1")
        buf.write("\u00d4\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2")
        buf.write("\u00d3\33\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d5\u00da\5\36")
        buf.write("\20\2\u00d6\u00d7\t\4\2\2\u00d7\u00d9\5\34\17\2\u00d8")
        buf.write("\u00d6\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da\u00d8\3\2\2\2")
        buf.write("\u00da\u00db\3\2\2\2\u00db\35\3\2\2\2\u00dc\u00da\3\2")
        buf.write("\2\2\u00dd\u00e2\5 \21\2\u00de\u00df\t\5\2\2\u00df\u00e1")
        buf.write("\5\36\20\2\u00e0\u00de\3\2\2\2\u00e1\u00e4\3\2\2\2\u00e2")
        buf.write("\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\37\3\2\2\2\u00e4")
        buf.write("\u00e2\3\2\2\2\u00e5\u00e7\7\6\2\2\u00e6\u00e8\7\t\2\2")
        buf.write("\u00e7\u00e6\3\2\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e9\3")
        buf.write("\2\2\2\u00e9\u00ea\5\32\16\2\u00ea\u00eb\7\7\2\2\u00eb")
        buf.write("\u00f5\3\2\2\2\u00ec\u00ee\7\t\2\2\u00ed\u00ec\3\2\2\2")
        buf.write("\u00ed\u00ee\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f5\5")
        buf.write("\b\5\2\u00f0\u00f5\7*\2\2\u00f1\u00f5\7+\2\2\u00f2\u00f5")
        buf.write("\7\"\2\2\u00f3\u00f5\7!\2\2\u00f4\u00e5\3\2\2\2\u00f4")
        buf.write("\u00ed\3\2\2\2\u00f4\u00f0\3\2\2\2\u00f4\u00f1\3\2\2\2")
        buf.write("\u00f4\u00f2\3\2\2\2\u00f4\u00f3\3\2\2\2\u00f5!\3\2\2")
        buf.write("\2\33%BKRX`gqw{\u0083\u0085\u008a\u0094\u009e\u00a6\u00ac")
        buf.write("\u00b4\u00be\u00d2\u00da\u00e2\u00e7\u00ed\u00f4")
        return buf.getvalue()


class sadbeepParser ( Parser ):

    grammarFileName = "sadbeep.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'print'", "'('", "')'", 
                     "'return'", "'-'", "'if'", "'&&'", "'||'", "'else'", 
                     "'while'", "'for'", "'switch'", "'{'", "'}'", "'func'", 
                     "'case'", "':'", "'break;'", "'>'", "'<'", "'>='", 
                     "'<='", "'=='", "'!='", "'+'", "'*'", "'/'", "'%'", 
                     "'input'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'True'", "'False'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'.'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "COMMENT", "LINE_COMMENT", "NUMBER", "INT", 
                      "FLOAT", "TRUE", "FALSE", "BOOL", "STRING", "WS", 
                      "DOT", "COMMA" ]

    RULE_parse = 0
    RULE_expr = 1
    RULE_operators = 2
    RULE_number = 3
    RULE_variable = 4
    RULE_function_def = 5
    RULE_args = 6
    RULE_cases = 7
    RULE_block = 8
    RULE_call = 9
    RULE_exprs = 10
    RULE_forexpr = 11
    RULE_exp = 12
    RULE_summ = 13
    RULE_mult = 14
    RULE_atom = 15

    ruleNames =  [ "parse", "expr", "operators", "number", "variable", "function_def", 
                   "args", "cases", "block", "call", "exprs", "forexpr", 
                   "exp", "summ", "mult", "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    ID=32
    COMMENT=33
    LINE_COMMENT=34
    NUMBER=35
    INT=36
    FLOAT=37
    TRUE=38
    FALSE=39
    BOOL=40
    STRING=41
    WS=42
    DOT=43
    COMMA=44

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ParseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(sadbeepParser.EOF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sadbeepParser.ExprContext)
            else:
                return self.getTypedRuleContext(sadbeepParser.ExprContext,i)


        def getRuleIndex(self):
            return sadbeepParser.RULE_parse

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParse" ):
                return visitor.visitParse(self)
            else:
                return visitor.visitChildren(self)




    def parse(self):

        localctx = sadbeepParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << sadbeepParser.T__2) | (1 << sadbeepParser.T__3) | (1 << sadbeepParser.T__5) | (1 << sadbeepParser.T__6) | (1 << sadbeepParser.T__7) | (1 << sadbeepParser.T__9) | (1 << sadbeepParser.T__11) | (1 << sadbeepParser.T__12) | (1 << sadbeepParser.T__13) | (1 << sadbeepParser.T__14) | (1 << sadbeepParser.T__16) | (1 << sadbeepParser.T__30) | (1 << sadbeepParser.ID) | (1 << sadbeepParser.INT) | (1 << sadbeepParser.FLOAT) | (1 << sadbeepParser.BOOL) | (1 << sadbeepParser.STRING))) != 0):
                self.state = 32
                self.expr(0)
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 38
            self.match(sadbeepParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return sadbeepParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Expr_parenthesisContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a sadbeepParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(sadbeepParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_parenthesis" ):
                return visitor.visitExpr_parenthesis(self)
            else:
                return visitor.visitChildren(self)


    class OrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a sadbeepParser.ExprContext
            super().__init__(parser)
            self.cond = None # ExprContext
            self.copyFrom(ctx)

        def block(self):
            return self.getTypedRuleContext(sadbeepParser.BlockContext,0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sadbeepParser.ExprContext)
            else:
                return self.getTypedRuleContext(sadbeepParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr" ):
                return visitor.visitOr(self)
            else:
                return visitor.visitChildren(self)


    class ForContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a sadbeepParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def forexpr(self):
            return self.getTypedRuleContext(sadbeepParser.ForexprContext,0)

        def block(self):
            return self.getTypedRuleContext(sadbeepParser.BlockContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor" ):
                return visitor.visitFor(self)
            else:
                return visitor.visitChildren(self)


    class Expr_functionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a sadbeepParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def function_def(self):
            return self.getTypedRuleContext(sadbeepParser.Function_defContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_function" ):
                return visitor.visitExpr_function(self)
            else:
                return visitor.visitChildren(self)


    class WhileContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a sadbeepParser.ExprContext
            super().__init__(parser)
            self.cond = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sadbeepParser.ExprContext)
            else:
                return self.getTypedRuleContext(sadbeepParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)


    class SwitchContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a sadbeepParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(sadbeepParser.ExprContext,0)

        def cases(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sadbeepParser.CasesContext)
            else:
                return self.getTypedRuleContext(sadbeepParser.CasesContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitch" ):
                return visitor.visitSwitch(self)
            else:
                return visitor.visitChildren(self)


    class Expr_callContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a sadbeepParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def call(self):
            return self.getTypedRuleContext(sadbeepParser.CallContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_call" ):
                return visitor.visitExpr_call(self)
            else:
                return visitor.visitChildren(self)


    class Expr_followContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a sadbeepParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sadbeepParser.ExprContext)
            else:
                return self.getTypedRuleContext(sadbeepParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_follow" ):
                return visitor.visitExpr_follow(self)
            else:
                return visitor.visitChildren(self)


    class PrintContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a sadbeepParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(sadbeepParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)


    class Expr_operatorsContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a sadbeepParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(sadbeepParser.ExprContext,0)

        def operators(self):
            return self.getTypedRuleContext(sadbeepParser.OperatorsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_operators" ):
                return visitor.visitExpr_operators(self)
            else:
                return visitor.visitChildren(self)


    class Expr_numberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a sadbeepParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def number(self):
            return self.getTypedRuleContext(sadbeepParser.NumberContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_number" ):
                return visitor.visitExpr_number(self)
            else:
                return visitor.visitChildren(self)


    class ElseContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a sadbeepParser.ExprContext
            super().__init__(parser)
            self.cond = None # ExprContext
            self.then = None # BlockContext
            self.otherwise = None # BlockContext
            self.copyFrom(ctx)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sadbeepParser.BlockContext)
            else:
                return self.getTypedRuleContext(sadbeepParser.BlockContext,i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sadbeepParser.ExprContext)
            else:
                return self.getTypedRuleContext(sadbeepParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse" ):
                return visitor.visitElse(self)
            else:
                return visitor.visitChildren(self)


    class Expr_stringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a sadbeepParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(sadbeepParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_string" ):
                return visitor.visitExpr_string(self)
            else:
                return visitor.visitChildren(self)


    class Expr_negativeContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a sadbeepParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def exp(self):
            return self.getTypedRuleContext(sadbeepParser.ExpContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_negative" ):
                return visitor.visitExpr_negative(self)
            else:
                return visitor.visitChildren(self)


    class IfContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a sadbeepParser.ExprContext
            super().__init__(parser)
            self.cond = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sadbeepParser.ExprContext)
            else:
                return self.getTypedRuleContext(sadbeepParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)


    class ReturnContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a sadbeepParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(sadbeepParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn" ):
                return visitor.visitReturn(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a sadbeepParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variable(self):
            return self.getTypedRuleContext(sadbeepParser.VariableContext,0)

        def expr(self):
            return self.getTypedRuleContext(sadbeepParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)


    class Expr_IDContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a sadbeepParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(sadbeepParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_ID" ):
                return visitor.visitExpr_ID(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = sadbeepParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = sadbeepParser.AssignContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 41
                self.variable()
                self.state = 42
                self.match(sadbeepParser.T__0)
                self.state = 43
                self.expr(0)
                self.state = 44
                self.match(sadbeepParser.T__1)
                pass

            elif la_ == 2:
                localctx = sadbeepParser.PrintContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 46
                self.match(sadbeepParser.T__2)
                self.state = 47
                self.expr(0)
                self.state = 48
                self.match(sadbeepParser.T__1)
                pass

            elif la_ == 3:
                localctx = sadbeepParser.Expr_numberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 50
                self.number()
                pass

            elif la_ == 4:
                localctx = sadbeepParser.Expr_functionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 51
                self.function_def()
                pass

            elif la_ == 5:
                localctx = sadbeepParser.Expr_parenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 52
                self.match(sadbeepParser.T__3)
                self.state = 53
                self.expr(0)
                self.state = 54
                self.match(sadbeepParser.T__4)
                pass

            elif la_ == 6:
                localctx = sadbeepParser.Expr_stringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 56
                self.match(sadbeepParser.STRING)
                pass

            elif la_ == 7:
                localctx = sadbeepParser.ReturnContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 57
                self.match(sadbeepParser.T__5)
                self.state = 58
                self.expr(0)
                self.state = 59
                self.match(sadbeepParser.T__1)
                pass

            elif la_ == 8:
                localctx = sadbeepParser.Expr_IDContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 61
                self.match(sadbeepParser.ID)
                pass

            elif la_ == 9:
                localctx = sadbeepParser.Expr_callContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 62
                self.call()
                pass

            elif la_ == 10:
                localctx = sadbeepParser.Expr_negativeContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 64
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 63
                    self.match(sadbeepParser.T__6)


                self.state = 66
                self.exp()
                pass

            elif la_ == 11:
                localctx = sadbeepParser.IfContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 67
                self.match(sadbeepParser.T__7)
                self.state = 68
                localctx.cond = self.expr(0)
                self.state = 73
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 69
                        self.match(sadbeepParser.T__8)
                        self.state = 70
                        localctx.cond = self.expr(0) 
                    self.state = 75
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                pass

            elif la_ == 12:
                localctx = sadbeepParser.ElseContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==sadbeepParser.T__9:
                    self.state = 76
                    self.match(sadbeepParser.T__9)
                    self.state = 77
                    localctx.cond = self.expr(0)
                    self.state = 82
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 83
                localctx.then = self.block()
                self.state = 86
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 84
                    self.match(sadbeepParser.T__10)
                    self.state = 85
                    localctx.otherwise = self.block()


                pass

            elif la_ == 13:
                localctx = sadbeepParser.WhileContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 88
                self.match(sadbeepParser.T__11)
                self.state = 89
                localctx.cond = self.expr(0)
                self.state = 94
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 90
                        self.match(sadbeepParser.T__8)
                        self.state = 91
                        localctx.cond = self.expr(0) 
                    self.state = 96
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

                pass

            elif la_ == 14:
                localctx = sadbeepParser.OrContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==sadbeepParser.T__9:
                    self.state = 97
                    self.match(sadbeepParser.T__9)
                    self.state = 98
                    localctx.cond = self.expr(0)
                    self.state = 103
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 104
                self.block()
                pass

            elif la_ == 15:
                localctx = sadbeepParser.ForContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 105
                self.match(sadbeepParser.T__12)
                self.state = 106
                self.forexpr()
                self.state = 107
                self.block()
                pass

            elif la_ == 16:
                localctx = sadbeepParser.SwitchContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 109
                self.match(sadbeepParser.T__13)
                self.state = 111
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 110
                    self.expr(0)


                self.state = 113
                self.match(sadbeepParser.T__14)
                self.state = 115 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 114
                    self.cases()
                    self.state = 117 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==sadbeepParser.T__17):
                        break

                self.state = 119
                self.match(sadbeepParser.T__15)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 131
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 129
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = sadbeepParser.Expr_followContext(self, sadbeepParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 123
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 124
                        self.expr(15)
                        pass

                    elif la_ == 2:
                        localctx = sadbeepParser.Expr_operatorsContext(self, sadbeepParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 125
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 126
                        self.operators()
                        self.state = 127
                        self.match(sadbeepParser.T__1)
                        pass

             
                self.state = 133
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mult(self):
            return self.getTypedRuleContext(sadbeepParser.MultContext,0)


        def summ(self):
            return self.getTypedRuleContext(sadbeepParser.SummContext,0)


        def getRuleIndex(self):
            return sadbeepParser.RULE_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperators" ):
                return visitor.visitOperators(self)
            else:
                return visitor.visitChildren(self)




    def operators(self):

        localctx = sadbeepParser.OperatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_operators)
        try:
            self.state = 136
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.mult()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.summ()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(sadbeepParser.INT, 0)

        def FLOAT(self):
            return self.getToken(sadbeepParser.FLOAT, 0)

        def getRuleIndex(self):
            return sadbeepParser.RULE_number

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = sadbeepParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            _la = self._input.LA(1)
            if not(_la==sadbeepParser.INT or _la==sadbeepParser.FLOAT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(sadbeepParser.ID, 0)

        def getRuleIndex(self):
            return sadbeepParser.RULE_variable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = sadbeepParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(sadbeepParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def block(self):
            return self.getTypedRuleContext(sadbeepParser.BlockContext,0)


        def ID(self):
            return self.getToken(sadbeepParser.ID, 0)

        def args(self):
            return self.getTypedRuleContext(sadbeepParser.ArgsContext,0)


        def getRuleIndex(self):
            return sadbeepParser.RULE_function_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_def" ):
                return visitor.visitFunction_def(self)
            else:
                return visitor.visitChildren(self)




    def function_def(self):

        localctx = sadbeepParser.Function_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_function_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(sadbeepParser.T__16)
            self.state = 143
            localctx.name = self.match(sadbeepParser.ID)
            self.state = 144
            self.match(sadbeepParser.T__3)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==sadbeepParser.ID:
                self.state = 145
                self.args()


            self.state = 148
            self.match(sadbeepParser.T__4)
            self.state = 149
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(sadbeepParser.ID)
            else:
                return self.getToken(sadbeepParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(sadbeepParser.COMMA)
            else:
                return self.getToken(sadbeepParser.COMMA, i)

        def getRuleIndex(self):
            return sadbeepParser.RULE_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = sadbeepParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(sadbeepParser.ID)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==sadbeepParser.COMMA:
                self.state = 152
                self.match(sadbeepParser.COMMA)
                self.state = 153
                self.match(sadbeepParser.ID)
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CasesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sadbeepParser.ExprContext)
            else:
                return self.getTypedRuleContext(sadbeepParser.ExprContext,i)


        def getRuleIndex(self):
            return sadbeepParser.RULE_cases

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCases" ):
                return visitor.visitCases(self)
            else:
                return visitor.visitChildren(self)




    def cases(self):

        localctx = sadbeepParser.CasesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cases)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(sadbeepParser.T__17)
            self.state = 160
            self.expr(0)
            self.state = 161
            self.match(sadbeepParser.T__18)
            self.state = 162
            self.expr(0)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==sadbeepParser.T__19:
                self.state = 163
                self.match(sadbeepParser.T__19)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sadbeepParser.ExprContext)
            else:
                return self.getTypedRuleContext(sadbeepParser.ExprContext,i)


        def getRuleIndex(self):
            return sadbeepParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = sadbeepParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(sadbeepParser.T__14)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << sadbeepParser.T__2) | (1 << sadbeepParser.T__3) | (1 << sadbeepParser.T__5) | (1 << sadbeepParser.T__6) | (1 << sadbeepParser.T__7) | (1 << sadbeepParser.T__9) | (1 << sadbeepParser.T__11) | (1 << sadbeepParser.T__12) | (1 << sadbeepParser.T__13) | (1 << sadbeepParser.T__14) | (1 << sadbeepParser.T__16) | (1 << sadbeepParser.T__30) | (1 << sadbeepParser.ID) | (1 << sadbeepParser.INT) | (1 << sadbeepParser.FLOAT) | (1 << sadbeepParser.BOOL) | (1 << sadbeepParser.STRING))) != 0):
                self.state = 167
                self.expr(0)
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 173
            self.match(sadbeepParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def ID(self):
            return self.getToken(sadbeepParser.ID, 0)

        def exprs(self):
            return self.getTypedRuleContext(sadbeepParser.ExprsContext,0)


        def getRuleIndex(self):
            return sadbeepParser.RULE_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = sadbeepParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            localctx.name = self.match(sadbeepParser.ID)
            self.state = 176
            self.match(sadbeepParser.T__3)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << sadbeepParser.T__2) | (1 << sadbeepParser.T__3) | (1 << sadbeepParser.T__5) | (1 << sadbeepParser.T__6) | (1 << sadbeepParser.T__7) | (1 << sadbeepParser.T__9) | (1 << sadbeepParser.T__11) | (1 << sadbeepParser.T__12) | (1 << sadbeepParser.T__13) | (1 << sadbeepParser.T__14) | (1 << sadbeepParser.T__16) | (1 << sadbeepParser.T__30) | (1 << sadbeepParser.ID) | (1 << sadbeepParser.INT) | (1 << sadbeepParser.FLOAT) | (1 << sadbeepParser.BOOL) | (1 << sadbeepParser.STRING))) != 0):
                self.state = 177
                self.exprs()


            self.state = 180
            self.match(sadbeepParser.T__4)
            self.state = 181
            self.match(sadbeepParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sadbeepParser.ExprContext)
            else:
                return self.getTypedRuleContext(sadbeepParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(sadbeepParser.COMMA)
            else:
                return self.getToken(sadbeepParser.COMMA, i)

        def getRuleIndex(self):
            return sadbeepParser.RULE_exprs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprs" ):
                return visitor.visitExprs(self)
            else:
                return visitor.visitChildren(self)




    def exprs(self):

        localctx = sadbeepParser.ExprsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_exprs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.expr(0)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==sadbeepParser.COMMA:
                self.state = 184
                self.match(sadbeepParser.COMMA)
                self.state = 185
                self.expr(0)
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForexprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.cond = None # ExprContext

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sadbeepParser.VariableContext)
            else:
                return self.getTypedRuleContext(sadbeepParser.VariableContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sadbeepParser.ExprContext)
            else:
                return self.getTypedRuleContext(sadbeepParser.ExprContext,i)


        def getRuleIndex(self):
            return sadbeepParser.RULE_forexpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForexpr" ):
                return visitor.visitForexpr(self)
            else:
                return visitor.visitChildren(self)




    def forexpr(self):

        localctx = sadbeepParser.ForexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_forexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(sadbeepParser.T__3)
            self.state = 192
            self.variable()
            self.state = 193
            self.match(sadbeepParser.T__0)
            self.state = 194
            self.expr(0)
            self.state = 195
            self.match(sadbeepParser.T__1)
            self.state = 196
            localctx.cond = self.expr(0)
            self.state = 197
            self.match(sadbeepParser.T__1)
            self.state = 198
            self.variable()
            self.state = 199
            self.match(sadbeepParser.T__0)
            self.state = 200
            self.expr(0)
            self.state = 201
            self.match(sadbeepParser.T__4)
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
            self.left = None # SummContext
            self.op = None # Token
            self.right = None # ExpContext

        def summ(self):
            return self.getTypedRuleContext(sadbeepParser.SummContext,0)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sadbeepParser.ExpContext)
            else:
                return self.getTypedRuleContext(sadbeepParser.ExpContext,i)


        def getRuleIndex(self):
            return sadbeepParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = sadbeepParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            localctx.left = self.summ()
            self.state = 208
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 204
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << sadbeepParser.T__20) | (1 << sadbeepParser.T__21) | (1 << sadbeepParser.T__22) | (1 << sadbeepParser.T__23) | (1 << sadbeepParser.T__24) | (1 << sadbeepParser.T__25))) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 205
                    localctx.right = self.exp() 
                self.state = 210
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SummContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # MultContext
            self.op = None # Token
            self.right = None # SummContext

        def mult(self):
            return self.getTypedRuleContext(sadbeepParser.MultContext,0)


        def summ(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sadbeepParser.SummContext)
            else:
                return self.getTypedRuleContext(sadbeepParser.SummContext,i)


        def getRuleIndex(self):
            return sadbeepParser.RULE_summ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSumm" ):
                return visitor.visitSumm(self)
            else:
                return visitor.visitChildren(self)




    def summ(self):

        localctx = sadbeepParser.SummContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_summ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            localctx.left = self.mult()
            self.state = 216
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 212
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==sadbeepParser.T__6 or _la==sadbeepParser.T__26):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 213
                    localctx.right = self.summ() 
                self.state = 218
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None # AtomContext
            self.op = None # Token
            self.right = None # MultContext

        def atom(self):
            return self.getTypedRuleContext(sadbeepParser.AtomContext,0)


        def mult(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(sadbeepParser.MultContext)
            else:
                return self.getTypedRuleContext(sadbeepParser.MultContext,i)


        def getRuleIndex(self):
            return sadbeepParser.RULE_mult

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMult" ):
                return visitor.visitMult(self)
            else:
                return visitor.visitChildren(self)




    def mult(self):

        localctx = sadbeepParser.MultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_mult)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            localctx.left = self.atom()
            self.state = 224
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 220
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << sadbeepParser.T__27) | (1 << sadbeepParser.T__28) | (1 << sadbeepParser.T__29))) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 221
                    localctx.right = self.mult() 
                self.state = 226
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(sadbeepParser.ExpContext,0)


        def number(self):
            return self.getTypedRuleContext(sadbeepParser.NumberContext,0)


        def BOOL(self):
            return self.getToken(sadbeepParser.BOOL, 0)

        def STRING(self):
            return self.getToken(sadbeepParser.STRING, 0)

        def ID(self):
            return self.getToken(sadbeepParser.ID, 0)

        def getRuleIndex(self):
            return sadbeepParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = sadbeepParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [sadbeepParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.match(sadbeepParser.T__3)
                self.state = 229
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
                if la_ == 1:
                    self.state = 228
                    self.match(sadbeepParser.T__6)


                self.state = 231
                self.exp()
                self.state = 232
                self.match(sadbeepParser.T__4)
                pass
            elif token in [sadbeepParser.T__6, sadbeepParser.INT, sadbeepParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==sadbeepParser.T__6:
                    self.state = 234
                    self.match(sadbeepParser.T__6)


                self.state = 237
                self.number()
                pass
            elif token in [sadbeepParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 238
                self.match(sadbeepParser.BOOL)
                pass
            elif token in [sadbeepParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 239
                self.match(sadbeepParser.STRING)
                pass
            elif token in [sadbeepParser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 240
                self.match(sadbeepParser.ID)
                pass
            elif token in [sadbeepParser.T__30]:
                self.enterOuterAlt(localctx, 6)
                self.state = 241
                self.match(sadbeepParser.T__30)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         




