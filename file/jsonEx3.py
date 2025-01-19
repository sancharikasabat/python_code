#save the json file
import json
dictfrmstr={"sno":100,"name":"russom","mark":100}
with open("C:\\Users\\sanch\\jsn\\jsonfile1.json","w") as fp:
    json.dump(dictfrmstr,fp)
