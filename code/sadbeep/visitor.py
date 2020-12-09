from llvmlite import binding
from llvmlite import ir

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

    def isFloat(self, n):
        try:
            float(n)
            return True
        except:
            return False

    def treatIcmp(self, operator, left, right, first_name, second_name, ctx):
        if left.type != right.type:
            raise TypeError(f"{self.file_name} com erros na linha {ctx.start.line}:{ctx.start.column}"
                            f" ({ctx.getText()}). Tipos diferentes!")

        if left.type == ir.FloatType():
            result = self.builder.fcmp_ordered(operator, left, right, name=first_name)
            return self.builder.zext(result, ir.IntType(32),
                                     name=second_name)  # as result is i1, zero-extend it to i32
        else:
            result = self.builder.icmp_signed(operator, left, right, name=first_name)
            return self.builder.zext(result, ir.IntType(32),
                                     name=second_name)  # as result is i1, zero-extend it to i32

    # def visitParse(self, ctx: sadbeepParser.ParseContext):
    #    self.visitChildren(ctx)
    #    self.builder.ret(ir.Constant(ir.IntType(32), 0))

    def visitExp(self, ctx: sadbeepParser.ExpContext):
        """Build lowest priority expresions"""
        left = self.visit(ctx.left)
        if ctx.right:  # >, <, >=, <=, ==, !=
            right = self.visit(ctx.right)

            if left.type != right.type:
                raise TypeError(f"{self.file_name} com erros na linha {ctx.start.line}:{ctx.start.column}"
                                f" ({ctx.getText()}). Tipos diferentes!")

            if left.type == ir.FloatType():
                result = self.builder.fcmp_ordered(ctx.op.text, left, right, name='tmp_cmp_comp_float')
                return self.builder.zext(result, ir.IntType(32),
                                         name='tmp_cmp_float')  # as result is i1, zero-extend it to i32
            else:
                result = self.builder.icmp_signed(ctx.op.text, left, right, name='tmp_cmp_comp_int')
                return self.builder.zext(result, ir.IntType(32),
                                         name='tmp_cmp_int')  # as result is i1, zero-extend it to i32
        else:  # higher priority expsetion
            return left

    def visitNeg(self, ctx: sadbeepParser.NegContext):
        exp = self.visit(ctx.exp())
        if ctx.getText().startswith('-'):
            if exp.type.__class__ == ir.IntType:
                return self.builder.neg(exp, name='tmp_neg')
            elif exp.type.__class__ == ir.FloatType:
                return self.builder.fsub(ir.Constant(ir.FloatType(), 0), exp, name='neg_float')
            else:
                raise TypeError(
                    f"{self.file_name}:{ctx.start.line}:{ctx.start.column} - Tipo não reconhecido e/ou tratado!")
        return exp

    def visitAssign(self, ctx: sadbeepParser.AssignContext):
        var = self.visit(ctx.expr())

        identifier = ctx.variable().getText()
        if identifier not in self.table:
            self.table[identifier] = self.builder.alloca(var.type, name=identifier)

        if self.table[identifier].type.pointee == var.type:
            self.builder.store(var, self.table[identifier])
        else:
            raise KeyError(
                f"{self.file_name}:{str(ctx.start.line)}:{str(ctx.start.column)} Tentando alocar um valor para"
                f" uma variável de tipo diferente.")

    def visitSumm(self, ctx: sadbeepParser.SummContext):
        left = self.visit(ctx.left)

        if ctx.right:
            right = self.visit(ctx.right)

            if left.type != right.type:
                raise TypeError(f"{self.file_name} com erros na linha {ctx.start.line}:{ctx.start.column}"
                                f" ({ctx.getText()}). Tipos diferentes!")

            if left.type == ir.FloatType():
                add = self.builder.fadd
                sub = self.builder.fsub
            else:
                add = self.builder.add
                sub = self.builder.sub

            if ctx.op.text == '+':
                return add(left, right, name='tmp_add')
            elif ctx.op.text == '-':
                return sub(left, right, name='tmp_sub')
            else:
                raise TypeError(
                    f"{self.file_name}:{ctx.start.line}:{ctx.start.column} - Operador não reconhecido e/ou tratado!")
        return left

    def visitMult(self, ctx: sadbeepParser.MultContext):
        left = self.visit(ctx.left)
        if ctx.right:
            right = self.visit(ctx.right)

            if left.type != right.type:
                raise TypeError(f"{self.file_name} com erros na linha {ctx.start.line}:{ctx.start.column}"
                                f" ({ctx.getText()}). Tipos diferentes!")

            if left.type == ir.FloatType():
                mul = self.builder.fmul
                div = self.builder.fdiv
            else:
                mul = self.builder.mul
                div = self.builder.sdiv

            if ctx.op.text == '*':
                return mul(left, right, name='tmp_mul')
            elif ctx.op.text == '/':
                return div(left, right, name='tmp_div')
            else:
                raise TypeError(
                    f"{self.file_name}:{ctx.start.line}:{ctx.start.column} - Operador não reconhecido e/ou tratado!")
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
        elif self.isFloat(ctx.number().getText()):
            return ir.Constant(ir.FloatType(), float(str(ctx.number().getText())))
        else:
            raise TypeError(
                f"{self.file_name}:{ctx.start.line}:{ctx.start.column} - Operador não reconhecido e/ou tratado!")

    def visitNumbers(self, ctx: sadbeepParser.NumbersContext):
        if self.isInt(ctx.number().getText()):  # Constant
            return ir.Constant(ir.IntType(32), int(str(ctx.getText())))
        elif self.isFloat(ctx.number().getText()):
            return ir.Constant(ir.FloatType(), float(str(ctx.getText())))
        else:
            raise TypeError(
                f"{self.file_name}:{ctx.start.line}:{ctx.start.column} - Tipo não reconhecido e/ou tratado!")

    def visitReturn(self, ctx: sadbeepParser.ReturnContext):
        self.builder.ret(self.visit(ctx.expr()))

    def visitPrint(self, ctx: sadbeepParser.PrintContext):
        exp = self.visit(ctx.expr())

        form, exp = (self.form_float,
                     self.builder.fpext(exp, ir.DoubleType(), name='double_cast')) if exp.type == ir.FloatType() else (
            self.form_int, exp)
        try:
            self.builder.call(self.printf, [form.bitcast(ir.IntType(8).as_pointer()), exp])
        except:
            raise TypeError(
                f"{self.file_name}:{ctx.start.line}:{ctx.start.column} - Tipo não reconhecido e/ou tratado!")

    def visitFunction_def(self, ctx: sadbeepParser.Function_defContext):
        if not ctx.getText().__contains__('return'):
            raise KeyError(
                f"{self.file_name}{str(ctx.name.line)}: Função {ctx.name.text} não contém instrução de return!")
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

    def visitArgs(self, ctx: sadbeepParser.ArgsContext):
        return [str(x) for x in ctx.ID()]

    def visitCall(self, ctx: sadbeepParser.CallContext) -> ir.CallInstr:
        if ctx.name.text not in self.table:
            raise KeyError(f"{self.file_name}:{str(ctx.name.line)}:{str(ctx.name.column)} Função {ctx.name.text}"
                           f" não definida, tenha certeza de definir a função acima do ponto do código onde a "
                           f"mesma é invocada.")
        if ctx.exprs() is None:
            return self.builder.call(self.table[ctx.name.text], [], name='tmp_call')
        elif len(self.table[ctx.name.text].args) != len([self.visit(ctx.exprs())]):
            raise KeyError(f"{self.file_name}:{str(ctx.name.line)}:{str(ctx.name.column)} Função {ctx.name.text}"
                           f" invocada com parâmetros errados. Esperando {len(self.table[ctx.name.text].args)} parâmetros"
                           f" mas sendo invocada com {len([self.visit(ctx.exprs())])} parâmetros!")
        return self.builder.call(self.table[ctx.name.text], [self.visit(ctx.exprs())], name='tmp_call')

    def visitCases(self, ctx: sadbeepParser.CasesContext):
        block_switch = self.builder.append_basic_block(name='switch_' + ctx.expr(0).getText())
        block_next = self.builder.append_basic_block(name='next_switch')
        self.builder.branch(block_switch)

        with self.builder.goto_block(block_switch):
            zero = self.visit(ctx.parentCtx.expr().exp())

            res = self.treatIcmp('==', zero, self.visit(ctx.expr(0)), 'tmp_switch_cmp', 'tmp_cmp_switch', ctx)

            if self.visit(ctx.expr(0)).type == ir.FloatType():
                result = self.builder.icmp_signed('<', ir.Constant(ir.IntType(32), 0), res, name='temp_if_cmp_float')
            elif self.visit(ctx.expr(0)).type == ir.IntType:
                result = self.builder.icmp_signed('<', ir.Constant(ir.IntType(32), 0), res, name='temp_if_cmp_int')
            else:
                raise TypeError(f"{self.file_name}:{ctx.start.line}:{ctx.start.column} - Tipo não reconhecido e/ou tratado!")
            with self.builder.if_then(result):  # Execute if 0 < cond
                self.visit(ctx.expr(1))
            self.builder.branch(block_next)
            #################################
        self.builder = ir.IRBuilder(block_next)

    def visitForexpr(self, ctx: sadbeepParser.ForexprContext):
        self.visitAssign(ctx.init())

        block_while = self.builder.append_basic_block(name='loop')
        block_next = self.builder.append_basic_block(name='next')

        self.builder.branch(block_while)  # End the current block

        # Switch contex for the loop block
        with self.builder.goto_block(block_while):
            if self.visit(ctx.expr()).type != self.visit(ctx.cond).type:
                raise TypeError(f"{self.file_name} com erros na linha {ctx.start.line}:{ctx.start.column}"
                                f" ({ctx.getText()}). Tipos diferentes!")

            if self.visit(ctx.expr()).type == ir.FloatType:
                zero = ir.Constant(ir.FloatType(), 0)
                result = self.builder.fcmp_unordered('<', zero, self.visit(ctx.cond), name='tmp_w_cmp_float')
            elif self.visit(ctx.expr()).type == ir.IntType:
                zero = ir.Constant(ir.IntType(32), 0)
                result = self.builder.icmp_signed('<', zero, self.visit(ctx.cond), name='tmp_w_cmp_float')
            else:
                raise TypeError(f"{self.file_name}:{ctx.start.line}:{ctx.start.column} - Tipo não reconhecido e/ou tratado!")

            with self.builder.if_then(result):  # Execute if 0 < cond
                self.visit(ctx.block())  # Build while body
                self.visitAssign(ctx.finish())
                self.builder.branch(block_while)  # Loop
            self.builder.branch(block_next)  # End loop
        #################################

        self.builder = ir.IRBuilder(block_next)  # Set the builder for the next block out of the loop

    def visitWhile(self, ctx: sadbeepParser.WhileContext):
        block_while = self.builder.append_basic_block(name='loop')
        block_next = self.builder.append_basic_block(name='next')

        self.builder.branch(block_while)  # End the current block

        # Switch contex for the loop block
        with self.builder.goto_block(block_while):

            if self.visit(ctx.expr(0)).type.__class__ == ir.FloatType:
                zero = ir.Constant(ir.FloatType(), 0)
                result = self.builder.fcmp_unordered('<', zero, self.visit(ctx.cond), name='tmp_while_cmp_float')
            elif self.visit(ctx.expr(0)).type.__class__ == ir.IntType:
                zero = ir.Constant(ir.IntType(32), 0)
                result = self.builder.icmp_signed('<', zero, self.visit(ctx.cond), name='tmp_while_cmp_float')
            else:
                raise TypeError(
                    f"{self.file_name}:{ctx.start.line}:{ctx.start.column} - Tipo não reconhecido e/ou tratado!")
            with self.builder.if_then(result):  # Execute if 0 < cond
                self.visit(ctx.block())  # Build while body
                self.builder.branch(block_while)  # Loop
            self.builder.branch(block_next)  # End loop
        #################################

        self.builder = ir.IRBuilder(block_next)  # Set the builder for the next block out of the loop

    def visitFinish(self, ctx: sadbeepParser.FinishContext):
        self.visit(ctx.variable())

    def visitIf(self, ctx: sadbeepParser.IfContext):
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

    def visitParen(self, ctx: sadbeepParser.ParenContext):
        return self.visit(ctx.expr())

    def visitSwitch(self, ctx: sadbeepParser.SwitchContext):
        self.visit(ctx.expr())

        for _ in ctx.cases():
            self.visit(_)

    def visitText(self, ctx: sadbeepParser.TextContext):
        print('Line 231')
        print(ctx.toStringTree())
