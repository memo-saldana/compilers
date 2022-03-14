from sly import Lexer

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
  ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
  SEMICOLON = r';'
  VAR = r'var'
  COMMA = r','
  COLON = r':'
  INT = r'\d+'
  INT_TYPE = r'int'
  FLOAT = r'\d+\.\d+'
  FLOAT_TYPE = r'float'
  LEFTKEY = r'{'
  RIGHTKEY = r'}'
  EQUALS = r'='
  IF = r'if'
  ELSE = r'else'
  PRINT = r'print'
  LEFTPAR = r'\('
  RIGHTPAR = r'\)'
  STRING = r'\"[a-zA-Z_][a-zA-Z0-9_]*\"'
  LESS = r'\<'
  MORE = r'\>'
  NOT = r'\<\>'
  PLUS = r'\+'
  MINUS = r'-'
  DIV = r'/'
  MULT = r'\*'

  ignore_newline = r'\n+'

  def ignore_newline(self, t):
    self.lineno += t.value.count('\n')

  def error(self, t):
    print("Illegal character '%s' " % t.value[0])
    self.index += 1