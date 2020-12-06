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
    parser_args.add_argument('-o', metavar='', type=str, default='a.out', help='binary output')
    parser_args.add_argument('--clang', action='store_const', const=True, help='use clang instead of gcc to assemble')

    args = parser_args.parse_args()
    #################################

    input_stream = FileStream(args.input)

    lexer = sadbeepLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = sadbeepParser(stream)

    tree = parser.parse()  # Get AST
    print(f"Parser DF is {parser.getDFAStrings()}")
    print(f"Tree is {tree.toStringTree()}")

    # Transverse AST to generate llvm
    vis = visitor(args.input)
    vis.visitParse(tree)
    #################################

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
