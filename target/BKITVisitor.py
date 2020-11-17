# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_declaration_part.
    def visitVar_declaration_part(self, ctx:BKITParser.Var_declaration_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#single_var_list.
    def visitSingle_var_list(self, ctx:BKITParser.Single_var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_list.
    def visitArray_list(self, ctx:BKITParser.Array_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_lit.
    def visitArray_lit(self, ctx:BKITParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_declaration_part.
    def visitFunc_declaration_part(self, ctx:BKITParser.Func_declaration_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#param_list.
    def visitParam_list(self, ctx:BKITParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#param_element.
    def visitParam_element(self, ctx:BKITParser.Param_elementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_body.
    def visitFunc_body(self, ctx:BKITParser.Func_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement_in_function.
    def visitStatement_in_function(self, ctx:BKITParser.Statement_in_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_statement_in_function.
    def visitIf_statement_in_function(self, ctx:BKITParser.If_statement_in_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_statement_in_function.
    def visitFor_statement_in_function(self, ctx:BKITParser.For_statement_in_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_statement_in_function.
    def visitWhile_statement_in_function(self, ctx:BKITParser.While_statement_in_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#do_while_statement_in_function.
    def visitDo_while_statement_in_function(self, ctx:BKITParser.Do_while_statement_in_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_decl_and_statement.
    def visitVar_decl_and_statement(self, ctx:BKITParser.Var_decl_and_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignment.
    def visitAssignment(self, ctx:BKITParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_statement.
    def visitBreak_statement(self, ctx:BKITParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_statement.
    def visitContinue_statement(self, ctx:BKITParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_statement.
    def visitReturn_statement(self, ctx:BKITParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_call_statement.
    def visitFunction_call_statement(self, ctx:BKITParser.Function_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function_call.
    def visitFunction_call(self, ctx:BKITParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#argument_list.
    def visitArgument_list(self, ctx:BKITParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#element_expression.
    def visitElement_expression(self, ctx:BKITParser.Element_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_operators.
    def visitIndex_operators(self, ctx:BKITParser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp.
    def visitExp(self, ctx:BKITParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp1.
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp2.
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp3.
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp4.
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp5.
    def visitExp5(self, ctx:BKITParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operand.
    def visitOperand(self, ctx:BKITParser.OperandContext):
        return self.visitChildren(ctx)



del BKITParser