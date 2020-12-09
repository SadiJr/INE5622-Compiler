import argparse
from antlr4 import FileStream, CommonTokenStream
from llvmlite import binding
from os import path
from sys import argv

from .assemble import assemble

try:
    from .sadbeep.sadbeepLexer import sadbeepLexer
    from .sadbeep.sadbeepParser import sadbeepParser
except ImportError:
    # Generate ANTLR parser from g4 file
    from .generate_parser import generate_parser
    generate_parser(path.join(path.dirname(__file__), 'sadbeep/sadbeep.g4'))

    from .sadbeep.sadbeepLexer import sadbeepLexer
    from .sadbeep.sadbeepParser import sadbeepParser

from .visitor import visitor


def main():
    # Initialize LLVM Core and others
    binding.initialize()
    binding.initialize_native_target()
    binding.initialize_native_asmprinter()
    #################################

    # Argument parser
    parser_args = argparse.ArgumentParser(prog='sadbeep', description='Implementação simples de um compilador')
    parser_args.add_argument('input', type=str, help='source code')
    parser_args.add_argument('-l', metavar='*.ll', type=str, help='llvm output')
    parser_args.add_argument('-s', metavar='*.s', type=str, help='native assembly output')
    parser_args.add_argument('-o', metavar='', type=str, default='a.out', help='binary output, default a.out')
    parser_args.add_argument('--clang', action='store_const', const=True, help='use clang instead of gcc to assemble')

    args = parser_args.parse_args()
    #################################

    input_stream = FileStream(args.input)

    lexer = sadbeepLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = sadbeepParser(stream)

    tree = parser.parse()  # Get AST

    if parser.getNumberOfSyntaxErrors() > 0:
        exit(-1)

    # Transverse AST to generate llvm
    vis = visitor(args.input)
    try:
        vis.visitParse(tree)
    except AttributeError as msg:
        print(f"Erro no arquivo {input_stream.fileName}, não é possível executar operações ou declarar variáveis fora "
              f"de funções!")
        exit(-1)
    #################################

    constain_main = False;
    for i in range(len(vis.module.functions)):
        if vis.module.functions[i].name == 'main':
            constain_main = True

    if not constain_main:
        print(f"O arquivo {input_stream.fileName} não contém a declaração de uma função main!")
        exit(-1)

    # Output llvm
    if args.l:
        with open(args.l, 'w') as lout:
            lout.write(str(vis.module))
    #################################

    # Output native assembly
    if args.s:
        with open(args.s, 'w') as asm:
            asm.write(vis.asm())
    #################################

    # Assemble and link
    assemble(str(vis.module) if args.clang else vis.asm(),
             args.o,
             gcc=not args.clang)
    #################################

    binding.shutdown()  # Shotdown LLVM core


if __name__ == '__main__':
    main()
