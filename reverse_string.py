def revstr(stri):
    if(len(stri)==1):
        return stri
    else:
        return stri[-1]+revstr(stri[:-1])
        
df=revstr("vikramkumar")
print(df)