grammar sadbeep;

parse : expr* EOF;

expr : variable '=' expr ';'                                                                            # assign
     | 'print' expr ';'                                                                                 # print
     | number                                                                                           # numbers
     | function_def                                                                                     # func
     | '(' expr ')'                                                                                     # paren
     | STRING                                                                                           # text
     | 'return' expr ';'                                                                                # return
     | call                                                                                             # op
     | LESS? exp                                                                                        # neg
     | 'if' cond=expr ('&&' cond=expr | '||' cond=expr)* then=block ('else' otherwise=block)?           # if
     | 'while' cond=expr ('&&' cond=expr | '||' cond=expr)* block                                       # while
     | 'for' forexpr                                                                                    # for
     | 'switch' expr? '{' (cases)+ '}'                                                                  # switch
     ;

operators: mult | summ;

number: NUMBER;

variable: ID;

function_def : 'func' name=ID '(' args? ')' ':' precision block;

args : ID ':' precision (',' ID ':' precision)*;

precision : 'int' | 'float';

cases: 'case' expr ':' expr 'break;'?;

block: '{' expr* '}';

call : name=ID '(' exprs? ')' ';';

exprs : expr (',' expr)*;

forexpr : '(' init';' cond=expr ';' finish ')' block;

init: variable '=' expr;

finish: variable '=' expr;

exp: left=summ (op=('>' | '<' | '>=' | '<=' | '==' | '!=') right=exp)*;

summ: left=mult (op=('+'|'-') right=summ)*;

mult: left=atom (op=('*' | '/' | '%') right=mult)*;

atom
   : '(' LESS?exp ')'
   | LESS?number
   | BOOL
   | STRING
   | ID
   | 'input'
   ;

fragment ID_START : [a-zA-Z]+;
fragment ID_BODY : ID_START | NUMBER;

ID : ID_START ID_BODY*;

LESS : '-';

// Comentário
COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;

// Números
NUMBER : INT | FLOAT;
INT: [0-9]+;
FLOAT: [0-9]+'.'[0-9]+;

// Booleano
TRUE: 'true';
FALSE: 'false';
BOOL: TRUE | FALSE;

// String
STRING: '\''~[\r\n']*'\'' | '"'~[\r\n']*'"';
// Quebra de linha e outros sinais
WS: [ \n\t\r]+ -> skip;
DOT: '.';
COMMA: ',';
