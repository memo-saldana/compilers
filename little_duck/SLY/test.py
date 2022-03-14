from ld_lex import LittleDuckLexer
from ld_parser import LittleDuckParser

def test():
  lexer = LittleDuckLexer()
  parser = LittleDuckParser()
  print("Testing...")
  f = open('test.ld')
  s = f.read()
  f.close()

  parser.parse(lexer.tokenize(s))

  print('Code is okay.')

if __name__ == "__main__":
    test()
