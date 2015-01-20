bob=0
for i in range(2,len(s)):
    e=s[i-2]+s[i-1]+s[i]
    if e == 'bob':
        bob+=1
print ('Number of times bob occurs is: '+str(bob))
