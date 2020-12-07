from llvmlite import binding
from llvmlite import ir
from typing import List

from .sadbeep.sadbeepParser import sadbeepParser
from .sadbeep.sadbeepVisitor import sadbeepVisitor


class visitor(sadbeepVisitor):
    def __init__(self, file_name):
        self.table = {}
        self.module = ir.Module()
        self.file_name = file_name

        ftype = ir.FunctionType(ir.IntType(32), [])
        self.main = ir.Function(self.module, ftype=ftype, name='main')
        entry_block = self.main.append_basic_block(name='entry')
        self.builder = ir.IRBuilder(entry_block)

        # Declare C printf and scanf in the module
        p_type = ir.FunctionType(ir.IntType(32), [ir.IntType(8).as_pointer()], var_arg=True)
        self.table['__isoc99_scanf'] = ir.Function(self.module, p_type, name='__isoc99_scanf')
        #################################

        ftype = ir.FunctionType(ir.IntType(8), [ir.IntType(8).as_pointer()], var_arg=True)
        self.printf = ir.Function(self.module, ftype=ftype, name='printf')

        form_int = "Imprimindo essa caralha de int: %d\n\0"
        form_const_int = ir.Constant(ir.ArrayType(ir.IntType(8), len(form_int)), bytearray(form_int.encode('utf8')))

        self.form_int = ir.GlobalVariable(self.module, form_const_int.type, name='form_int')
        self.form_int.initializer = form_const_int

        form_float = "Imprimindo esse filho da puta de float: %f\n\0"
        form_const_float = ir.Constant(ir.ArrayType(ir.IntType(8), len(form_float)),
                                       bytearray(form_float.encode('utf8')))

        self.form_float = ir.GlobalVariable(self.module, form_const_float.type, name='form_float')
        self.form_float.initializer = form_const_float

        # Global variable for the printf first parameter
        fmt_str = '%d\n\0'
        fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt_str)), bytearray(fmt_str.encode('utf8')))
        self.global_fmt = ir.GlobalVariable(self.module, fmt.type, 'fmt')
        self.global_fmt.linkage = 'internal'
        self.global_fmt.global_constant = True
        self.global_fmt.initializer = fmt
        #################################

        # Global variable for the scanf first parameter
        fmt_str_in = '%d'
        fmt_in = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt_str_in)), bytearray(fmt_str_in.encode('utf8')))
        self.global_fmt_in = ir.GlobalVariable(self.module, fmt_in.type, 'fmt_in')
        self.global_fmt_in.linkage = 'internal'
        self.global_fmt_in.global_constant = True
        self.global_fmt_in.initializer = fmt_in
        #################################

        self.id_table = {}

    def asm(self) -> str:
        target_machine = binding.Target.from_default_triple().create_target_machine()
        llvm = binding.parse_assembly(str(self.module))
        return target_machine.emit_assembly(llvm)

    def isInt(self, n) -> bool:
        try:
            int(n)
            return True
        except:
            return False

    def visitParse(self, ctx:sadbeepParser.ParseContext):
        self.visitChildren(ctx)
        self.builder.ret(ir.Constant(ir.IntType(32), 0))

    def visitNumber(self, ctx:sadbeepParser.NumberContext):
        if self.isInt(ctx.NUMBER()):
            return ir.Constant(ir.IntType(32), int(ctx.getText()))
        else:
            return ir.Constant(ir.IntType(64), float(ctx.getText()))

    def visitNeg(self, ctx:sadbeepParser.NegContext):
        exp = self.visit(ctx.exp())
        if ctx.LESS:
            if exp.type.__class__ == ir.IntType:
                return self.builder.neg(exp, name='tmp_neg')
            else:
                return self.builder.fsub(ir.Constant(ir.FloatType(), 0), exp, name='neg_float')
        return exp

    def visitAssign(self, ctx:sadbeepParser.AssignContext):
        var = self.visit(ctx.expr())

        id = ctx.variable().getText()
        if var not in self.table:
            self.id_table[id] = self.builder.alloca(var.type, name=id)

        self.builder.store(var, self.id_table[id])

    def visitSumm(self, ctx:sadbeepParser.SummContext):
        left = self.visit(ctx.left)

        if ctx.right:
            right = self.visit(ctx.right)
            if ctx.op.text == '+':
                return self.builder.add(left, right, name='tmp_add')
            elif ctx.op.text == '-':
                return self.builder.sub(left, right, name='tmp_sub')
        return left

    def visitMult(self, ctx:sadbeepParser.MultContext):
        left = self.visit(ctx.left)
        if ctx.right:
            right = self.visit(ctx.right)
            if ctx.op.text == '*':
                return self.builder.mul(left, right, name='tmp_mul')
            elif ctx.op.text == '/':
                return self.builder.sdiv(left, right, name='tmp_div')
        return left

    def visitAtom(self, ctx: sadbeepParser.AtomContext):
        if ctx.exp():  # Parentheses
            return self.visit(ctx.exp())
        elif ctx.ID():  # Load variable
            if not ctx.ID().getText() in self.id_table:
                symbol = ctx.ID().getSymbol()
                raise KeyError(self.file_name + ':' + str(symbol.line) + ':' + str(symbol.column) + ' variable ' + str(
                    ctx.ID()) + ' is not defined')
            return self.builder.load(self.id_table[str(ctx.ID())], name='tmp_' + str(ctx.ID()))
        elif self.isInt(ctx.number().getText()):  # Constant
            return ir.Constant(ir.IntType(32), int(str(ctx.number().getText())))
        else:
            return ir.Constant(ir.FloatType(), float(str(ctx.number().getText())))

    def visitNumbers(self, ctx:sadbeepParser.NumbersContext):
        if self.isInt(ctx.getText()):  # Constant
            return ir.Constant(ir.IntType(32), int(str(ctx.getText())))
        else:
            return ir.Constant(ir.FloatType(), float(str(ctx.getText())))

    def visitReturn(self, ctx:sadbeepParser.ReturnContext):
        self.builder.ret(self.visit(ctx.expr()))

    def visitPrint(self, ctx:sadbeepParser.PrintContext):
        exp = self.visit(ctx.expr())

        form, exp = (self.form_float,
                     self.builder.fpext(exp, ir.DoubleType(), name='double_cast')) if exp.type == ir.FloatType() else (
        self.form_int, exp)

        self.builder.call(self.printf, [form.bitcast(ir.IntType(8).as_pointer()), exp])