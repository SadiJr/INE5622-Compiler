// Generated from exem.g4 by ANTLR 4.8
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link exemParser}.
 */
public interface exemListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link exemParser#start}.
	 * @param ctx the parse tree
	 */
	void enterStart(exemParser.StartContext ctx);
	/**
	 * Exit a parse tree produced by {@link exemParser#start}.
	 * @param ctx the parse tree
	 */
	void exitStart(exemParser.StartContext ctx);
	/**
	 * Enter a parse tree produced by {@link exemParser#func}.
	 * @param ctx the parse tree
	 */
	void enterFunc(exemParser.FuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link exemParser#func}.
	 * @param ctx the parse tree
	 */
	void exitFunc(exemParser.FuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link exemParser#args}.
	 * @param ctx the parse tree
	 */
	void enterArgs(exemParser.ArgsContext ctx);
	/**
	 * Exit a parse tree produced by {@link exemParser#args}.
	 * @param ctx the parse tree
	 */
	void exitArgs(exemParser.ArgsContext ctx);
	/**
	 * Enter a parse tree produced by {@link exemParser#statms}.
	 * @param ctx the parse tree
	 */
	void enterStatms(exemParser.StatmsContext ctx);
	/**
	 * Exit a parse tree produced by {@link exemParser#statms}.
	 * @param ctx the parse tree
	 */
	void exitStatms(exemParser.StatmsContext ctx);
	/**
	 * Enter a parse tree produced by the {@code assign}
	 * labeled alternative in {@link exemParser#statm}.
	 * @param ctx the parse tree
	 */
	void enterAssign(exemParser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by the {@code assign}
	 * labeled alternative in {@link exemParser#statm}.
	 * @param ctx the parse tree
	 */
	void exitAssign(exemParser.AssignContext ctx);
	/**
	 * Enter a parse tree produced by the {@code print}
	 * labeled alternative in {@link exemParser#statm}.
	 * @param ctx the parse tree
	 */
	void enterPrint(exemParser.PrintContext ctx);
	/**
	 * Exit a parse tree produced by the {@code print}
	 * labeled alternative in {@link exemParser#statm}.
	 * @param ctx the parse tree
	 */
	void exitPrint(exemParser.PrintContext ctx);
	/**
	 * Enter a parse tree produced by the {@code if}
	 * labeled alternative in {@link exemParser#statm}.
	 * @param ctx the parse tree
	 */
	void enterIf(exemParser.IfContext ctx);
	/**
	 * Exit a parse tree produced by the {@code if}
	 * labeled alternative in {@link exemParser#statm}.
	 * @param ctx the parse tree
	 */
	void exitIf(exemParser.IfContext ctx);
	/**
	 * Enter a parse tree produced by the {@code while}
	 * labeled alternative in {@link exemParser#statm}.
	 * @param ctx the parse tree
	 */
	void enterWhile(exemParser.WhileContext ctx);
	/**
	 * Exit a parse tree produced by the {@code while}
	 * labeled alternative in {@link exemParser#statm}.
	 * @param ctx the parse tree
	 */
	void exitWhile(exemParser.WhileContext ctx);
	/**
	 * Enter a parse tree produced by the {@code return}
	 * labeled alternative in {@link exemParser#statm}.
	 * @param ctx the parse tree
	 */
	void enterReturn(exemParser.ReturnContext ctx);
	/**
	 * Exit a parse tree produced by the {@code return}
	 * labeled alternative in {@link exemParser#statm}.
	 * @param ctx the parse tree
	 */
	void exitReturn(exemParser.ReturnContext ctx);
	/**
	 * Enter a parse tree produced by {@link exemParser#call}.
	 * @param ctx the parse tree
	 */
	void enterCall(exemParser.CallContext ctx);
	/**
	 * Exit a parse tree produced by {@link exemParser#call}.
	 * @param ctx the parse tree
	 */
	void exitCall(exemParser.CallContext ctx);
	/**
	 * Enter a parse tree produced by {@link exemParser#exprs}.
	 * @param ctx the parse tree
	 */
	void enterExprs(exemParser.ExprsContext ctx);
	/**
	 * Exit a parse tree produced by {@link exemParser#exprs}.
	 * @param ctx the parse tree
	 */
	void exitExprs(exemParser.ExprsContext ctx);
	/**
	 * Enter a parse tree produced by {@link exemParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(exemParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link exemParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(exemParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link exemParser#summ}.
	 * @param ctx the parse tree
	 */
	void enterSumm(exemParser.SummContext ctx);
	/**
	 * Exit a parse tree produced by {@link exemParser#summ}.
	 * @param ctx the parse tree
	 */
	void exitSumm(exemParser.SummContext ctx);
	/**
	 * Enter a parse tree produced by {@link exemParser#mult}.
	 * @param ctx the parse tree
	 */
	void enterMult(exemParser.MultContext ctx);
	/**
	 * Exit a parse tree produced by {@link exemParser#mult}.
	 * @param ctx the parse tree
	 */
	void exitMult(exemParser.MultContext ctx);
	/**
	 * Enter a parse tree produced by {@link exemParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterAtom(exemParser.AtomContext ctx);
	/**
	 * Exit a parse tree produced by {@link exemParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitAtom(exemParser.AtomContext ctx);
}