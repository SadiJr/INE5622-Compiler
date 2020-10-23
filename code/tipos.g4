grammar tipos;

expr : left=summ (op=('>'|'<'|'>='|'<='|'=='|'!=') right=expr)*
     ;

summ : left=mult (op=('+'|'-') right=summ)*
     ;

mult : left=atom (op=('*'|'/') right=mult)*
     ;

atom : '(' expr ')'
     | INT
     | BOOL
     | FLOAT
     | ID
     | 'input'
     ;

ID : [a-zA-Z]+[0-9a-zA-Z]*;
INT : '-'?[0-9]+;
FLOAT : '-'?[0-9]+ '.'[0-9]+;
TRUE : 'true';
FALSE : 'false';
BOOL : TRUE | FALSE;
WS : [ \n\t\r] -> skip;
