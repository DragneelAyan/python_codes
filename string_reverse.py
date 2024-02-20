str1 = "hktb-hfjs-kbch-gknk"
str2 = "Hi, how are you?"

print(str1[-1::-1])
print(str2[-1::-1])
# #--------------------
rstr1 = reversed(str1) #reversed() returns an reversed object, in separated form.
print("".join(rstr1)) #We need to use "".join(), to get the output properly

rstr2 = reversed(str2)
print("".join(rstr2))
#--------------------
    # Suppose there is a string st='AyanSinha', so len(st)=9. Now, string iteration starts from position '0',
    # so 9th position comes as '8'. That's why we need to start iteration from 'len(str2)-1'.
    # In range function, if I write range(0,8) that means our loop will iterate from i=0
    # to i=7. So, it stops iterating before i=8, for that reason we wrote 'range(len(str2)-1, -1, -1). 
    # So, it will iterate till i=0.'
resultstr2 = ''
for i in range(len(str2)-1, -1, -1): 
    resultstr2 = resultstr2 + str2[i]
    
print(resultstr2)
#-----------------------
