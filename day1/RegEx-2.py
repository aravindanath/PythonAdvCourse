"""
REGular Expression (RegEx) is a used to search the sequeance of char in String.

Meta char --> [].^*$?+{}()\|
"""
import re

pat = "\d"
msg = "Hello Nagamani, OTP for txn id asdfasdf xxx2322 ICICI-2452234 ajhsdkfhj asdkjhasd"
#
# result = re.match(pat,sat)
# print(result)

def getOTP(msg):
    for i in msg.replace("-", " ").split(" "):
        result = re.match(pat, i)
        if result:
           return i

g = getOTP(msg)
print("OTP: ",g)