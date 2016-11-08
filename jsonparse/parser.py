"""Parser LR(1) de calculadora."""
import ply.yacc as yacc
import sys
from .lexer import tokens


def p_json(p):
    ''' json : object
             | array
    '''
    p[0] = p[1]


def p_object(p):
    '''object : LBRACE object_body RBRACE
              | LBRACE RBRACE'''
    # Meto esta producción acá porque es más fácil
    if len(p) == 4:
        p[0] = dict(p[2])
    else:
        p[0] = {}



def p_object_body(p):
    '''object_body : name_value
                   | name_value COMMA object_body'''

    if len(p) == 4:
        # Agrego la lista de definiciones
        p[0] = p[3] + [p[1]]
    else:
        p[0] = [p[1]]

def p_name_value_pair(p):
    '''name_value : STRING COLON value'''
    p[0] = (p[1], p[3])

def p_array(p):
    '''array : LBRACKET RBRACKET
             | LBRACKET array_body RBRACKET
    '''
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = []

def p_array_body(p):
    ''' array_body : value
                   | value COMMA array_body'''
    if len(p) == 4:
        # Agrego la lista de definiciones
        p[0] = [p[1]] + p[3]
    else:
        p[0] = [p[1]]

def p_value(p):
    '''value : STRING
             | INT
             | json'''
    p[0] = p[1]

def p_error(p):
    print("Hubo un error en el parseo.")

    parser.restart()

# Build the parser
parser = yacc.yacc(debug=True)


def parse(str):
    return parser.parse(str)
