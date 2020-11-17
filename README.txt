Version 1.1
- Fix AST.py:
	- Change type of arr of class ArrayCell to Expr
	- Remove field idx2 of class For
	- Fix method __str__ of ArrayLiteral and FuncDecl

Version 1.0

Change current directory to initial/src where there is file run.py
Type: python run.py gen 
Then type: python run.py test ASTGenSuite

WHAT'S NEW IN AUTOMATION TEST VERSION :	
- Change AST.py to make the output (in the solution folder) have the same format with the expect in ASTGenSuite.py
- Added madao_v1.py and madao_v2.py to copy the solution to the expect in ASTGenSuite.py

The code to make test automatically is written by Nguyen Cong Minh.
