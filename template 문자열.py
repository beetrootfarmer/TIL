tstring = "this is {template} {template} is {state}"
variables = [["template", "string"], ["state", "changed"]]




# result = "this is string string is changed"
from string import Template
import re

# def solution (tstring, variables):
#     v = {} #딕셔너리 생성
#     while(True):
#         for i in range(len(variables)):
#             key = variables[i][0]
#             value = variables[i][1]
#             v[key] = value
            
#         tem = re.sub('{',"$",tstring)
#         tem1 = re.sub('}','',tem) 
#         a = Template(tem1)
#         answer = '"'+ a.substitute(v) +'"'
#         if key not in v:
#             break
#     return answer
def solution (tstring, variables):
    v = {} #딕셔너리 생성
    for i in range(len(variables)):
        key = variables[i][0]
        value = variables[i][1]
        v[key] = value
                
    tem = re.sub('{',"$",tstring)
    tem1 = re.sub('}','',tem) 
    a = Template(tem1)
    answer = '"'+ a.substitute(v) +'"'
            
    return answer
print(solution (tstring, variables))



# 테스트 케이스와 결과값 

# "this is {template} {template} is {state}"
# [["template", "string"], ["state", "{template}"]]
# result = "this is string string is changed"

# "this is {template} {template} is {state}"
# [["template", "{state}"], ["state", "{template}"]]
# result = "this is {template} {template} is {state}"

# "this is {template} {template} is {state}"
# [["template", "{state}"], ["state", "{templates}"]]
# result = "this is {templates} {templates} is {templates}"

# "{a} {b} {c} {d} {i}"
# [["b", "{c}"], ["a", "{b}"], ["e", "{f}"], ["h", "i"], ["d", "{e}"], ["f", "{d}"], ["c", "d"]]
# result = "d d d {d} {i}"