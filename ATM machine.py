x,y=input().split()
x,y=int(x),float(y)
if x<(y-0.5):
    if x%5==0:
        print("%.2f"%(y-x-0.5))
    else:
        print("%.2f"%y)
else:
    print("%.2f"%y)