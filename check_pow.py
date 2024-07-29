def checkpow(a,b):
    if(b==0):
        return 1
    else:
        return a * checkpow(a,b-1)
        
df=checkpow(3,4)
print(df)