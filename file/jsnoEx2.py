
#converted dict format to string format 
print("-----------------------------------------------------------")
dictfrmstr={"sno":100,"name":"russom","mark":100}
print("content od dict ",dictfrmstr)
print("type of data in it ",type(dictfrmstr))
print("-----------------------------------------------------------")
import json

jsonstrfrm=json.dumps(dictfrmstr)
print("content od dict ",jsonstrfrm)
print("type of data in it ",type(jsonstrfrm))
print("-----------------------------------------------------------")
