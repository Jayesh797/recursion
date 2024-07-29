def checkpalindrome(stri):
    if(stri[0]!=stri[-1]):
        return False
    else:
        if(len(stri)==1):
            return True
        else:
            return checkpalindrome(stri[1:len(stri)-1])
    
df=checkpalindrome("abcbas")
print(df)