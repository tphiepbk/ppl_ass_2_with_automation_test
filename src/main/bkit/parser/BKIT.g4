grammar BKIT;
//ID: 1812227

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
    language=Python3;
}

program :                                   var_declaration_part* func_declaration_part* EOF;

// Variable declaration

var_declaration_part:                        VAR COLON (single_var_list | array_list) (COMMA (single_var_list | array_list))* SEMI;

single_var_list:                             ID (ASSIGN (INT_LIT | FLOAT_LIT | STRING_LIT | BOOL_LIT | array_lit))?;

array_list:                                  ID (LSB INT_LIT RSB)+ (ASSIGN (array_lit | FLOAT_LIT | INT_LIT | BOOL_LIT | STRING_LIT))?;

/*
array_1d:                                   LB (INT_LIT | FLOAT_LIT | STRING_LIT | BOOL_LIT)? (COMMA (INT_LIT | FLOAT_LIT | BOOL_LIT | STRING_LIT)? )* RB;

array_multidimension:                       LB (array_1d |  array_multidimension | INT_LIT | FLOAT_LIT | STRING_LIT | BOOL_LIT)? (COMMA (array_1d | array_multidimension | INT_LIT |FLOAT_LIT | BOOL_LIT | STRING_LIT))* RB;

array_lit:                                  array_multidimension;
*/
array_lit:                                  LB (INT_LIT | FLOAT_LIT | STRING_LIT | BOOL_LIT | array_lit)? (COMMA (INT_LIT | BOOL_LIT | STRING_LIT | FLOAT_LIT | array_lit) )* RB;


// Function declaration

func_declaration_part:                      FUNCTION COLON ID param_list? func_body;

param_list:                                 PARAMETER COLON param_element (COMMA param_element)*;

//param_element:                              ID | array_list;
param_element:                              single_var_list | array_list;

//func_body:                                  BODY COLON var_declaration_part* (statement_in_function)*  ENDBODY DOT;
func_body:                                  BODY COLON var_decl_and_statement  ENDBODY DOT;

statement_in_function:                      (assignment | function_call_statement | if_statement_in_function | for_statement_in_function | while_statement_in_function | do_while_statement_in_function | return_statement | break_statement | continue_statement);

//if_statement_in_function:                   IF (exp) THEN var_declaration_part* (statement_in_function)* (ELSEIF (exp) THEN var_declaration_part* (statement_in_function)*)* (ELSE var_declaration_part* (statement_in_function)*)? ENDIF DOT;
if_statement_in_function:                   IF (exp) THEN var_decl_and_statement (ELSEIF (exp) THEN var_decl_and_statement)* (ELSE var_decl_and_statement)? ENDIF DOT;

//for_statement_in_function:                  FOR LP (ID ASSIGN exp COMMA exp COMMA exp) RP DO var_declaration_part* (statement_in_function)* ENDFOR DOT;
for_statement_in_function:                  FOR LP (ID ASSIGN exp COMMA exp COMMA exp) RP DO var_decl_and_statement ENDFOR DOT;
/*
for_statement_in_function:                  FOR LP (assign_in_for COMMA condition_expression COMMA update_expression) RP DO var_declaration_part* (statement_in_function)* ENDFOR DOT;

assign_in_for:                              (ID) ASSIGN (exp);

condition_expression:                       (exp);

update_expression:                          exp;
*/

//while_statement_in_function:                WHILE (exp) DO var_declaration_part* (statement_in_function)* ENDWHILE DOT;
while_statement_in_function:                WHILE (exp) DO var_decl_and_statement ENDWHILE DOT;

//do_while_statement_in_function:             DO var_declaration_part* (statement_in_function)* WHILE (exp) ENDDO DOT;
do_while_statement_in_function:             DO var_decl_and_statement WHILE (exp) ENDDO DOT;

var_decl_and_statement:                     var_declaration_part* statement_in_function*;

assignment:                                 (ID | element_expression) ASSIGN (exp) SEMI;

break_statement:                            'Break' SEMI;

continue_statement:                         'Continue' SEMI;

return_statement:                           'Return' (exp)? SEMI;

function_call_statement:                    ID LP argument_list? RP SEMI;

// Expression

function_call:                              ID LP argument_list? RP;

argument_list:                              exp (COMMA exp)*;

//element_expression:                         (ID | function_call) index_operators;
element_expression:                         (LP exp RP | ID | function_call)  index_operators;

/*
index_operators
    //: LSB (index_operand | element_expression) RSB
    : LSB (exp) RSB
    //| LSB (index_operand | element_expression) RSB index_operators
    | LSB (exp) RSB index_operators
    ;
*/
index_operators: (LSB exp RSB)+;

//index_operand: exp;

exp
    : exp1 EQUAL exp1
    | exp1 NOTEQUAL_INT exp1
    | exp1 LT_INT exp1
    | exp1 GT_INT exp1
    | exp1 GTE_INT exp1
    | exp1 LTE_INT exp1
    | exp1 NOTEQUAL_FLOAT exp1
    | exp1 LT_FLOAT exp1
    | exp1 GT_FLOAT exp1
    | exp1 LTE_FLOAT exp1
    | exp1 GTE_FLOAT exp1
    | exp1
    ;

exp1
    : exp1 AND exp2
    | exp1 OR exp2
    | exp2
    ;

