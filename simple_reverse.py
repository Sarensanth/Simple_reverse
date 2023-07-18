def string_rev(s):
    s=list(s)
    j=len(s)-1
    i=0
    while(i<=j):
        s[i],s[j]=s[j],s[i]
        i+=1
        j-=1
    return "".join(s)

s=input()
print(string_rev(s))