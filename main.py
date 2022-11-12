import rationalController as rat
import type as ty
import complexController as com

type = ty.type()

while type == 'rational':
    rat.mainterminal()

if type == 'complex':
    repeat = True
    while repeat == True:
        operands = com.Insert_Numbers()
        if operands[2] == "+":
            com.record_in_file(com.Addition(com.Take_Rational_Part(operands[0]), com.Take_Symbol(operands[0]),
                                            com.Take_Imaginary_Part(operands[0]),
                                            com.Take_Rational_Part(operands[1]), com.Take_Symbol(operands[1]),
                                            com.Take_Imaginary_Part(operands[1])))
        elif operands[2] == "-":
            com.record_in_file(com.Deduction(com.Take_Rational_Part(operands[0]), com.Take_Symbol(operands[0]),
                                             com.Take_Imaginary_Part(operands[0]),
                                             com.Take_Rational_Part(operands[1]), com.Take_Symbol(operands[1]),
                                             com.Take_Imaginary_Part(operands[1])))
        elif operands[2] == "*":
            com.record_in_file(com.Multiply(com.Take_Rational_Part(operands[0]), com.Take_Symbol(operands[0]),
                                            com.Take_Imaginary_Part(operands[0]),
                                            com.Take_Rational_Part(operands[1]), com.Take_Symbol(operands[1]),
                                            com.Take_Imaginary_Part(operands[1])))
        else:
            com.record_in_file(com.division(com.Take_Rational_Part(operands[0]), com.Take_Symbol(operands[0]),
                                            com.Take_Imaginary_Part(operands[0]),
                                            com.Take_Rational_Part(operands[1]), com.Take_Symbol(operands[1]),
                                            com.Take_Imaginary_Part(operands[1])))
        repeat = com.Repeat_Or_No()
