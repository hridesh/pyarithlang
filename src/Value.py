'''
This class hierarchy represents the set of program values produced by
this interpreter.
 
@author hridesh
'''

class Value:
    def __str__(self):
        return "value"

class NumVal(Value):
    val = 0.0
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return str(self.val)