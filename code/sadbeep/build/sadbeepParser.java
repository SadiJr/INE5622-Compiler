// Generated from sadbeep.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class sadbeepParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, OPEN_PAREN=22, CLOSE_PAREN=23, 
		ID=24, NUMBER=25, INT=26, UINT=27, FLOAT=28, TRUE=29, FALSE=30, BOOL=31, 
		WS=32, DOT=33, COMMA=34, STRING=35, COMMENT=36, LINE_COMMENT=37;
	public static final int
		RULE_parse = 0, RULE_expr = 1, RULE_operators = 2, RULE_function_def = 3, 
		RULE_args = 4, RULE_block = 5, RULE_call = 6, RULE_exprs = 7, RULE_number = 8, 
		RULE_variable = 9, RULE_exp = 10, RULE_summ = 11, RULE_mult = 12, RULE_atom = 13;
	private static String[] makeRuleNames() {
		return new String[] {
			"parse", "expr", "operators", "function_def", "args", "block", "call", 
			"exprs", "number", "variable", "exp", "summ", "mult", "atom"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'='", "';'", "'return'", "'if'", "'else'", "'while'", "'+'", "'-'", 
			"'/'", "'*'", "'func'", "'{'", "'}'", "'>'", "'<'", "'>='", "'<='", "'=='", 
			"'!='", "'%'", "'input'", "'('", "')'", null, null, null, null, null, 
			"'true'", "'false'", null, null, "'.'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, "OPEN_PAREN", 
			"CLOSE_PAREN", "ID", "NUMBER", "INT", "UINT", "FLOAT", "TRUE", "FALSE", 
			"BOOL", "WS", "DOT", "COMMA", "STRING", "COMMENT", "LINE_COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "sadbeep.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public sadbeepParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ParseContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(sadbeepParser.EOF, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ParseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parse; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).enterParse(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).exitParse(this);
		}
	}

	public final ParseContext parse() throws RecognitionException {
		ParseContext _localctx = new ParseContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_parse);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(31);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__2) | (1L << T__3) | (1L << T__5) | (1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__20) | (1L << OPEN_PAREN) | (1L << ID) | (1L << NUMBER) | (1L << INT) | (1L << UINT) | (1L << FLOAT) | (1L << BOOL) | (1L << STRING))) != 0)) {
				{
				{
				setState(28);
				expr(0);
				}
				}
				setState(33);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(34);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public ExprContext cond;
		public BlockContext then;
		public BlockContext otherwise;
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public NumberContext number() {
			return getRuleContext(NumberContext.class,0);
		}
		public Function_defContext function_def() {
			return getRuleContext(Function_defContext.class,0);
		}
		public TerminalNode OPEN_PAREN() { return getToken(sadbeepParser.OPEN_PAREN, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(sadbeepParser.CLOSE_PAREN, 0); }
		public TerminalNode STRING() { return getToken(sadbeepParser.STRING, 0); }
		public TerminalNode ID() { return getToken(sadbeepParser.ID, 0); }
		public CallContext call() {
			return getRuleContext(CallContext.class,0);
		}
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public OperatorsContext operators() {
			return getRuleContext(OperatorsContext.class,0);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).enterExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).exitExpr(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 2;
		enterRecursionRule(_localctx, 2, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(37);
				variable();
				setState(38);
				match(T__0);
				setState(39);
				expr(0);
				setState(40);
				match(T__1);
				}
				break;
			case 2:
				{
				setState(42);
				number();
				}
				break;
			case 3:
				{
				setState(43);
				function_def();
				}
				break;
			case 4:
				{
				setState(44);
				match(OPEN_PAREN);
				setState(45);
				expr(0);
				setState(46);
				match(CLOSE_PAREN);
				}
				break;
			case 5:
				{
				setState(48);
				match(STRING);
				}
				break;
			case 6:
				{
				setState(49);
				match(T__2);
				setState(50);
				expr(0);
				setState(51);
				match(T__1);
				}
				break;
			case 7:
				{
				setState(53);
				match(ID);
				}
				break;
			case 8:
				{
				setState(54);
				call();
				}
				break;
			case 9:
				{
				setState(55);
				exp();
				}
				break;
			case 10:
				{
				setState(56);
				operators();
				}
				break;
			case 11:
				{
				setState(57);
				match(T__3);
				setState(58);
				((ExprContext)_localctx).cond = expr(0);
				setState(59);
				((ExprContext)_localctx).then = block();
				setState(62);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
				case 1:
					{
					setState(60);
					match(T__4);
					setState(61);
					((ExprContext)_localctx).otherwise = block();
					}
					break;
				}
				}
				break;
			case 12:
				{
				setState(64);
				match(T__5);
				setState(65);
				((ExprContext)_localctx).cond = expr(0);
				setState(66);
				block();
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(74);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new ExprContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_expr);
					setState(70);
					if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
					setState(71);
					expr(11);
					}
					} 
				}
				setState(76);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class OperatorsContext extends ParserRuleContext {
		public OperatorsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operators; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).enterOperators(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).exitOperators(this);
		}
	}

	public final OperatorsContext operators() throws RecognitionException {
		OperatorsContext _localctx = new OperatorsContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_operators);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__9))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_defContext extends ParserRuleContext {
		public Token name;
		public TerminalNode OPEN_PAREN() { return getToken(sadbeepParser.OPEN_PAREN, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(sadbeepParser.CLOSE_PAREN, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode ID() { return getToken(sadbeepParser.ID, 0); }
		public ArgsContext args() {
			return getRuleContext(ArgsContext.class,0);
		}
		public Function_defContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_def; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).enterFunction_def(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).exitFunction_def(this);
		}
	}

	public final Function_defContext function_def() throws RecognitionException {
		Function_defContext _localctx = new Function_defContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_function_def);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(79);
			match(T__10);
			setState(80);
			((Function_defContext)_localctx).name = match(ID);
			setState(81);
			match(OPEN_PAREN);
			setState(83);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(82);
				args();
				}
			}

			setState(85);
			match(CLOSE_PAREN);
			setState(86);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgsContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(sadbeepParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(sadbeepParser.ID, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(sadbeepParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(sadbeepParser.COMMA, i);
		}
		public ArgsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_args; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).enterArgs(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).exitArgs(this);
		}
	}

	public final ArgsContext args() throws RecognitionException {
		ArgsContext _localctx = new ArgsContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_args);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			match(ID);
			setState(93);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(89);
				match(COMMA);
				setState(90);
				match(ID);
				}
				}
				setState(95);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).enterBlock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).exitBlock(this);
		}
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_block);
		int _la;
		try {
			setState(105);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__11:
				enterOuterAlt(_localctx, 1);
				{
				setState(96);
				match(T__11);
				setState(100);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__2) | (1L << T__3) | (1L << T__5) | (1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__20) | (1L << OPEN_PAREN) | (1L << ID) | (1L << NUMBER) | (1L << INT) | (1L << UINT) | (1L << FLOAT) | (1L << BOOL) | (1L << STRING))) != 0)) {
					{
					{
					setState(97);
					expr(0);
					}
					}
					setState(102);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(103);
				match(T__12);
				}
				break;
			case T__2:
			case T__3:
			case T__5:
			case T__6:
			case T__7:
			case T__8:
			case T__9:
			case T__10:
			case T__20:
			case OPEN_PAREN:
			case ID:
			case NUMBER:
			case INT:
			case UINT:
			case FLOAT:
			case BOOL:
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(104);
				expr(0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CallContext extends ParserRuleContext {
		public Token name;
		public TerminalNode OPEN_PAREN() { return getToken(sadbeepParser.OPEN_PAREN, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(sadbeepParser.CLOSE_PAREN, 0); }
		public TerminalNode ID() { return getToken(sadbeepParser.ID, 0); }
		public ExprsContext exprs() {
			return getRuleContext(ExprsContext.class,0);
		}
		public CallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_call; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).enterCall(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).exitCall(this);
		}
	}

	public final CallContext call() throws RecognitionException {
		CallContext _localctx = new CallContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			((CallContext)_localctx).name = match(ID);
			setState(108);
			match(OPEN_PAREN);
			setState(110);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__2) | (1L << T__3) | (1L << T__5) | (1L << T__6) | (1L << T__7) | (1L << T__8) | (1L << T__9) | (1L << T__10) | (1L << T__20) | (1L << OPEN_PAREN) | (1L << ID) | (1L << NUMBER) | (1L << INT) | (1L << UINT) | (1L << FLOAT) | (1L << BOOL) | (1L << STRING))) != 0)) {
				{
				setState(109);
				exprs();
				}
			}

			setState(112);
			match(CLOSE_PAREN);
			setState(113);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprsContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(sadbeepParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(sadbeepParser.COMMA, i);
		}
		public ExprsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprs; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).enterExprs(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).exitExprs(this);
		}
	}

	public final ExprsContext exprs() throws RecognitionException {
		ExprsContext _localctx = new ExprsContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_exprs);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			expr(0);
			setState(120);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(116);
				match(COMMA);
				setState(117);
				expr(0);
				}
				}
				setState(122);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NumberContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(sadbeepParser.NUMBER, 0); }
		public NumberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_number; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).enterNumber(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).exitNumber(this);
		}
	}

	public final NumberContext number() throws RecognitionException {
		NumberContext _localctx = new NumberContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_number);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(123);
			match(NUMBER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariableContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(sadbeepParser.ID, 0); }
		public VariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).enterVariable(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).exitVariable(this);
		}
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_variable);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpContext extends ParserRuleContext {
		public SummContext left;
		public Token op;
		public ExpContext right;
		public SummContext summ() {
			return getRuleContext(SummContext.class,0);
		}
		public List<ExpContext> exp() {
			return getRuleContexts(ExpContext.class);
		}
		public ExpContext exp(int i) {
			return getRuleContext(ExpContext.class,i);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).enterExp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).exitExp(this);
		}
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_exp);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(127);
			((ExpContext)_localctx).left = summ();
			setState(132);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(128);
					((ExpContext)_localctx).op = _input.LT(1);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__13) | (1L << T__14) | (1L << T__15) | (1L << T__16) | (1L << T__17) | (1L << T__18))) != 0)) ) {
						((ExpContext)_localctx).op = (Token)_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(129);
					((ExpContext)_localctx).right = exp();
					}
					} 
				}
				setState(134);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SummContext extends ParserRuleContext {
		public MultContext left;
		public Token op;
		public SummContext right;
		public MultContext mult() {
			return getRuleContext(MultContext.class,0);
		}
		public List<SummContext> summ() {
			return getRuleContexts(SummContext.class);
		}
		public SummContext summ(int i) {
			return getRuleContext(SummContext.class,i);
		}
		public SummContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_summ; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).enterSumm(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).exitSumm(this);
		}
	}

	public final SummContext summ() throws RecognitionException {
		SummContext _localctx = new SummContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_summ);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(135);
			((SummContext)_localctx).left = mult();
			setState(140);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(136);
					((SummContext)_localctx).op = _input.LT(1);
					_la = _input.LA(1);
					if ( !(_la==T__6 || _la==T__7) ) {
						((SummContext)_localctx).op = (Token)_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(137);
					((SummContext)_localctx).right = summ();
					}
					} 
				}
				setState(142);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class MultContext extends ParserRuleContext {
		public AtomContext left;
		public Token op;
		public MultContext right;
		public AtomContext atom() {
			return getRuleContext(AtomContext.class,0);
		}
		public List<MultContext> mult() {
			return getRuleContexts(MultContext.class);
		}
		public MultContext mult(int i) {
			return getRuleContext(MultContext.class,i);
		}
		public MultContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mult; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).enterMult(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).exitMult(this);
		}
	}

	public final MultContext mult() throws RecognitionException {
		MultContext _localctx = new MultContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_mult);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(143);
			((MultContext)_localctx).left = atom();
			setState(148);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(144);
					((MultContext)_localctx).op = _input.LT(1);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__8) | (1L << T__9) | (1L << T__19))) != 0)) ) {
						((MultContext)_localctx).op = (Token)_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(145);
					((MultContext)_localctx).right = mult();
					}
					} 
				}
				setState(150);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AtomContext extends ParserRuleContext {
		public TerminalNode OPEN_PAREN() { return getToken(sadbeepParser.OPEN_PAREN, 0); }
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public TerminalNode CLOSE_PAREN() { return getToken(sadbeepParser.CLOSE_PAREN, 0); }
		public TerminalNode INT() { return getToken(sadbeepParser.INT, 0); }
		public TerminalNode UINT() { return getToken(sadbeepParser.UINT, 0); }
		public TerminalNode BOOL() { return getToken(sadbeepParser.BOOL, 0); }
		public TerminalNode FLOAT() { return getToken(sadbeepParser.FLOAT, 0); }
		public TerminalNode STRING() { return getToken(sadbeepParser.STRING, 0); }
		public TerminalNode ID() { return getToken(sadbeepParser.ID, 0); }
		public AtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atom; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).enterAtom(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof sadbeepListener ) ((sadbeepListener)listener).exitAtom(this);
		}
	}

	public final AtomContext atom() throws RecognitionException {
		AtomContext _localctx = new AtomContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_atom);
		try {
			setState(162);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPEN_PAREN:
				enterOuterAlt(_localctx, 1);
				{
				setState(151);
				match(OPEN_PAREN);
				setState(152);
				exp();
				setState(153);
				match(CLOSE_PAREN);
				}
				break;
			case INT:
				enterOuterAlt(_localctx, 2);
				{
				setState(155);
				match(INT);
				}
				break;
			case UINT:
				enterOuterAlt(_localctx, 3);
				{
				setState(156);
				match(UINT);
				}
				break;
			case BOOL:
				enterOuterAlt(_localctx, 4);
				{
				setState(157);
				match(BOOL);
				}
				break;
			case FLOAT:
				enterOuterAlt(_localctx, 5);
				{
				setState(158);
				match(FLOAT);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 6);
				{
				setState(159);
				match(STRING);
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 7);
				{
				setState(160);
				match(ID);
				}
				break;
			case T__20:
				enterOuterAlt(_localctx, 8);
				{
				setState(161);
				match(T__20);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 1:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 10);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\'\u00a7\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\3\2\7\2 \n\2\f\2\16\2#\13\2\3"+
		"\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3A\n\3\3\3\3\3\3\3\3\3\5\3"+
		"G\n\3\3\3\3\3\7\3K\n\3\f\3\16\3N\13\3\3\4\3\4\3\5\3\5\3\5\3\5\5\5V\n\5"+
		"\3\5\3\5\3\5\3\6\3\6\3\6\7\6^\n\6\f\6\16\6a\13\6\3\7\3\7\7\7e\n\7\f\7"+
		"\16\7h\13\7\3\7\3\7\5\7l\n\7\3\b\3\b\3\b\5\bq\n\b\3\b\3\b\3\b\3\t\3\t"+
		"\3\t\7\ty\n\t\f\t\16\t|\13\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\7\f\u0085\n"+
		"\f\f\f\16\f\u0088\13\f\3\r\3\r\3\r\7\r\u008d\n\r\f\r\16\r\u0090\13\r\3"+
		"\16\3\16\3\16\7\16\u0095\n\16\f\16\16\16\u0098\13\16\3\17\3\17\3\17\3"+
		"\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00a5\n\17\3\17\2\3\4\20\2"+
		"\4\6\b\n\f\16\20\22\24\26\30\32\34\2\6\3\2\t\f\3\2\20\25\3\2\t\n\4\2\13"+
		"\f\26\26\2\u00b6\2!\3\2\2\2\4F\3\2\2\2\6O\3\2\2\2\bQ\3\2\2\2\nZ\3\2\2"+
		"\2\fk\3\2\2\2\16m\3\2\2\2\20u\3\2\2\2\22}\3\2\2\2\24\177\3\2\2\2\26\u0081"+
		"\3\2\2\2\30\u0089\3\2\2\2\32\u0091\3\2\2\2\34\u00a4\3\2\2\2\36 \5\4\3"+
		"\2\37\36\3\2\2\2 #\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"$\3\2\2\2#!\3\2\2\2"+
		"$%\7\2\2\3%\3\3\2\2\2&\'\b\3\1\2\'(\5\24\13\2()\7\3\2\2)*\5\4\3\2*+\7"+
		"\4\2\2+G\3\2\2\2,G\5\22\n\2-G\5\b\5\2./\7\30\2\2/\60\5\4\3\2\60\61\7\31"+
		"\2\2\61G\3\2\2\2\62G\7%\2\2\63\64\7\5\2\2\64\65\5\4\3\2\65\66\7\4\2\2"+
		"\66G\3\2\2\2\67G\7\32\2\28G\5\16\b\29G\5\26\f\2:G\5\6\4\2;<\7\6\2\2<="+
		"\5\4\3\2=@\5\f\7\2>?\7\7\2\2?A\5\f\7\2@>\3\2\2\2@A\3\2\2\2AG\3\2\2\2B"+
		"C\7\b\2\2CD\5\4\3\2DE\5\f\7\2EG\3\2\2\2F&\3\2\2\2F,\3\2\2\2F-\3\2\2\2"+
		"F.\3\2\2\2F\62\3\2\2\2F\63\3\2\2\2F\67\3\2\2\2F8\3\2\2\2F9\3\2\2\2F:\3"+
		"\2\2\2F;\3\2\2\2FB\3\2\2\2GL\3\2\2\2HI\f\f\2\2IK\5\4\3\rJH\3\2\2\2KN\3"+
		"\2\2\2LJ\3\2\2\2LM\3\2\2\2M\5\3\2\2\2NL\3\2\2\2OP\t\2\2\2P\7\3\2\2\2Q"+
		"R\7\r\2\2RS\7\32\2\2SU\7\30\2\2TV\5\n\6\2UT\3\2\2\2UV\3\2\2\2VW\3\2\2"+
		"\2WX\7\31\2\2XY\5\f\7\2Y\t\3\2\2\2Z_\7\32\2\2[\\\7$\2\2\\^\7\32\2\2]["+
		"\3\2\2\2^a\3\2\2\2_]\3\2\2\2_`\3\2\2\2`\13\3\2\2\2a_\3\2\2\2bf\7\16\2"+
		"\2ce\5\4\3\2dc\3\2\2\2eh\3\2\2\2fd\3\2\2\2fg\3\2\2\2gi\3\2\2\2hf\3\2\2"+
		"\2il\7\17\2\2jl\5\4\3\2kb\3\2\2\2kj\3\2\2\2l\r\3\2\2\2mn\7\32\2\2np\7"+
		"\30\2\2oq\5\20\t\2po\3\2\2\2pq\3\2\2\2qr\3\2\2\2rs\7\31\2\2st\7\4\2\2"+
		"t\17\3\2\2\2uz\5\4\3\2vw\7$\2\2wy\5\4\3\2xv\3\2\2\2y|\3\2\2\2zx\3\2\2"+
		"\2z{\3\2\2\2{\21\3\2\2\2|z\3\2\2\2}~\7\33\2\2~\23\3\2\2\2\177\u0080\7"+
		"\32\2\2\u0080\25\3\2\2\2\u0081\u0086\5\30\r\2\u0082\u0083\t\3\2\2\u0083"+
		"\u0085\5\26\f\2\u0084\u0082\3\2\2\2\u0085\u0088\3\2\2\2\u0086\u0084\3"+
		"\2\2\2\u0086\u0087\3\2\2\2\u0087\27\3\2\2\2\u0088\u0086\3\2\2\2\u0089"+
		"\u008e\5\32\16\2\u008a\u008b\t\4\2\2\u008b\u008d\5\30\r\2\u008c\u008a"+
		"\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f"+
		"\31\3\2\2\2\u0090\u008e\3\2\2\2\u0091\u0096\5\34\17\2\u0092\u0093\t\5"+
		"\2\2\u0093\u0095\5\32\16\2\u0094\u0092\3\2\2\2\u0095\u0098\3\2\2\2\u0096"+
		"\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\33\3\2\2\2\u0098\u0096\3\2\2"+
		"\2\u0099\u009a\7\30\2\2\u009a\u009b\5\26\f\2\u009b\u009c\7\31\2\2\u009c"+
		"\u00a5\3\2\2\2\u009d\u00a5\7\34\2\2\u009e\u00a5\7\35\2\2\u009f\u00a5\7"+
		"!\2\2\u00a0\u00a5\7\36\2\2\u00a1\u00a5\7%\2\2\u00a2\u00a5\7\32\2\2\u00a3"+
		"\u00a5\7\27\2\2\u00a4\u0099\3\2\2\2\u00a4\u009d\3\2\2\2\u00a4\u009e\3"+
		"\2\2\2\u00a4\u009f\3\2\2\2\u00a4\u00a0\3\2\2\2\u00a4\u00a1\3\2\2\2\u00a4"+
		"\u00a2\3\2\2\2\u00a4\u00a3\3\2\2\2\u00a5\35\3\2\2\2\20!@FLU_fkpz\u0086"+
		"\u008e\u0096\u00a4";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}