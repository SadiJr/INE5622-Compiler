// Generated from sadbeep.g4 by ANTLR 4.8
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link sadbeepParser}.
 */
public interface sadbeepListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link sadbeepParser#parse}.
	 * @param ctx the parse tree
	 */
	void enterParse(sadbeepParser.ParseContext ctx);
	/**
	 * Exit a parse tree produced by {@link sadbeepParser#parse}.
	 * @param ctx the parse tree
	 */
	void exitParse(sadbeepParser.ParseContext ctx);
	/**
	 * Enter a parse tree produced by {@link sadbeepParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(sadbeepParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link sadbeepParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(sadbeepParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link sadbeepParser#operators}.
	 * @param ctx the parse tree
	 */
	void enterOperators(sadbeepParser.OperatorsContext ctx);
	/**
	 * Exit a parse tree produced by {@link sadbeepParser#operators}.
	 * @param ctx the parse tree
	 */
	void exitOperators(sadbeepParser.OperatorsContext ctx);
	/**
	 * Enter a parse tree produced by {@link sadbeepParser#function_def}.
	 * @param ctx the parse tree
	 */
	void enterFunction_def(sadbeepParser.Function_defContext ctx);
	/**
	 * Exit a parse tree produced by {@link sadbeepParser#function_def}.
	 * @param ctx the parse tree
	 */
	void exitFunction_def(sadbeepParser.Function_defContext ctx);
	/**
	 * Enter a parse tree produced by {@link sadbeepParser#args}.
	 * @param ctx the parse tree
	 */
	void enterArgs(sadbeepParser.ArgsContext ctx);
	/**
	 * Exit a parse tree produced by {@link sadbeepParser#args}.
	 * @param ctx the parse tree
	 */
	void exitArgs(sadbeepParser.ArgsContext ctx);
	/**
	 * Enter a parse tree produced by {@link sadbeepParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(sadbeepParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link sadbeepParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(sadbeepParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link sadbeepParser#call}.
	 * @param ctx the parse tree
	 */
	void enterCall(sadbeepParser.CallContext ctx);
	/**
	 * Exit a parse tree produced by {@link sadbeepParser#call}.
	 * @param ctx the parse tree
	 */
	void exitCall(sadbeepParser.CallContext ctx);
	/**
	 * Enter a parse tree produced by {@link sadbeepParser#exprs}.
	 * @param ctx the parse tree
	 */
	void enterExprs(sadbeepParser.ExprsContext ctx);
	/**
	 * Exit a parse tree produced by {@link sadbeepParser#exprs}.
	 * @param ctx the parse tree
	 */
	void exitExprs(sadbeepParser.ExprsContext ctx);
	/**
	 * Enter a parse tree produced by {@link sadbeepParser#number}.
	 * @param ctx the parse tree
	 */
	void enterNumber(sadbeepParser.NumberContext ctx);
	/**
	 * Exit a parse tree produced by {@link sadbeepParser#number}.
	 * @param ctx the parse tree
	 */
	void exitNumber(sadbeepParser.NumberContext ctx);
	/**
	 * Enter a parse tree produced by {@link sadbeepParser#variable}.
	 * @param ctx the parse tree
	 */
	void enterVariable(sadbeepParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by {@link sadbeepParser#variable}.
	 * @param ctx the parse tree
	 */
	void exitVariable(sadbeepParser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by {@link sadbeepParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterExp(sadbeepParser.ExpContext ctx);
	/**
	 * Exit a parse tree produced by {@link sadbeepParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitExp(sadbeepParser.ExpContext ctx);
	/**
	 * Enter a parse tree produced by {@link sadbeepParser#summ}.
	 * @param ctx the parse tree
	 */
	void enterSumm(sadbeepParser.SummContext ctx);
	/**
	 * Exit a parse tree produced by {@link sadbeepParser#summ}.
	 * @param ctx the parse tree
	 */
	void exitSumm(sadbeepParser.SummContext ctx);
	/**
	 * Enter a parse tree produced by {@link sadbeepParser#mult}.
	 * @param ctx the parse tree
	 */
	void enterMult(sadbeepParser.MultContext ctx);
	/**
	 * Exit a parse tree produced by {@link sadbeepParser#mult}.
	 * @param ctx the parse tree
	 */
	void exitMult(sadbeepParser.MultContext ctx);
	/**
	 * Enter a parse tree produced by {@link sadbeepParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterAtom(sadbeepParser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link sadbeepParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitAtom(sadbeepParser.AtomContext ctx);
}