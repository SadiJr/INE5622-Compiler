grammar sadbeep;

parse : expr* EOF;

expr : ID '=' expr ';'        
     | NUMBER                       
     | function_def                 
     | expr expr                    
     | OPEN_PAREN expr CLOSE_PAREN  
     | STRING
     | 'return' expr ';'
     | ID
     | call
     | exp
     | operators
     ;
     
operators: '+' | '-' | '*' | '/' | '%';

function_def : 'func' name=ID '(' args? ')' block;

args : ID (',' ID)*;

block: '{' expr* '}';

call : name=ID '(' exprs? ')' ';';

exprs : expr (',' expr)*;

exp: left=summ (op=('>' | '<' | '>=' | '<=' | '==' | '!=') right=exp)*;

summ: left=mult (op=('+'|'-') right=summ)*;

mult: left=atom (op=('*' | '/' | '%') right=mult)*;

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

fragment ID_START : [a-zA-Z]+;
fragment ID_BODY : ID_START | NUMBER;

ID : ID_START ID_BODY*;

// Comentário
COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;

// Parentêses
OPEN_PAREN : '(';
CLOSE_PAREN : ')';

// Números
NUMBER : INT | UINT | FLOAT;
INT: '-'?[0-9]+;
UINT: [0-9]+;
FLOAT: '-'?[0-9]+'.'[0-9]+;

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
