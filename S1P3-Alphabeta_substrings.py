ls= []
for i in range(len(s)-1):
    ls.append(0)
    k=i
    while s[k]<=s[k+1] and k<len(s)-2:
        ls[i]+=1
        k+=1
    if s[k]<=s[k+1]:
        ls[i]+=1
print (s[ls.index(max(ls)):ls.index(max(ls))+max(ls)+1])
