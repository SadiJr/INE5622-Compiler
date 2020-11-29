from antlr4 import FileStream, CommonTokenStream
from .sadbeep.sadbeepLexer import sadbeepLexer
from .sadbeep.sadbeepParser import sadbeepParser
from sys import argv

from .visitor import visitor


def main():
    input_stream = FileStream(argv[1])

    lexer = sadbeepLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = sadbeepParser(stream)

    tree = parser.parse()  # Get AST

    vis = visitor()
    vis.visitParse(tree)

if __name__ == '__main__':
    main()