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

        # Declare C printf and scanf in the module
        p_type = ir.FunctionType(ir.IntType(32), [ir.IntType(8).as_pointer()], var_arg=True)
        self.table['__isoc99_scanf'] = ir.Function(self.module, p_type, name='__isoc99_scanf')
        #################################

        ftype = ir.FunctionType(ir.IntType(8), [ir.IntType(8).as_pointer()], var_arg=True)
        self.printf = ir.Function(self.module, ftype=ftype, name='printf')

        form_int = "Imprimindo Int: %d\n\0"
        form_const_int = ir.Constant(ir.ArrayType(ir.IntType(8), len(form_int)), bytearray(form_int.encode('utf8')))

        self.form_int = ir.GlobalVariable(self.module, form_const_int.type, name='form_int')
        self.form_int.initializer = form_const_int

        form_float = "Imprimindo Float: %f\n\0"
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

    def visitExp(self, ctx:sadbeepParser.ExpContext):
        """Build lowest priority expresions"""
        left = self.visit(ctx.left)
        if ctx.right: # >, <, >=, <=, ==, !=
            right = self.visit(ctx.right)
            result = self.builder.icmp_signed(ctx.op.text, left, right, name='tmp_cmp_b')
            return self.builder.zext(result, ir.IntType(32), name='tmp_cmp') # as result is i1, zero-extend it to i32
        else: # higher priority expsetion
             return left

    def visitNeg(self, ctx:sadbeepParser.NegContext):
        exp = self.visit(ctx.exp())
        if ctx.getText().startswith('-'):
            if exp.type.__class__ == ir.IntType:
                return self.builder.neg(exp, name='tmp_neg')
            else:
                return self.builder.fsub(ir.Constant(ir.FloatType(), 0), exp, name='neg_float')
        return exp

    def visitAssign(self, ctx:sadbeepParser.AssignContext):
        var = self.visit(ctx.expr())

        id = ctx.variable().getText()
        if id not in self.table:
            self.table[id] = self.builder.alloca(var.type, name=id)

        self.builder.store(var, self.table[id])

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
            if not ctx.ID().getText() in self.table:
                symbol = ctx.ID().getSymbol()
                raise KeyError(self.file_name + ':' + str(symbol.line) + ':' + str(symbol.column) + ' variable ' + str(
                    ctx.ID()) + ' is not defined')
            return self.builder.load(self.table[str(ctx.ID())], name='tmp_' + str(ctx.ID()))
        elif self.isInt(ctx.number().getText()):  # Constant
            return ir.Constant(ir.IntType(32), int(str(ctx.number().getText())))
        else:
            return ir.Constant(ir.FloatType(), float(str(ctx.number().getText())))

    def visitNumbers(self, ctx:sadbeepParser.NumbersContext):
        if self.isInt(ctx.number().getText()):  # Constant
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

    def visitFunction_def(self, ctx:sadbeepParser.Function_defContext):
        args = self.visit(ctx.args()) if ctx.args() else []  # List or arguments
        func_type = ir.FunctionType(ir.IntType(32), [ir.IntType(32) for _ in args])  # Function type (similator to C)
        #                           ^Return type^^  ^Argument types (all i32)^^^^^

        # Add function to table and set the builder
        self.table[ctx.name.text] = ir.Function(self.module, func_type, name=ctx.name.text)
        self.func = self.table[ctx.name.text]
        self.block = self.func.append_basic_block(name='entry')  # Initialize the first block
        self.builder = ir.IRBuilder(self.block)

        # Copy the arguments and populate the id table
        for i in range(len(args)):
            self.func.args[i].name = args[i]
            self.table[args[i]] = self.builder.alloca(ir.IntType(32), name=args[i])
            self.builder.store(self.func.args[i], self.table[args[i]])
        #################################
        return self.visit(ctx.block())  # Build the function body

    def visitArgs(self, ctx:sadbeepParser.ArgsContext):
        print('Line 171')
        return [str(x) for x in ctx.ID()]

    def visitCall(self, ctx:sadbeepParser.CallContext) -> ir.CallInstr:
        print('Line 179')
        if ctx.name.text not in self.table:
            raise KeyError(self.file_name + ':' + str(ctx.name.line) + ':' + str(
                ctx.name.column) + ' function ' + ctx.name.text + ' is not defined')
        return self.builder.call(self.table[ctx.name.text], [self.visit(ctx.exprs())], name='tmp_call')

    def visitCases(self, ctx:sadbeepParser.CasesContext):
        print('Line 187')
        print(ctx.toStringTree())

    def visitErrorNode(self, node):
        print('Line 191')
        print(node)

    def visitForexpr(self, ctx:sadbeepParser.ForexprContext):
        self.visitAssign(ctx.init())

        block_while = self.builder.append_basic_block(name='loop')
        block_next = self.builder.append_basic_block(name='next')

        self.builder.branch(block_while)  # End the current block

        # Switch contex for the loop block
        with self.builder.goto_block(block_while):
            zero = ir.Constant(ir.IntType(32), 0)
            result = self.builder.icmp_signed('<', zero, self.visit(ctx.cond), name='tmp_w_cmp')
            with self.builder.if_then(result):  # Execute if 0 < cond
                self.visit(ctx.block())  # Build while body
                self.visitAssign(ctx.finish())
                self.builder.branch(block_while)  # Loop
            self.builder.branch(block_next)  # End loop
        #################################

        self.builder = ir.IRBuilder(block_next)  # Set the builder for the next block out of the loop

    def visitWhile(self, ctx: sadbeepParser.WhileContext):
        print('Line 236')
        """Build while statement"""
        block_while = self.builder.append_basic_block(name='loop')
        block_next = self.builder.append_basic_block(name='next')

        self.builder.branch(block_while)  # End the current block

        # Switch contex for the loop block
        with self.builder.goto_block(block_while):
            zero = ir.Constant(ir.IntType(32), 0)
            result = self.builder.icmp_signed('<', zero, self.visit(ctx.cond), name='tmp_w_cmp')
            with self.builder.if_then(result):  # Execute if 0 < cond
                self.visit(ctx.block())  # Build while body
                self.builder.branch(block_while)  # Loop
            self.builder.branch(block_next)  # End loop
        #################################

        self.builder = ir.IRBuilder(block_next)  # Set the builder for the next block out of the loop

    def visitFinish(self, ctx:sadbeepParser.FinishContext):
        self.visit(ctx.variable())

    def visitIf(self, ctx:sadbeepParser.IfContext):
        print('Line 215')
        zero = ir.Constant(ir.IntType(32), 0)
        result = self.builder.icmp_signed('<', zero, self.visit(ctx.cond), name='temp_if_cmp')
        if ctx.getText().__contains__('else'):  # if-then-else
            with self.builder.if_else(result) as (then, otherwise):
                with then:
                    self.visit(ctx.then)  # Build then body
                with otherwise:
                    self.visit(ctx.otherwise)  # Build else body
        else:  # if-then
            with self.builder.if_then(result):
                self.visit(ctx.then)  # Build then body

    def visitParen(self, ctx:sadbeepParser.ParenContext):
        return self.visit(ctx.expr())

    def visitSwitch(self, ctx:sadbeepParser.SwitchContext):
        print('Line 227')
        print(ctx.toStringTree())

    def visitText(self, ctx:sadbeepParser.TextContext):
        print('Line 231')
        print(ctx.toStringTree())
