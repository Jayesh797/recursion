def removestring(mainstring,checkstring):
    if(not mainstring):
        return " "
    else:
        if(mainstring.startswith(checkstring)):
            return removestring(mainstring[len(checkstring):],checkstring)
        else:
            return mainstring[0]+removestring(mainstring[1:],checkstring)
df=removestring('abcdapplemankoda','apple')
print(df)