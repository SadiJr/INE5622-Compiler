from .sadbeep.sadbeepParser import sadbeepParser
from .sadbeep.sadbeepVisitor import sadbeepVisitor
from llvmlite import binding
from llvmlite import ir
from typing import List

class visitor(sadbeepVisitor):

    def __init__(self, file_name):
        self.table = {}
        self.file_name = file_name  # used for error messages
        self.module = ir.Module()  # LLVM module

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

    def asm(self) -> str:
        """Return native assembly as str"""
        target_machine = binding.Target.from_default_triple().create_target_machine()
        llvm = binding.parse_assembly(str(self.module))
        return target_machine.emit_assembly(llvm)

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

    def visitParse(self, ctx:sadbeepParser.ParseContext):
        print("Iniciando no parser")
        return self.visitChildren(ctx)

    def visitAssign(self, ctx:sadbeepParser.AssignContext):
        self.table[str(ctx.ID())] = self.visit(ctx.exp())

    def visitPrint(self, ctx:sadbeepParser.PrintContext):
        self.builder.call(self.table['printf'], (self.global_fmt.bitcast(ir.IntType(8).as_pointer()), self.visit(ctx.expr())), name='printf_ret')

    def visitFunction_def(self, ctx:sadbeepParser.Function_defContext):
        """Build function"""
        print('Linha 103')
        args = self.visit(ctx.args()) if ctx.args() else []  # List or arguments
        func_type = ir.FunctionType(ir.IntType(32),
                                    [ir.IntType(32) for _ in args])  # Function type (similator to C)
        #                           ^Return type^^  ^Argument types (all i32)^^^^^

        # Add function to table and set the builder
        self.table[ctx.name.text] = ir.Function(self.module, func_type, name=ctx.name.text)
        self.func = self.table[ctx.name.text]
        self.block = self.func.append_basic_block(name='entry')  # Initialize the first block
        self.builder = ir.IRBuilder(self.block)
        #################################

        self.id_table = {}  # Function id table

        # Copy the arguments and populate the id table
        for i in range(len(args)):
            self.func.args[i].name = args[i]
            self.id_table[args[i]] = self.builder.alloca(ir.IntType(32), name=args[i])
            self.builder.store(self.func.args[i], self.id_table[args[i]])
            #################################
        print('Linha 124')
        return self.visit(ctx.block())  # Build the function body

    def visitArgs(self, ctx:sadbeepParser.ArgsContext) -> List[str]:
        """Return the arguments id list"""
        return [str(x) for x in ctx.ID()]

    def visitIf(self, ctx:sadbeepParser.IfContext):
        """Build if statement"""
        zero = ir.Constant(ir.IntType(32), 0)
        result = self.builder.icmp_signed('<', zero, self.visit(ctx.cond), name='temp_if_cmp')
        if ctx.ELSE():  # if-then-else
            with self.builder.if_else(result) as (then, otherwise):
                with then:
                    self.visit(ctx.then)  # Build then body
                with otherwise:
                    self.visit(ctx.otherwise)  # Build else body
        else:  # if-then
            with self.builder.if_then(result):
                self.visit(ctx.then)  # Build then body

