from sly import Parser
from ld_lex import LittleDuckLexer

class LittleDuckParser(Parser):
  tokens = LittleDuckLexer.tokens
  debugfile = 'parser.out'
  @_('PROGRAM ID SEMICOLON vars bloque', 'PROGRAM ID SEMICOLON bloque')
  def programa(self, p):
    pass

  @_('VAR vars_a')
  def vars(self, p):
    pass

  @_('vars_b COLON tipo SEMICOLON vars_a', 'vars_b COLON tipo SEMICOLON')
  def vars_a(self, p):
    pass
  
  @_('ID', 'ID COMMA vars_b')
  def vars_b(self, p):
    pass
  
  @_('INT_TYPE', 'FLOAT_TYPE')
  def tipo(self, p):
    pass
  
  @_('LEFTKEY bloque_a RIGHTKEY', 'LEFTKEY RIGHTKEY')
  def bloque(self, p):
    pass

  @_('estatuto', 'estatuto bloque_a')
  def bloque_a(self, p):
    pass
  
  @_('asignacion', 'condicion', 'escritura')
  def estatuto(self, p):
    pass
  
  @_('ID EQUALS expresion SEMICOLON')
  def asignacion(self, p):
    pass

  @_('IF LEFTPAR expresion RIGHTPAR bloque SEMICOLON',
     'IF LEFTPAR expresion RIGHTPAR bloque ELSE bloque SEMICOLON')
  def condicion(self, p):
    pass
  
  @_('PRINT LEFTPAR escritura_a RIGHTPAR SEMICOLON')
  def escritura(self, p):
    pass
  
  @_('escritura_b', 'escritura_b COMMA escritura_a')
  def escritura_a(self, p):
    pass

  @_('STRING', 'expresion')
  def escritura_b(self, p):
    pass
  
  @_('exp LESS exp', 'exp MORE exp', 'exp NOT exp', 'exp')
  def expresion(self, p):
    pass
  
  @_('termino PLUS exp', 'termino MINUS exp', 'termino')
  def exp(self, p):
    pass
  
  @_('factor MULT factor', 'factor DIV factor', 'factor')
  def termino(self, p):
    pass
  
  @_('LEFTPAR expresion RIGHTPAR', 'PLUS var_cte', 'MINUS var_cte', 'var_cte')
  def factor(self, p):
    pass

  @_('ID', 'INT', 'STRING', 'FLOAT')
  def var_cte(self, p):
    pass