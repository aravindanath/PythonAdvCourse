"""
REGular Expression (RegEx) is a used to search the sequeance of char in String.

"""
import re

pattern = '^a....s$'

stat = "abacus"

result= re.match(pattern,stat)

if result:
    print("Sucess")
else:
    print("fail")