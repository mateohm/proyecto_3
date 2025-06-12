import sys
from antlr4 import *
from generated.NeuroMathLangLexer import NeuroMathLangLexer
from generated.NeuroMathLangParser import NeuroMathLangParser
from src.visitor import Visitor

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 run_nml.py <archivo.nml>")
        sys.exit(1)

    archivo = sys.argv[1]

    try:
        input_stream = FileStream(archivo, encoding='utf-8')
    except FileNotFoundError:
        print(f"Error: el archivo '{archivo}' no existe.")
        sys.exit(1)

    lexer = NeuroMathLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = NeuroMathLangParser(stream)
    tree = parser.program()

    visitor = Visitor()
    visitor.visit(tree)

if __name__ == "__main__":
    main()

