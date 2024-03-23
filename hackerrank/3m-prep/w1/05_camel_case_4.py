# Camel Case is a naming style common in many programming languages. In Java, 
# method and variable names typically start with a lowercase letter, with all 
# subsequent words starting with a capital letter (example: startThread). 
# Names of classes follow the same pattern, except that they start with a capital 
# letter (example: BlueCar).

# Your task is to write a program that creates or splits Camel Case variable, 
# method, and class names.

# Input Format

# - Each line of the input file will begin with an operation (S or C) followed 
# by a semi-colon followed by M, C, or V followed by a semi-colon followed by the 
# words you'll need to operate on.

# - The operation will either be S (split) or C (combine).

# - M indicates method, C indicates class, and V indicates variable.

# - In the case of a split operation, the words will be a camel case method, class 
# or variable name that you need to split into a space-delimited list of words starting 
# with a lowercase letter.

# - In the case of a combine operation, the words will be a space-delimited list 
# of words starting with lowercase letters that you need to combine into the appropriate 
# camel case String. Methods should end with an empty set of parentheses to differentiate 
# them from variable names.

# Output Format
# - For each input line, your program should print either the space-delimited list of words 
# (in the case of a split operation) or the appropriate camel case string (in the case 
# of a combine operation).

# Sample Input
# S;M;plasticCup()
# C;V;mobile phone
# C;C;coffee machine
# S;C;LargeSoftwareBook
# C;M;white sheet of paper
# S;V;pictureFrame

# Sample Output
# plastic cup
# mobilePhone
# CoffeeMachine
# large software book
# whiteSheetOfPaper()
# picture frame

# Explanation
# Use Scanner to read in all information as if it were coming from the keyboard.
# Print all information to the console using standard output (System.out.print() or System.out.println()).
# Outputs must be exact (exact spaces and casing).

# Enter your code here. Read input from STDIN. Print output to STDOUT

# S(split) or C(combine)
# M(method), C(class), V(variable)

# (S,C);(M,C,V);<word,s>

# This was my first try, trying to split by delimiter or regexp
# import re
# 
# lines = []
# while True:
#     try:
#         line = input("Enter a command string:\n")
#     except EOFError:
#         break
#     lines.append(line)
#     
# # print(lines)
# 
# for line in lines:
#     cmd = line.split(';')
#     op = cmd[0]
#     type = cmd[1]
#     content = cmd[2]
#     # print(op, type, content)
# 
#     output = ""
#     if op == 'S':
#         split_by_cap = re.findall('[A-Za-z][^A-Z]*', content)
#         lowercases = []
#         for w in split_by_cap:
#             lowercases.append(w.lower())
#         output = (' ').join(lowercases)
#         
#     else:
#         words = content.split(' ')
#         # print("words", words)
#         capitalized = []
#         for w in words:
#             capitalized.append(w.capitalize())
#         if type == 'V':
#             capitalized[0] = capitalized[0].lower()
#         if type == 'M':
#             capitalized[0] = capitalized[0].lower()
#             capitalized.append('()')
#         output = ('').join(capitalized)
# 
#     print(output)

# This is a version from ChatGPT, with some tuning
def camel_case_operations(op, cat, words):
    if op == 'S':
        return split_camel_case(words)
        
    elif op == 'C':
        if cat == 'M':
            return combine_camel_case(words, 1) + '()'
        if cat == 'V':
            return combine_camel_case(words, 1)
        return combine_camel_case(words, 0)

def combine_camel_case(words, offset):
    words_list = words.split()
    result = ''
    if offset == 1:
        result += words_list[0]
    for i in range(offset, len(words_list)):
        result += words_list[i].capitalize()
    return result

def split_camel_case(string):
    result = []
    current_word = ''
    for c in string:
        if c.isupper():
            if current_word:
                result.append(current_word.lower())
            current_word = c
        elif c == '(' or c == ')':
            pass
        else:
            current_word += c
    if current_word:
        result.append(current_word.lower())
    
    return ' '.join(result)

while True:
    try:
        user_input = input()
        op, cat, words = user_input.split(";")
        output = camel_case_operations(op, cat, words)
        print(output)
        
    except EOFError:
        break
    
