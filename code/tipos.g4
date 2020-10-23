grammar tipos;

expr : left=summ (op=('>'|'<'|'>='|'<='|'=='|'!=') right=expr)*
     ;

summ : left=mult (op=('+'|'-') right=summ)*
     ;

mult : left=atom (op=('*'|'/'|'%') right=mult)*
     ;

atom : '(' expr ')'
     | INT
     | UINT
     | BOOL
     | FLOAT
     | STRING
     | ID
     | 'input'
     ;

ID : [a-zA-Z]+[0-9a-zA-Z]*;
INT : '-'?[0-9]+;
UINT: [0-9]+;
FLOAT : '-'?[0-9]+ '.'[0-9]+;
STRING: [\!-\~]+
TRUE : 'true';
FALSE : 'false';
BOOL : TRUE | FALSE;
WS : [ \n\t\r] -> skip;
