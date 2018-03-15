* Python 3

This interpreter requires Python 3 to work. No attempts have been made
to achieve backward compatibility with Python 2, nor is there any interest
among authors and contributors. 

You must install Python 3 before proceedings forward. Please see elsewhere
for more information on installing Python 3. 


* Python installation of ANTLR grammar
https://github.com/antlr/antlr4/blob/master/doc/python-target.md

You must install ANTLR runtime for this interpreter to work. This can be 
done by using the pip3 command as follows

pip3 install antlr4-python3-runtime

You must have sufficient rights to install packages. Access control 
issues are beyond the scope of this document. 



* How to run the interpreter?

 Type the following on the command-line.
 
 python3 interpreter.py input.txt 


* How to regenerate the parser?

 If you have made any grammar changes, it would be necessary to regenerate
 the lexer and parser related files. To do so, run the following commands.

 cd src
 java -jar ../lib/antlr-4.7.1-complete.jar -Dlanguage=Python3 -no-listener ArithLang.g4

