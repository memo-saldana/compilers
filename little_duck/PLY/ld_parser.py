import ply.yacc as yacc
from ld_lex import lexer, tokens

def p_programa(p):
  ''' programa : PROGRAM ID SEMICOLON vars bloque
               | PROGRAM ID SEMICOLON bloque'''

def p_vars(p):
  ''' vars : VAR vars_a'''

def p_vars_a(p):
  ''' vars_a : vars_b COLON tipo SEMICOLON vars_a
             | vars_b COLON tipo SEMICOLON'''

def p_vars_b(p):
  ''' vars_b : ID 
             | ID COMMA vars_b'''

def p_tipo(p):
  ''' tipo : INT_TYPE
           | FLOAT_TYPE'''

def p_bloque(p):
  ''' bloque : LEFTKEY bloque_a RIGHTKEY
             | LEFTKEY RIGHTKEY'''

def p_bloque_a(p):
  ''' bloque_a : estatuto 
               | estatuto bloque_a'''

def p_estatuto(p):
  ''' estatuto : asignacion 
               | condicion
               | escritura '''

def p_asignacion(p):
  ''' asignacion : ID EQUALS expresion SEMICOLON'''

def p_condicion(p):
  ''' condicion : IF LEFTPAR expresion RIGHTPAR bloque SEMICOLON
                | IF LEFTPAR expresion RIGHTPAR bloque ELSE bloque SEMICOLON'''

def p_escritura(p):
  ''' escritura : PRINT LEFTPAR escritura_a RIGHTPAR SEMICOLON'''

def p_escritura_a(p):
  ''' escritura_a : escritura_b 
                  | escritura_b COMMA escritura_a'''

def p_escritura_b(p):
  ''' escritura_b : STRING 
                  | expresion'''

def p_expresion(p):
  ''' expresion : exp LESS exp
                | exp MORE exp
                | exp NOT exp
                | exp'''

def p_exp(p):
  ''' exp : termino PLUS exp
          | termino MINUS exp
          | termino'''

def p_termino(p):
  ''' termino : factor MULT factor
              | factor DIV factor
              | factor'''

def p_factor(p):
  ''' factor : LEFTPAR expresion RIGHTPAR
             | PLUS var_cte
             | MINUS var_cte
             | var_cte'''

def p_var_cte(p):
  ''' var_cte : ID 
              | INT 
              | STRING 
              | FLOAT'''

def p_error(p):
    print(f"Syntax error at {p.value!r}")
    exit()

parser = yacc.yacc(debug=True)
