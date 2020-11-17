from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):

    def IntegerStandardization(self, s: str):
        if self.checkHex(s):
            temp = int(s, base=16)
            return temp
        elif self.checkOct(s):
            temp = int (s, base=8)
            return temp
        else:
            return int(s)

    def checkHex(self, s: str):
        if 'x' in s or 'X' in s:
            return True
        else:
            return False

    def checkOct(self, s: str):
        if 'o' in s or 'O' in s:
            return True
        else:
            return False

    def visitProgram(self, ctx: BKITParser.ProgramContext):
        if ctx.getChildCount() == 1:
            return Program([])
        else:
            listDecl = []
            for i in range(ctx.getChildCount()-1):
                listDecl += self.visit(ctx.getChild(i))
            return Program(listDecl)

    def visitVar_declaration_part(self, ctx: BKITParser.Var_declaration_partContext):
        res = []
        for i in range(2, ctx.getChildCount() - 1, 2):
            res = res + [self.visit(ctx.getChild(i))]
        return res

    def visitSingle_var_list(self, ctx:BKITParser.Single_var_listContext):
        idName = ctx.ID().getText()
        dimen = []
        if ctx.ASSIGN():
            if ctx.INT_LIT():
                init = IntLiteral(self.IntegerStandardization(ctx.INT_LIT().getText()))
            elif ctx.FLOAT_LIT():
                init = FloatLiteral(float(ctx.FLOAT_LIT().getText()))
            elif ctx.STRING_LIT():
                init = StringLiteral(ctx.STRING_LIT().getText())
            elif ctx.BOOL_LIT():
                temp = ctx.BOOL_LIT().getText()
                if temp == 'True':
                    init = BooleanLiteral(True)
                else:
                    init = BooleanLiteral(False)
            else:
                init = self.visit(ctx.array_lit())
            return VarDecl(Id(idName), dimen, init)
        else:
            return VarDecl(Id(idName), dimen, None)

    def visitArray_list(self, ctx: BKITParser.Array_listContext):
        idName = ctx.ID().getText()
        numberOfLSB = len(ctx.getTokens(27))
        dimen = []
        for i in range(numberOfLSB):
            temp = self.IntegerStandardization(ctx.INT_LIT(i).getText())
            dimen = dimen + [temp]
        init = None
        if ctx.ASSIGN():
            if ctx.INT_LIT(numberOfLSB):
                init = IntLiteral(self.IntegerStandardization(ctx.INT_LIT(numberOfLSB).getText()))
            elif ctx.FLOAT_LIT():
                init = FloatLiteral(float(ctx.FLOAT_LIT().getText()))
            elif ctx.STRING_LIT():
                init = StringLiteral(ctx.STRING_LIT().getText())
            elif ctx.BOOL_LIT():
                temp = ctx.BOOL_LIT().getText()
                if temp == 'True':
                    init = BooleanLiteral(True)
                else:
                    init = BooleanLiteral(False)
            else:
                init = self.visit(ctx.array_lit())
            return VarDecl(Id(idName), dimen, init)
        else:
            return VarDecl(Id(idName), dimen, init)

    def visitArray_lit(self, ctx:BKITParser.Array_litContext):
        res = []
        indexINT = 0
        indexFLOAT = 0
        indexSTRING = 0
        indexBOOL = 0
        for i in range(1, ctx.getChildCount()-1, 2):
            temp = ctx.getChild(i)
            if isinstance(temp, BKITParser.Array_litContext):
                res = res + [self.visit(ctx.getChild(i))]
            else:
                if ctx.getChild(i) == ctx.INT_LIT(indexINT):
                    res = res + [IntLiteral(self.IntegerStandardization(ctx.INT_LIT(indexINT).getText()))]
                    indexINT += 1
                elif ctx.getChild(i) == ctx.FLOAT_LIT(indexFLOAT):
                    res = res + [FloatLiteral(float(ctx.FLOAT_LIT(indexFLOAT).getText()))]
                    indexFLOAT += 1
                elif ctx.getChild(i) == ctx.BOOL_LIT(indexBOOL):
                    temp = ctx.BOOL_LIT(indexBOOL).getText()
                    if temp == 'True':
                        res = res + [BooleanLiteral(True)]
                    else:
                        res = res + [BooleanLiteral(False)]
                    indexBOOL += 1
                else:
                    res = res + [StringLiteral(ctx.STRING_LIT(indexSTRING).getText())]
                    indexSTRING += 1
        return ArrayLiteral(res)

    # FUNCTION DECLARATION PART

    def visitFunc_declaration_part(self, ctx: BKITParser.Func_declaration_partContext):
        idName = ctx.ID().getText()
        if ctx.param_list():
            paramList = self.visit(ctx.param_list())
        else:
            paramList = []
        funcBody = self.visit(ctx.func_body())
        return [FuncDecl(Id(idName), paramList, funcBody)]

    def visitParam_list(self, ctx: BKITParser.Param_listContext):
        res = []
        listParamElement = ctx.param_element()
        if listParamElement:
            for ele in listParamElement:
                res += [self.visit(ele)]
        return res

    '''
    def visitParam_element(self, ctx: BKITParser.Param_elementContext):
        return self.visit(ctx.getChild(0))
    '''

    def visitParam_element(self, ctx: BKITParser.Param_elementContext):
        idName = ctx.ID().getText()
        if ctx.getChildCount() == 1:
            return VarDecl(Id(idName), [], None)
        else:
            listOfTokenInt = ctx.INT_LIT()
            listDimen = []
            for it in listOfTokenInt:
                listDimen += [self.IntegerStandardization(it.getText())]
            return VarDecl(Id(idName), listDimen, None)

    def visitFunc_body(self, ctx: BKITParser.Func_bodyContext):
        return self.visit(ctx.var_decl_and_statement())

    # STATEMENTS

    def visitStatement_in_function(self, ctx: BKITParser.Statement_in_functionContext):
        return self.visit(ctx.getChild(0))

    def visitAssignment(self, ctx: BKITParser.AssignmentContext):
        lhs = ctx.getChild(0)
        if isinstance(lhs, BKITParser.Element_expressionContext):
            lhs = self.visit(lhs)
        else:
            lhs = Id(lhs.getText())
        expression = self.visit(ctx.exp())
        return Assign(lhs, expression)

    def visitIf_statement_in_function(self, ctx: BKITParser.If_statement_in_functionContext):
        ifthenStmt = []
        elseStmt = ([], [])

        for i in range(ctx.getChildCount()):
            if ctx.exp(i) and ctx.var_decl_and_statement(i):
                expression = self.visit(ctx.exp(i))
                declAndStatement = self.visit(ctx.var_decl_and_statement(i))
                ifthenStmt += [(expression, declAndStatement[0], declAndStatement[1])]
            elif not(ctx.exp(i)) and ctx.var_decl_and_statement(i):
                elseStmt = self.visit(ctx.var_decl_and_statement(i))
            else:
                pass

        return If(ifthenStmt, elseStmt)

    def visitFor_statement_in_function(self, ctx:BKITParser.For_statement_in_functionContext):
        idx1 = ctx.ID().getText()
        exp1 = self.visit(ctx.exp(0))
        exp2 = self.visit(ctx.exp(1))
        exp3 = self.visit(ctx.exp(2))
        loop = self.visit(ctx.var_decl_and_statement())
        return For(Id(idx1), exp1, exp2, exp3, loop)

    def visitWhile_statement_in_function(self, ctx: BKITParser.While_statement_in_functionContext):
        expr = self.visit(ctx.exp())
        sl = self.visit(ctx.var_decl_and_statement())
        return While(expr, sl)

    def visitDo_while_statement_in_function(self, ctx: BKITParser.Do_while_statement_in_functionContext):
        expr = self.visit(ctx.exp())
        sl = self.visit(ctx.var_decl_and_statement())
        return Dowhile(sl, expr)

    def visitVar_decl_and_statement(self, ctx:BKITParser.Var_decl_and_statementContext):
        varDecl = []
        stmt = []
        for i in range(ctx.getChildCount()):
            temp = ctx.getChild(i)
            if isinstance(temp, BKITParser.Var_declaration_partContext):
                varDecl += self.visit(temp)
            else:
                stmt += [self.visit(temp)]
        return (varDecl, stmt)

    def visitBreak_statement(self, ctx: BKITParser.Break_statementContext):
        return Break()

    def visitContinue_statement(self, ctx: BKITParser.Continue_statementContext):
        return Continue()

    def visitReturn_statement(self, ctx:BKITParser.Return_statementContext):
        expr = None
        if ctx.exp():
            expr = self.visit(ctx.exp())

        return Return(expr)

    def visitFunction_call_statement(self, ctx: BKITParser.Function_call_statementContext):
        methodName = ctx.ID().getText()
        argList = []
        if ctx.argument_list():
            argList = self.visit(ctx.argument_list())
        return CallStmt(Id(methodName), argList)

    def visitFunction_call(self, ctx: BKITParser.Function_callContext):
        methodName = ctx.ID().getText()
        argList = []
        if ctx.argument_list():
            argList = self.visit(ctx.argument_list())
        return CallExpr(Id(methodName), argList)

    def visitArgument_list(self, ctx: BKITParser.Argument_listContext):
        res = []
        for i in range(ctx.getChildCount()):
            temp = ctx.exp(i)
            if temp:
                res += [self.visit(temp)]
        return res

    # EXPRESSION

    def visitElement_expression(self, ctx: BKITParser.Element_expressionContext):
        if ctx.ID():
            arr = Id(ctx.ID().getText())
        if ctx.exp():
            arr = self.visit(ctx.exp())
        if ctx.function_call():
            arr = self.visit(ctx.function_call())
        expList = self.visit(ctx.index_operators())
        return ArrayCell(arr, expList)

    def visitIndex_operators(self, ctx: BKITParser.Index_operatorsContext):
        res = []
        for i in range(ctx.getChildCount()):
            temp = ctx.exp(i)
            if temp:
                res += [self.visit(temp)]
        return res

    def visitExp(self, ctx: BKITParser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1(0))
        else:
            left = self.visit(ctx.exp1(0))
            right = self.visit(ctx.exp1(1))
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)

    def visitExp1(self, ctx: BKITParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp2())
        else:
            left = self.visit(ctx.exp1())
            right = self.visit(ctx.exp2())
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)

    def visitExp2(self, ctx: BKITParser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp3())
        else:
            left = self.visit(ctx.exp2())
            right = self.visit(ctx.exp3())
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)

    def visitExp3(self, ctx: BKITParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp4())
        else:
            left = self.visit(ctx.exp3())
            right = self.visit(ctx.exp4())
            op = ctx.getChild(1).getText()
            return BinaryOp(op, left, right)

    def visitExp4(self, ctx: BKITParser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp5())
        else:
            op = ctx.NOT().getText()
            body = self.visit(ctx.exp4())
            return UnaryOp(op, body)

    def visitExp5(self, ctx: BKITParser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.operand())
        else:
            op = ctx.getChild(0).getText()
            body = self.visit(ctx.exp5())
            return UnaryOp(op, body)

    def visitOperand(self, ctx: BKITParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INT_LIT():
            return IntLiteral(self.IntegerStandardization(ctx.INT_LIT().getText()))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.BOOL_LIT():
            temp = ctx.BOOL_LIT().getText()
            if temp == 'False':
                return BooleanLiteral(False)
            else:
                return BooleanLiteral(True)
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.function_call():
            return self.visit(ctx.function_call())
        elif ctx.element_expression():
            return self.visit(ctx.element_expression())
        elif ctx.array_lit():
            return self.visit(ctx.array_lit())
        else:
            return self.visit(ctx.exp())