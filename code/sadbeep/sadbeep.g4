grammar sadbeep;

OPEN_PAREN : '(';
CLOSE_PAREN : ')';
fragment ID_START : [a-zA-Z]+;
fragment ID_BODY : ID_START | NUMBER;
ID : ID_START ID_BODY*;
NUMBER : INT | UINT | FLOAT;
INT: '-'?[0-9]+;
UINT: [0-9]+;
FLOAT: '-'?[0-9]+'.'[0-9]+;
TRUE: 'true';
FALSE: 'false';
BOOL: TRUE | FALSE;
WS: [ \n\t\r]+ -> skip;
DOT: '.';
COMMA: ',';

parse : expr* EOF;

expr : variable '=' expr ';'        
     | number                       
     | function_def                 
     | expr expr                    
     | OPEN_PAREN expr CLOSE_PAREN  
     | STRING
     | 'return' expr ';'
     | ID
     | call
     | exp
     | operators
     | if_smtm
     | smtm
     ;
     
operators: '+' | '-' | '/' | '*';

function_def : 'func' name=ID '(' args? ')' block;

args : ID (',' ID)*;

block: '{' expr* '}';

call : name=ID '(' exprs? ')' ';';

exprs : expr (',' expr)*;

number : NUMBER; 
variable : ID;
STRING: '\''~[\r\n']*'\'' | '"'~[\r\n']*'"';

exp: left=summ (op=('>' | '<' | '>=' | '<=' | '==' | '!=') right=exp)*;

summ: left=mult (op=('+'|'-') right=summ)*;

mult: left=atom (op=('*' | '/' | '%') right=mult)*;

expf : exp
        | summ
        | mult
        | expr
        ;

atom
   : '(' exp ')'
   | INT
   | UINT
   | BOOL
   | FLOAT
   | STRING
   | ID
   | 'input'
   ;

if_smtm: 'if' expf '{' stmt* '}'
    ;

COMMENT
    : '/*' .*? '*/' -> skip
;

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
;