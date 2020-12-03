# Generated from /home/sadi/Curso/Fase Atual/Introdução a Compiladores/Implementação de Compiladores/INE5622-Compiler/code/sadbeep/sadbeep/sadbeep.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .sadbeepParser import sadbeepParser
else:
    from sadbeepParser import sadbeepParser

# This class defines a complete generic visitor for a parse tree produced by sadbeepParser.

class sadbeepVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by sadbeepParser#parse.
    def visitParse(self, ctx:sadbeepParser.ParseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#expr_parenthesis.
    def visitExpr_parenthesis(self, ctx:sadbeepParser.Expr_parenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#or.
    def visitOr(self, ctx:sadbeepParser.OrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#for.
    def visitFor(self, ctx:sadbeepParser.ForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#expr_function.
    def visitExpr_function(self, ctx:sadbeepParser.Expr_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#while.
    def visitWhile(self, ctx:sadbeepParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#switch.
    def visitSwitch(self, ctx:sadbeepParser.SwitchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#expr_call.
    def visitExpr_call(self, ctx:sadbeepParser.Expr_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#expr_follow.
    def visitExpr_follow(self, ctx:sadbeepParser.Expr_followContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#print.
    def visitPrint(self, ctx:sadbeepParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#expr_operators.
    def visitExpr_operators(self, ctx:sadbeepParser.Expr_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#expr_number.
    def visitExpr_number(self, ctx:sadbeepParser.Expr_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#else.
    def visitElse(self, ctx:sadbeepParser.ElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#expr_string.
    def visitExpr_string(self, ctx:sadbeepParser.Expr_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#expr_negative.
    def visitExpr_negative(self, ctx:sadbeepParser.Expr_negativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#if.
    def visitIf(self, ctx:sadbeepParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#return.
    def visitReturn(self, ctx:sadbeepParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#assign.
    def visitAssign(self, ctx:sadbeepParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#expr_ID.
    def visitExpr_ID(self, ctx:sadbeepParser.Expr_IDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#operators.
    def visitOperators(self, ctx:sadbeepParser.OperatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#number.
    def visitNumber(self, ctx:sadbeepParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#variable.
    def visitVariable(self, ctx:sadbeepParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#function_def.
    def visitFunction_def(self, ctx:sadbeepParser.Function_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#args.
    def visitArgs(self, ctx:sadbeepParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#cases.
    def visitCases(self, ctx:sadbeepParser.CasesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#block.
    def visitBlock(self, ctx:sadbeepParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#call.
    def visitCall(self, ctx:sadbeepParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#exprs.
    def visitExprs(self, ctx:sadbeepParser.ExprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#forexpr.
    def visitForexpr(self, ctx:sadbeepParser.ForexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#exp.
    def visitExp(self, ctx:sadbeepParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#summ.
    def visitSumm(self, ctx:sadbeepParser.SummContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#mult.
    def visitMult(self, ctx:sadbeepParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sadbeepParser#atom.
    def visitAtom(self, ctx:sadbeepParser.AtomContext):
        return self.visitChildren(ctx)



del sadbeepParser