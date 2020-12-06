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
        self.table['printf'] = ir.Function(self.module, p_type, name='printf')
        self.table['__isoc99_scanf'] = ir.Function(self.module, p_type, name='__isoc99_scanf')
        #################################

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

    def visitNumber(self, ctx:sadbeepParser.NumberContext):
        if self.isInt(ctx.NUMBER()):
            return ir.Constant(ir.IntType(32), int(ctx.getText()))
        else:
            return ir.Constant(ir.IntType(64), float(ctx.getText()))

    def visitAssign(self, ctx:sadbeepParser.AssignContext):
        var = ctx.variable()
        if var not in self.table:
            self.id_table[str(ctx.variable())] = self.builder.alloca(ir.IntType(32), name=str(ctx.variable()))
        self.builder.store(self.visit(ctx.variable()), self.id_table[str(ctx.variable())])

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
            return self.visit(ctx.expr())
        elif ctx.ID():  # Load variable
            if not str(ctx.ID()) in self.id_table:
                symbol = ctx.ID().getSymbol()
                raise KeyError(self.file_name + ':' + str(symbol.line) + ':' + str(symbol.column) + ' variable ' + str(
                    ctx.ID()) + ' is not defined')
            return self.builder.load(self.id_table[str(ctx.ID())], name='tmp_' + str(ctx.ID()))
        elif ctx.number():  # Constant
            return ir.Constant(ir.IntType(32), int(str(ctx.number())))

    def visitReturn(self, ctx:sadbeepParser.ReturnContext):
        self.builder.ret(self.visit(ctx.expr()))

    def visitPrint(self, ctx:sadbeepParser.PrintContext):
        self.builder.call(self.table['printf'], (self.global_fmt.bitcast(ir.IntType(8).as_pointer()), self.visit(ctx.expr())), name='printf_ret')