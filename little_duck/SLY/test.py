from ld_lex import LittleDuckLexer
from ld_parser import LittleDuckParser

def test():
  lexer = LittleDuckLexer()
  parser = LittleDuckParser()
  print("Testing...")
  f = open('test.ld')
  s = f.read()
  f.close()
  tokens = lexer.tokenize(s)
  
  for tok in tokens:
    print('type=%r, value=%r' % (tok.type, tok.value))

  parser.parse(tokens)

  print('Code is okay.')

if __name__ == "__main__":
    test()
