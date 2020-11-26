# Generated from /home/marcos/PycharmProjects/INE5622-Compiler/code/sadbeep/sadbeep/sadbeep.g4 by ANTLR 4.8
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


    # Visit a parse tree produced by sadbeepParser#expr.
    def visitExpr(self, ctx:sadbeepParser.ExprContext):
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