exp2
    : exp2 ADD_INT exp3
    | exp2 ADD_FLOAT exp3
    | exp2 SUB_FLOAT exp3
    | exp2 SUB_INT exp3
    | exp3
    ;

exp3
    : exp3 MUL_FLOAT exp4
    | exp3 MUL_INT exp4
    | exp3 DIV_FLOAT exp4
    | exp3 DIV_INT exp4
    | exp3 MOD exp4
    | exp4
    ;

exp4
    : NOT exp4
    | exp5
    ;

exp5
    : SUB_FLOAT exp5
    | SUB_INT exp5
    | operand
    ;

operand
    : ID
    | INT_LIT
    | FLOAT_LIT 
    | function_call
    | element_expression
    | BOOL_LIT
    | STRING_LIT
    | array_lit
    | LP exp RP
    ;

fragment LOWERCASE_LETTER: [a-z];
fragment UPPERCASE_LETTER: [A-Z];
fragment DIGIT: [0-9];
fragment UNDERSCORE: '_';

// Identifier
ID: LOWERCASE_LETTER (LOWERCASE_LETTER | UPPERCASE_LETTER | DIGIT | UNDERSCORE)* ;

// Keyword
BODY:           'Body';
BREAK:          'Break';
CONTINUE:       'Continue';
DO:             'Do';
ELSE:           'Else';
ELSEIF:         'ElseIf';
ENDBODY:        'EndBody';
ENDIF:          'EndIf';
ENDFOR:         'EndFor';
ENDWHILE:       'EndWhile';
FOR:            'For';
FUNCTION:       'Function';
IF:             'If';
PARAMETER:      'Parameter';
RETURN:         'Return';
THEN:           'Then';
VAR:            'Var' ;
WHILE:          'While';
ENDDO:          'EndDo';

SEMI:       ';';
COLON:      ':';
DOT:        '.';
COMMA:      ',';
LP:         '(';
RP:         ')';
LSB:        '[';
RSB:        ']';
LB:         '{';
RB:         '}';


// Operator
ADD_INT:                 '+';
ADD_FLOAT:               ADD_INT DOT;
SUB_INT:                 '-';
SUB_FLOAT:               SUB_INT DOT;
MUL_INT:                 '*';
MUL_FLOAT:               MUL_INT DOT;
DIV_INT:                 '\\';
DIV_FLOAT:               DIV_INT DOT;
MOD:                    '%';
ASSIGN:                  '=';

NOT:                    '!';
AND:                    '&&';
OR:                     '||';

EQUAL:                  '==';
NOTEQUAL_INT:            '!=';
LT_INT:                  '<';
GT_INT:                  '>';
LTE_INT:                 '<=';
GTE_INT:                 '>=';
NOTEQUAL_FLOAT:           '=/=';
LT_FLOAT:                LT_INT DOT;
GT_FLOAT:                GT_INT DOT;
LTE_FLOAT:               LTE_INT DOT;
GTE_FLOAT:               GTE_INT DOT;


// Integer Literal
INT_LIT:                (HEX | OCTAL | DECIMAL | ZERO_LIT);
// Fragment for INTEGER LITERAL
fragment DECIMAL:       ([1-9] /*~([a-zA-Z])*/ DIGIT*);
fragment HEX:           ('0x' | '0X') [1-9A-F] HEX_DIGIT*;
fragment HEX_DIGIT:     [0-9A-F];
fragment OCTAL:         ('0o' | '0O') [1-7] OCTAL_DIGIT*;
fragment OCTAL_DIGIT:   [0-7];

ZERO_LIT:               '0' /*(~[a-zA-Z0-9])*/;

// Float Literal
FLOAT_LIT:               INT_PART (DEC_PART? EXP_PART | DEC_PART EXP_PART?);
// Fragment for FLOAT LITERAL
fragment INT_PART:       [0-9]+;
fragment DEC_PART:       DOT DIGIT*;
fragment EXP_PART:       ('e' | 'E') ('-' | '+')? DIGIT+;

STRING_LIT
    : '"' (('\'"') | '\\'([bfrnt\\'])| ~(["\n\\]| '\''))* '"'
    {
        self.text = self.text[1:-1]
    };


BOOL_LIT:                (TRUE | FALSE);

TRUE:           'True';
FALSE:          'False';


COMMENT:        '**' .*? '**' -> skip;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ILLEGAL_ESCAPE
    : '"' (('\'"') | '\\'([bfrnt\\']) | ~(["\n\\] | '\''))* ('\\'~[bfrnt'\\] | '\''~'"') '"'
    {
        raise IllegalEscape(self.text[1:])
    };

UNCLOSE_STRING
    : '"'  (('\'"') | '\\'([bfrnt\\'])| ~(["\n\\]| '\''))*
    {
        raise UncloseString(self.text[1:])
    };

// Fragment for STRING LITERAL
fragment STR_CHAR:       ~[\n"\\];
fragment ESC_SEQ:        ('\\' [bfrnt'\\]);
fragment DOUBLE_QUOTE:   '\'"';
fragment ESC_ILLEGAL:    ('\\' ~[bfrnt'\\]) | ('\'' ~'"');

UNTERMINATED_COMMENT
    :'**' .*?
    {
        raise UnterminatedComment()
    };

ERROR_CHAR: .
    {
        raise ErrorToken(self.text[0:])
    };
