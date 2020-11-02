import json
import operator
import re
import cache

#calculation regex format
regex = "[0-9] [-+*^/] [0-9]"
pattern = re.compile(regex)

#instantiate cache object
calcCache = cache.Cache()

#operators lookup table
ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '^' : operator.pow
}

#parse input, apply calculation, and return it
def calculate(calcStr, get_operator=ops.get):
    args = calcStr.split(" ")
    return get_operator(args[1])(int(args[0]),int(args[2]))

#takes the input, validates it for valid formatting, and returns the
#calculation if successful
def lambda_handler(event, context):
    calculation = event.get("calculation")
    if (pattern.match(calculation) != None):
        calc_result = calculate(calculation)
        return_body = str(calculation + " = " + str(calc_result))
        calcCache.addCalc(return_body)
        return {
            'statusCode': 200,
            'body': return_body
        }
    else:
        return {
            'statusCode' : 400,
            'body' : "Invalid calculation"
        }
