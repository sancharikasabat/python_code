x=(True,"sad",56,"dfg",7.9,3+4j) # tuple data type
with open("std4.data" , "a") as fb: # wantbreplace the previous data open w mode
    fb.writelines(str(x))
    fb.write("\n")
    print("done")