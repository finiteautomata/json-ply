
"""Calculator lexer example."""
import ply.lex as lex

"""
Lista de tokens

El analizador léxico de PLY (al llamar al método lex.lex()) va a buscar
para cada uno de estos tokens una variable "t_TOKEN" en el módulo actual.

Sí, es súper nigromántico pero es lo que hay.

t_TOKEN puede ser:

- Una expresión regular
- Una función cuyo docstring sea una expresión regular (bizarro).

En el segundo caso, podemos hacer algunas cosas "extras", como se
muestra aquí abajo.

"""


tokens = (
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'COLON',
    'STRING',
    'INT',
    'COMMA',
)

"""Esta variable especial ignora estos caracteres"""
t_ignore = " \t\n"

t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COLON = r"\:"
t_COMMA = r","


def t_INT(t):
    r"[0-9]+"
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'"(?P<strvalue>.*?)"'
    """Regla para Strings.

    Explicación de la regex:

    - La regex está dentro de comillas dobles (según estándar de JSON).
    - (?P<strvalue>) mete el valor dentro de las comillas en un grupo
    - .*? captura el interior, pero de manera no greedy

    Luego, accedemos al grupo con el choclo de acá abajo
    """
    t.value = t.lexer.lexmatch.groupdict()['strvalue']
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()


def apply(string):
    u"""Aplica el análisis léxico al string dado."""
    lexer.input(string)

    return list(lexer)
