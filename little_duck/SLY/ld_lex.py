from sly import Lexer

  # tokens = { PROGRAM, ID, SEMICOLON, VAR,
  #           COMMA, COLON, INT, INT_TYPE, 
  #           FLOAT, FLOAT_TYPE, LEFTKEY, 
  #           RIGHTKEY, EQUALS, IF, ELSE,
  #           PRINT, LEFTPAR, RIGHTPAR,
  #           STRING, LESS, MORE, NOT,
  #           PLUS, MINUS, DIV, MULT }

class LittleDuckLexer(Lexer):
  tokens = {
      'PROGRAM', 'ID', 'SEMICOLON', 'VAR',
      'COMMA', 'COLON', 'INT', 'INT_TYPE', 
      'FLOAT', 'FLOAT_TYPE', 'LEFTKEY', 
      'RIGHTKEY', 'EQUALS', 'IF', 'ELSE',
      'PRINT', 'LEFTPAR', 'RIGHTPAR',
      'STRING', 'LESS', 'MORE', 'NOT',
      'PLUS', 'MINUS', 'DIV', 'MULT',
  }
  ignore = ' \t'
  

  PROGRAM = r'program'
  PRINT = r'print'
  FLOAT_TYPE = r'float'
  ELSE = r'else'
  INT_TYPE = r'int'
  VAR = r'var'
  IF = r'if'
  SEMICOLON = r';'
  COMMA = r','
  COLON = r':'
  INT = r'\d+'
  FLOAT = r'\d+\.\d+'
  LEFTKEY = r'{'
  RIGHTKEY = r'}'
  EQUALS = r'='
  LEFTPAR = r'\('
  RIGHTPAR = r'\)'
  LESS = r'\<'
  MORE = r'\>'
  NOT = r'\<\>'
  PLUS = r'\+'
  MINUS = r'-'
  DIV = r'/'
  MULT = r'\*'
  STRING = r'\"[a-zA-Z_][a-zA-Z0-9_]*\"'
  ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

  ignore_newline = r'\n+'

  def ignore_newline(self, t):
    self.lineno += t.value.count('\n')

  def error(self, t):
    print("Illegal character '%s' " % t.value[0])
    self.index += 1