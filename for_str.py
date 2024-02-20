# for i in reversed(range(1, 11)):
#     print(i)

str = "4685-7461-4628-4615"
str2 = "hktb-hfjs-kbch-gknk"

# for i in str:
#     if i == "-":
#         print("\n")
#         continue
#     print(i)

# for i in range(1, len(str)):
#     print(i)
    
# for i in str2:
#     if i == 'b':
#         print(i)   

#find character position in string

i = str2.rfind("b")
print(i, end=" ")

for n in range(1, len(str2)):
    if str2[i] == 'b':
        print(i)
        break