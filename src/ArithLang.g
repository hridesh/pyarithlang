grammar ArithLang;            // Define a grammar called Hello

@header {
from AST import *
}

// Grammar of this Programming Language
//  - grammar rules start with lowercase
//  - this is a comment. 
 
// This is an example of a production rule in its simplified form.
// program : exp ; 
// 
//
// The rule above in its full form, where actions enclosed in { }
// are used to construct abstract syntax tree (AST) nodes. 
program returns [Program ast] :   
 		e=exp {$ast = AST.Program($e.ast); }
 		;
 		
//
// In the rule above, the form "returns [Program ast]" says that this 
// rule produces an object of type Program and other rules can access that 
// produced object using the name ast. If that rule is the start rule, which
// is the case here, then ast is the object returned by parsing the program.
// In the rule above, the form "e=exp" should be read as let us called this 
// non-terminal "e". Furthermore, the form { } is an action that runs 
// when the parser is successful in demonstrating that a string belonging to
// the language was the input. For instance, in the rule above when the parser
// is successful in demonstrating that it has parsed an expression, the action
// "{ $ast = AST.Program($e.ast); } runs that creates a new object Program 
// using the object produced by the rule for non-terminal "e".
//

// The following is another example of a production rule in its simplified form.
// exp : 
//     numexp
//     | addexp
//     | subexp
//     | multexp
//     | divexp
//
// The rule above in its full form, where actions are enclosed in { }
//
 exp returns [Exp ast]: 
		n=numexp {$ast = $n.ast; }
//        | a=addexp {$ast = $a.ast; }
//        | s=subexp {$ast = $s.ast; }
//        | m=multexp {$ast = $m.ast; }
//        | d=divexp {$ast = $d.ast; }
        ;


// The following is another example of a production rule in its simplified form.
// numexp : 
//         Number 
//       | '-' Number
//       | Number Dot Number 
//       | '-' Number Dot Number 
//       ;
//
// The rule above in its full form, where actions are enclosed in { }
// 
 numexp returns [NumExp ast]:
 		n0=Number {$ast = AST.NumExp(int($n0.text)); } 
  		| '-' n0=Number {$ast = AST.NumExp(-int($n0.text)); }
  		| n0=Number Dot n1=Number {$ast = AST.NumExp(float($n0.text+"."+$n1.text)); }
  		| '-' n0=Number Dot n1=Number {$ast = AST.NumExp(float("-" + $n0.text+"."+$n1.text)); }
  		;		


 // Lexical Specification of this Programming Language
 //  - lexical specification rules start with uppercase
 
 Dot : '.' ;

 Number : DIGIT+ ;

 Identifier :   Letter LetterOrDigit*;

 Letter :   [a-zA-Z$_]
	|   ~[\u0000-\u00FF\uD800-\uDBFF] 
	|   [\uD800-\uDBFF] [\uDC00-\uDFFF] ;

 LetterOrDigit: [a-zA-Z0-9$_]
	|   ~[\u0000-\u00FF\uD800-\uDBFF] 
	|    [\uD800-\uDBFF] [\uDC00-\uDFFF] ;

 fragment DIGIT: ('0'..'9');

 AT : '@';
 ELLIPSIS : '...';
 WS  :  [ \t\r\n\u000C]+ -> skip;
 Comment :   '/*' .*? '*/' -> skip;
 Line_Comment :   '//' ~[\r\n]* -> skip;