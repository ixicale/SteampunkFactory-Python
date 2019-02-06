print("suma",1+1)
print("division",1/1)
print("multiplicacion",1*1)
# print("mod",1%2)
arr = [
    "grey darken-3",
    "grey darken-2",
    "grey darken-1",
    "grey",
    "grey lighten-1",
    "grey lighten-2",
    "grey lighten-3",
    "grey lighten-4",
    "grey lighten-5",
    ]


for x in range(len(arr)*3):
    print("operacion",x,"%",len(arr),"=  ",x%len(arr), "=>  ", arr[x%len(arr)])
