'''
This class hierarchy represents the set of program values produced by
this interpreter.
 
@author: Hridesh Rajan
Copyright (c) 2018. All rights reserved.
See LICENSE file in the root directory for licensing information.
'''
from abc import ABC, abstractmethod

class Value(ABC):
    @abstractmethod
    def __str__(self):
        pass

class NumVal(Value):
    val = 0.0
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return str(self.val)