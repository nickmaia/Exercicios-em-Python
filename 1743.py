x = input().split()
y = input().split()
i=0

for i, data in enumerate(zip(x,y), start=0):
    
    if({data[0]} != {data[1]}):{
        print("Y")
    }
    else:{
        print("N")
    }