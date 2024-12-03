import os
import re

#input = open("input_example.txt")
input = open("input.txt").read()
mul_pattern = r"mul\(\d+,\d+\)"
result = 0

#print(matches)

# Part 1
def extract_muls(input_string):
    return re.findall(mul_pattern, input_string)

def extract_multipliers(expression):
    stripped = expression.replace("mul(", "").replace(")", "").split(",")
    return tuple(map(int, stripped))

part1_matches = extract_muls(input)

for match in part1_matches:
    a, b = extract_multipliers(match)
    
    result += a * b

print(result)



# Part 2

first_valid_mul_pattern = r"(.*)don\'t\(\)"
valid_mul_pattern = r"do\(\)(.*?)don\'t\(\)"
#final_mul_pattern = r"(.*?)do\(\)(.*)"
result = 0

def extract_valid_multiplications(input_string):
    matches = re.findall(valid_mul_pattern, input_string)
    return matches

first_do_expression = re.findall(first_valid_mul_pattern, input)
do_expressions = extract_valid_multiplications(input)
final_do_expression = input.split("do()")

final_do_expression.reverse()

first_matches = extract_muls(first_do_expression[0])
final_matches = extract_muls(final_do_expression[0])

for match in first_matches:
    first_a, first_b = extract_multipliers(match)
    result += first_a * first_b

for match in final_matches:
    final_a, final_b = extract_multipliers(match)
    result += final_a * final_b

for expression in do_expressions:
#    print(expression)
    mul_expressions = extract_muls(expression)

    for mul_expression in mul_expressions:
        a, b = extract_multipliers(mul_expression)

        result += a * b

print(result)
