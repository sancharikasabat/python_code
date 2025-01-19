"""varname='{"kye1":"val1", "key2":"val2", "key3":"val3" ,"keyn":"valn"}'

it is str type
not a dict
"""
print("-----------------------------------------------------------")
jsonstrfrm='{"Sno":"100","name":"russom","mark":"100"}'
print("json str format :", jsonstrfrm)
print("type of jsonstrfrm is:",type(jsonstrfrm))
print("-----------------------------------------------------------")

#conerted string format to dict using json.loads()
print("-----------------------------------------------------------")
import json
dictfrm=json.loads(jsonstrfrm)
print("dict format :", dictfrm)
print("type of dictfrm is:",type(dictfrm))
print("-----------------------------------------------------------")
print("-----------------------------------------------------------")
for key,val in dictfrm.items():
    print(f"key is {key}----------> {val}")

   
print("-----------------------------------------------------------")

