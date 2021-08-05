'''
Author: Yiling He
Date: 2021-03-09 10:41:34
LastEditTime: 2021-04-25 10:36:28
LastEditors: Yiling He
Contact: heyilinge0@gmail.com
Description: 
FilePath: \AI4Code-Framework\ai4code\features\preprocessing\preprocess.py
'''

class Analyzer(self):
    def __init__(self, data, code_level, feature_level, analysis_obj):
        pass

    def disassemble(self, binary):
        """
        from binary to bytecode
        """
        return NotImplementedError

    def decompile(self, binary):
        """
        from binary to pseudocode
        """
        return NotImplementedError

    def get_call_graph(self) -> nx.MultiDiGraph:
        """
        call graph: program-wide contextual information
        """
        return NotImplementedError

    def get_method_cfg(self) -> nx.MultiDiGraph:
        """
        contol flow graph: basic block information
        """
        return NotImplementedError

    def get_method_ast(self) -> dict:
        """
        abstract syntax trees (AST) of a method
        """
        return NotImplementedError

    def get_method_tokens(self, operand=None) -> list:
        """
        tokens (opcode / operand) list of a method / basic block
        """
        return NotImplementedError
