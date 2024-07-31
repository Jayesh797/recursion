def removea(i,mainstri,substri):
    if(i>=len(mainstri)):
        return substri
    else:
        if(mainstri[i]=='a'):
            return removea(i+1,mainstri,substri)
        else:
            substri+=mainstri[i]
            return removea(i+1,mainstri,substri)
            
df=removea(0,"baccda","")
print(df)