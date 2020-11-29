grammar sadbeep;

parse : expr* EOF;

expr : variable '=' expr ';'                                    # assign
     | number                                                   # expr_number
     | function_def                                             # expr_function
     | expr expr                                                # expr_follow
     | '(' expr ')'                                             # expr_parenthesis
     | STRING                                                   # expr_string
     | 'return' expr ';'                                        # return
     | ID                                                       # expr_ID
     | call                                                     # expr_call
     | expr operators ';'                                       # expr_operators
     | '-'? exp                                                 # expr_negative
     | 'if' cond=expr ('&&' cond=expr)*                         # if
     | ('||' cond=expr)* then=block ('else' otherwise=block)?   # else
     | 'while' cond=expr ('&&' cond=expr)*                      # while
     | ('||' cond=expr)* block                                  # or
     | 'for' forexpr block                                      # for
     | 'switch' expr? '{' (cases)+ '}'                          # switch
     ;

operators: mult | summ;

number: INT | FLOAT;

variable: ID;

function_def : 'func' name=ID '(' args? ')' block;

args : ID (',' ID)*;

cases: 'case' expr ':' expr 'break;'?;

block: '{' expr* '}';

call : name=ID '(' exprs? ')' ';';

exprs : expr (',' expr)*;

forexpr : '(' variable '=' expr ';' cond=expr ';' variable '=' expr ')';

exp: left=summ (op=('>' | '<' | '>=' | '<=' | '==' | '!=') right=exp)*;

summ: left=mult (op=('+'|'-') right=summ)*;

mult: left=atom (op=('*' | '/' | '%') right=mult)*;

atom
   : '(' '-'?exp ')'
   | '-'?number
   | BOOL
   | STRING
   | ID
   | 'input'
   ;

fragment ID_START : [a-zA-Z]+;
fragment ID_BODY : ID_START | NUMBER;

ID : ID_START ID_BODY*;

// Comentário
COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;

// Números
NUMBER : INT | FLOAT;
INT: [0-9]+;
FLOAT: [0-9]+'.'[0-9]+;

// Booleano
TRUE: 'True';
FALSE: 'False';
BOOL: TRUE | FALSE;

// String
STRING: '\''~[\r\n']*'\'' | '"'~[\r\n']*'"';
// Quebra de linha e outros sinais
WS: [ \n\t\r]+ -> skip;
DOT: '.';
COMMA: ',';
