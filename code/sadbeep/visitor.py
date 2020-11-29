from .sadbeep.sadbeepParser import sadbeepParser
from .sadbeep.sadbeepVisitor import sadbeepVisitor

class visitor(sadbeepVisitor):

    def __init__(self):
        self.table = {}

    def visitAssign(self, ctx:sadbeepParser.AssignContext):
        print(str(ctx.expr()))
        self.table[str(ctx.variable())] = self.visit(ctx.expr())

    def visitExpr_number(self, ctx:sadbeepParser.Expr_numberContext):
        print("expr-number")
        return self.visit(ctx.number())

    def visitMult(self, ctx: sadbeepParser.MultContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if ctx.op.text == '*':
            return left * right
        elif ctx.op.text == '/':
            return left / right
        else:
            return left % right

    def visitSumm(self, ctx: sadbeepParser.SummContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if ctx.op.text == '+':
            return left + right
        else:
            return left - right

    def visitExpr_parenthesis(self, ctx: sadbeepParser.Expr_parenthesisContext):
        return self.visit(ctx.expr())

    def visitAtom(self, ctx: sadbeepParser.AtomContext):
        #definir o negativo e o parenteses
        if ctx.ID():
            print("id")
            return self.table[str(ctx.ID())]
        elif ctx.number():
            print('number')
            return self.visit(ctx.number())
        elif ctx.BOOL():
            return bool(str(ctx.BOOL()))

    def visitNumber(self, ctx: sadbeepParser.NumberContext):
        print('number')
        if ctx.INT():
            return int(str(ctx.INT()))
        else:
            return float(str(ctx.FLOAT()))
