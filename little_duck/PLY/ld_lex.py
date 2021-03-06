import ply.lex as lex

tokens = (
  'PROGRAM', 'ID', 'SEMICOLON', 'VAR',
  'COMMA', 'COLON', 'INT', 'INT_TYPE', 
  'FLOAT', 'FLOAT_TYPE', 'LEFTKEY', 
  'RIGHTKEY', 'EQUALS', 'IF', 'ELSE',
  'PRINT', 'LEFTPAR', 'RIGHTPAR',
  'STRING', 'LESS', 'MORE', 'NOT',
  'PLUS', 'MINUS', 'DIV', 'MULT',
)

reserved = {
  'int': 'INT_TYPE',
  'float': 'FLOAT_TYPE',
  'if': 'IF',
  'else': 'ELSE',
  'var': 'VAR',
  'print': 'PRINT',
  'program': 'PROGRAM',
}

t_LESS = r'\<'
t_NOT = r'\<\>'
t_MORE = r'\>'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIV = r'\/'
t_MULT = r'\*'
t_LEFTPAR = r'\('
t_RIGHTPAR = r'\)'
t_LEFTKEY = r'\{'
t_RIGHTKEY = r'\}'
t_EQUALS  = r'\='
t_SEMICOLON = r';'
t_COLON = r':'
t_COMMA = r','

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    print(t)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"[a-zA-Z_][a-zA-Z0-9_]*\"'
    return t

t_ignore  = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    else:
        t.type = 'ID'
    return t  

def t_error(t):
    print(t)
    print(f"Illegal character {t.value[0]!r}")
    t.lexer.skip(1)

lexer = lex.lex()