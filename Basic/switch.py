
def cross_table(data):
    print("cross")
    return data
 
def pivote_table(data):
    print("pivot")
    return data
 
def default_table(data):
    print("default")
    return data
 
def switch(argument = None):
    case  = {
        1: cross_table,
        2: pivote_table,
        3: default_table,
    }
    
    return case[argument]
pos = 3
myfunc= switch(pos)
text = "hola"
print(myfunc(text))

    